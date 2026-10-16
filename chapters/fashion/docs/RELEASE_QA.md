# Fashion web release — 2026-10-16

The author requested deployment of the five supplied Fashion v02 packages. The release publishes Chapter 02 at `chapters/02/`, with `chapters/fashion/` as an alias and a homepage card before Chapter 03.

- All 81 supplied files are preserved byte-for-byte under `references/fashion-v02/`; the import manifest records SHA-256 checksums and package names.
- The canonical manuscript is the supplied `content/original.md`, copied byte-for-byte to both source files. All 14 paragraphs render in static HTML and remain readable without JavaScript. The proposed edit remains a reference; it is not the published prose.
- Chromium checks passed at 320, 390, 820 and 1440 pixels: four homepage cards, no horizontal overflow, decoded images, six keyboard-operated wardrobe buttons, accessible selected states and matching descriptions.
- Both supplied films played successfully and reported 24 seconds; ambient audio played. No narration was generated. Source, PDF and social downloads returned successfully.
- The offline web page retained its manuscript, assets and wardrobe interaction. Homepage navigation and the slug redirect worked.
- The A5 PDF contains nine 148 × 210 mm pages and retains “Peace and love!”; the A4 poster is one 210 × 297 mm page. The A5 uses the supplied proposed edit and is labelled as that editorial proof. Neither PDF is represented as a final printer-ready edition.
- Five supplied carousel images measure 1080 × 1440 pixels.
- All three existing chapters retained their complete canonical paragraphs and working interactive artifacts.
- Repository tests cover supplied-template manuscript rendering, navigation, escaping and template path containment. The site validator checks all four chapters, ten pages, links, inventories, product ZIPs, original-source hashes and preserved references.

Browser previews are in `previews/`. Narration, synchronized speech subtitles, final print production and social posting remain separate production steps.
