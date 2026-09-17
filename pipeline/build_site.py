"""Render digests, memory tiers, radar posts, topic/deep-dive mirrors, and RSS into site/."""

from __future__ import annotations

import datetime as dt
import re
import shutil
import sys
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader

from .common import (
    DIGEST_DIR,
    MEMORY_ARCHIVE_DIR,
    MEMORY_DIR,
    SITE_DIR,
    STATIC_DIR,
    TEMPLATE_DIR,
    load_config,
)
from .substack import latex_to_unicode

RADAR_DIR = DIGEST_DIR / "radar"
WATCH_DIR = DIGEST_DIR.parent / "watch"
SCAN_DIR = WATCH_DIR / "scan"  # abstract-only keyword hits from pipeline.scan

MD = markdown.Markdown(
    extensions=["tables", "smarty", "toc", "pymdownx.arithmatex"],
    extension_configs={"pymdownx.arithmatex": {"generic": True}},
)


def md_to_html(text: str) -> str:
    MD.reset()
    return MD.convert(text)


def pretty_date(iso: str) -> str:
    d = dt.date.fromisoformat(iso)
    return d.strftime("%A, %B %-d, %Y")


def load_posts(directory: Path) -> list[dict]:
    posts = []
    for path in sorted(directory.glob("????-??-??.md"), reverse=True):
        post = frontmatter.load(path)
        posts.append(
            {
                "date": path.stem,
                "pretty_date": pretty_date(path.stem),
                "themes": post.get("themes", []),
                "paper_count": post.get("paper_count"),
                "citations": post.get("citations", {}),
                "topics": list((post.get("topics") or {}).keys()),
                "md": post.content,
                "html": md_to_html(post.content),
            }
        )
    return posts


# --- topic pages: split one watched topic back out of the shared watch entries ---

# The paper heading `watchlist.py` produces via digest.add_bylines/linkify:
# "### [arXiv:2608.02714](https://arxiv.org/abs/2608.02714) — Title (First Author et al.)"
ID_LINK_RE = re.compile(r"\[arXiv:(\d{4}\.\d{4,5})\]\([^)]*\)")
BYLINE_RE = re.compile(r"\s*\(([^()]+)\)\s*$")


def split_sections(text: str, level: int) -> tuple[str, list[tuple[str, str]]]:
    """Split markdown on ATX headings of exactly `level`.

    Returns (text before the first heading, [(heading text, body)]). The space
    after the hashes is required, so `###` never matches at level 2.
    """
    rx = re.compile(rf"^{'#' * level} +(.+?)[ \t]*$", re.MULTILINE)
    marks = list(rx.finditer(text))
    preamble = text[: marks[0].start()] if marks else text
    sections = [
        (m.group(1), text[m.end() : (marks[i + 1].start() if i + 1 < len(marks) else len(text))])
        for i, m in enumerate(marks)
    ]
    return preamble.strip(), sections


def parse_paper_heading(heading: str) -> tuple[str | None, str, str]:
    """(arXiv id, title, byline) from a `### [arXiv:ID](…) — Title (Author et al.)`."""
    m = ID_LINK_RE.search(heading)
    arxiv_id = m.group(1) if m else None
    rest = (heading[: m.start()] + heading[m.end() :]) if m else heading
    rest = rest.strip().lstrip("—-–").strip()
    byline = ""
    if b := BYLINE_RE.search(rest):
        byline, rest = b.group(1), rest[: b.start()].strip()
    # Models sometimes write their own author list into the title, which
    # add_bylines then follows with the ground-truth byline. Drop the model's
    # copy only when it demonstrably names the same lead author.
    if byline and (dup := BYLINE_RE.search(rest)):
        lead = dup.group(1).split(",")[0].strip()
        if lead and re.search(rf"\b{re.escape(lead)}\b", byline):
            rest = rest[: dup.start()].strip()
    # Headings are plain text on the page and in the feed — no KaTeX pass reaches
    # them, so flatten any inline math the way substack does.
    return arxiv_id, latex_to_unicode(rest), byline


