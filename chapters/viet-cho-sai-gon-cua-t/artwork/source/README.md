# Supplied artwork references

The originals are stored once, with the board they belong to:

- [Poster concept PNG](../../references/project-board-v01/assets/saigon_landmark_poster_proof.png) — 1254 × 1254.
- [Board display JPEG](../../references/project-board-v01/assets/saigon_landmark_poster_proof.jpg) — 960 × 960.
- [Anonymous vector alternative](../../references/project-board-v01/assets/saigon_cover_mock.svg).

These are design concepts. The supplied board describes the poster as a stylized reconstruction from author-provided photos; the source photos and a textless/layered master are absent. Keep that provenance when deriving crops. The two supplied screenshots show the project board, not a finished chapter website.

Future scene crops belong in `../scenes/`, with source boxes recorded in `production.json`; composed covers and responsive exports belong in `../exports/`. Use supplied artwork and crops as the author requested. Do not describe repeated crops as newly illustrated scenes.

The reader release now uses four crops in `../scenes/` and two responsive exports in `../exports/`. Their exact source boxes and native sizes are recorded in `../scenes/index.json` and `production.json`. The crop excludes the poster's embedded provisional Chapter 01 lettering; Chapter 03 is rendered as real text on the website. The original artwork is unchanged. Regenerate with `python scripts/build_reader_artwork.py --chapter viet-cho-sai-gon-cua-t` from the repository root.
