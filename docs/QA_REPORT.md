# QA report — Cơm nguội v0.1

## Verified
- A5 PDF: 4 pages rendered to PNG, inspected as contact sheet. Vietnamese accents rendered; no visibly clipped prose.
- Video: 24.0s, H.264, 720×1280, 24 fps, AAC audio, playable MP4; inspected extracted frame.
- Mobile HTML: browser-rendered at 390×844; page title and 10 paragraph tags verified; memory-scene switch and original/revision tab functionality verified with injected local image assets.
- Digital sound: original synthesized sound study is included as WAV; not actual historic or author recording.
- Source is preserved separately. The text on the PDF is the *proposed edited version*, not approved canonical manuscript.

## Not verified / outstanding
- Browser navigation to file:// and localhost was blocked by the testing environment. Browser QA used `page.set_content` and data-uri images instead. Actual deployed HTTP/HTTPS loading is **untested**.
- No iOS/Android real-device test, screen-reader test, performance audit or QR test.
- Final original-layer artwork, 300-dpi/CMYK preparation and printer preflight absent.
- Narration, licensed music, final motion graphics and social exports absent.
- Privacy, rights, author edits and family-artistic fidelity approval pending.

## Human approval request
1. Is the edited chapter text acceptable as canonical, or preserve the original verbatim?
2. Does the father/child in a lamp-lit apartment and city view feel emotionally accurate despite being a fictionalized visual setting?
3. Do you want the companion mainly visual/quiet, or to add your own voice recording?
