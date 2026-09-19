import tempfile
from contextlib import closing
import unittest
from pathlib import Path
from unittest.mock import patch, Mock

from pipeline import category_harvest as harvest, build_site


def page(token='next'):
    return f'''<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/">
<ListRecords><record><header><identifier>oai:arXiv.org:cs/0001001</identifier>
<datestamp>2005-09-16</datestamp></header><metadata>
<arXiv xmlns="http://arxiv.org/OAI/arXiv/"><id>cs/0001001</id>
<created>2000-01-01</created><title>LHC &amp; learning</title>
<abstract>Collider results.</abstract><categories>cs.AI cs.LG</categories>
<authors><author><forenames>Jesse</forenames><keyname>Thaler</keyname></author></authors>
</arXiv></metadata></record><resumptionToken>{token}</resumptionToken></ListRecords></OAI-PMH>'''


class HarvestTests(unittest.TestCase):
    def test_transactional_pages_dedup_submission_dates_and_render(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            with closing(harvest.connect(root/'test.db')) as db, patch.object(harvest,'SCAN_DIR',root/'scan'):
                self.assertEqual(harvest.save_page(db,'cs.AI',page()),(1,True))
                self.assertEqual(harvest.save_page(db,'cs.AI',page('')),(1,False))
                self.assertEqual(db.execute('SELECT COUNT(*) FROM papers').fetchone()[0],1)
                self.assertEqual(db.execute('SELECT complete FROM state').fetchone()[0],1)
                topic=dict(category='cs.AI',name='cs.AI',slug='cs-ai',keywords=['LHC'])
                self.assertEqual(harvest.render_history(db,topic),1)
                days=build_site.load_topic_days('cs.AI',root/'scan'/'cs-ai')
                self.assertEqual(days[0]['date'],'2000-01-01')
                self.assertEqual(days[0]['papers'][0]['id'],'cs/0001001')
                topic['keywords']=[]
                self.assertEqual(harvest.render_history(db,topic),0)
                self.assertEqual(build_site.load_topic_days('cs.AI',root/'scan'/'cs-ai'),[])

    def test_page_limit_and_resume_use_saved_token(self):
        with tempfile.TemporaryDirectory() as tmp, closing(harvest.connect(Path(tmp)/'test.db')) as db:
            topic=dict(category='cs.AI',name='cs.AI',slug='cs-ai',keywords=['LHC'])
            client=Mock()
            client.__enter__=Mock(return_value=client)
            client.__exit__=Mock(return_value=False)
            client.get.return_value.status_code=200
            client.get.return_value.content=page()
            with patch.object(harvest.httpx,'Client',return_value=client), patch.object(harvest.time,'sleep') as sleep, patch.object(harvest,'render_history',return_value=1):
                harvest.harvest(db,[topic],max_pages=1)
                self.assertEqual(client.get.call_count,1)
                sleep.assert_called_with(5.0)
                client.get.return_value.content=page('')
                harvest.harvest(db,[topic],max_pages=1)
                self.assertEqual(client.get.call_args.kwargs['params'], {'verb':'ListRecords','resumptionToken':'next'})
                harvest.harvest(db,[topic],max_pages=1)
                self.assertEqual(client.get.call_count,2)
                self.assertEqual(db.execute('SELECT complete FROM state').fetchone()[0],1)

    def test_bad_page_does_not_advance_checkpoint(self):
        with tempfile.TemporaryDirectory() as tmp, closing(harvest.connect(Path(tmp)/'test.db')) as db:
            harvest.save_page(db,'cs.AI',page())
            with self.assertRaises(ValueError):
                harvest.save_page(db,'cs.AI',page().replace('<abstract>Collider results.</abstract>',''))
            self.assertEqual(db.execute('SELECT token,pages FROM state').fetchone(),('next',1))

    def test_expired_token_and_server_pause(self):
        with self.assertRaises(harvest.ExpiredToken):
            harvest.parse_page('<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/"><error code="badResumptionToken">expired</error></OAI-PMH>','cs.AI')
        with tempfile.TemporaryDirectory() as tmp, closing(harvest.connect(Path(tmp)/'test.db')) as db:
            topic=dict(category='cs.AI',name='cs.AI',slug='cs-ai',keywords=['LHC'])
            client=Mock()
            client.__enter__=Mock(return_value=client)
            client.__exit__=Mock(return_value=False)
            client.get.return_value.status_code=429
            client.get.return_value.headers={'retry-after':'60'}
            with patch.object(harvest.httpx,'Client',return_value=client),patch.object(harvest.time,'sleep'):
                with self.assertRaisesRegex(RuntimeError,'Retry-After=60'):
                    harvest.harvest(db,[topic])
            self.assertEqual(db.execute('SELECT COUNT(*) FROM state').fetchone()[0],0)
            client.get.assert_called_once()


if __name__=='__main__':
    unittest.main()
