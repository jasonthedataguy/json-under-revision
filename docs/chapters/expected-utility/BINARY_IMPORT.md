# Expected_utility v0.2 — binary asset import and review

This document accompanies the downloadable **Expected_utility_poster_v02_full_chapter.zip** from the author's ChatGPT project workspace.

The GitHub connector used to create this branch could write the text/source files and original SVG but could not transfer local PDF/PNG/JPG/MP4 binaries into the repository. **Do not mark the PR as a complete media release until these verified binaries are imported and reviewed.**

## Intended destination mapping

| In ZIP | In repository (on this branch) |
|---|---|
| `assets/poster_original.png` | `digital/chapters/expected-utility/assets/poster_master.png` |
| `assets/decision_tree_paper.png` | `digital/chapters/expected-utility/assets/decision_tree_paper.png` |
| `book/04_expected_utility_POSTER_A5_PROOF.pdf` | `book/04_expected_utility_POSTER_A5_PROOF.pdf` |
| `video/expected_utility_poster_animatic_9x16.mp4` | `video/expected-utility/expected_utility_poster_animatic_9x16.mp4` |
| `video/stills/*.jpg` | `video/expected-utility/stills/*.jpg` |
| `social/instagram/slide_??_3x4.jpg` | `social/expected-utility/instagram/slide_??_3x4.jpg` |
| `social/facebook_landscape.jpg` | `social/expected-utility/facebook_landscape.jpg` |
| `social/youtube_thumbnail.jpg` | `social/expected-utility/youtube_thumbnail.jpg` |

All of these are **draft assets** until approved. Do not publish manuscript/photo/voice or merge automatically.

## Suggested local Codex steps

1. `git fetch origin && git checkout design/expected-utility-poster-v02 && git pull --ff-only`.
2. Download and unzip the chapter bundle outside the repo.
3. Copy the vetted media according to the table above. Preserve existing shared assets.
4. If desired, change `digital/chapters/expected-utility/index.html` to use `assets/poster_master.png` for the hero; keep the committed SVG as its lightweight fallback.
5. Verify PNG/JPEG dimensions, A5 PDF page count and video duration/codec. Ensure no editorial proof claims to be print ready or narrated.
6. Run local HTTPS/browser tests for the manuscript version switch and interactive decision tree.
7. Commit media: `git add book/04_expected_utility_POSTER_A5_PROOF.pdf digital/chapters/expected-utility/assets/ video/expected-utility/ social/expected-utility/` then `git commit -m "assets(chapter): import Expected_utility poster proof pack"`.
8. Push to this branch and update the draft PR. Obtain separate author approval before deployment.

## Explicit limitations

- The full-size poster illustration includes **decorative imagined probabilities in a notebook**. They are not calculated likelihoods. The functional graph intentionally shows `P = ?`.
- The proof PDF contains the **proposed edit**, not a frozen press-ready manuscript.
- The MP4 is **24 seconds of still-based animation** with synthesized ambience; no human voice nor synchronized captions.
- Public GitHub repository visibility is not a license to reuse third-party likeness, literature, artwork, sounds or recordings.
