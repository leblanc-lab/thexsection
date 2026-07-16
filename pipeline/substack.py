"""Push a digest (or radar / watch post) to Substack as a draft.

Uses the unofficial `python-substack` library, which authenticates with a
browser *session cookie* — Substack has no official posting API. Supply the
cookie via the SUBSTACK_COOKIES env var (copy it from your browser dev tools:
Application → Cookies → substack.com, as a "name=value; name=value" string).
Nothing is hardcoded and the cookie is never printed.

By default this creates a **draft** you review in Substack's editor; it never
publishes on its own. `--publish` opts in to publishing (and emailing) an issue.

`--dry-run` prints the cleaned, paste-ready Markdown without touching the
network or needing a cookie — useful for a manual copy-paste, or to preview
exactly what would be sent.

Known limitations of the Markdown → Substack conversion:
  - LaTeX math ($...$) lands as literal text; fix it in the draft editor, or
    leave it — Substack renders inline $...$ in its own editor for many cases.
  - Markdown tables aren't supported by the library, so we convert them to
    bullet lists before sending (otherwise they'd be silently dropped).
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
from pathlib import Path

import frontmatter

from .common import DIGEST_DIR, digest_path, load_config, parse_date

WATCH_DIR = DIGEST_DIR.parent / "watch"
RADAR_DIR = DIGEST_DIR / "radar"

TABLE_ROW_RE = re.compile(r"^\s*\|(.+)\|\s*$")
TABLE_SEP_RE = re.compile(r"^\s*\|?[\s:|-]+\|?\s*$")


def pretty_date(iso: str) -> str:
    return dt.date.fromisoformat(iso).strftime("%A, %B %-d, %Y")


def tables_to_lists(md: str) -> str:
    """Rewrite GitHub-style pipe tables as bullet lists.

    The Substack library ignores tables entirely, so left alone they vanish.
    A data row `| a | b | c |` becomes `- a — b — c`, preserving each cell's own
    Markdown; the header and `|---|` separator rows are dropped.
    """
    out: list[str] = []
    row_block: list[list[str]] = []

    def flush() -> None:
        for cells in row_block:
            bullet = "- " + " — ".join(c for c in cells if c)
            out.append(bullet)
        row_block.clear()

    lines = md.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        m = TABLE_ROW_RE.match(line)
        if m and i + 1 < len(lines) and TABLE_SEP_RE.match(lines[i + 1]) and "|" in lines[i + 1]:
            # Header row + separator + data rows: gather the whole table.
            i += 2  # skip header and separator
            while i < len(lines) and TABLE_ROW_RE.match(lines[i]):
                cells = [c.strip() for c in TABLE_ROW_RE.match(lines[i]).group(1).split("|")]
                row_block.append(cells)
                i += 1
            flush()
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


KIND_DIRS = {"digest": DIGEST_DIR, "radar": RADAR_DIR, "watch": WATCH_DIR}


def load_source(kind: str, date: dt.date) -> tuple[frontmatter.Post, Path]:
    path = KIND_DIRS[kind] / f"{date.isoformat()}.md"
    if not path.exists():
        raise FileNotFoundError(path)
    return frontmatter.load(path), path


def theme_text(theme) -> str:
    """A theme is normally a string, but a theme containing a colon (e.g.
    "Hadron spectroscopy: new states") is parsed by YAML as a one-key mapping.
    Flatten that back to "key: value" so it renders as the author intended."""
    if isinstance(theme, dict):
        return "; ".join(f"{k}: {v}" for k, v in theme.items())
    return str(theme)


def build_title_subtitle(kind: str, post: frontmatter.Post, cfg: dict) -> tuple[str, str]:
    when = pretty_date(post.get("date") or post.metadata.get("date"))
    site_title = cfg["site"]["title"]
    if kind == "digest":
        themes = [theme_text(t) for t in (post.get("themes", []) or [])]
        return when, " · ".join(themes) if themes else cfg["site"]["tagline"]
    if kind == "radar":
        return f"Citation radar — week of {when}", f"{site_title}: what the field is citing"
    return f"{cfg.get('watchlist', {}).get('page_title', 'Watch')} — {when}", site_title


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--date", help="YYYY-MM-DD (default: today)")
    ap.add_argument("--kind", choices=list(KIND_DIRS), default="digest", help="which post to send")
    ap.add_argument("--title", help="override the draft title")
    ap.add_argument("--subtitle", help="override the draft subtitle")
    ap.add_argument("--dry-run", action="store_true", help="print cleaned markdown; no network, no cookie needed")
    ap.add_argument("--publish", action="store_true", help="publish (and email) instead of leaving a draft")
    ap.add_argument("--no-send", action="store_true", help="with --publish, don't email subscribers")
    args = ap.parse_args()

    cfg = load_config()
    date = parse_date(args.date)

    try:
        post, path = load_source(args.kind, date)
    except FileNotFoundError as e:
        print(f"No {args.kind} at {e} — nothing to send.")
        return 0

    title = args.title or None
    subtitle = args.subtitle or None
    if not title or not subtitle:
        auto_title, auto_subtitle = build_title_subtitle(args.kind, post, cfg)
        title = title or auto_title
        subtitle = subtitle or auto_subtitle

    body = tables_to_lists(post.content.strip())

    if args.dry_run:
        print(f"# {title}\n_{subtitle}_\n\n{body}")
        print(f"\n---\n[dry-run] would create a {'published post' if args.publish else 'draft'} "
              f"from {path} ({len(body)} chars)", file=sys.stderr)
        return 0

    cookies = os.environ.get("SUBSTACK_COOKIES")
    if not cookies:
        print("SUBSTACK_COOKIES is not set. Copy your substack.com session cookies from "
              "browser dev tools (a 'name=value; name=value' string) into that env var, "
              "then re-run. Use --dry-run to preview without a cookie.", file=sys.stderr)
        return 1

    pub_url = cfg.get("substack", {}).get("publication_url") or os.environ.get("SUBSTACK_PUBLICATION_URL")

    try:
        from substack import Api
    except ImportError:
        print("python-substack is not installed (pip install python-substack).", file=sys.stderr)
        return 1

    api = Api(cookies_string=cookies, publication_url=pub_url)
    result = api.create_draft_from_markdown(
        title=title,
        markdown=body,
        subtitle=subtitle,
        publish=args.publish,
        send=not args.no_send,
    )
    draft_id = (result.get("draft") or {}).get("id")
    if args.publish:
        print(f"Published '{title}' (draft id {draft_id}).")
    else:
        print(f"Created draft '{title}' (id {draft_id}) — review it in Substack before publishing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