def topic_section(path: Path, topic_name: str) -> str | None:
    """Body of the `## topic_name` section of a watch-shaped file, or None.

    The `## Topic name` heading is mandated verbatim by prompts/watchlist_system.md,
    and the frontmatter `topics` map is written server-side, so the two agreeing is
    the normal case; a file whose frontmatter claims the topic but whose body has no
    matching heading is reported and skipped rather than silently dropped.
    """
    post = frontmatter.load(path)
    if topic_name not in (post.get("topics") or {}):
        return None
    _, sections = split_sections(post.content, 2)
    body = next((b for h, b in sections if h.strip() == topic_name), None)
    if body is None:
        print(f"  ! {path.parent.name}/{path.name}: frontmatter lists {topic_name!r} but no "
              f"'## {topic_name}' heading — skipped", file=sys.stderr)
    return body


def load_topic_days(topic_name: str) -> list[dict]:
    """Every day that covered `topic_name`, newest first, split per paper.

    A day is the LLM briefing from watch/ when there is one, with any
    abstract-only hits from watch/scan/ (pipeline.scan) appended after it; a
    day with only a scan entry is all abstracts. Briefed papers win the dedupe.
    """
    days = []
    if not WATCH_DIR.exists():
        return days
    dates = {p.stem for d in (WATCH_DIR, SCAN_DIR) if d.exists() for p in d.glob("????-??-??.md")}
    for date in sorted(dates, reverse=True):
        day = None
        briefed = WATCH_DIR / f"{date}.md"
        if briefed.exists() and (body := topic_section(briefed, topic_name)) is not None:
            day = paper_day(date, body, source="watch.html")
        scanned = SCAN_DIR / f"{date}.md"
        if scanned.exists() and (body := topic_section(scanned, topic_name)) is not None:
            extra = paper_day(date, body)
            if day is None:
                day = extra
            else:
                seen = {p["id"] for p in day["papers"]}
                day["papers"] += [p for p in extra["papers"] if p["id"] not in seen]
        if day is not None:
            days.append(day)
    return days


def paper_day(date: str, body: str, source: str = "") -> dict:
    """One day's worth of `### [arXiv:ID](…) — Title (byline)` sections, split per paper.

    `source` is the page (relative to the site root) the section was lifted from,
    so mirrors can point back at the original context.
    """
    intro, papers = split_sections(body, 3)
    return {
        "date": date,
        "pretty_date": pretty_date(date),
        "source": source,
        "intro_html": md_to_html(intro) if intro else "",
        "papers": [
            {
                "id": pid,
                # Fragment ids can't contain a dot, and this also avoids the
                # duplicate-id collision watch.html has from repeated headings.
                "anchor": f"a{pid.replace('.', '-')}" if pid else f"p{i}",
                "title": title,
                "byline": byline,
                "url": f"https://arxiv.org/abs/{pid}" if pid else "",
                "md": text.strip(),
                "html": md_to_html(text.strip()),
            }
            for i, (heading, text) in enumerate(papers)
            for pid, title, byline in [parse_paper_heading(heading)]
        ],
    }


DEEP_DIVE_HEADING = "Deep dives"


def load_deep_dive_days(digests: list[dict]) -> list[dict]:
    """Every digest's "## Deep dives" section, newest first, split per paper.

    `deep_dive.py` appends the section verbatim under that heading and the
    prompt mandates `### arXiv:ID — Title` per paper, so this is the same shape
    as a watch topic. A day whose section has no paper headings (a malformed
    completion) contributes nothing rather than a garbage item. The preamble is
    dropped: unlike a watch topic there is no per-day intro by design, so
    anything in front of the first paper is noise.
    """
    days = []
    for d in digests:
        _, sections = split_sections(d["md"], 2)
        body = next((b for h, b in sections if h.strip() == DEEP_DIVE_HEADING), None)
        if body is None:
            continue
        day = paper_day(d["date"], body, source=f"digest/{d['date']}.html")
        if not day["papers"]:
            print(f"  ! {d['date']}.md: '## {DEEP_DIVE_HEADING}' has no paper headings — skipped",
                  file=sys.stderr)
            continue
        day["intro_html"] = ""
        days.append(day)
    return days


