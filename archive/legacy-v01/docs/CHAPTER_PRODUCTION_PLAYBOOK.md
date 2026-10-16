# .json — Reusable Chapter Production Playbook
**Project:** .json — Jason, under revision  
**Version:** 1.0 | **Based on:** Chapter 07, Cơm nguội  
**Repository:** https://github.com/jasonthedataguy/json-under-revision  
**Purpose:** Turn each newly submitted memoir article into the same coherent, reviewable book + digital + video + social experience.

> **North star:** The book is the story. The digital archive should add feeling, context, or contradiction—not compensate for weak writing. A chapter can be moving without any technology.

---

## 0. HOW TO USE THIS WITH A NEW ARTICLE

In a new ChatGPT/Codex conversation, share this file (or its GitHub URL), then paste your original article using this message. Fields are optional except the article itself.

### COPY / PASTE PROMPT

**Project:** .json — Jason, under revision

Use the **Reusable Chapter Production Playbook** from:
https://github.com/jasonthedataguy/json-under-revision/blob/main/docs/CHAPTER_PRODUCTION_PLAYBOOK.md

**Task:** Build the next memoir chapter as a complete immersive product following the Cơm nguội pilot. Start by reviewing the existing GitHub repository, preserving all old work, and assessing the new chapter. Produce as many real, usable assets as tools and permissions allow in the current turn. Maintain a transparent READY / PROOF / MISSING / BLOCKED checklist. Do not present placeholders as released products.

**Working title:** [optional]  
**Chapter identifier / part:** [optional; do not guess a permanent number]  
**Approximate narrator age:** [optional]  
**What Jason believed then:** [optional]  
**What older Jason may later revise:** [optional]  
**Important people/places/objects/motifs:** [optional]  
**Source/inspiration or borrowed passages:** [optional; flag uncertainties]  
**What must remain private:** [optional]  
**Desired language / voice:** Vietnamese with natural Vinglish  
**Requested publication status:** draft / review / approved for public release [default: draft]

**ORIGINAL ARTICLE START**

[PASTE THE FULL NEW POST HERE]

**ORIGINAL ARTICLE END**

**Please deliver:**
1. Editorial review, original-preserved version, proposed polished chapter, and brief edit notes.
2. Chapter identity, motif, original illustration direction, and creative brief.
3. Printable illustrated A5 PDF proof; identify unmet printer-specific requirements.
4. Digital chapter artifact with metadata, responsive website preview, and accessible reading experience.
5. Short-video storyboard, narration script, subtitles/script, and honest video export status.
6. Instagram visual post/carousel and caption; TikTok/Reel/YouTube Short assets; Facebook post; YouTube description.
7. File inventory, QA and copyright/privacy checklist, production board, and exact next tasks.
8. A focused GitHub branch/commit and draft PR *only for files approved to be stored in the public repository*. Do not silently publish private manuscript text or merge/deploy a public release.
9. Working links to created assets, PR, preview, and actual live release only if verified.

If a necessary tool, file, permission, narration, or printer specification is missing, produce the best safe partial result, label it honestly, and record the blocker. Do not invent approval, live URLs, successful builds, voice recordings, or sales metrics.

---

## 1. PRODUCT IDENTITY AND EDITORIAL RULES

**Book:** .json  
**Subtitle:** Jason, under revision  
**Format:** Vietnamese memoir-in-essays, natural Vinglish.  
**Deep narrative tendency:** observation → interpretation → model → prediction → error → revision. This is the *book-wide* arc, not a structure forced into every essay.

Preserve Jason's:
- Conversation-like tone (t / tớ / tôi / anh when appropriate), jokes, occasional profanity, asymmetry and emotional indirectness.
- Specific objects, sensory details, awkward memories, dialogue, places and dates when sourced.
- Natural economics, mathematics, AI, engineering and game-theory comparisons *only where his own thinking requires them*.
- Time-specific naïveté, confidence and contradictions; younger Jason must not automatically have older Jason's perspective.
- Original strongest lines and memorable endings. Avoid generic wisdom, moralizing and inflated poetic prose.

