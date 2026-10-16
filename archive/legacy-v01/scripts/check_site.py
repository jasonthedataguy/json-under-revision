"""Check exported links, selected prose, and complete artifact packaging using stdlib."""
import argparse
import html
import json
import re
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.ids, self.paragraphs = [], set(), []
        self.in_story = self.in_paragraph = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f"Duplicate id: {attrs['id']}"
            self.ids.add(attrs['id'])
        for name in ['href', 'src', 'poster']:
            if name in attrs:
                self.links.append(attrs[name])
        if tag == 'article' and 'story' in attrs.get('class', '').split():
            self.in_story = True
        if tag == 'p' and self.in_story:
            self.in_paragraph = True
            self.paragraphs.append('')

    def handle_endtag(self, tag):
        if tag == 'article':
            self.in_story = False
        if tag == 'p':
            self.in_paragraph = False

    def handle_data(self, data):
        if self.in_paragraph:
            self.paragraphs[-1] += data


def normalize(text):
    return ' '.join(text.split())


def check_site(manuscript):
    pages = {path.resolve(): Page(path.read_text(encoding='utf-8')) for path in SITE.rglob('*.html')}
    assert len(pages) == 4, 'Expected index, two chapters and slug alias'
    for path, page in pages.items():
        css_links = re.findall(r'url\([\s\'\"]*([^\)\'\"]+)', path.read_text(encoding='utf-8'))
        for link in page.links + css_links:
            url = urlsplit(html.unescape(link))
            if url.scheme or url.netloc:
                continue
            assert not url.path.startswith('/'), f'Repository-prefix-unsafe link: {link}'
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            assert target.is_relative_to(SITE.resolve()), f'Link escapes published site: {link}'
            if target.is_dir():
                target /= 'index.html'
            assert target.is_file(), f'Broken link in {path}: {link}'
            if url.fragment and target in pages:
                assert unquote(url.fragment) in pages[target].ids, f'Broken anchor: {link}'
    selected = SITE / 'chapters/04/index.html'
    supplied = ROOT / 'Expected_utility/web/index.html'
    assert pages[selected.resolve()].paragraphs == Page(supplied.read_text(encoding='utf-8')).paragraphs, 'Expected_utility prose changed'
    source = (ROOT / 'content' / f'{manuscript}.md').read_text(encoding='utf-8').strip().split('\n\n')[1:]
    actual = pages[(SITE / 'chapters/07/index.html').resolve()].paragraphs
    assert [normalize(p) for p in actual] == [normalize(p) for p in source], 'Cơm nguội prose differs from selection'
    for marker in ['NOT RELEASED', 'NOT FINAL', 'WORKING PROOF', 'Not a released publication']:
        assert marker not in selected.read_text(encoding='utf-8'), f'Stale release label: {marker}'
    files = [p for p in (ROOT / 'Expected_utility').rglob('*') if p.is_file()]
    assert len(files) == 37, 'Selected package inventory changed'
    inventory = json.loads((ROOT / 'docs/chapters/expected-utility/BUNDLE_INVENTORY.json').read_text(encoding='utf-8'))
    assert {item['path'] for item in inventory['files']} == {p.relative_to(ROOT / 'Expected_utility').as_posix() for p in files}
    for item in inventory['files']:
        source = ROOT / 'Expected_utility' / item['path']
        assert source.stat().st_size == item['bytes'] and sha256(source.read_bytes()).hexdigest() == item['sha256'], f"Supplied artifact changed: {item['path']}"
    with ZipFile(SITE / 'chapters/04/files/Expected_utility.zip') as archive:
        assert archive.testzip() is None, 'Corrupt ZIP'
        assert len(archive.namelist()) == len(files) + 1, 'ZIP must include all files and release note'
        for path in files:
            name = path.relative_to(ROOT).as_posix()
            assert sha256(archive.read(name)).digest() == sha256(path.read_bytes()).digest(), f'ZIP differs: {name}'
        assert 'RELEASE.md' in archive.namelist()
    for path in (SITE / 'chapters/04/files').rglob('*'):
        if path.is_file() and path.suffix != '.zip':
            source = ROOT / 'Expected_utility' / path.relative_to(SITE / 'chapters/04/files')
            assert path.read_bytes() == source.read_bytes(), f'Media changed: {path}'
    print(f'PASS: {len(pages)} pages, local links and anchors, both selected manuscripts, 37-file ZIP and media integrity')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--text', choices=['original', 'proposed-edit'], default='proposed-edit')
    check_site(parser.parse_args().text)