# --- RSS ---


def rfc822(iso: str) -> str:
    """Feed pubDate for a date-keyed post: midnight UTC on that day."""
    d = dt.date.fromisoformat(iso)
    return format_datetime(dt.datetime(d.year, d.month, d.day, tzinfo=dt.timezone.utc))


def feed_html(md_text: str) -> str:
    """Body HTML for a feed item.

    Feed readers don't run KaTeX, so arithmatex would leave raw `\\(…\\)` on
    screen. Flatten the math to Unicode first — the same treatment
    `pipeline.substack` already applies for the other non-KaTeX consumer.
    """
    return md_to_html(latex_to_unicode(md_text))


def topic_feed_items(days: list[dict], base: str, slug: str) -> list[dict]:
    """One item per paper, so the feed reads as a stream of paper alerts."""
    items = []
    for day in days:
        for p in day["papers"]:
            items.append(
                {
                    "title": p["title"] or f"arXiv:{p['id']}",
                    "link": f"{base}{slug}/#{p['anchor']}",
                    "guid": f"arxiv:{p['id']}" if p["id"] else f"{base}{slug}/#{p['anchor']}",
                    "guid_permalink": "false",
                    "pub_date": rfc822(day["date"]),
                    "author": p["byline"],
                    "html": feed_html(p["md"]),
                }
            )
    return items


def digest_feed_items(digests: list[dict], base: str, limit: int = 30) -> list[dict]:
    """One item per daily issue."""
    return [
        {
            "title": d["pretty_date"],
            "link": f"{base}digest/{d['date']}.html",
            "guid": f"{base}digest/{d['date']}.html",
            "guid_permalink": "true",
            "pub_date": rfc822(d["date"]),
            "author": "",
            "html": feed_html(d["md"]),
        }
        for d in digests[:limit]
    ]


MEMORY_TIERS = [
    ("week", "This week", "The last seven days of postings, compressed."),
    ("month", "This month", "The month's trajectories."),
    ("season", "This term", "The academic term, in synthesis."),
    ("year", "This year", "The academic year's long arcs."),
]


def load_memory() -> list[dict]:
    tiers = []
    for name, label, blurb in MEMORY_TIERS:
        path = MEMORY_DIR / f"{name}.md"
        if path.exists():
            tiers.append(
                {"name": name, "label": label, "blurb": blurb,
                 "html": md_to_html(path.read_text())}
            )
    return tiers


def load_memory_archive() -> list[dict]:
    entries = []
    for sub in ("yearly", "seasonal", "monthly", "weekly"):
        for path in sorted((MEMORY_ARCHIVE_DIR / sub).glob("*.md"), reverse=True):
            entries.append({"tier": sub[:-2], "label": path.stem, "html": md_to_html(path.read_text())})
    return entries


