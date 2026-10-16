# Chapter 03 reader release

On 2026-10-16, the author rejected the assistant's board-derived rewrite and supplied the original essay. This correction restores all 20 original paragraphs without literary edits. `source/original.md` and `source/approved.md` preserve the attachment's exact 10,658 bytes, including its heading and CRLF line endings. The author's T/t voice, slang, dialogue, names, events and paragraph order are unchanged.

Source SHA-256: `911b174411dced9668dffd01c6860c079cc17e231c5235f5153666c6021d8b26`. The site validator enforces that hash and exact equality of the original and published manuscript. The original heading retains number 1 in the source files; the existing book registry and public route remain Chapter 03.

The generated draft and drafting notes are archived under `archive/superseded/saigon-board-derived-draft-v01/`, outside the deployed chapter. Their former reader-source URLs are removed. The version-history panel now contains the author's original, and the homepage subtitle, eight memory quotes and closing quotation use the author's own words.

- Reader URL: https://jasonthedataguy.github.io/json-under-revision/chapters/03/
- Slug alias: https://jasonthedataguy.github.io/json-under-revision/chapters/viet-cho-sai-gon-cua-t/
- Homepage: https://jasonthedataguy.github.io/json-under-revision/

The release includes the complete prose, a homepage card, responsive supplied-art crops, eight keyboard-accessible memory stops, version history and a selected-manuscript download. All eight memory excerpts occur verbatim in the selected text. The four crops are documented in `artwork/scenes/index.json`; no new scenes or photographs were generated.

The reader release is independent of later multimedia production. It has no video or audio controls, PDF/social links or full-product ZIP because those products have not been built for this chapter. Chapters 04 and 07 retain their existing full multimedia pages and download URLs.

## Local verification

- Eight unit tests pass, including rendering a reader chapter without an earlier original essay or multimedia assets.
- Homepage and Chapter 03 checked at 320, 390, 820 and 1440px: no horizontal overflow; images decode.
- Homepage contains three chapter cards, with Chapter 03 first; navigation and slug redirect work.
- All 20 rendered paragraphs match the original attachment, with and without JavaScript; Markdown film-title emphasis is preserved.
- All eight journey controls work by keyboard, update their pressed state, caption and image.
- Version-history details show the original; reduced-motion behavior checked. The manuscript download matches the attachment's exact SHA-256. The rejected draft and drafting-note URLs return 404.
- Existing Chapter 04 decision controls and Chapter 07 memory controls still work; Chapter 07 links onward to Chapter 03.
- Standalone chapter HTML loads its images, shared styles and manuscript download from the local folder.
- Browser reports no page errors. Actual 390px and 1440px screenshots are stored in `previews/`.
- The normal site validator checks all eight generated pages, local links, product inventories, the 12 supplied Saigon reference files and 92 archived originals.

GitHub Actions performs the build, tests and site validation again on the published commit before deploying `site/` to Pages.
