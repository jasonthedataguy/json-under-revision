# QA report — Cơm nguội v0.1

## Verified
- A5 PDF: 4 pages rendered to PNG, inspected as contact sheet. Vietnamese accents rendered; no visibly clipped prose.
- Video: 24.0s, H.264, 720×1280, 24 fps, AAC audio, playable MP4; inspected extracted frame.
- Mobile HTML: browser-rendered at 390×844; page title and 10 paragraph tags verified; memory-scene switch and original/revision tab functionality verified with injected local image assets.
- Digital sound: original synthesized sound study is included as WAV; not actual historic or author recording.
- Source is preserved separately. The text on the PDF is the *proposed edited version*, not approved canonical manuscript.

## Not verified / outstanding
- Follow-up local HTTP checks passed at 390/820/1440px: ten original paragraphs, image/audio loading, memory switching and no horizontal overflow. Equivalent live HTTPS checks now pass at [the published chapter](https://jasonthedataguy.github.io/json-under-revision/chapters/07/): original prose, images, audio HTTP response, landing response, memory state and no overflow at the same widths. Real-device audio playback is still unverified.
- No iOS/Android real-device test, screen-reader test, performance audit or QR test.
- Final original-layer artwork, 300-dpi/CMYK preparation and printer preflight absent.
- Narration, licensed music, final motion graphics and social exports absent.
- Privacy, rights, author edits and family-artistic fidelity approval pending.

## Human approval request
1. Is the edited chapter text acceptable as canonical, or preserve the original verbatim?
2. Does the father/child in a lamp-lit apartment and city view feel emotionally accurate despite being a fictionalized visual setting?
3. Narrator audio is now required. Reference URL supplied; speaker/time range and recording/generation method remain pending. No narrator has been generated or mixed yet.