Editorial sequence:
1. Save the unchanged source as source/original.md in a **private workspace** unless explicitly approved for public GitHub.
2. Create source/proposed-edit.md without inventing events, dialogue, identities, memories or claims.
3. Create EDIT_NOTES.md identifying major cuts, reordered passages, uncertain factual claims and continuity conflicts.
4. Run borrowing/provenance review where relevant; attribution does not legitimize copying protected text or borrowing another writer's personal memories as Jason's.
5. Request or record Jason's explicit selection of the canonical version; separately review privacy, factual claims and publication rights.
6. Only then freeze manuscript version, hash and publication metadata.

Do not turn a third party into a recognizable character without deliberate privacy review. Letters, private posts, voice, personal videos and photos are **not** publishable simply because Jason has a copy.

---

## 2. CHAPTER IDENTITY: ONE STORY, ONE WORLD

Every new chapter gets:
- **Stable slug** such as com-nguoi or to-mary-jane (unchanged even if the book moves chapters).
- **Working number**, separate from final table-of-contents number.
- **Narrator age** if known; otherwise unknown.
- **One concrete motif** (object, place, physical gesture or image).
- **Narrative role** (what this chapter does in the memoir).
- **Core scene** and **emotional tension**, without added events.
- **Commit message** only if it adds literary meaning.
- **Primary palette** and 1–2 original illustration approaches.
- **Provenance, sensitivity and release flags**.

A Git metaphor should function as occasional typography/structure, not a joke repeated in every paragraph. The visual direction combines intimate everyday illustration, painterly or rough colored-pencil gestures, cinematic light and discreet digital/archive cues. **Do not imitate a living illustrator's identifiable style.**

---

## 3. DELIVERABLE MATRIX — REQUIRED FOR EACH CHAPTER

| ID | Deliverable | Output / acceptance | Initial status |
|---|---|---|---|
| E01 | Original article | Verbatim archive + source provenance | Missing |
| E02 | Edited chapter | Polished Vietnamese/Vinglish + editorial notes | Missing |
| E03 | Editorial signoff | Author selects canonical text; factual/privacy review | Blocked until approval |
| A01 | Creative brief | Motifs, style, factual vs reconstructed details, art direction | Missing |
| A02 | Key illustration | Original image; source and rights recorded | Missing |
| A03 | Production art | Layered/lossless master where possible; print/web/social variants | Missing |
| B01 | Printable PDF proof | Readable A5 illustrated chapter, page numbers, correct Vietnamese glyphs | Missing |
| B02 | Print-ready PDF | Only after printer specifications, proofing, bleeds/PDF/X and approvals | Blocked by printer |
| W01 | Chapter web page | Responsive and accessible reading experience at stable slug | Missing |
| W02 | Digital memory artifact | Interactive or archival element that adds meaning; no fake functionality | Missing |
| W03 | Hosted release | Public HTTPS after author publishing authorization and deployment QA | Blocked by approval |
| V01 | Video storyboard | Shot-by-shot images, script, audio, disclosure, captions | Missing |
| V02 | Video animatic | Playable proof; clearly marked NOT final if unfinished | Missing |
| V03 | Final narrated vertical video | 9:16, 1080×1920, approved voice and synchronized Vietnamese captions | Blocked by media |
| V04 | YouTube landscape video | Optional 16:9 long-form, separate from YouTube Short | Optional |
| S01 | Instagram post | 3:4 (1080×1440) if requested, or platform-suitable 4:5; caption + carousel | Missing |
| S02 | TikTok + Reels | 9:16 video, cover, subtitles, caption, hashtags | Missing |
| S03 | YouTube Short | 9:16 video, thumbnail/title/description and verified link | Missing |
| S04 | Facebook | Finished copy, approved artwork and chapter CTA | Missing |
| G01 | GitHub chapter pack | Branch, documented commit, PR, changed-file manifest | Missing |
| R01 | Chapter release checklist | QA evidence, approval decisions, blockers, actual URLs | Missing |

