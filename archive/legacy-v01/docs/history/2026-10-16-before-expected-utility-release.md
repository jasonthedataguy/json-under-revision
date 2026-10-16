# .json — Project update

**Updated:** 16 October 2026, Asia/Bangkok  
**Repository:** [jasonthedataguy/json-under-revision](https://github.com/jasonthedataguy/json-under-revision)  
**Main reviewed:** `c64f3a1c645fe836a4dd77356bcaa419d888422b`

The repository now contains two chapter packages: **Cơm nguội** and **Expected_utility**. Cơm nguội has a published chapter website and an approved edit and illustration treatment. Expected_utility has manuscript drafts, a poster-style web experience and social copy merged into main, but its binary media pack is not in the repository and the chapter is not deployed by the current publishing script. Neither chapter has a final narrated social video ready to upload.

## Repository update

- Fetched origin and fast-forwarded local main from `5b0f221` to `c64f3a1`: **23 incoming commits, 15 added files**. Main matched origin/main with **0 ahead / 0 behind** after the pull.
- Preserved the unfinished local Cơm nguội work in local branch `backup/com-nguoi-local-before-main-pull`, commit `6ba565d`. This backup was not pushed or merged into main.
- The backup includes the revised reading script, checklist edits, video-rendering scripts and a synthetic-narration trial. These are historical production drafts, not approved upload assets. Its older voice-generation instructions are superseded by the author's stop instruction.
- Temporary voice/media work remains locally excluded through Git's local exclude file. No voice-generation job was started during this update.
- This pull did not deploy a website, publish social posts or import media from an external ZIP. This update document is a new local file and has not been committed or pushed.

## Current author decisions

- **Cơm nguội text:** use the proposed edit; preserve the original separately.
- **Cơm nguội illustration:** the existing illustrated treatment is approved. That does not make the raster a print-grade master.
- **Narration:** voice generation is stopped. Jason will provide his own recorded reading; use that recording for the final videos.
- **Social publication:** Jason will create/manage the channels and upload the finished files himself, then provide the published URLs.
- **QR:** deferred. It is not a blocker for preparing social posts.
- **Repository:** remains public.

These decisions supersede stale pending-approval and voice-reference statements in the older Cơm nguội metadata, narration brief and master checklist. Those historical files were not rewritten as part of this pull.

## Cơm nguội — requested deliverables

| Deliverable | Status | Evidence / missing work |
|---|---|---|
| Printable PDF | **PROOF AVAILABLE** | [Four-page A5 proof](book/07_com_nguoi_A5_PROOF.pdf) is present. Final print-resolution artwork, printer specifications and preflight remain; do not call it press-ready. |
| Illustration | **TREATMENT APPROVED** | [Family illustration](assets/kitchen_memory_provisional.png) is present. Layered production art and high-resolution print exports remain unfinished. |
| TikTok/Reel video, requested 3:4 | **MISSING** | No completed 3:4 video. Needs Jason's recording, final composition, captions and export in the requested ratio. |
| YouTube video, requested 9:16 | **DRAFT ONLY** | Main contains the [24-second ambient-only animatic](video/com_nguoi_animatic_v01.mp4). A 53.14-second 1080×1920 synthetic trial is preserved only on the local backup branch; it had pronunciation and Vietnamese glyph problems and is not approved for upload. Final video must use Jason's actual recording, corrected text rendering and newly timed captions. |
| Facebook post | **MISSING** | No dedicated Cơm nguội Facebook copy-and-media package. Existing [channel launch copy](docs/CHANNEL_LAUNCH.md) is for YouTube/TikTok preparation. |
| Website | **PUBLISHED PREVIOUSLY** | [Chapter page](https://jasonthedataguy.github.io/json-under-revision/chapters/07/). The selected edit's [successful deployment](https://github.com/jasonthedataguy/json-under-revision/actions/runs/38883115962) used `5b0f221`. This update did not rerun deployment or fresh live-browser QA. |

**Immediate blocker:** Jason's own narration recording has not been supplied in this session. The selected-edit reading script is preserved in the backup commit; restore and reconcile it with [the approved text](content/proposed-edit.md) before recording or final editing. Do not assume the older script currently on main is that revised script.

## Expected_utility — newly pulled work

Merged work includes the original and proposed edit, editorial notes, creative brief, a poster-themed responsive archive with an interactive decision tree, a lightweight SVG illustration, Facebook/Instagram/TikTok/YouTube copy, and a storyboard and proposed narration script.

| Deliverable | Status | Evidence / missing work |
|---|---|---|
| Manuscript | **DRAFTS AVAILABLE** | [Original](content/chapters/expected-utility/original.md), [proposed edit](content/chapters/expected-utility/proposed-edit.md), and [editorial notes](content/chapters/expected-utility/EDIT_NOTES.md). Final manuscript and release signoff remain pending according to the chapter notes. |
| Printable PDF | **MISSING FROM REPOSITORY** | Chapter documentation reports an eight-page A5 proof in an external ZIP. It was not imported or independently inspected during this update. |
| Illustration | **SVG FALLBACK AVAILABLE** | [Poster SVG](digital/chapters/expected-utility/assets/poster_illustration_v02.svg) is present. The selected full-resolution poster PNG is listed in the external media pack and is not committed. |
| 3:4 content | **MISSING FROM REPOSITORY** | Documentation reports five 1080×1440 carousel images outside GitHub. These are still images, not a completed 3:4 video. |
| 9:16 video | **MISSING FROM REPOSITORY** | Documentation reports an external 24-second ambient-only animatic. No final narrator recording, synchronized captions or finished 1080×1920 video is committed. See [storyboard](video/expected-utility/STORYBOARD.md) and [narration draft](video/expected-utility/NARRATION.md). |
| Facebook post | **COPY DRAFT AVAILABLE** | [Facebook draft](social/expected-utility/facebook-post.md) exists. Its artwork and final chapter URL still need to be attached and reviewed; the post is not published. |
| Website | **SOURCE MERGED; NOT DEPLOYED BY CURRENT BUILD** | [Web source](digital/chapters/expected-utility/index.html) is on main. [The site builder](scripts/build_site.py) still exports only Cơm nguội at chapters/07/. Expected_utility needs explicit export integration, browser QA and release approval before deployment. |

The [chapter status file](docs/chapters/expected-utility/STATUS.md) still describes a proposal branch. The Git merge is now complete, but that does not complete its media import or publishing gates. Use [the binary import map](docs/chapters/expected-utility/BINARY_IMPORT.md) to locate and review the external ZIP assets before copying them into the repository. Its historical QA claims are not fresh verification of files in this checkout.

## Next actions

- [ ] **Jason:** supply the actual Cơm nguội reading.
- [ ] **Editor:** recover the selected-edit reading script from the local backup and retire superseded cloning instructions in the active production documents.
- [ ] **Video editor:** mix the real recording, correct Vietnamese text rendering, retime captions, and export the requested **3:4** and **9:16** cuts. Preserve these as distinct deliverables.
- [ ] **Editor/designer:** prepare the Cơm nguội Facebook caption, approved image and chapter link.
- [ ] **Jason/editor:** locate the Expected_utility ZIP described in the import map; import and verify its PDF, poster, carousel and animatic before claiming those files are available in the repository.
- [ ] **Jason:** review Expected_utility's manuscript and release decisions.
- [ ] **Engineer:** integrate Expected_utility into the public site export and complete browser checks before any authorized deployment.
- [ ] **Jason:** review the finished videos on a phone, upload them, and record the post URLs.
- [ ] **Production team:** prepare printer-specific artwork/PDFs when print production resumes. QR remains deferred.

## Verification and limits

This update is based on the fetched Git history, tracked-file inventory, current chapter status/import documents, deployment build code, and the author's decisions in this session. The Cơm nguội PDF, illustration and animatic were confirmed present. The main branch was synchronized without conflicts. No media was regenerated, no external ZIP was imported, and no new audiovisual, print or live-site QA is implied by this report.

The new [chapter production playbook](docs/CHAPTER_PRODUCTION_PLAYBOOK.md) provides a reusable workflow. Treat it as guidance alongside the author's latest decisions; distinguish prepared copy, proof media, approved assets and actual publication.
