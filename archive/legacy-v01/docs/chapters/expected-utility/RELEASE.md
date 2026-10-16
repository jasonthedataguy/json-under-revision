# Expected_utility — selected chapter release

Release decision: 16 October 2026 (Asia/Bangkok). The author identified the supplied Expected_utility folder as the final chapter artifact and explicitly requested review, push and deployment of everything.

The complete 37-file package is preserved unchanged in `Expected_utility/`. Its older README, metadata, QA and checklist describe the delivery before this authorization. Their pending author approval, binary import and website publication holds are superseded by this release decision. This document is the current release record and is also included at the root of the downloadable ZIP.

- Chapter URL: https://jasonthedataguy.github.io/json-under-revision/chapters/04/
- Slug alias: https://jasonthedataguy.github.io/json-under-revision/chapters/expected-utility/
- Manuscript: the selected package's `content/proposed-edit.md`, already embedded in `web/index.html`; original prose remains archived.
- Artwork, PDF, video, social images, previews, metadata and original builder are all committed. Individual media and a complete ZIP are available from the chapter page.
- The site builder preserves the selected prose and design, replaces historical review labels, adds navigation/downloads/share metadata, corrects the narrow-screen title and paper-section text contrast, and fixes the reset button's toggle semantics.
- Cơm nguội continues to use its previously selected edit at `/chapters/07/`. Both chapters are linked from the archive index.

The selected artifact is complete for this release. The supplied PDF remains an eight-page A5 layout proof, not a printer-certified PDF/X file. The supplied video remains a 24-second 720×1280 animatic with synthetic ambience, without narration or synchronized captions. Selecting the package does not change those technical properties. No media is regenerated during website deployment. The historical media builder requires Pillow, ReportLab, ffmpeg and the Linux fonts named in its source; the website build uses only Python's standard library.

Social copy and media are published as downloadable files. Posts have not been sent to social platforms; the author manages those uploads. Narration generation remains stopped; any future narrated exports use the author's supplied recording. A custom domain and print QR remain deferred.

Build: `python scripts/build_site.py --text proposed-edit`.
Validate: `python scripts/check_site.py`.
GitHub Pages builds and validates on pushes to `main`, with manual dispatch retained. Only the generated `site/` directory is uploaded.
