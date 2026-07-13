# The Cross Section

A daily zeitgeist digest of new arXiv postings — not a paper list, but a read on
*what the field is collectively thinking about today* and how it connects to the
recent past, at multiple timescales.

## How it works

Once a day (GitHub Actions cron), the pipeline:

1. **Fetches** the day's announcements for the categories in `config.yaml`
   (arXiv Atom feeds, free — abstracts only, never PDFs).
2. **Writes the daily digest** in one model call: today's abstracts + rolling
   memory context (week / month / season / year syntheses + last 7 dailies).
3. **Deep-dives** the digest's 3–5 picks from their arXiv HTML renderings.
4. **Refreshes memory tiers**: `week.md` daily; `month.md` on the 1st;
   `season.md` on academic-term boundaries (Sep 1 / Feb 1 / May 1:
   Autumn = Sep–Jan, Spring = Feb–Apr, Summer = May–Aug); `year.md` on Sep 1.
5. **Citation radar** (Fridays): queries INSPIRE-HEP for highly-cited recent
   papers the deep dives missed and covers them.
6. **Rebuilds the static site** into `site/` (committed — the repo is private,
   so open `site/index.html` locally, or read the digests right in GitHub).

All state is files in this repo; the digests and memory tiers double as the
model's context. No server, no database.

## Cost

Development/testing runs on the **Gemini free tier** ($0). Production on
**Claude Opus 4.8** costs roughly **$0.75/day (~$18/month)** for hep-ex+hep-ph:
~40K input tokens for the digest, plus deep dives and the memory refresh.
Levers, cheapest first: `deep_dive.count: 0`, switch `llm.provider`/model
(e.g. `claude-sonnet-5`), or move calls to the Batches API (50% off, future work).

## Running locally

```sh
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

export GEMINI_API_KEY=...        # free key from aistudio.google.com
# or: export ANTHROPIC_API_KEY=...  and set llm.provider: anthropic in config.yaml

python -m pipeline.fetch                 # today's papers → data/YYYY-MM-DD.jsonl
python -m pipeline.digest --dry-run      # token count + cost estimate, no API call
python -m pipeline.digest                # write digests/YYYY-MM-DD.md
python -m pipeline.deep_dive             # expand the digest's picks
python -m pipeline.memory                # refresh rolling syntheses
python -m pipeline.radar                 # (Fridays) INSPIRE citation sweep
python -m pipeline.build_site            # render site/ ; open site/index.html
```

Every stage accepts `--date YYYY-MM-DD` to rerun/backfill from stored data.

## Switching to Claude

Set `llm.provider: anthropic` in `config.yaml` and add the `ANTHROPIC_API_KEY`
secret. Note: prompt tuning for digest voice/synthesis quality should be
re-checked on the Claude backend — models write differently, and the prompts
were drafted with Claude in mind.

## Cross-posting to Substack

Substack has no official posting API, so this uses the unofficial
`python-substack` library, which authenticates with a browser **session
cookie**. Copy your `substack.com` cookies from browser dev tools
(Application → Cookies) as a `name=value; name=value` string:

```sh
export SUBSTACK_COOKIES='...'                    # your session cookie string
python -m pipeline.substack --date 2026-07-09    # creates a DRAFT to review
python -m pipeline.substack --date 2026-07-09 --dry-run   # preview markdown, no cookie needed
python -m pipeline.substack --date 2026-07-09 --publish   # publish + email (opt-in)
```

The default action creates a **draft** you review in Substack's editor; nothing
publishes without `--publish`. `--kind radar|watch` posts those instead, and
`--dry-run` prints the cleaned, paste-ready Markdown (also handy for a manual
copy-paste). Caveats: LaTeX math lands as literal text, and Markdown tables are
converted to bullet lists (the library drops tables otherwise). Set
`substack.publication_url` in `config.yaml` only if you have more than one
publication.

From CI, once the `SUBSTACK_COOKIES` repo secret is set (Settings → Secrets →
Actions), the daily digest workflow automatically mirrors each new issue to
Substack as a **draft** — so there's one waiting to review every morning without
pushing anything. That step never publishes and never fails the run if the
cookie is missing or expired. The separate **Post to Substack** workflow
(`.github/workflows/substack.yml`) is the manual path for backfills, radar/watch
posts, or actually publishing (`publish` input).

## Future ideas

- Hosted private site for the group: Cloudflare Pages + Cloudflare Access
  (free ≤ 50 users). If the site goes public: GitHub Pages toggle.
- Batches API (halves API cost), email/RSS delivery, theme trend charts,
  semantic search over the archive.
