# Chapter product architecture

The strategy's pages 3–4 define Read / Explore / Revisit; page 8 calls for a lasting chapter URL; page 17 gives the short film a discovery role. Pages 18–19 call for a small pilot and reusable production system. This repository implements those product principles with the two supplied chapters, without inventing chapters 10–12 or treating the deck's commercial assumptions as commitments.

```
book.json                       # ordered chapter registry and site identity
chapters/<stable-slug>/
  chapter.json                  # number, slug, source, palette, artifact, state
  source/                       # original, approved, notes, real revision log
  artwork/{source,scenes,exports}/
  book/                         # illustrated A5 proof
  web/                          # generated chapter page
  audio/                        # ambience; author narration only when supplied
  video/                        # cuts, timeline, SRT/VTT, storyboard
  social/{instagram,facebook,tiktok,youtube}/
  docs/                         # inventory, provenance, QA and release state
  previews/                     # actual renders and contact sheets
  references/                   # unmodified supplied boards and design references
shared/                         # design tokens and shared web assets/templates
templates/chapter/              # reusable intake template
scripts/                        # scaffold, media build, site build, validation
docs/                           # architecture and cross-chapter review
archive/                        # original deliveries and earlier work
site/                           # ignored generated deployment only
```

Canonical public number URLs are `/chapters/02/` through `/chapters/09/`, plus `/chapters/15/` and `/chapters/16/`. Slug URLs redirect there. The author selected Chapter 09 for Thế giới trong mơ của tôi because the kit's 06 conflicts with Play to Win; original kit labels remain archived. Three Meeting Theory and Dating 102 retain their supplied Chapter 15/16 labels; numbering gaps do not require invented chapters or changed existing URLs. Folder identity uses the stable slug so a future table-of-contents change does not require moving source assets. Add a chapter through the scaffold; metadata and the registry drive all builds. No chapter-specific conditionals belong in the site renderer; artifact types use their own small templates.

The website consumes finished exports, so deployment requires only Python's standard library. Offline production uses Pillow, ReportLab and ffmpeg; PDF QA uses PyMuPDF. All input paths are repo-relative and output writes are restricted to the chapter and generated site folders. The original Expected_utility delivery is retained byte-for-byte, while current products are versioned separately.

Supplied chapters may opt into `build_supplied_media.py` with a `publish_media.carousel` recipe and ordinary `films`. The optional `scene_fit: contain` keeps a complete diagram inside each media frame; the default `cover` behavior stays unchanged for other chapters. Original imports remain in `references/`. Derived timelines receive the same continuity and source-excerpt checks as other generated media. Dating Algorithm uses this path for Chapter 08; its static template also preserves the full manuscript and empty table without JavaScript.

Chapter 03 (`viet-cho-sai-gon-cua-t`) began as a reference-only intake. The assistant's board-derived rewrite was later rejected by the author, who supplied the original essay on 2026-10-16. `source/original.md` and `source/approved.md` now preserve the attachment byte-for-byte, and version history uses that original. The superseded draft is archived outside the deployment. The supplied source heading retains its original number 1; the book registry and existing public URL stay at Chapter 03.

Publication and multimedia production are separate. `publish: false` excludes an unfinished draft from the site. An authorized `publish: true` chapter can use `release_stage: reader` for its complete prose, hero artwork, interactive artifact and real version history. `shared/chapter-reader.html` includes only the reader downloads; it does not require or advertise PDF, video, audio or social files. `history_text`, `history_label` and `revision_note` describe the actual manuscript lineage. Existing chapters default to `release_stage: multimedia`, retaining their complete product template and validation. Reader artwork is generated from documented crop boxes with `scripts/build_reader_artwork.py`; full-product builders skip reader releases until their multimedia recipe is ready.

An optional `reference_manifest` points to an exact-byte SHA-256 import inventory; validation checks those files even when the chapter is unpublished. Supplied files under `chapters/*/references/` bypass Git newline conversion. Draft routes must be absent from the generated public site; published chapters must appear on the homepage. Every published manuscript, inventory, local page link and available product is checked. Multimedia releases additionally require their timed video assets and complete ZIP.

A multimedia chapter may set `web_template` to a chapter-local template to preserve its existing design while exposing its finished product set. Optional `supplemental` cards, copy and product entries in `production.json` add channel formats without requiring them from every chapter. Landscape film cards use side-by-side image/text composition. Each cut receives a recording script; `excerpts_verbatim` adds original-source checks for all film, carousel and supplemental-card excerpts. `--chapter` scopes board generation and media verification to the changed product set.

Optional `reading_illustrations` place supplied images after zero-based canonical paragraph indices without embedding or rewriting manuscript text in a template. Each placement declares `src`, `alt`, `width` and `height`; an invalid paragraph index fails the build. For Mother Russia uses these placements to preserve its supplied illustrated reader while rendering the full original without JavaScript. Its author-selected number 05 avoids changing the existing 03 URL, and its imported proof labels remain documented separately.

For an author-requested verbatim restoration, `text_policy: verbatim-author-original` and `manuscript_source` record the supplied source path, byte count and SHA-256. Validation checks the raw original bytes, exact equality of the published source and verbatim membership of memory excerpts. Git attributes preserve the source newlines. Superseded generated prose belongs in the repository archive, outside the deployed chapter.

An author-approved title and number change may use `text_policy: verbatim-author-body`. The checker requires the exact metadata-derived heading and preserves every remaining source byte, including line endings and trailing whitespace. Chapter 06 uses this policy alongside the `beliefs` artifact and a chapter-local multimedia template. Its board history remains in `docs/chapters/choi-de-khong-thua`; the production chapter has the slug `play-to-win`.

Recipes may declare a separate `source` SVG and rendered `raster` for each scene. `render_vector_artwork.py` renders the approved vectors with Playwright/Chromium before the shared product builder applies framing. Scene manifests retain both source and raster provenance. `print_extras` adds an A4 poster and a 50 × 150 mm bookmark proof. The generated full reading script must match the selected canonical manuscript, and `excerpts_verbatim` checks carousel, film and story quotations against the preserved original.

`release_stage: supplied` supports a complete uploaded product set with its own design and media formats. `web_template` selects a chapter-local template; the shared renderer injects the canonical prose as static HTML, canonical URL and next-chapter navigation. `web/assets/` is copied to the published chapter's `assets/` and stays adjacent to its offline page. Imported products retain explicit states in `docs/PRODUCTS.json`; inventory generation does not relabel proofs or invent missing formats. The shared media builders skip supplied releases. Validation checks the original, reference hashes, rendered prose, links, product files and ZIP contents, while generated multimedia chapters retain their timeline checks. Fashion's untouched five-package delivery lives in `chapters/fashion/references/fashion-v02/`; the public page and complete download preserve that provenance. Its unapproved proposed manuscript is not substituted for the original.
