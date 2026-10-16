# Chapter 03 reader release

The author selected the current manuscript by requesting deployment and homepage publication on 2026-10-16. `source/approved.md` preserves all 36 paragraphs from `source/draft-v01.md` unchanged. The original essay mentioned in the historical board remains unavailable; the website labels its actual first draft accurately.

- Reader URL: https://jasonthedataguy.github.io/json-under-revision/chapters/03/
- Slug alias: https://jasonthedataguy.github.io/json-under-revision/chapters/viet-cho-sai-gon-cua-t/
- Homepage: https://jasonthedataguy.github.io/json-under-revision/

The release includes the complete prose, a homepage card, responsive supplied-art crops, eight keyboard-accessible memory stops, version history and a selected-manuscript download. All eight memory excerpts occur verbatim in the selected text. The four crops are documented in `artwork/scenes/index.json`; no new scenes or photographs were generated.

The reader release is independent of later multimedia production. It has no video or audio controls, PDF/social links or full-product ZIP because those products have not been built for this chapter. Chapters 04 and 07 retain their existing full multimedia pages and download URLs.

## Local verification

- Eight unit tests pass, including rendering a reader chapter without an earlier original essay or multimedia assets.
- Homepage and Chapter 03 checked at 320, 390, 820 and 1440px: no horizontal overflow; images decode.
- Homepage contains three chapter cards, with Chapter 03 first; navigation and slug redirect work.
- All 36 rendered paragraphs match the selected manuscript, with and without JavaScript.
- All eight journey controls work by keyboard, update their pressed state, caption and image.
- Version-history details, reduced-motion behavior and manuscript download checked.
- Existing Chapter 04 decision controls and Chapter 07 memory controls still work; Chapter 07 links onward to Chapter 03.
- Standalone chapter HTML loads its images, shared styles and manuscript download from the local folder.
- Browser reports no page errors. Actual 390px and 1440px screenshots are stored in `previews/`.
- The normal site validator checks all eight generated pages, local links, product inventories, the 12 supplied Saigon reference files and 92 archived originals.

GitHub Actions performs the build, tests and site validation again on the published commit before deploying `site/` to Pages.
