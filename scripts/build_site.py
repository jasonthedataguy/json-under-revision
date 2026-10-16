"""Build the author-selected chapters and their downloadable artifacts."""
import argparse
import html
import re
import shutil
import stat
from pathlib import Path
from build_expected_utility import build_expected_utility, build_landing

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--text', choices=['original', 'proposed-edit'], default='proposed-edit')
args = parser.parse_args()
source = (ROOT / 'content' / f'{args.text}.md').read_text(encoding='utf-8')
paragraphs = source.strip().split('\n\n')[1:]
story = ''.join(f'<p>{html.escape(p)}</p>' for p in paragraphs)
page = (ROOT / 'digital/index.html').read_text(encoding='utf-8')
page = re.sub(r'<article class="story".*?</article>',
              '<article class="story" aria-label="Cơm nguội"><div class="marker">07 / CƠM NGUỘI</div>' + story + '</article>',
              page, flags=re.S)
page = re.sub(r'<figure class="hero">.*?</figure>', '', page, flags=re.S)
start = page.index('<section class="archive"')
end = page.index('</section></main>', start)
page = page[:start] + '''<section class="archive" id="archive"><div class="kicker">REVISIT / GHI CHÚ</div>
<h2>Một ký ức còn lại.</h2><p>Câu chuyện tự nó đã trọn vẹn. Hai tô cơm ở đây là một minh họa, không phải ảnh tư liệu.</p>
<p>Âm thanh dưới đây được tổng hợp cho không gian đọc, không phải bản ghi của gia đình.</p>
<audio controls preload="none" aria-label="Âm thanh không gian được tổng hợp"><source src="assets/room_tone.wav" type="audio/wav"></audio>
''' + page[end:]
page = page.replace('local prototype, not deployed', 'Cơm nguội')
page = page.replace('ONE HABIT. TWO GENERATIONS.', 'MỘT THÓI QUEN. HAI THẾ HỆ.')
page = page.replace('An interpretive illustration, not a record of how the original room looked. Move between three moments from the text.', 'Một minh họa gợi nhớ, không phải tư liệu về căn phòng. Chạm để đi qua ba khoảnh khắc trong câu chuyện.')
page = page.replace('Illustration of two rice bowls on an evening table', 'Minh họa hai tô cơm trên bàn ăn')
memory_line = ('“Tớ để ý rằng bố luôn là người ăn hết tô cơm ấy, còn phần cơm nóng thì để mẹ và tớ ăn.”'
               if args.text == 'original' else
               '“Tớ để ý bố luôn là người ăn hết tô cơm ấy, còn phần cơm nóng thì để mẹ và tớ ăn.”')
page = page.replace('“Tớ để ý bố luôn là người ăn hết tô cơm ấy.”', memory_line)
page = page.replace('</title>', '</title><meta name="description" content="Cơm nguội — một ký ức gia đình trong .json / Jason, under revision.">', 1)
page = page.replace('</style>', 'audio{max-width:100%}</style>', 1)
out = ROOT / 'site'
if out.resolve() != ROOT.resolve() / 'site':
    raise ValueError('site must be a real directory inside the repository')
def remove_readonly(function, path, error):
    if not isinstance(error[1], PermissionError):
        raise error[1]
    Path(path).chmod(stat.S_IWRITE | stat.S_IREAD | stat.S_IEXEC)
    function(path)

if out.exists():
    shutil.rmtree(out, onerror=remove_readonly)
chapter = out / 'chapters/07'
(chapter / 'assets').mkdir(parents=True, exist_ok=True)
for name in ['two_bowls.svg', 'room_tone.wav']:
    shutil.copy2(ROOT / 'digital/assets' / name, chapter / 'assets' / name)
(chapter / 'index.html').write_text(page, encoding='utf-8')
(out / '.nojekyll').touch()
build_expected_utility(ROOT, out)
build_landing(out)
print(f'Built candidate from {args.text}: {chapter}')