**Important aspect ratios:** TikTok, Instagram Reels and YouTube Shorts = **9:16**. A requested **3:4** asset is best treated as a *still/feed export*. Standard landscape YouTube videos = **16:9**. Do not label one export as all four without format/safe-zone checks.

**Statuses:** READY (exists and passes acceptance), PROOF (exists but unfinished), MISSING (absent), BLOCKED (needs approval/rights/input), N/A (not requested).

---

## 4. PRINT / PDF SPEC

### A5 illustrated proof
- A5 trim: 148 × 210 mm; comfortable margins for a book, correct gutter side, suitable Vietnamese serif.
- Create a complete chapter reading layout, ideally with a visual opener and restrained chapter metadata.
- Export a PDF and render/check every page for legibility, clipped text, encoding, mismatched page numbers, missing assets and narrative continuity.
- Label clearly **PROOF — not print ready** until vendor specs and preflight are satisfied.

### Print-release gate
- Final printer quote and trim/binding/gutter/bleed specs.
- Final-approved high-resolution art at printed size (typically 300 ppi for raster imagery).
- Printer-compatible color conversion/profile; embedded fonts and appropriate PDF/X if required.
- Real, tested QR to an owned durable URL; **never** substitute a decorative QR slot.
- Proofreading, artwork/license check, physical printed proof, Jason approval.

---

## 5. VISUAL AND DIGITAL ARTIFACT SPEC

Build one recognizable chapter mood across formats, while giving every memory distinct physical objects and lighting.

**Core image pack**
1. Main original chapter painting / illustration.
2. Print crop at chapter dimensions.
3. Web hero and mobile crops, with alt text and optimized formats.
4. Vertical 9:16 film scenes/keyframes (not just a stretched still).
5. 3:4 requested social still (or 4:5 Instagram feed), 1:1 optional thumbnail.
6. One quote/artifact card with typography that remains readable on a phone.

**Reader archive (READ / EXPLORE / REVISIT)**
- READ: canonical approved chapter; no mandatory sign-in to finish the story.
- EXPLORE: the original illustration, ambient sound (clearly identified), short clip or a manuscript-grounded interaction.
- REVISIT: author-approved version history, a small note on an assumption that changed, or a preserved image. Do not manufacture social counters or fake history.
- Include accessibility: semantic headings, text alternatives, accessible controls, reduced-motion support, keyboard navigation and visible focus.
- No autoplay sound. No collection of personal data without an explicit policy.
- Host at a stable path. The physical book's QR should point there *after testing*.

A digital artifact must contribute new emotional or interpretive value. If it only repeats the chapter, simplify it.

---

## 6. VIDEO / NARRATION SPEC

**Vertical discovery film**
- Preferred target: approximately 40–70 seconds after the actual narration is timed.
- 1080×1920 H.264 MP4 9:16 master; create upload-safe version and poster frame.
- Film beats: hook → concrete scene → emotional turning point → quiet consequence → source-grounded final line.
- Preserve the source's genuine dialogue and ending; no invented family speech or documentary footage.
- Record Jason's own voice, hire/obtain rights for a narrator, or use a clearly authorized synthetic voice. Never clone or imitate a third party's voice without permission.
- Produce narration script, source-aligned transcript, actual timed SRT/VTT, ambience/music credits, final captions and thumbnail.
- Review on a phone for readable subtitles, safe zones, loudness, clipping and vertical framing.
- An ambient-only animatic is a **PROOF**, not a finished narrated video.

**YouTube**
- A YouTube **Short** can reuse the 9:16 master once platform safe zones, captions and metadata are reviewed.
- A separate normal YouTube storytelling film, if desired, should be composed in 16:9 rather than padded from the portrait crop.
- Do not claim anything is uploaded until an actual published/private link is verified.

---

## 7. SOCIAL / COMMUNITY PACKAGE

### Instagram
- Hero carousel: 4–6 slides, alternating image, vivid source line, scene/motif, and a non-spoiler ending.
- Still export: 3:4 (1080×1440) **when requested**; otherwise check current platform best crop (often 4:5).
- Reel: from the finished 9:16 video.
- Deliver caption in natural Vietnamese/Vinglish, image alt text, cover, relevant non-spam hashtags, chapter URL and post status.

