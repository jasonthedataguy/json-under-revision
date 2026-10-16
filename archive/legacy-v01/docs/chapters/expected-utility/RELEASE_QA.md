# Release review — 16 October 2026

Reviewed main at `c64f3a1` and the author-selected `Expected_utility_poster_v02_full_chapter` delivery. The existing site builder omitted Expected_utility and its media; the branch's earlier SVG preview was still the active source. The complete selected package is now the release source.

Resolved findings:

- Imported all 37 supplied files and recorded SHA-256 checksums. Git preserves the package's original bytes, including text newlines.
- Added chapter 04, the readable slug alias, two-chapter index, cross-links and downloadable media/complete ZIP.
- Removed stale author-review/publication labels from the deployed HTML; preserved those labels in the original delivery as historical records.
- Corrected Expected_utility's title sizing at narrow widths, pink-on-paper eyebrow contrast and reset-button toggle semantics.
- Fixed Cơm nguội's audio-player overflow at 320px.
- Updated release/import/status records and social-copy URLs. The earlier project update is archived.
- Added validation before the Pages artifact upload and automatic deployment on pushes to main. Manual manuscript selection remains available for Cơm nguội.

Verified locally:

- Build and standard-library checks: all four exported HTML pages, local asset links, fragment targets, both selected manuscripts, bundle inventory, ZIP contents and media bytes.
- Headless Chromium: index and both chapters at 320, 390, 820 and 1440px without horizontal overflow; images loaded; no JavaScript errors.
- Keyboard activation of both decision branches and reset; Cơm nguội memory buttons; slug redirect; reduced-motion CSS; complete chapter reading without JavaScript.
- All linked chapter 04 downloads returned HTTP 200; MP4 loaded and played in the browser with 720×1280 dimensions and exactly 24 seconds.
- PDF parser: eight A5 pages, final Vietnamese sentence preserved. The supplied contact-sheet preview is historical and includes a ninth preview tile; the actual PDF page count is eight.
- All 26 PNG/JPEG images passed decoding checks. Instagram poster and five carousel slides are 1080×1440.
- Full video decoding: H.264/AAC, 720×1280, 24 fps, 24 seconds; no decoding errors.
- Common credential-pattern scan found no matches in repository source files. Local private media scratch and temporary tooling remain excluded.

The selected artifact is approved for this website release. The PDF remains a layout proof and the video remains an ambient-only animatic. No narration, synchronized captions, print certification, social-platform upload, physical-device test or screen-reader audit is implied. The Pages run provides the deployment result; live HTTPS checks follow deployment.
