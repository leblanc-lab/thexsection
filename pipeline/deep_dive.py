"""Pass 2: expand the digest's picks from their arXiv HTML renderings.

Fetches https://arxiv.org/html/<id> (available for most >=2024 submissions),
strips it to text, and writes one short expert deep dive per pick, appended to
the daily digest under "## Deep dives".
"""

from __future__ import annotations

import argparse
import re
import sys

import frontmatter
import httpx
from bs4 import BeautifulSoup

from .common import digest_path, load_config, load_papers, load_prompt, parse_date
from .digest import add_bylines, linkify
from .llm import LLM

HTML_URL = "https://arxiv.org/html/{id}"
UA = {"User-Agent": "thexsection/0.1 (daily digest builder)"}


def fetch_paper_text(arxiv_id: str, max_chars: int) -> str | None:
    """Plain text of the paper's HTML rendering, or None if unavailable."""
    try:
        resp = httpx.get(
            HTML_URL.format(id=arxiv_id), headers=UA, timeout=30, follow_redirects=True
        )
    except httpx.HTTPError:
        return None
    if resp.status_code != 200:
        return None
    soup = BeautifulSoup(resp.text, "html.parser")
    main = soup.find("article") or soup.find("main") or soup.body
    if main is None:
        return None
    for tag in main.find_all(["script", "style", "nav", "header", "footer"]):
        tag.decompose()
    text = re.sub(r"\n{3,}", "\n\n", main.get_text("\n")).strip()
    if len(text) < 500:  # a stub/error page, not a paper
        return None
    return text[:max_chars]


def build_input(digest_body: str, picks: list[dict], max_chars: int) -> tuple[str, int]:
    blocks, fetched = [], 0
    for p in picks:
        text = fetch_paper_text(p["id"], max_chars)
        if text:
            fetched += 1
            body = f"FULL TEXT (from arXiv HTML rendering):\n{text}"
        else:
            body = f"NO HTML RENDERING AVAILABLE — abstract only:\n{p['abstract']}"
        blocks.append(f"# Paper arXiv:{p['id']}\nTitle: {p['title']}\n\n{body}")
    user = (
        f"# Today's digest (context for why these were picked)\n\n{digest_body}\n\n"
        + "\n\n".join(blocks)
    )
    return user, fetched


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--date", help="YYYY-MM-DD (default: today)")
    ap.add_argument("--force", action="store_true", help="regenerate existing section")
    args = ap.parse_args()

    cfg = load_config()
    ddcfg = cfg["deep_dive"]
    if ddcfg["count"] <= 0:
        print("Deep dives disabled (deep_dive.count: 0).")
        return 0

    date = parse_date(args.date)
    path = digest_path(date)
    if not path.exists():
        print(f"No digest for {date} — nothing to do.")
        return 0

    post = frontmatter.load(path)
    if "## Deep dives" in post.content and not args.force:
        print(f"{path} already has deep dives (use --force).")
        return 0

    papers = {p["id"]: p for p in load_papers(date)}
    picks = [papers[i] for i in post.get("deep_dive_ids", [])[: ddcfg["count"]] if i in papers]
    if not picks:
        print("No valid deep-dive picks in the digest — nothing to do.")
        return 0

    user, fetched = build_input(
        post.content, picks, ddcfg["max_tokens_per_paper"] * 4
    )
    print(f"Fetched HTML for {fetched}/{len(picks)} picks", file=sys.stderr)

    llm = LLM(cfg)
    result = llm.complete(
        load_prompt("deep_dive_system"), user, ddcfg["max_output_tokens"]
    )

    body = re.sub(r"^## Deep dives\s*\n", "", result.text.strip())
    content = post.content
    if "## Deep dives" in content:  # --force: replace the old section
        content = content.split("## Deep dives")[0].rstrip()
    post.content = content + "\n\n## Deep dives\n\n" + add_bylines(linkify(body, set(papers)), papers)
    post["cost_usd"] = round(post.get("cost_usd", 0) + result.cost, 4)
    path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Appended {len(picks)} deep dives to {path} (${result.cost:.4f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