### TikTok
- 9:16 narrated cut, cover frame, subtitles/safe zones, short hook, caption and CTA.
- Avoid sensationalizing grief, relationships, other people's identities or mental-health episodes to chase views.

### Facebook
- A standalone **authentic post**: an intimate but concise reflection or excerpt, approved artwork and stable website link.
- Include a separate Page caption and optional discussion question when it fits; no engagement bait.

### YouTube
- Short title, thumbnail, description, proper media credits, chapter link, optional pinned comment.
- A long-form episode is a **separate, optional deliverable**, not automatically complete.

**Posting gate:** Drafting posts is not publishing them. Channel creation, login, upload and scheduling require account access and authorized actions. Record actual URLs only after success.

---

## 8. RECOMMENDED FILE STRUCTURE

Keep the existing repo intact. Use the stable slug within new chapter bundles:

    content/
      chapters/<slug>/              # only if the content is approved for the PUBLIC repo
        approved.md
        metadata.json
        edit-notes.md
    book/
      <slug>_A5_PROOF.pdf
      <slug>_PRINT.pdf              # only after printer release gate
    digital/
      chapters/<slug>/
        index.html                  # or generated output
        assets/
          artwork.webp
          memory.svg
          room_tone.wav
    video/
      <slug>/
        storyboard.md
        narration-script.md
        captions.srt
        animatic.mp4
        social-master-9x16.mp4      # only when finished
        youtube-landscape-16x9.mp4  # optional
    social/
      <slug>/
        instagram-carousel/
        instagram-caption.md
        facebook-post.md
        tiktok-caption.md
        youtube-metadata.md
    docs/
      chapters/<slug>/
        CREATIVE_BRIEF.md
        CHECKLIST.md
        QA_REPORT.md
        RELEASE_REVIEW.md
        RIGHTS_AND_CREDITS.md
    previews/
      <slug>/
        book-contact-sheet.png
        mobile-screenshot.png
        video-frame.png

**Private source material:** Never assume that unpublished original drafts, private messages, reference media or source photos belong in a *public* repository. Keep them outside GitHub until publication has been explicitly approved, or use an authorized private repository.

Reuse shared assets/components instead of creating redundant per-chapter copies when possible.

---

## 9. EXECUTION PHASES AND RELEASE GATES

### Phase A — Intake and editorial
- [ ] Preserve original with version/source date.
- [ ] Read the full article and existing relevant book context.
- [ ] Make proposed edit, note what is changed, preserve key details.
- [ ] Identify sensitive third parties, borrowed passages, quotation/music/photo rights, uncertain facts.
- [ ] Select chapter role, slug, working number and motif.
- [ ] Record whether Jason explicitly approves final text and PUBLIC publication.

### Phase B — Visual, print and archive prototype
- [ ] Generate an original key illustration or provide a realistic creative brief where image creation is unavailable.
- [ ] Mark depicted invented details as artistic reconstruction pending approval.
- [ ] Produce and visually inspect A5 PDF proof.
- [ ] Build or update the mobile-first chapter website / archive.
- [ ] Prepare website screenshots and check linked media.

### Phase C — Video and social pack
- [ ] Build 5-beat storyboard and source-grounded narration.
- [ ] Create animatic/proof; identify if it lacks voice or synchronized captions.
- [ ] Produce final authorized voice if feasible; never fabricate completed recording.
- [ ] Export and verify final 9:16 video, captions and poster frame.
- [ ] Make requested 3:4/4:5 feed art, Instagram carousel, Facebook post, TikTok caption, YouTube metadata.

