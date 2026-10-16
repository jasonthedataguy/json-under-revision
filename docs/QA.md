# Product-system verification

Date: 16 October 2026, Asia/Bangkok.

- Six scaffold/security tests cover creating an unpublished chapter, preserving an existing manuscript, duplicate-number protection, path traversal and escaped manuscript markup.
- Static validation checks the registry, all exported local links/anchors, complete selected prose, product inventories, ZIP integrity, provisional edit timelines and all 92 archived file checksums.
- Headless Chromium checks at 320, 390, 820 and 1440px cover the index, About and both chapters; no horizontal overflow or JavaScript errors. All five carousel cards remain visible on mobile.
- Keyboard controls, memory-image loading, branch/reset state, original-manuscript disclosures, reduced motion and no-JavaScript reading pass.
- Chapter PDF/ZIP/social downloads, actual 1080×1920 video playback and ambient audio loading pass. Standalone chapter previews load shared styling from the repo or extracted product ZIP.
- Per-chapter MEDIA_QA.json records image decoding, native artwork size, every PDF paragraph and full H.264/AAC decoding of all three video cuts. PDF contact sheets and actual production boards are available in previews/.

Known limits: source artwork is lower than final print-master resolution. PDFs are editorial proofs. The six videos are edit previews for Jason's actual narration; SRT/VTT timing is provisional. Physical phone testing, human screen-reader review, a printer proof and social-platform publication are not claimed. The design boards' placeholder QR is not reproduced.
