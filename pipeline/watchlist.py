"""Personal-interest keyword tracks.

Scans the day's papers for configured topic keywords (title + abstract) and
watched authors, and when any fire, writes a focused technical briefing for the matched papers to
watch/YYYY-MM-DD.md (rendered on the subtly-linked watch page). One LLM call
per day, only on days something matches.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata

import frontmatter

from .common import DIGEST_DIR, load_config, load_papers, load_prompt, parse_date
from .deep_dive import fetch_paper_text
from .digest import add_bylines, linkify
from .llm import LLM

WATCH_DIR = DIGEST_DIR.parent / "watch"


def _compile(keyword: str) -> re.Pattern:
    # Word-boundary match so short acronyms ("MuC") don't hit inside words
    # ("much"). \b behaves at alphanumeric edges; hyphens inside phrases are fine.
    return re.compile(r"\b" + re.escape(keyword) + r"\b", re.IGNORECASE)


# Initials-only author strings ("J. Thaler") are accepted only on short author
# lists. Collaboration papers list hundreds of initialled names, and "M. Williams"
# is on every LHCb paper; on those, only a full first name counts.
INITIALS_MAX_AUTHORS = 25


def _name_tokens(name: str) -> list[str]:
    """Lower-cased, accent-stripped tokens: 'Grégory  Soyez' -> ['gregory', 'soyez']."""
    flat = "".join(c for c in unicodedata.normalize("NFKD", name) if not unicodedata.combining(c))
    return re.sub(r"[.,]", " ", flat).lower().split()


def _author_spec(spec) -> tuple[str, list[tuple[str, str]]]:
    """A watched author: a name, or a list of that person's name variants.

    Returns (display name, [(first, last), ...]). Middle names/initials are
    ignored on both sides, so "Gavin Salam" already covers "Gavin P. Salam";
    list variants for genuinely different first names ("Ben"/"Benjamin").
    """
    names = [spec] if isinstance(spec, str) else list(spec)
    variants = [(t[0], t[-1]) for n in names if (t := _name_tokens(n))]
    return names[0], variants


class TopicMatcher:
    """Match papers against watchlist topics by `keywords` (title+abstract,
    word-bounded, case-insensitive) and/or `authors` (see _author_spec)."""

    def __init__(self, topics: list[dict]):
        self.topics = [
            (
                t,
                [(k, _compile(k)) for k in t.get("keywords", [])],
                [_author_spec(a) for a in t.get("authors", [])],
            )
            for t in topics
        ]

    def hits(self, paper: dict) -> dict[str, list[str]]:
        """topic name -> what matched (keywords and/or watched authors' names)."""
        text = f"{paper['title']} {paper['abstract']}"
        names = [(t[0], t[-1]) for a in paper.get("authors", []) if (t := _name_tokens(a))]
        allow_initials = len(names) <= INITIALS_MAX_AUTHORS
        out: dict[str, list[str]] = {}
        for topic, patterns, authors in self.topics:
            matched = [k for k, pat in patterns if pat.search(text)]
            for display, variants in authors:
                if any(
                    last == L and (first == F or (allow_initials and len(first) == 1 and first == F[0]))
                    for first, last in names
                    for F, L in variants
                ):
                    matched.append(display)
            if matched:
                out[topic["name"]] = matched
        return out


def match_topics(papers: list[dict], topics: list[dict]) -> dict[str, list[dict]]:
    """topic name -> matching papers (a paper may match several topics)."""
    matcher = TopicMatcher(topics)
    hits: dict[str, list[dict]] = {}
    for p in papers:
        for name in matcher.hits(p):
            hits.setdefault(name, []).append(p)
    return hits


def build_input(hits: dict[str, list[dict]], max_chars: int) -> tuple[str, int]:
    blocks, fetched, seen = [], 0, set()
    for topic, papers in hits.items():
        blocks.append(f"# TOPIC: {topic}")
        for p in papers:
            if p["id"] not in seen:
                seen.add(p["id"])
            text = fetch_paper_text(p["id"], max_chars)
            if text:
                fetched += 1
                body = f"FULL TEXT (from arXiv HTML):\n{text}"
            else:
                body = f"ABSTRACT ONLY:\n{p['abstract']}"
            blocks.append(f"## arXiv:{p['id']} — {p['title']}\n\n{body}")
    return "\n\n".join(blocks), fetched


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--date", help="YYYY-MM-DD (default: today)")
    ap.add_argument("--force", action="store_true", help="overwrite an existing entry")
    args = ap.parse_args()

    cfg = load_config()
    wcfg = cfg["watchlist"]
    if not wcfg.get("enabled", True):
        print("Watchlist disabled.")
        return 0

    date = parse_date(args.date)
    papers = load_papers(date)
    if not papers:
        print(f"No paper data for {date} — nothing to watch.")
        return 0

    hits = match_topics(papers, wcfg["topics"])
    # `brief: false` topics are scan-only streams (pipeline.scan): matched, but
    # never sent to the LLM.
    briefable = {t["name"] for t in wcfg["topics"] if t.get("brief", True)}
    hits = {t: ps for t, ps in hits.items() if t in briefable}
    if not hits:
        print("No watched topics fired today.")
        return 0

    n_papers = len({p["id"] for ps in hits.values() for p in ps})
    print(
        "Watchlist fired: "
        + ", ".join(f"{t} ({len(ps)})" for t, ps in hits.items())
        + f" — {n_papers} papers",
        file=sys.stderr,
    )

    out_path = WATCH_DIR / f"{date.isoformat()}.md"
    if out_path.exists() and not args.force:
        print(f"{out_path} already exists (use --force).")
        return 0

    user, fetched = build_input(hits, wcfg["max_tokens_per_paper"] * 4)
    print(f"Fetched HTML for {fetched}/{n_papers} matched papers", file=sys.stderr)

    llm = LLM(cfg)
    result = llm.complete(
        load_prompt("watchlist_system"), user, wcfg["max_output_tokens"]
    )

    valid = {p["id"] for ps in hits.values() for p in ps}
    papers_by_id = {p["id"]: p for ps in hits.values() for p in ps}
    post = frontmatter.Post(
        add_bylines(linkify(result.text.strip(), valid), papers_by_id),
        date=date.isoformat(),
        topics={t: [p["id"] for p in ps] for t, ps in hits.items()},
        generator=f"{llm.provider}/{llm.model}",
        cost_usd=round(result.cost, 4),
    )
    WATCH_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Wrote {out_path} (${result.cost:.4f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
