"""A complete manuscript can be published before its multimedia products exist."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from build_site import render_chapter, reader_release

class ReaderReleaseTests(unittest.TestCase):
    def test_reader_needs_no_original_essay_or_unfinished_media(self):
        with tempfile.TemporaryDirectory() as temporary:
            chapter=Path(temporary)
            (chapter/'source').mkdir()
            (chapter/'source/approved.md').write_text('# A chapter\n\nA complete story.\n',encoding='utf-8')
            (chapter/'source/draft-v01.md').write_text('# A chapter\n\nAn earlier draft.\n',encoding='utf-8')
            (chapter/'source/revisions.log').write_text('Selected for publication.',encoding='utf-8')
            (chapter/'production.json').write_text(json.dumps({'memory':{'heading':'A journey','intro':'Explore','moments':[{'title':'Arrival','image':'artwork/scenes/arrival.jpg','alt':'A bridge','quote':'A complete story.'}]}}),encoding='utf-8')
            meta={'release_stage':'reader','canonical_text':'source/approved.md','history_text':'source/draft-v01.md','history_label':'First draft','title':'A chapter','subtitle':'A story','number':'03','canonical_path':'chapters/03/','palette':{'dark':'#123','paper':'#eee','accent':'#faa','ink':'#123'},'theme':['memory'],'artifact':'memory','revision_note':'Selected from the proposed draft.'}
            page,_=render_chapter(chapter,meta,{'public_url':'https://example.org/book/'},meta)
            self.assertIn('<p>A complete story.</p>',page)
            self.assertIn('<summary>First draft</summary>',page)
            self.assertIn('<p>An earlier draft.</p>',page)
            self.assertIn('data-memory="0"',page)
            self.assertIn('source/approved.md',page)
            for unavailable in ['original.md','<video','<audio','product-set.zip','chapter-A5-proof.pdf','social/instagram']:
                self.assertNotIn(unavailable,page)

    def test_existing_chapters_keep_multimedia_release(self):
        self.assertFalse(reader_release({}))
        with self.assertRaises(ValueError):reader_release({'release_stage':'unknown'})

if __name__=='__main__':unittest.main()
