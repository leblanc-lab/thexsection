"""Fetch the day's arXiv announcements for the configured categories.

Default mode reads the per-category Atom feeds (exactly the day's announced
papers). `--backfill YYYY-MM-DD` instead queries the export API by submission
date — an approximation of that day's announcement list, for testing and for
recovering missed days.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
import time

import feedparser

from .common import ARXIV_ID, data_path, load_config, parse_date

FEED_URL = "https://rss.arxiv.org/atom/{cat}"
EXPORT_URL = (
    "http://export.arxiv.org/api/query?search_query={query}"
    "&start={start}&max_results=200&sortBy=submittedDate&sortOrder=descending"
)

ID_RE = re.compile(f"({ARXIV_ID})")


def _clean_abstract(summary: str) -> str:
    # Feed summaries look like "arXiv:2507.01234v1 Announce Type: new\nAbstract: ..."
    text = re.sub(r"^arXiv:\S+\s+Announce Type:\s*\S+\s*", "", summary).strip()
    text = re.sub(r"^Abstract:\s*", "", text)
    return re.sub(r"\s+", " ", text).strip()


def _entry_to_paper(entry) -> dict | None:
    m = ID_RE.search(entry.get("id", "")) or ID_RE.search(entry.get("link", ""))
    if not m:
        return None
    authors = [a.get("name", "") for a in entry.get("authors", [])]
    # The rss.arxiv.org feeds put the whole author list in one dc:creator string.
    if len(authors) == 1 and "," in authors[0]:
        authors = [a.strip() for a in authors[0].split(",")]
    tags = [t["term"] for t in entry.get("tags", [])]
    return {
        "id": m.group(1),
        "title": re.sub(r"\s+", " ", entry.get("title", "")).strip(),
        "authors": authors,
        "abstract": _clean_abstract(entry.get("summary", "")),
        "primary_category": tags[0] if tags else "",
        "categories": tags,
        "announce_type": entry.get("arxiv_announce_type", "new"),
    }


def fetch_feeds(categories: list[str], announce_types: list[str]) -> list[dict]:
    papers: dict[str, dict] = {}
    for cat in categories:
        feed = feedparser.parse(FEED_URL.format(cat=cat))
        for entry in feed.entries:
            paper = _entry_to_paper(entry)
            if paper and paper["announce_type"] in announce_types:
                papers.setdefault(paper["id"], paper)
        print(f"  {cat}: {len(feed.entries)} entries", file=sys.stderr)
    return list(papers.values())


def fetch_backfill(categories: list[str], date: dt.date) -> list[dict]:
    """Approximate a past day's list via the export API (by submission date)."""
    cat_query = "+OR+".join(f"cat:{c}" for c in categories)
    day = date.strftime("%Y%m%d")
    query = f"%28{cat_query}%29+AND+submittedDate:[{day}0000+TO+{day}2359]"
    papers: dict[str, dict] = {}
    start = 0
    while True:
        feed = feedparser.parse(EXPORT_URL.format(query=query, start=start))
        if not feed.entries:
            break
        for entry in feed.entries:
            paper = _entry_to_paper(entry)
            if paper:
                paper["primary_category"] = entry.get("arxiv_primary_category", {}).get(
                    "term", paper["primary_category"]
                )
                papers[paper["id"]] = paper
        if len(feed.entries) < 200:
            break
        start += 200
        time.sleep(3)  # export API asks for >=3s between requests
    return list(papers.values())


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--date", help="label for the output file (default: today)")
    ap.add_argument(
        "--backfill",
        metavar="YYYY-MM-DD",
        help="fetch by submission date from the export API instead of today's feeds",
    )
    args = ap.parse_args()

    cfg = load_config()["arxiv"]
    if args.backfill:
        date = parse_date(args.backfill)
        papers = fetch_backfill(cfg["categories"], date)
    else:
        date = parse_date(args.date)
        papers = fetch_feeds(cfg["categories"], cfg["announce_types"])

    if not papers:
        print(f"No papers for {date} (weekend/holiday?) — nothing to do.")
        return 0

    path = data_path(date)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        for paper in sorted(papers.values() if isinstance(papers, dict) else papers, key=lambda p: p["id"]):
            f.write(json.dumps(paper) + "\n")

    by_cat: dict[str, int] = {}
    for p in papers:
        by_cat[p["primary_category"]] = by_cat.get(p["primary_category"], 0) + 1
    summary = ", ".join(f"{c}: {n}" for c, n in sorted(by_cat.items()))
    print(f"Wrote {len(papers)} papers to {path} ({summary})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
