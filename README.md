# .json / 07 — Cơm nguội | build kit v0.1

This is the **first complete vertical-slice prototype** for a memoir chapter: book, digital artifact, short-form video.

## Read online

[Read Cơm nguội](https://jasonthedataguy.github.io/json-under-revision/chapters/07/) — original manuscript, published through GitHub Pages. The source repository is public by author choice.

## Open it

- `book/07_com_nguoi_A5_PROOF.pdf`: printable **layout proof** (four A5 pages). Not final press-ready art or PDF/X.
- `digital/index.html`: mobile-first **local** chapter experience. Open in any modern browser; it does not require a server. Tabs, three memory buttons, and room-tone playback work offline.
- `video/com_nguoi_animatic_v01.mp4`: a vertical **animatic proof**, not a finished film. Includes original low-volume synthetic room tone; no recording or author voiceover.
- `video/STORYBOARD.md`: all shots, texts, audio and decisions.
- `docs/FULL_CHECKLIST.md` / `docs/CHECKLIST.csv`: detailed, staged production tasks with owners, dependencies and acceptance criteria.
- `content/original.md`, `content/proposed-edit.md`, `content/EDIT_NOTES.md`: original remains untouched; editorial changes are **not author-approved**.
- `docs/CREATIVE_BRIEF.md`, `docs/chapter-metadata.json`: creative guidelines and asset states.

## What is provisional

The father-child family scene is a **reconstruction** with a not necessarily accurate city view and lighting. The book PDF has lower-than-print-standard artwork; the last page has a **QR SLOT, not a scannable QR**. The original-text chapter is live on GitHub Pages; the local editorial prototype remains available separately. Video is an animatic and cannot substitute for final animated art, voice, mix and captions.

## Steps to release

1. Approve or amend the edited text.
2. Approve the visual storytelling interpretation; clarify any inaccurate invented objects in the provisional art.
3. Create layered production art, print-size exports and social edits.
4. Complete mobile accessibility/performance checks and choose the lasting owned domain; GitHub Pages hosting is already live.
5. Create and device-test a QR only **after** the domain is final. Replace print PDF QR slot.
6. Proof final book sample with printer; complete required video narration and synchronized subtitles.
7. Check permissions, get test reader feedback and release after gates.

## Strategy alignment

Implements the source 21-page `.json immersive product strategy`: **book canonical; chapter artifact adds feeling, context or contradiction; read/explore/revisit; one URL per chapter; test three hero chapters before scaling**.

## License & privacy

Memoir prose stays the author's content. The author chose a **public** repository on 16 October 2026, including drafts and production notes. Public access does not imply approval of provisional art, final print production, or a license to reuse the work.

## Release preparation — 16 October 2026

See [launch review](docs/LAUNCH_REVIEW.md) for inspection findings and outstanding dependencies, and [channel copy](docs/CHANNEL_LAUNCH.md) for prepared YouTube/TikTok descriptions.

Build a public candidate with `python scripts/build_site.py --text original`. Preview it with `python -m http.server 8765 --directory site --bind 127.0.0.1`. The website export contains only the selected chapter assets; the full source kit is also public in GitHub. The [manual Pages workflow](https://github.com/jasonthedataguy/json-under-revision/actions/runs/38878045413) successfully deployed the original text. Channels have not yet been created.

## Required narrator track and checklist updates

Narration is required for the next video export. See the [audio brief](video/NARRATION.md) and [reading draft](video/narration-script.txt). The healwayssmile reference URL is recorded; the existing MP4 still has room tone only.

The [CSV checklist](docs/CHECKLIST.csv) is the status source of truth. Run `python scripts/build_checklists.py` to update Markdown and browser views. With `reportlab` installed, add `--pdf --font /path/to/Unicode.ttf` to regenerate the printable checklist.
