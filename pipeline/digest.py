"""Pass 1: today's abstracts + rolling memory context -> the daily digest.

`--dry-run` assembles the full prompt and reports token count + cost estimate
without calling the API. `--prompt-out` writes that prompt to a file and
`--from-file` turns a completion produced anywhere else back into a digest, so
the day can be recovered by hand when the API path is unavailable.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

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
from .llm import LLM, LLMResult

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
    cross = [c for c in p["categories"] if c != p["primary_category"]]
    cats = p["primary_category"] + (f"; cross: {', '.join(cross)}" if cross else "")
    return f"[arXiv:{p['id']}] {p['title']} — {byline(p['authors']) or '?'} ({cats})\n{p['abstract']}"


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


def byline(authors: list[str]) -> str:
    if not authors:
        return ""
    return authors[0] + (" et al." if len(authors) > 1 else "")


HEADING_RE = re.compile(
    r"^(#{2,3}\s*\[arXiv:(\d{4}\.\d{4,5})\]\([^)]+\)\s*—\s*.+)$", re.MULTILINE
)


def add_bylines(text: str, papers: dict[str, dict]) -> str:
    """Append '(Author et al.)' to every '### arXiv:ID — Title' heading.

    These headings are LLM-authored prose and inconsistently name authors;
    this guarantees every paper heading is followed by its byline from
    ground-truth metadata, regardless of what the model wrote.
    """

    def add(m: re.Match) -> str:
        line, arxiv_id = m.group(1), m.group(2)
        paper = papers.get(arxiv_id)
        b = byline(paper["authors"]) if paper else ""
        return f"{line} ({b})" if b else line

    return HEADING_RE.sub(add, text)


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
    ap.add_argument(
        "--prompt-out",
        metavar="PATH",
        help="write the assembled system+user prompt here and exit (no API call)",
    )
    ap.add_argument(
        "--from-file",
        metavar="PATH",
        help="build the digest from a completion in this file instead of calling "
        "the API (pairs with --prompt-out for a hand-run day)",
    )
    args = ap.parse_args()
    if args.from_file and args.dry_run:
        ap.error("--from-file has nothing to estimate; drop --dry-run")

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

    if args.prompt_out:
        # Two prompts, one file: everything above the rule is the system prompt.
        # Paste the whole thing wherever you can get a completion.
        sep = "=" * 72
        Path(args.prompt_out).write_text(
            f"{sep}\nSYSTEM PROMPT\n{sep}\n\n{system}\n\n"
            f"{sep}\nUSER PROMPT ({len(papers)} papers, {date})\n{sep}\n\n{user}\n"
        )
        print(
            f"Wrote prompt for {date} ({len(papers)} papers) to {args.prompt_out}.\n"
            f"Save the model's reply verbatim, then: "
            f"python -m pipeline.digest --date {date} --from-file REPLY.md"
        )
        return 0

    if args.from_file:
        # No LLM constructed at all — this path needs no API key.
        raw = Path(args.from_file).read_text()
        result = LLMResult(raw, 0, 0, 0.0, False)
        generator = "manual"
    else:
        llm = LLM(cfg)
        generator = f"{llm.provider}/{llm.model}"

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

    if not args.from_file:
        result = llm.complete(system, user, cfg["digest"]["max_output_tokens"])
    post = parse_output(result.text)

    # A truncated digest is still worth publishing — a short issue beats no
    # issue. An *empty* body is not: it means the model spent the whole budget
    # on thinking and never emitted text (2026-07-20), and writing it out would
    # ship a blank page and poison the memory context that reads it back.
    if not post.content.strip():
        print(
            f"error: model returned no digest body ({result.output_tokens} output "
            f"tokens, truncated={result.truncated}). Nothing written — raise "
            f"digest.max_output_tokens in config.yaml or simplify the prompt.",
            file=sys.stderr,
        )
        return 1

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
    post["generator"] = generator
    post["cost_usd"] = round(result.cost, 4)
    if result.truncated:
        post["truncated"] = True
    post.content = linkify(post.content, valid_ids)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(frontmatter.dumps(post) + "\n")
    note = " [TRUNCATED]" if result.truncated else ""
    print(
        f"Wrote {out_path} ({result.output_tokens} tokens, ${result.cost:.4f}){note}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
