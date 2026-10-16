# .json — Jason, under revision

A book with a version history. Each chapter is a complete story with an optional memory archive and a consistent product set.

| Chapter | Read | Product folder | Production board |
|---|---|---|---|
| 02 — Fashion | [Online](https://jasonthedataguy.github.io/json-under-revision/chapters/02/) | [chapters/fashion](chapters/fashion/) | [Supplied board](chapters/fashion/references/fashion-v02/docs/PROJECT_BOARD.html) |
| 03 — Viết cho Sài Gòn của t | [Online](https://jasonthedataguy.github.io/json-under-revision/chapters/03/) | [chapters/viet-cho-sai-gon-cua-t](chapters/viet-cho-sai-gon-cua-t/) | [Supplied board](chapters/viet-cho-sai-gon-cua-t/references/project-board-v01/PROJECT_BOARD.html) |
| 04 — Expected_utility | [Online](https://jasonthedataguy.github.io/json-under-revision/chapters/04/) | [chapters/expected-utility](chapters/expected-utility/) | [Board](chapters/expected-utility/previews/product-board.jpg) |
| 05 — For Mother Russia | [Online](https://jasonthedataguy.github.io/json-under-revision/chapters/05/) | [chapters/for-mother-russia](chapters/for-mother-russia/) | [Supplied board](chapters/for-mother-russia/references/mother-russia-v01/docs/PROJECT_BOARD.html) |
| 06 — Play to Win, Don’t Play Not to Lose | [Online](https://jasonthedataguy.github.io/json-under-revision/chapters/06/) | [chapters/play-to-win](chapters/play-to-win/) | [Approved board](docs/chapters/choi-de-khong-thua/PROJECT_BOARD.html) |
| 07 — Cơm nguội | [Online](https://jasonthedataguy.github.io/json-under-revision/chapters/07/) | [chapters/com-nguoi](chapters/com-nguoi/) | [Board](chapters/com-nguoi/previews/product-board.jpg) |

## Repository

`book.json` is the ordered registry. Each `chapters/<slug>/` contains its metadata, production recipe, preserved original and selected prose, artwork source/crops, A5 proof, web page, audio, video cuts, channel packs, documentation and previews. Shared design and website templates live in `shared/`; builders live in `scripts/`. See [architecture](docs/ARCHITECTURE.md) and [design review](docs/PRODUCT_REVIEW.md).

Chapter 02 publishes the uploaded Fashion original verbatim, with the supplied room design and six-stop Wardrobe Explorer. The five v02 packages are preserved as 81 checksum-verified reference files. Its PDF proofs, two ambient animatics and social packs are available from the chapter; the supplied A5 proof is explicitly labelled as a proposed-edit proof. It appears first in chapter-number order on the homepage.

Chapter 03 publishes the author's original manuscript, eight supplied-art crops and an eight-stop memory journey. Its multimedia set includes the complete illustrated A5 proof, five video edits, recording scripts, provisional captions, a carousel and platform assets. Its 12 original reference files are checksum-verified; the board's provisional number 01 is superseded by Chapter 03. `source/original.md` and `source/approved.md` preserve the supplied essay byte-for-byte; the rejected rewrite is archived outside the deployed chapter. Video narration and final print production remain pending.

Chapter 05 publishes For Mother Russia's original 25-paragraph essay, supplied winter design, seven-node Memory Graph and nine-scene gallery. Its four uploaded ZIPs are preserved as 68 unique reference files; the duplicate video is byte-identical. The author selected 05 because 03 already belongs to Sài Gòn. Supplied PDFs, artwork and filenames retain their working 03 labels; the A5 download is identified as a proposed-edit proof. The 24-second video awaits author narration.

Earlier work remains under `archive/`, with a checksum-verified [migration map](docs/MIGRATION.json). The complete prior Expected_utility delivery is unchanged. Existing chapter URLs and earlier media download URLs remain supported. Private ignored voice scratch was neither moved into the archive nor included in product ZIPs.

Chapter 06 publishes all 41 original paragraphs of Play to Win, Don’t Play Not to Lose with the approved jade/table illustrations and a qualitative before/after beliefs matrix. The author authorized a new title and chapter number; validation permits that heading change and requires the body to remain byte-identical. The current release is the reader and interactive artifact. Print, video, narration and social production remain separately tracked.

## Build the website

Requires Python 3.12 in CI; standard library only. Finished product assets are committed.

```sh
python scripts/build_site.py
python scripts/check_site.py
python -m unittest discover -s tests
python -m http.server 8765 --directory site --bind 127.0.0.1
```

GitHub Pages builds, tests and validates on pushes to `main`; manual dispatch is retained. Only `site/` is deployed.

## Add a chapter

```sh
python scripts/new_chapter.py --slug new-memory --number 09 --title "New memory"
```

The scaffold starts with `publish: false`. Add the original and selected prose, supplied artwork, palette and artifact metadata. Fill `production.json` with scene crops, five carousel excerpts, print placements and film segments. Memory artifacts take their moments from the same recipe. Production builders never insert another chapter's text. Set `publish: true` after the chapter is authorized for public release.

A selected manuscript can also ship as a reader release before the full multimedia set: set `release_stage: reader`, provide the selected text and its real version-history source, reader artwork and memory moments. The reader template displays actual available downloads. Generate its artwork with `python scripts/build_reader_artwork.py --chapter <slug>`, then build the site and inventory. The original full multimedia behavior remains the default for existing chapters.

## Rebuild products

Install `requirements-production.txt`, provide ffmpeg on PATH, and use Times/Arial on Windows or DejaVu TTF fonts on Linux. Set `CHAPTER_FONT_DIR` for another installation of those fonts.

```sh
python scripts/build_products.py --chapter com-nguoi --video
python scripts/verify_products.py --ffmpeg /path/to/ffmpeg
python scripts/build_site.py
# After capturing web screenshots in each chapter's previews/:
python scripts/build_board.py
python scripts/build_inventory.py
python scripts/build_site.py
python scripts/check_site.py
```

Omit `--video` to rebuild print/social assets and timing notes without re-encoding cuts. `production.json` controls provisional film timing. MP4 outputs are 1080×1920 (discovery and YouTube) and 1080×1440 (feed). SRT/VTT describe the existing on-screen card timing; they are not a recorded narration transcript.

## Current production decision

The author chose **supplied artwork and crops** and **edit cuts prepared for his recorded narration**. There is no generated voice. All six cuts are playable edit previews, awaiting the actual recording and retiming. The source images limit close-up and print detail; the PDFs are A5 editorial proofs. Printer-certified production, real-device/screen-reader review and author-managed social uploads remain separate. QR remains deferred.

The boards' checkmarks, illustrative probabilities, sample durations, locations and QR graphics are references, not verified product facts. The strategy's commercial assumptions are not prices or checkout commitments. No store, payment flow or social post has been created.
