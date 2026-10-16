"""Generate checklist views from docs/CHECKLIST.csv; --pdf needs reportlab."""
import argparse
import csv
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pdf', action='store_true')
    parser.add_argument('--font', type=Path, help='Unicode TrueType font for PDF')
    args = parser.parse_args()
    with (DOCS / 'CHECKLIST.csv').open(encoding='utf-8', newline='') as source:
        tasks = list(csv.DictReader(source))
    ids = [t['id'] for t in tasks]
    assert len(ids) == len(set(ids)), 'Duplicate task IDs'
    for task in tasks:
        assert task['status'] in {'DONE', 'TODO', 'IN PROGRESS', 'BLOCKED', 'NEEDS APPROVAL'}
        assert all(d in ids or d == '—' for d in task['depends_on'].split(','))
    streams = list(dict.fromkeys(t['stream'] for t in tasks))
    path = DOCS / 'FULL_CHECKLIST.md'
    previous = path.read_text(encoding='utf-8')
    intro = previous.split('## Editorial')[0]
    outro = previous[previous.index('## Core product constraints'):]
    lines = [intro.rstrip()]
    for stream in streams:
        lines.append(f'\n## {stream.title()}')
        for t in tasks:
            if t['stream'] == stream:
                lines.append(f"- [{'x' if t['status'] == 'DONE' else ' '}] **{t['id']} · {t['task']}** — `{t['status']}`  \n"
                             f"  Owner: {t['owner']} · Depends: {t['depends_on']} · Pass: {t['acceptance_criteria']}")
    path.write_text('\n'.join(lines) + '\n\n' + outro, encoding='utf-8')
    board_path = DOCS / 'PROJECT_BOARD.html'
    board = board_path.read_text(encoding='utf-8')
    board, count = re.subn(r'const tasks=.*?;const k=', lambda _: 'const tasks=' +
                          json.dumps(tasks, ensure_ascii=False).replace('</', '<\\/') + ';const k=',
                          board, count=1, flags=re.S)
    assert count == 1, 'Board data marker not found'
    board_path.write_text(board, encoding='utf-8')
    if args.pdf:
        if not args.font or not args.font.is_file():
            parser.error('--pdf requires --font pointing to a Unicode TTF')
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import ParagraphStyle
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer
        pdfmetrics.registerFont(TTFont('Checklist', str(args.font)))
        body = ParagraphStyle('body', fontName='Checklist', fontSize=9, leading=13, spaceAfter=4)
        heading = ParagraphStyle('heading', parent=body, fontSize=16, leading=21, spaceBefore=14, spaceAfter=10)
        small = ParagraphStyle('small', parent=body, fontSize=8, leading=11)
        doc = SimpleDocTemplate(str(DOCS / 'CHECKLIST_PRINTABLE.pdf'), pagesize=A4,
                                rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36,
                                title='Cơm nguội — production checklist', author='jasonthedataguy')
        story = [Paragraph('.json / 07 — Cơm nguội', heading),
                 Paragraph('16 October 2026 · Release preparation · Narrator audio required', body),
                 Paragraph('DONE applies to the task acceptance criteria, not final release approval. '
                           'Source of truth: CHECKLIST.csv. Browser checkmarks are local personal notes.', body)]
        for stream in streams:
            story.append(Paragraph(html.escape(stream.title()), heading))
            for t in tasks:
                if t['stream'] == stream:
                    mark = '[x]' if t['status'] == 'DONE' else '[ ]'
                    story.append(KeepTogether([
                        Paragraph(html.escape(f"{mark} {t['id']} / {t['task']} — {t['status']}"), body),
                        Paragraph(html.escape(f"Owner: {t['owner']} · After: {t['depends_on']}"), small),
                        Paragraph(html.escape(t['acceptance_criteria']), small), Spacer(1, 7)]))
        doc.build(story)
    print(f'Generated views for {len(tasks)} tasks; {sum(t["status"] == "DONE" for t in tasks)} done')


if __name__ == '__main__':
    main()
