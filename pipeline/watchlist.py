"""Personal-interest keyword tracks.

Scans the day's papers for configured topic keywords (title + abstract), and
when any fire, writes a focused technical briefing for the matched papers to
watch/YYYY-MM-DD.md (rendered on the subtly-linked watch page). One LLM call
per day, only on days something matches.
"""

from __future__ import annotations

import argparse
import re
import sys

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


def match_topics(papers: list[dict], topics: list[dict]) -> dict[str, list[dict]]:
    """topic name -> matching papers (a paper may match several topics)."""
    hits: dict[str, list[dict]] = {}
    for topic in topics:
        patterns = [_compile(k) for k in topic["keywords"]]
        matched = [
            p
            for p in papers
            if any(pat.search(f"{p['title']} {p['abstract']}") for pat in patterns)
        ]
        if matched:
            hits[topic["name"]] = matched
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
