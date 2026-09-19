import datetime as dt
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from pipeline import category_scan as scan, build_site, common


class CategoryScanTests(unittest.TestCase):
    def setUp(self):
        self.cfg = common.load_config()
        self.topics = scan.category_topics(self.cfg)

    def test_inherited_and_extra_criteria(self):
        papers = [dict(id=f"2609.{i:05}", title=title, abstract="", authors=authors)
                  for i, (title, authors) in enumerate([
                      ("Wasserstein geometry", []), ("Unrelated", ["Jesse Thaler"]),
                      ("LHC measurements", []), ("Future colliders", []),
                      ("Unrelated", []), ("much better", [])])]
        for topic in self.topics:
            hits = scan.scan_day(papers, [topic], {})[topic['name']]
            self.assertEqual([p['id'] for p, _ in hits], [f"2609.{i:05}" for i in range(4)])
        self.assertEqual(self.cfg['arxiv']['categories'], ['hep-ex', 'hep-ph'])

    def test_overrides(self):
        self.cfg['category_scan']['feeds'][0].update(keywords=[], authors=['Test Author'])
        topic = scan.category_topics(self.cfg)[0]
        self.assertEqual(topic['keywords'], [])
        self.assertEqual(topic['authors'], ['Test Author'])
        self.cfg['category_scan']['enabled'] = False
        self.assertEqual(scan.category_topics(self.cfg), [])

    def test_isolation_render_rss_and_rescan_removal(self):
        with tempfile.TemporaryDirectory() as tmp, patch('pipeline.llm.LLM', side_effect=AssertionError('LLM forbidden')):
            root = Path(tmp)
            topic = self.topics[0]
            path = root / 'data' / 'category-scan' / topic['slug'] / '2026-09-18.jsonl'
            path.parent.mkdir(parents=True)
            path.write_text(json.dumps(dict(id='2609.12345', title='LHC & detectors',
                                           abstract='A < B & C', authors=['Jesse Thaler']))+'\n')
            with patch.object(scan, 'SCAN_DIR', root/'watch'), patch.object(common, 'DATA_DIR', root/'data'), patch.object(common, 'BACKFILL_DIR', root/'backfill'):
                self.assertEqual(common.load_papers(dt.date(2026, 9, 18)), [])
                self.assertEqual(common.paper_dates(), [])
                self.assertEqual(scan.scan_file(path, topic), 1)
                days = build_site.load_topic_days(topic['name'], root/'watch'/topic['slug'])
                self.assertEqual(len(days), 1)
                self.assertIn('no AI summary', days[0]['papers'][0]['html'])
                items = build_site.topic_feed_items(days, 'https://example.org/', topic['slug'])
                self.assertEqual(len(items), 1)
                repeated = path.with_name('2026-09-19.jsonl')
                repeated.write_text(path.read_text())
                scan.scan_file(repeated, topic)
                days = build_site.load_topic_days(topic['name'], root/'watch'/topic['slug'])
                self.assertEqual(len(days), 1)
                self.assertEqual(days[0]['date'], '2026-09-18')
                repeated.write_text('')
                scan.scan_file(repeated, topic)
                path.write_text('')
                self.assertEqual(scan.scan_file(path, topic), 0)
                self.assertEqual(build_site.load_topic_days(topic['name'], root/'watch'/topic['slug']), [])

    def test_fetch_deduplicates_and_filters_replacements(self):
        entry = dict(id='https://arxiv.org/abs/2609.12345v1', title='LHC', summary='Abstract: test',
                     arxiv_announce_type='new')
        response = unittest.mock.Mock(content=b'feed')
        feed = unittest.mock.Mock(bozo=False, version='atom10', entries=[entry, entry, dict(entry, id='2609.99999', arxiv_announce_type='replace')])
        with patch.object(scan.httpx, 'get', return_value=response), patch.object(scan.feedparser, 'parse', return_value=feed):
            self.assertEqual(len(scan.fetch_category('cs.LG', ['new', 'cross'])), 1)
            feed.bozo = True
            with self.assertRaises(ValueError):
                scan.fetch_category('cs.LG', ['new', 'cross'])


if __name__ == '__main__':
    unittest.main()
