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
shared/                         # design tokens and shared web assets/templates
templates/chapter/              # reusable intake template
scripts/                        # scaffold, media build, site build, validation
docs/                           # architecture and cross-chapter review
archive/                        # original deliveries and earlier work
site/                           # ignored generated deployment only
```

Canonical public number URLs `/chapters/04/` and `/chapters/07/` remain valid. Slug URLs redirect there. Folder identity uses the stable slug so a future table-of-contents change does not require moving source assets. Add a chapter through the scaffold; metadata and the registry drive all builds. No chapter-specific conditionals belong in the site renderer; artifact types use their own small templates.

The website consumes finished exports, so deployment requires only Python's standard library. Offline production uses Pillow, ReportLab and ffmpeg; PDF QA uses PyMuPDF. All input paths are repo-relative and output writes are restricted to the chapter and generated site folders. The original Expected_utility delivery is retained byte-for-byte, while current products are versioned separately.
