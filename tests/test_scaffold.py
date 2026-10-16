import contextlib
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import new_chapter
from common import inline,safe_path

class ChapterScaffoldTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)
        shutil.copytree(new_chapter.ROOT/'templates',self.root/'templates')
        (self.root/'book.json').write_text('{"chapters":[]}',encoding='utf-8')
    def tearDown(self):self.temp.cleanup()
    def invoke(self,slug='new-memory',number='09'):
        with patch.object(new_chapter,'ROOT',self.root),patch.object(sys,'argv',['new_chapter','--slug',slug,'--number',number,'--title','A new memory']),contextlib.redirect_stdout(io.StringIO()),contextlib.redirect_stderr(io.StringIO()):
            new_chapter.main()
    def test_new_chapter_is_registered_but_not_published(self):
        self.invoke()
        meta=json.loads((self.root/'chapters/new-memory/chapter.json').read_text())
        self.assertFalse(meta['publish'])
        self.assertEqual(meta['canonical_path'],'chapters/09/')
        self.assertEqual(json.loads((self.root/'book.json').read_text())['chapters'],['new-memory'])
        for name in ['source','artwork/source','audio','video','book','web','docs','social/instagram']:
            self.assertTrue((self.root/'chapters/new-memory'/name).is_dir())
    def test_duplicate_keeps_existing_manuscript(self):
        self.invoke();source=self.root/'chapters/new-memory/source/original.md';source.write_text('An irreplaceable manuscript')
        with self.assertRaises(SystemExit):self.invoke()
        self.assertEqual(source.read_text(),'An irreplaceable manuscript')
    def test_duplicate_number_does_not_create_folder(self):
        self.invoke()
        with self.assertRaises(SystemExit):self.invoke('different-memory')
        self.assertFalse((self.root/'chapters/different-memory').exists())
    def test_slug_cannot_escape_chapter_directory(self):
        with self.assertRaises(SystemExit):self.invoke('../outside')
        self.assertEqual(json.loads((self.root/'book.json').read_text())['chapters'],[])
    def test_media_reference_cannot_escape_folder(self):
        with self.assertRaises(ValueError):safe_path(self.root,'../outside.wav')
    def test_manuscript_markup_cannot_become_script(self):
        rendered=inline('<script>alert(1)</script> *memory* `x < y`')
        self.assertNotIn('<script>',rendered)
        self.assertIn('<em>memory</em>',rendered)
        self.assertIn('<code>x &lt; y</code>',rendered)

if __name__=='__main__':unittest.main()