def main() -> int:
    cfg = load_config()
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), autoescape=False)
    # Autoescape is off site-wide (page templates emit pre-rendered HTML), so the
    # RSS template escapes its own text nodes through this filter.
    env.filters["xml"] = xml_escape
    watchlist_cfg = cfg.get("watchlist", {})
    topics = watchlist_cfg.get("topics", [])
    base_url = cfg["site"].get("base_url", "")
    deep_dive_cfg = cfg.get("deep_dive", {})
    # The deep-dive mirror is configured like a watch topic (page/slug/theme/
    # tagline) but sourced from the digests, so it's a synthetic topic here.
    deep_dive_topic = (
        {
            "name": DEEP_DIVE_HEADING,
            "slug": deep_dive_cfg.get("slug", "deep-dives"),
            "theme": deep_dive_cfg.get("theme", "default"),
            "tagline": deep_dive_cfg.get("tagline", "The digest's standout picks, read in full"),
            "blurb": deep_dive_cfg.get(
                "blurb",
                "Each issue's picks for a closer read, expanded from the papers' full text "
                "rather than the abstract.",
            ),
        }
        if deep_dive_cfg.get("page") and deep_dive_cfg.get("count", 0) > 0
        else None
    )
    env.globals.update(
        site=cfg["site"],
        categories=cfg["arxiv"]["categories"],
        built_at=dt.datetime.now().strftime("%Y-%m-%d %H:%M"),
        watchlist=watchlist_cfg,
        topics=topics,
        topic_names=[t["name"] for t in topics],
        mirrored={t["name"]: t["slug"] for t in topics if t.get("page")},
        deep_dives=deep_dive_topic,
    )

    digests = load_posts(DIGEST_DIR)
    radar_posts = load_posts(RADAR_DIR) if RADAR_DIR.exists() else []
    watch_posts = load_posts(WATCH_DIR) if WATCH_DIR.exists() else []
    memory_tiers = load_memory()

    # Group the archive by month for the back-issues page.
    by_month: dict[str, list[dict]] = {}
    for d in digests:
        by_month.setdefault(d["date"][:7], []).append(d)
    months = [
        {"label": dt.date.fromisoformat(k + "-01").strftime("%B %Y"), "digests": v}
        for k, v in sorted(by_month.items(), reverse=True)
    ]

    if SITE_DIR.exists():
        shutil.rmtree(SITE_DIR)
    (SITE_DIR / "digest").mkdir(parents=True)

    def render(template: str, out: str, **ctx) -> None:
        (SITE_DIR / out).write_text(env.get_template(template).render(**ctx))

    render(
        "index.html", "index.html",
        digest=digests[0] if digests else None,
        recent=digests[1:8],
        has_radar=bool(radar_posts),
    )
    for i, d in enumerate(digests):
        render(
            "digest.html", f"digest/{d['date']}.html",
            digest=d,
            newer=digests[i - 1] if i > 0 else None,
            older=digests[i + 1] if i + 1 < len(digests) else None,
        )
    render("archive.html", "archive.html", months=months)
    render("radar.html", "radar.html", posts=radar_posts)
    render(
        "memory.html", "memory.html",
        tiers=memory_tiers, archive=load_memory_archive(),
    )
    if watchlist_cfg.get("enabled"):
        render("watch.html", "watch.html", posts=watch_posts)

    render(
        "rss.xml", "feed.xml",
        channel={
            "title": cfg["site"]["title"],
            "link": base_url,
            "description": cfg["site"]["tagline"],
            "self": f"{base_url}feed.xml",
        },
        items=digest_feed_items(digests, base_url),
    )

    # Mirrors: a paper stream rendered as its own page, in its own theme, plus a
    # feed with one item per paper. Any watched topic flagged `page: true` is one;
    # so is the digests' deep-dive section when `deep_dive.page` is set.
    topic_pages = []

    def mirror(topic: dict, days: list[dict]) -> None:
        slug, name = topic["slug"], topic["name"]
        (SITE_DIR / slug).mkdir(parents=True, exist_ok=True)
        render(
            f"topic_{topic.get('theme', 'default')}.html", f"{slug}/index.html",
            topic=topic, days=days, root="../",
        )
        items = topic_feed_items(days, base_url, slug)
        render(
            "rss.xml", f"{slug}/feed.xml",
            channel={
                "title": f"{name} — {cfg['site']['title']}",
                "link": f"{base_url}{slug}/",
                "description": topic.get("tagline", f"{name} papers from arXiv, summarized daily."),
                "self": f"{base_url}{slug}/feed.xml",
            },
            items=items,
        )
        topic_pages.append(f"{slug} ({len(days)} days, {len(items)} papers)")

    if watchlist_cfg.get("enabled"):
        for topic in topics:
            if topic.get("page"):
                mirror(topic, load_topic_days(topic["name"]))
    if deep_dive_topic:
        mirror(deep_dive_topic, load_deep_dive_days(digests))

    if STATIC_DIR.exists():
        shutil.copytree(STATIC_DIR, SITE_DIR / "static")
    print(
        f"Built site/ — {len(digests)} digests, {len(radar_posts)} radar posts, "
        f"{len(watch_posts)} watch posts, {len(memory_tiers)} memory tiers"
        + (f", topic pages: {', '.join(topic_pages)}" if topic_pages else "")
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
