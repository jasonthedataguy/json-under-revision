"""Publish the supplied chapter package without changing its source files."""
import shutil
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

PUBLIC_URL = 'https://jasonthedataguy.github.io/json-under-revision/'


def replace_once(page, old, new):
    if page.count(old) != 1:
        raise ValueError(f'Expected exactly one template marker: {old!r}')
    return page.replace(old, new, 1)


def build_expected_utility(root, site):
    bundle = root / 'Expected_utility'
    chapter = site / 'chapters/04'
    shutil.copytree(bundle / 'web/assets', chapter / 'assets')
    page = (bundle / 'web/index.html').read_text(encoding='utf-8')
    replacements = {
        '04 / WORKING PROOF': '04 / EXPECTED_UTILITY',
        'STATUS / AUTHOR REVIEW · NOT RELEASED': '04 / POSTER EDITION',
        'THE STORY / PROPOSED EDIT · NOT FINAL': 'THE STORY / EXPECTED_UTILITY',
        '© Jason / .json · Prototype v0.2 · Not a released publication.': '© Jason / .json · Expected_utility · Poster edition v0.2.',
        '<span>.json / JASON, UNDER REVISION</span>': '<a href="../../">.json / JASON, UNDER REVISION</a>',
        'font-size:clamp(48px,8vw,115px)': 'font-size:clamp(30px,8vw,115px)',
        "b.setAttribute('aria-pressed',String(b.dataset.choice===k))": "if(b.dataset.choice!=='reset')b.setAttribute('aria-pressed',String(b.dataset.choice===k))",
    }
    for old, new in replacements.items():
        page = replace_once(page, old, new)
    page = replace_once(page, '</style>', '''.paper .eyebrow{color:#81516a}.hero h1{overflow-wrap:anywhere}.downloads{border-top:1px solid #577263}.downloads ul{padding-left:22px;line-height:2}.downloads a{overflow-wrap:anywhere}
</style>''')
    page = replace_once(page, '</head>', f'''<link rel="canonical" href="{PUBLIC_URL}chapters/04/">
<meta property="og:title" content="Expected_utility — .json">
<meta property="og:type" content="article">
<meta property="og:url" content="{PUBLIC_URL}chapters/04/">
<meta property="og:image" content="{PUBLIC_URL}chapters/04/assets/hero_wide.jpg">
</head>''')
    page = replace_once(page, '</main>', '''<section class="artifact downloads" id="revisit" aria-labelledby="downloads-title">
<p class="eyebrow">REVISIT / CHAPTER FILES</p><h2 id="downloads-title">Những gì còn lại.</h2>
<p class="intro">Poster, bản dàn trang và những khung hình của chương này.</p>
<ul><li><a href="files/book/04_expected_utility_POSTER_A5_PROOF.pdf">Bản dàn trang A5 — 8 trang (PDF)</a></li>
<li><a href="files/assets/poster_original.png" download>Poster gốc (PNG)</a></li>
<li><a href="files/video/expected_utility_poster_animatic_9x16.mp4">Animatic — 24 giây, âm thanh nền (MP4)</a></li>
<li><a href="files/social/instagram/poster_3x4.jpg" download>Poster 3:4 (JPG)</a> · <a href="files/social/facebook_landscape.jpg" download>Facebook</a> · <a href="files/social/youtube_thumbnail.jpg" download>YouTube</a></li>
<li>Carousel: <a href="files/social/instagram/slide_01_3x4.jpg" download>01</a> · <a href="files/social/instagram/slide_02_3x4.jpg" download>02</a> · <a href="files/social/instagram/slide_03_3x4.jpg" download>03</a> · <a href="files/social/instagram/slide_04_3x4.jpg" download>04</a> · <a href="files/social/instagram/slide_05_3x4.jpg" download>05</a></li>
<li><a href="files/Expected_utility.zip" download>Toàn bộ bộ tài liệu chương (ZIP, khoảng 21 MB)</a></li></ul>
<p class="notes">PDF là bản dàn trang thử. Video có âm thanh nền tổng hợp, chưa có giọng đọc hay phụ đề đồng bộ.</p>
<p><a href="../../">← Mục lục .json</a> · <a href="../07/">Cơm nguội →</a></p></section></main>''')
    (chapter / 'index.html').write_text(page, encoding='utf-8')
    for directory in ['assets', 'book', 'social', 'video']:
        shutil.copytree(bundle / directory, chapter / 'files' / directory)
    with ZipFile(chapter / 'files/Expected_utility.zip', 'w', compression=ZIP_DEFLATED) as archive:
        for path in sorted(bundle.rglob('*')):
            if path.is_file():
                archive.write(path, Path('Expected_utility') / path.relative_to(bundle))
        archive.write(root / 'docs/chapters/expected-utility/RELEASE.md', 'RELEASE.md')
    alias = site / 'chapters/expected-utility'
    alias.mkdir(parents=True)
    (alias / 'index.html').write_text(f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0;url=../04/"><link rel="canonical" href="{PUBLIC_URL}chapters/04/"><title>Expected_utility</title></head><body><a href="../04/">Đọc Expected_utility →</a></body></html>''', encoding='utf-8')
    # Expose the existing chapter's proof media alongside the newly published pack.
    other = site / 'chapters/07'
    (other / 'files').mkdir()
    for name in ['book/07_com_nguoi_A5_PROOF.pdf', 'video/com_nguoi_animatic_v01.mp4']:
        shutil.copy2(root / name, other / 'files' / Path(name).name)
    other_page = (other / 'index.html').read_text(encoding='utf-8')
    other_page = replace_once(other_page, '</section></main>', '''<p><a href="files/07_com_nguoi_A5_PROOF.pdf">Bản dàn trang A5 (PDF)</a> · <a href="files/com_nguoi_animatic_v01.mp4">Animatic có âm thanh nền (MP4)</a></p><p><a href="../../">← Mục lục .json</a> · <a href="../04/">Expected_utility →</a></p></section></main>''')
    (other / 'index.html').write_text(other_page, encoding='utf-8')
    print('Built Expected_utility from the selected final package, with all supplied media')


def build_landing(site):
    (site / 'index.html').write_text('''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#0c2c24"><meta name="description" content=".json — Jason, under revision. Những câu chuyện và những gì còn lại."><title>.json — Jason, under revision</title><style>
*{box-sizing:border-box}body{margin:0;background:#f4ead5;color:#192e28;font:19px/1.7 Georgia,serif}main{max-width:1000px;margin:8vh auto;padding:24px}h1{font-size:clamp(64px,12vw,112px);line-height:1;margin:0}a{color:inherit}a:focus-visible{outline:3px solid #81516a;outline-offset:5px}.intro{max-width:620px;margin-bottom:48px}.chapters{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:28px}.card{border:1px solid #7e8d7a;text-decoration:none;display:block}.card img{width:100%;height:220px;object-fit:cover;display:block;background:#0c2c24}.copy{padding:22px}.copy h2{font-size:28px;margin:6px 0;overflow-wrap:anywhere}.copy p{margin:0}.number{font:12px monospace;letter-spacing:.15em}footer{margin-top:56px;font:12px/1.8 monospace}</style></head><body><main><h1>.json</h1><div class="intro"><p>Jason, under revision</p><p>Một cuốn sách với lịch sử phiên bản.<br>Những câu chuyện và những gì còn lại.</p></div><nav class="chapters" aria-label="Các chương">
<a class="card" href="chapters/04/"><img src="chapters/04/assets/hero_wide.jpg" alt="Minh họa một người viết code bên cà phê và những cuốn sách" width="1600" height="860"><div class="copy"><span class="number">04 / MODEL SPECIFICATION</span><h2>Expected_utility</h2><p>Về trái tim, lý trí và những quyết định mà ta không bao giờ biết kết quả.</p></div></a>
<a class="card" href="chapters/07/"><img src="chapters/07/assets/two_bowls.svg" alt="Minh họa hai tô cơm trên bàn ăn" width="1600" height="860"><div class="copy"><span class="number">07 / MEMORY</span><h2>Cơm nguội</h2><p>Một thói quen. Hai thế hệ.</p></div></a></nav><footer>© Jason / .json — Jason, under revision</footer></main></body></html>''', encoding='utf-8')
