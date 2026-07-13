"""Weekly citation radar: highly-cited recent papers the deep dives missed.

Queries INSPIRE-HEP for the most-cited papers of the last `window_days` in the
tracked categories, drops anything already deep-dived or already featured, and
writes deep-dive-style summaries for the top picks. Output goes to
digests/radar/YYYY-MM-DD.md and is also appended to the day's digest if one
exists.
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from urllib.parse import quote

import frontmatter
import httpx

from .common import DIGEST_DIR, digest_path, load_config, load_prompt, parse_date
from .deep_dive import fetch_paper_text
from .digest import add_bylines, linkify
from .llm import LLM

RADAR_DIR = DIGEST_DIR / "radar"
INSPIRE_URL = (
    "https://inspirehep.net/api/literature?sort=mostcited&size=25"
    "&fields=titles,arxiv_eprints,citation_count,earliest_date,authors&q={q}"
)


def _inspire_authors(authors: list[dict]) -> list[str]:
    names = []
    for a in authors:
        full = a.get("full_name", "")
        if "," in full:
            last, _, first = full.partition(",")
            full = f"{first.strip()} {last.strip()}"
        if full:
            names.append(full)
    return names


def already_covered_ids() -> set[str]:
    ids: set[str] = set()
    for p in DIGEST_DIR.glob("????-??-??.md"):
        ids.update(str(i) for i in frontmatter.load(p).get("deep_dive_ids", []))
    for p in RADAR_DIR.glob("????-??-??.md"):
        ids.update(str(i) for i in frontmatter.load(p).get("radar_ids", []))
    return ids


def inspire_top_cited(categories: list[str], date: dt.date, window_days: int) -> list[dict]:
    start = date - dt.timedelta(days=window_days)
    cats = " or ".join(f"primarch {c}" for c in categories)
    q = quote(f"de {start.isoformat()}->{date.isoformat()} and ({cats})")
    resp = httpx.get(INSPIRE_URL.format(q=q), timeout=30)
    resp.raise_for_status()
    papers = []
    for hit in resp.json()["hits"]["hits"]:
        m = hit["metadata"]
        eprints = m.get("arxiv_eprints") or []
        if not eprints:
            continue
        papers.append(
            {
                "id": eprints[0]["value"],
                "title": m["titles"][0]["title"],
                "citations": m.get("citation_count", 0),
                "earliest_date": m.get("earliest_date", ""),
                "inspire_url": f"https://inspirehep.net/literature/{hit['id']}",
                "authors": _inspire_authors(m.get("authors") or []),
            }
        )
    return papers


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--date", help="YYYY-MM-DD (default: today)")
    ap.add_argument("--force", action="store_true", help="overwrite an existing radar file")
    args = ap.parse_args()

    cfg = load_config()
    rcfg = cfg["radar"]
    if not rcfg.get("enabled", True):
        print("Radar disabled.")
        return 0

    date = parse_date(args.date)
    out_path = RADAR_DIR / f"{date.isoformat()}.md"
    if out_path.exists() and not args.force:
        print(f"{out_path} already exists (use --force).")
        return 0

    candidates = inspire_top_cited(
        cfg["arxiv"]["categories"], date, rcfg["window_days"]
    )
    covered = already_covered_ids()
    picks = [
        p
        for p in candidates
        if p["citations"] >= rcfg["min_citations"] and p["id"] not in covered
    ][: rcfg["top_n"]]
    if not picks:
        print("No radar candidates cleared the bar this week.")
        return 0
    print(
        "Radar picks: "
        + ", ".join(f"{p['id']} ({p['citations']} cites)" for p in picks),
        file=sys.stderr,
    )

    blocks = []
    for p in picks:
        text = fetch_paper_text(p["id"], cfg["deep_dive"]["max_tokens_per_paper"] * 4)
        body = (
            f"FULL TEXT (from arXiv HTML rendering):\n{text}"
            if text
            else "NO HTML RENDERING AVAILABLE — use title and citation data only."
        )
        blocks.append(
            f"# Paper arXiv:{p['id']}\nTitle: {p['title']}\n"
            f"Citations: {p['citations']} (posted {p['earliest_date']})\n"
            f"INSPIRE: {p['inspire_url']}\n\n{body}"
        )

    llm = LLM(cfg)
    result = llm.complete(
        load_prompt("radar_system"), "\n\n".join(blocks), rcfg["max_output_tokens"]
    )
    picks_by_id = {p["id"]: p for p in picks}
    body = add_bylines(linkify(result.text.strip(), set(picks_by_id)), picks_by_id)

    post = frontmatter.Post(
        body,
        date=date.isoformat(),
        radar_ids=[p["id"] for p in picks],
        citations={p["id"]: p["citations"] for p in picks},
        generator=f"{llm.provider}/{llm.model}",
        cost_usd=round(result.cost, 4),
    )
    RADAR_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Wrote {out_path}")

    day_digest = digest_path(date)
    if day_digest.exists():
        dpost = frontmatter.load(day_digest)
        if "## Citation radar" not in dpost.content:
            dpost.content += "\n\n## Citation radar\n\n" + body
            day_digest.write_text(frontmatter.dumps(dpost) + "\n")
            print(f"Appended radar section to {day_digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
