# The Cross Section

**Subscribe on Substack: https://thexsection.substack.com**
Read the archive: https://leblanc-lab.github.io/thexsection/ (RSS: [`feed.xml`](https://leblanc-lab.github.io/thexsection/feed.xml))

A daily digest and trend analysis of new hep-ex and hep-ph postings on arXiv.
It isn't a paper list. It's a read on *what the field is collectively thinking about
today* and how that connects to the recent past, at multiple timescales.

Digests are written by an LLM (Claude) from arXiv abstracts and full-text HTML.
Treat them as a starting point, not a substitute for reading the papers.

## How it works

Every posting day a GitHub Actions job:

1. **Fetches** the day's announcements (arXiv feeds; abstracts only, never PDFs).
2. **Writes the digest** from today's abstracts plus rolling memory: the last
   week of digests and week / month / academic-term / year syntheses.
3. **Deep-dives** the digest's picks from their arXiv HTML renderings.
4. **Refreshes the memory tiers.** On Fridays it also runs a **citation radar**
   (INSPIRE-HEP) for highly cited recent papers the deep dives missed, and the
   week's synthesis becomes the weekend *Long View* post.
5. **Rebuilds the static site** in `site/`, which deploys to GitHub Pages, and
   drafts the issue to Substack for review.

There's no server. Everything published is a file in this repo, and the
digests and memory files double as the model's context for the next day.

## Running it

```sh
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...   # or GEMINI_API_KEY with llm.provider: gemini

python -m pipeline.fetch                # today's papers → data/YYYY-MM-DD.jsonl
python -m pipeline.digest --dry-run     # token count + cost estimate, no API call
python -m pipeline.digest               # → digests/YYYY-MM-DD.md
python -m pipeline.deep_dive
python -m pipeline.memory
python -m pipeline.build_site           # → site/
```

Every stage takes `--date YYYY-MM-DD` to rerun from stored data. Everything
else (categories, models, token budgets, Batches API, page options) is set in
`config.yaml`, which is commented throughout. On Claude Opus 5.5 with the
Batches API a day costs well under a dollar.

## Substack

`python -m pipeline.substack` posts an issue through the unofficial
`python-substack` library, authenticated with a browser session cookie
(`SUBSTACK_COOKIES`). It creates a **draft** by default; `--publish` is opt-in,
and `--dry-run` prints the Markdown without needing a cookie. `--kind`
selects `digest`, `radar` or `longview`. The nightly workflow drafts each
issue automatically when the cookie secret is set.

## License

Code is [MIT](LICENSE). The written content (digests, memory, posts and the
generated site) is [CC BY 4.0](LICENSE-CONTENT). Titles, authors and abstracts
quoted from arXiv stay under arXiv's own terms.
