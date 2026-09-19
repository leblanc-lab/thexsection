import datetime as dt
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import feedparser
import httpx

from pipeline import category_backfill as backfill, category_scan as scan, build_site


class BackfillTests(unittest.TestCase):
    def test_resume_empty_days_crosslists_and_merge(self):
        day = dt.date(2000, 1, 1)
        topics = [dict(category=c, name=c, slug=c, keywords=['LHC']) for c in ['cs.AI', 'cs.LG']]
        paper = dict(id='cs/0001001', title='LHC reconstruction', abstract='test', authors=[],
                     categories=['cs.AI','cs.LG'])
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with patch.object(backfill, 'HISTORY_DIR', root/'raw'), patch.object(scan, 'SCAN_DIR', root/'scan'), patch.object(backfill, 'fetch_window', return_value=[(day,paper)]) as fetch:
                backfill.backfill(topics, day, day+dt.timedelta(days=1))
                backfill.backfill(topics, day, day+dt.timedelta(days=1))
                fetch.assert_called_once()
                for topic in topics:
                    self.assertEqual((root/'raw'/topic['slug']/'2000-01-02.jsonl').read_text(), '')
                    history = root/'scan'/topic['slug']/'history'/'2000-01-01.md'
                    # Same paper on live announcement day: only one RSS item survives.
                    (history.parent.parent/'2000-01-02.md').write_text(history.read_text())
                    days = build_site.load_topic_days(topic['name'], history.parent.parent)
                    self.assertEqual(len(days), 1)
                    self.assertEqual(days[0]['date'], '2000-01-01')
                    self.assertEqual(len(build_site.topic_feed_items(days, 'https://example.org/', topic['slug'])),1)

    def test_http_failure_never_creates_checkpoints(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(backfill, 'HISTORY_DIR', Path(tmp)/'raw'), patch.object(backfill, 'fetch_window', side_effect=httpx.HTTPError('406')):
            with self.assertRaises(httpx.HTTPError):
                backfill.backfill([dict(category='cs.AI', slug='cs-ai')], dt.date(2000,1,1), dt.date(2000,1,2))
            self.assertFalse((Path(tmp)/'raw').exists())

    def test_pagination_and_invalid_empty_response(self):
        day = dt.date(2000,1,1)
        def feed(ident, total=2):
            return feedparser.FeedParserDict(bozo=False, feed={'opensearch_totalresults':str(total)}, entries=[dict(id=ident, published='2000-01-01T00:00:00Z', title='LHC', summary='test', tags=[{'term':'cs.AI'}])])
        client = Mock()
        client.get.return_value.status_code = 200
        client.__enter__ = Mock(return_value=client)
        client.__exit__ = Mock(return_value=False)
        with patch.object(backfill.httpx,'Client',return_value=client), patch.object(backfill.time,'sleep'), patch.object(backfill.feedparser,'parse',side_effect=[feed('cs/0001001'),feed('cs/0001002')]):
            self.assertEqual(len(backfill.fetch_window(['cs.AI'],day,day)),2)
        broken = feedparser.FeedParserDict(bozo=False, feed={}, entries=[])
        with patch.object(backfill.httpx,'Client',return_value=client), patch.object(backfill.time,'sleep'), patch.object(backfill.feedparser,'parse',return_value=broken):
            with self.assertRaisesRegex(ValueError,'missing result count'):
                backfill.fetch_window(['cs.AI'],day,day)


if __name__ == '__main__':
    unittest.main()