### Phase D — GitHub QA and optional release
- [ ] Keep changes on a branch; avoid overwriting existing chapter assets.
- [ ] Commit only safe and approved public content; create a draft PR with the asset inventory.
- [ ] Validate local build, PDF pages, video codec/dimensions/duration, Vietnamese font rendering, website mobile behavior.
- [ ] Check rights, privacy, captions, performance, reader comprehension, actual links.
- [ ] Deploy publicly only with explicit publication approval; verify HTTPS and exact manuscript version.
- [ ] Update permanent QR **after** URL selection, then obtain print proof.
- [ ] Conduct reader test; record feedback and decide RELEASE / REVISE / HOLD.

### Approval independence
Approval of the *editing* does **not** automatically approve artwork, private footage, publication in a public repo, social posting or commercial printing. Track those separately.

---

## 10. REQUIRED QA REPORT FOR EVERY CHAPTER

At the end of each production run, report:

### A. Asset scorecard
| Asset | File path/link | Status | Verified? | Missing requirement |
|---|---|---|---|---|
| Canonical text | ... | ... | ... | ... |
| A5 PDF proof | ... | ... | ... | ... |
| Print PDF | ... | ... | ... | ... |
| Key artwork | ... | ... | ... | ... |
| Web archive | ... | ... | ... | ... |
| Interactive artifact | ... | ... | ... | ... |
| 9:16 video | ... | ... | ... | ... |
| 3:4 feed image | ... | ... | ... | ... |
| Instagram pack | ... | ... | ... | ... |
| Facebook copy/art | ... | ... | ... | ... |
| TikTok copy/art | ... | ... | ... | ... |
| YouTube package | ... | ... | ... | ... |
| GitHub branch/PR | ... | ... | ... | ... |

### B. Evidence
- Which file was opened, rendered and inspected (not merely named)?
- Website actual deployment workflow and commit (if published).
- Video dimensions, duration, narration, captions, voice rights and mobile QA.
- Print PDF page count, trim, readability and print-production readiness.
- Explicit author approvals; unresolved legal/rights/privacy flags.

### C. Blocking decisions
- What is safe to publish now?
- What is only a concept or proof?
- What needs Jason's approval or an external provider?
- What is the **single highest-value next production step**?

**Never say “deployed,” “print ready,” “narrated,” or “published” on the basis of mockups, documentation or an unverified file path.**

---

## 11. REFERENCE PILOT (CƠM NGUỘI)

Existing reference paths:
- Original and edit: content/original.md and content/proposed-edit.md
- A5 proof: book/07_com_nguoi_A5_PROOF.pdf
- Interactive source: digital/index.html and digital/assets/
- Video proof: video/com_nguoi_animatic_v01.mp4
- Production storyboard/audio brief: video/STORYBOARD.md and video/NARRATION.md
- Existing 61-task tracker: docs/CHECKLIST.csv and docs/FULL_CHECKLIST.md
- Release QA: docs/QA_REPORT.md and docs/LAUNCH_REVIEW.md
- Published archive: https://jasonthedataguy.github.io/json-under-revision/chapters/07/

Cơm nguội established the **repeatable pipeline**, not a fully finished commercial multimedia chapter. Its PDF is a proof, art remains provisional, the MP4 is an ambient-only animatic, and print/voice/social release gates remain. For subsequent chapters, reuse the workflow—not the unfinished status labels or unchecked assumptions.

---

## 12. DEFINITION OF “THE SAME EXPERIENCE”

A new post has received the complete .json treatment only when it has:

1. A **complete, author-approved** chapter that stands alone in the book.
2. Original, approved visual storytelling with the appropriate print/digital/social exports.
3. An illustrated, printable and verified PDF proof; plus a distinct print-ready version only when the printer gates pass.
4. A working accessible web chapter and optional, honest memory artifact.
5. A **finished** narrated and captioned 9:16 short, or a clearly marked and documented animatic proof.
6. Instagram/TikTok/Facebook/YouTube publication packs with real files and honest post status.
7. Organized source/control files, release QA, credits, and a reviewable Git commit/PR.
8. Actual deployed/published URLs only where verified.
9. No unauthorized private data, false scientific claims, unlicensed material, or invented autobiographical scenes.

**Guiding sentence:** Build a richer doorway into the memory without explaining away the memory itself.
