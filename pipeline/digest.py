"""Pass 1: today's abstracts + rolling memory context -> the daily digest.

`--dry-run` assembles the full prompt and reports token count + cost estimate
without calling the API.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys

import frontmatter

from .common import (
    DIGEST_DIR,
    MEMORY_DIR,
    digest_path,
    load_config,
    load_papers,
    load_prompt,
    parse_date,
)
from .llm import LLM

BACKTICKED_ID_RE = re.compile(r"`((?:arXiv:)?\d{4}\.\d{4,5})`")
BRACKETED_ID_RE = re.compile(r"\[arXiv:(\d{4}\.\d{4,5})\](?!\()")
BRACKETED_LIST_RE = re.compile(r"\[((?:arXiv:\d{4}\.\d{4,5})(?:\s*,\s*arXiv:\d{4}\.\d{4,5})+)\]")
PLAIN_ID_RE = re.compile(r"(?<!\[)arXiv:(\d{4}\.\d{4,5})(?!\]|\d)")
BARE_ID_RE = re.compile(r"(?<![\[/.\d])(\d{4}\.\d{4,5})(?![\]\d])")

MEMORY_TIERS = [
    ("year", "Synthesis of the current academic year"),
    ("season", "Synthesis of the current term"),
    ("month", "Synthesis of the current month"),
    ("week", "Synthesis of the last seven days"),
]


def format_paper(p: dict) -> str:
    authors = p["authors"]
    byline = authors[0] + (" et al." if len(authors) > 1 else "") if authors else "?"
    cross = [c for c in p["categories"] if c != p["primary_category"]]
    cats = p["primary_category"] + (f"; cross: {', '.join(cross)}" if cross else "")
    return f"[arXiv:{p['id']}] {p['title']} — {byline} ({cats})\n{p['abstract']}"


def memory_context(date: dt.date, lookback: int) -> str:
    parts = []
    for tier, label in MEMORY_TIERS:
        path = MEMORY_DIR / f"{tier}.md"
        if path.exists():
            parts.append(f"## {label}\n\n{path.read_text().strip()}")

    prior = sorted(
        p for p in DIGEST_DIR.glob("????-??-??.md") if p.stem < date.isoformat()
    )[-lookback:]
    for p in prior:
        post = frontmatter.load(p)
        parts.append(f"## Daily digest, {p.stem}\n\n{post.content.strip()}")

    if not parts:
        return (
            "(No memory context yet — this is one of the first issues. "
            "Do not invent continuity with the past.)"
        )
    return "\n\n".join(parts)


def assemble(date: dt.date, papers: list[dict], cfg: dict) -> str:
    dcfg = cfg["digest"]
    paper_blocks = [format_paper(p) for p in papers]

    # Guard: stay under the input-token cap by truncating abstracts, not
    # dropping papers. ~4 chars/token is close enough for a guardrail.
    budget_chars = dcfg["max_input_tokens"] * 4
    while sum(len(b) for b in paper_blocks) > budget_chars:
        paper_blocks = [
            b.split("\n")[0] + "\n" + " ".join(b.split("\n")[1].split()[:120])
            for b in paper_blocks
        ]
        budget_chars *= 10  # one truncation pass only

    return (
        f"# Memory context\n\n{memory_context(date, dcfg['daily_lookback'])}\n\n"
        f"# Today's papers ({date.isoformat()}, {len(papers)} total)\n\n"
        + "\n\n".join(paper_blocks)
    )


def linkify(text: str, valid_ids: set[str]) -> str:
    def link(arxiv_id: str) -> str:
        return f"[arXiv:{arxiv_id}](https://arxiv.org/abs/{arxiv_id})"

    # Models sometimes put IDs in code spans, where links don't render.
    text = BACKTICKED_ID_RE.sub(lambda m: m.group(1), text)
    # "[arXiv:A, arXiv:B]" lists: drop the brackets, let the plain rule link each.
    text = BRACKETED_LIST_RE.sub(lambda m: m.group(1), text)
    # "[arXiv:ID]" without a URL — a dangling reference-style link.
    text = BRACKETED_ID_RE.sub(lambda m: link(m.group(1)), text)
    text = PLAIN_ID_RE.sub(lambda m: link(m.group(1)), text)
    # Bare IDs only when they match a known paper (avoids false positives).
    return BARE_ID_RE.sub(
        lambda m: link(m.group(1)) if m.group(1) in valid_ids else m.group(0), text
    )


def parse_output(raw: str) -> frontmatter.Post:
    # Models sometimes wrap the whole answer in a markdown fence — strip it.
    raw = raw.strip()
    raw = re.sub(r"^```(?:markdown|md|yaml)?\s*\n", "", raw)
    raw = re.sub(r"\n```\s*$", "", raw)
    return frontmatter.loads(raw)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--date", help="YYYY-MM-DD (default: today)")
    ap.add_argument("--dry-run", action="store_true", help="token/cost estimate only")
    ap.add_argument("--force", action="store_true", help="overwrite an existing digest")
    args = ap.parse_args()

    cfg = load_config()
    date = parse_date(args.date)
    papers = load_papers(date)
    if not papers:
        print(f"No paper data for {date} — nothing to do.")
        return 0

    out_path = digest_path(date)
    if out_path.exists() and not args.force and not args.dry_run:
        print(f"{out_path} already exists (use --force to regenerate).")
        return 0

    system = load_prompt("daily_system")
    user = assemble(date, papers, cfg)
    llm = LLM(cfg)

    if args.dry_run:
        try:
            tokens = llm.count_tokens(system, user)
            how = "counted"
        except Exception:
            tokens = (len(system) + len(user)) // 4
            how = "estimated (chars/4)"
        out = cfg["digest"]["max_output_tokens"]
        print(
            f"[dry-run] {len(papers)} papers; input ~{tokens} tokens ({how}); "
            f"cost ceiling ~${llm.estimate_cost(tokens, out):.4f} "
            f"on {llm.provider}/{llm.model}"
        )
        return 0

    result = llm.complete(system, user, cfg["digest"]["max_output_tokens"])
    post = parse_output(result.text)

    valid_ids = {p["id"] for p in papers}
    picks = [str(i) for i in post.get("deep_dive_ids", []) if str(i) in valid_ids]
    dropped = len(post.get("deep_dive_ids", [])) - len(picks)
    if dropped:
        print(f"warning: dropped {dropped} hallucinated deep_dive_ids", file=sys.stderr)
    community = [str(i) for i in post.get("community_ids", []) if str(i) in valid_ids]

    post["date"] = date.isoformat()
    post["paper_count"] = len(papers)
    post["deep_dive_ids"] = picks
    post["community_ids"] = community
    post["generator"] = f"{llm.provider}/{llm.model}"
    post["cost_usd"] = round(result.cost, 4)
    post.content = linkify(post.content, valid_ids)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Wrote {out_path} ({result.output_tokens} tokens, ${result.cost:.4f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
