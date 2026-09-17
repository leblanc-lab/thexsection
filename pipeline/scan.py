"""Zero-LLM keyword scan: abstract-only entries for the topic mirrors.

`watchlist.py` only writes a briefing on days it runs, and only for the keyword
set in force that day. This re-runs the same keyword/author match over every day of
raw paper data (data/ and the gitignored data/backfill/) and writes the hits that no briefing covers to
watch/scan/YYYY-MM-DD.md — same frontmatter and heading shape as a watch
entry, but each paper's body is its abstract with a "keyword hit" note, so the
topic pages and per-paper feeds can carry them. No API calls, no cost.

The watch page itself ignores these; they surface only on mirrored topics'
pages and feeds, where `build_site.load_topic_days` merges them under any
briefing the same day (briefed papers win; the scan fills the gaps).

Default: every day in data/. `--date` for one day. Idempotent: rewrites or
removes the scan file for each day it processes.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys

import frontmatter

from .common import load_config, load_papers, paper_dates, parse_date
from .digest import byline
from .watchlist import WATCH_DIR, TopicMatcher

SCAN_DIR = WATCH_DIR / "scan"
GENERATOR = "keyword-scan"


def briefed_ids(date_iso: str) -> dict[str, set[str]]:
    """topic name -> paper ids the day's LLM briefing already covers."""
    path = WATCH_DIR / f"{date_iso}.md"
    if not path.exists():
        return {}
    return {t: set(map(str, ids)) for t, ids in (frontmatter.load(path).get("topics") or {}).items()}


def scan_day(papers: list[dict], topics: list[dict], covered: dict[str, set[str]]) -> dict[str, list[tuple[dict, list[str]]]]:
    """topic name -> [(paper, matched keywords)] for hits with no briefing."""
    hits: dict[str, list[tuple[dict, list[str]]]] = {}
    matcher = TopicMatcher(topics)
    for p in papers:
        for name, matched in matcher.hits(p).items():
            if p["id"] not in covered.get(name, set()):
                hits.setdefault(name, []).append((p, matched))
    return hits


def render(date_iso: str, hits: dict[str, list[tuple[dict, list[str]]]]) -> str:
    sections = []
    for topic, entries in hits.items():
        parts = [f"## {topic}"]
        for p, matched in entries:
            title = re.sub(r"\s+", " ", p["title"]).strip()
            b = byline(p.get("authors", []))
            heading = f"### [arXiv:{p['id']}](https://arxiv.org/abs/{p['id']}) — {title}"
            parts.append(
                f"{heading} ({b})" if b else heading
            )
            parts.append(
                f"_Watchlist hit ({', '.join(matched)}) — abstract only, not yet read for a briefing._\n\n"
                + re.sub(r"\s+", " ", p["abstract"]).strip()
            )
        sections.append("\n\n".join(parts))
    post = frontmatter.Post(
        "\n\n".join(sections),
        date=date_iso,
        topics={t: [p["id"] for p, _ in entries] for t, entries in hits.items()},
        generator=GENERATOR,
        cost_usd=0.0,
    )
    return frontmatter.dumps(post) + "\n"


def scan_dates(dates: list[dt.date], topics: list[dict]) -> str:
    """(Re)write the scan file for each date; returns a one-line summary."""
    SCAN_DIR.mkdir(parents=True, exist_ok=True)
    totals: dict[str, int] = {}
    written = removed = 0
    for date in dates:
        iso = date.isoformat()
        papers = load_papers(date)
        out = SCAN_DIR / f"{iso}.md"
        hits = scan_day(papers, topics, briefed_ids(iso)) if papers else {}
        if not hits:
            if out.exists():
                out.unlink()
                removed += 1
            continue
        out.write_text(render(iso, hits))
        written += 1
        for t, entries in hits.items():
            totals[t] = totals.get(t, 0) + len(entries)
        print(f"  {iso}: " + ", ".join(f"{t} ({len(e)})" for t, e in hits.items()), file=sys.stderr)
    return (
        f"Scanned {len(dates)} days — wrote {written} scan files"
        + (f", removed {removed} stale" if removed else "")
        + (": " + ", ".join(f"{t} +{n}" for t, n in totals.items()) if totals else "; nothing uncovered")
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", help="YYYY-MM-DD (default: every day with data)")
    args = ap.parse_args()

    topics = load_config()["watchlist"]["topics"]
    dates = [parse_date(args.date)] if args.date else paper_dates()
    print(scan_dates(dates, topics))
    return 0


if __name__ == "__main__":
    sys.exit(main())
