# Fashion v0.1 — QA / binary import manifest

## QA completed in local production
- ReportLab PDF A5: **9 pages**, chapter ends in `Peace and love!`; source text retained. Rendering/contact-sheet review completed.
- Responsive reader loaded via self-contained Chromium test on **390px** and **1440px**: **14 body paragraphs**, original/editorial switch works, **6** Wardrobe Explorer controls, no horizontal overflow, no runtime JS errors.
- MP4: **24.000s, 720×1280, H.264/AAC**, synthetic ambient sound only. Not narrated.
- Instagram: **five 1080×1440 (3:4) JPEGs**; Facebook graphic 1600×900; YouTube thumbnail 1280×720.
- Six spot illustrations + custom cover poster locally generated and shipped in author review ZIP.

## From local ZIP -> optional repository import AFTER approval
| ZIP artifact | Repository destination |
|---|---|
| `art/01_cover_FASHION.png` | `digital/chapters/fashion/assets/cover.png` |
| `art/scene_*.png` | `digital/chapters/fashion/assets/scenes/` |
| `book/02_Fashion_illustrated_A5_PROOF.pdf` | `book/02_Fashion_A5_PROOF.pdf` |
| `web/index.html`, `web/assets/*` | `digital/chapters/fashion/` |
| `social/instagram/slide_*_3x4.jpg` | `social/fashion/instagram/` |
| `social/facebook_1600x900.jpg` | `social/fashion/facebook_1600x900.jpg` |
| `social/youtube_thumbnail_1280x720.jpg` | `social/fashion/youtube_thumbnail_1280x720.jpg` |
| `video/02_Fashion_ANIMATIC_9x16.mp4` | `video/fashion/ANIMATIC_ONLY.mp4` |

This connector environment cannot directly transfer local JPG/PNG/PDF/MP4 bytes into the GitHub repo; the binary kit remains downloadable through the conversation. The PR is source/docs only until approved binaries are imported in Codex or local git.

## Known release blockers
- No author-approved canonical manuscript or website publication scope.
- No external claim/third-party quote clearance where needed.
- No final studio art with editable layered files.
- No voiceover, synchronized spoken subtitles or 1080×1920 final social export.
- No print vendor preflight, physical proof or permanent QR.
- No live public chapter URL or posted social platforms.

**Do not label this PR deployed, commercially licensed, narrated or printer-ready.**
