# .json / 07 — Cơm nguội: Production Checklist

**Checkpoint:** 2026-10-16 · Release preparation; narrator required

Source of truth: [CHECKLIST.csv](CHECKLIST.csv). DONE applies to task acceptance criteria, not release approval. IN PROGRESS means partial verification; BLOCKED means a dependency is missing.

## Definition of done

A complete, approved chapter manuscript; final-resolution illustrated book pages and printer proof; deployed HTTPS archive reachable by a scanned QR; and a released vertical video with required narrator audio, cleared media, synchronized Vietnamese captions and approved visuals. Ambient sound alone does not satisfy narration.

## Editorial
- [x] **E01 · Freeze original manuscript** — `DONE`  
  Owner: Assistant · Depends: — · Pass: Original file matches user source; no overwrites
- [x] **E02 · Prepare restrained line edit** — `DONE`  
  Owner: Assistant · Depends: E01 · Pass: Edited copy plus tracked explanation
- [ ] **E03 · Approve edited text & voice** — `NEEDS APPROVAL`  
  Owner: Jason · Depends: E02 · Pass: Author signs off on every substantive edit
- [ ] **E04 · Verify ages/timeline/history as appropriate** — `TODO`  
  Owner: Jason · Depends: E03 · Pass: No unverifiable details presented as fact
- [ ] **E05 · Rights and sensitivity review (family privacy)** — `TODO`  
  Owner: Jason · Depends: E03 · Pass: No private information exposed without consent
- [ ] **E06 · Freeze canonical text version v1.0** — `BLOCKED`  
  Owner: Jason · Depends: E03,E04,E05 · Pass: Release-tagged manuscript hash recorded

## Illustration
- [x] **A01 · Extract design direction from strategy deck** — `DONE`  
  Owner: Assistant · Depends: — · Pass: Warm dusk, graphic memory, paper, imperfect mark system
- [x] **A02 · Make first visual keyframe** — `DONE`  
  Owner: Assistant · Depends: A01 · Pass: One coherent father/child dinner reconstruction
- [ ] **A03 · Confirm period, cast and setting fidelity** — `NEEDS APPROVAL`  
  Owner: Jason · Depends: A02 · Pass: Illustrated scene clearly authorized or revised
- [ ] **A04 · Create original layered production art** — `TODO`  
  Owner: Artist/Assistant · Depends: A03 · Pass: Background, figures, table, bowls on separate layers
- [ ] **A05 · Export print-grade illustration** — `TODO`  
  Owner: Artist · Depends: A04 · Pass: 300 dpi at final printed size, CMYK conversion vendor-approved
- [ ] **A06 · Export digital/responsive visual assets** — `TODO`  
  Owner: Designer · Depends: A04 · Pass: WebP/AVIF alternatives, alt text, <300KB optimized hero target
- [ ] **A07 · Approve final visual treatment** — `BLOCKED`  
  Owner: Jason · Depends: A05,A06 · Pass: Author approves art across book, web, video

## Book
- [x] **B01 · Create A5 editorial layout proof PDF** — `DONE`  
  Owner: Assistant · Depends: E02,A02 · Pass: Four-page mock PDF with complete text and provisional art
- [ ] **B02 · Choose definitive trim, margins, paper and binding** — `TODO`  
  Owner: Jason + Printer · Depends: B01 · Pass: Written print specification plus vendor quotation
- [ ] **B03 · Apply final chapter numbering across full book** — `TODO`  
  Owner: Editor · Depends: B02 · Pass: Chapter code consistent with final TOC
- [ ] **B04 · Place production art and canonical text** — `BLOCKED`  
  Owner: Designer · Depends: E06,A07,B02 · Pass: No missing glyphs; page parity/baseline grid inspected
- [ ] **B05 · Generate working QR pointing to owned chapter URL** — `BLOCKED`  
  Owner: Engineer · Depends: D10 · Pass: QR scans on Android/iOS over cellular; no redirects to placeholders
- [ ] **B06 · Proofreader pass and art rights check** — `BLOCKED`  
  Owner: Editor · Depends: B04 · Pass: Independent QA documented; permissions present
- [ ] **B07 · Export printer-specific PDF/X, bleeds and color** — `BLOCKED`  
  Owner: Print designer · Depends: B04,B06 · Pass: Printer preflight passes, correct embedded fonts/bleed
- [ ] **B08 · Print physical proof, inspect, approve** — `BLOCKED`  
  Owner: Jason + Printer · Depends: B07 · Pass: Physical text contrast, color, QR and trim approved

## Digital
- [x] **D01 · Implement local mobile chapter page** — `DONE`  
  Owner: Assistant · Depends: E02,A02 · Pass: Offline-loadable HTML; text, artwork, controls visible
- [x] **D02 · Implement interactive memory moments** — `DONE`  
  Owner: Assistant · Depends: D01 · Pass: Accessible buttons cycle three manuscript-derived moments
- [x] **D03 · Implement original/revision archive** — `DONE`  
  Owner: Assistant · Depends: D01 · Pass: Original and editorial explanations accessible separately
- [x] **D04 · Create nonhistorical sound study** — `DONE`  
  Owner: Assistant · Depends: D01 · Pass: Original ambient audio plays when user chooses
- [ ] **D05 · Replace provisional art with approved exports** — `BLOCKED`  
  Owner: Engineer · Depends: A07 · Pass: All image slots use approved optimized assets
- [ ] **D06 · Complete screen reader, keyboard, reduced motion tests** — `IN PROGRESS`  
  Owner: QA · Depends: D05 · Pass: Focus styles and tab initialization improved; full keyboard, screen-reader and reduced-motion checks still pending
- [ ] **D07 · Measure speed, CLS and mobile loading** — `TODO`  
  Owner: Engineer · Depends: D05 · Pass: Real 4G phone load target <3s where feasible
- [ ] **D08 · Confirm privacy and analytics consent decisions** — `TODO`  
  Owner: Jason · Depends: E05 · Pass: No personal data capture without explicit policy
- [ ] **D09 · Publish to a real owned domain** — `IN PROGRESS`  
  Owner: Engineer · Depends: D06,D07,D08 · Pass: GitHub Pages HTTPS chapter is live; owned custom domain and remaining mobile accessibility/performance work pending
- [ ] **D10 · Confirm final chapter permalink and redirects** — `IN PROGRESS`  
  Owner: Engineer · Depends: D09 · Pass: Live /json-under-revision/chapters/07/ path documented; long-term owned domain and print QR destination still to confirm
- [ ] **D11 · Test archive access from final printed QR** — `BLOCKED`  
  Owner: QA · Depends: B05,D10 · Pass: iOS/Android camera opens exact chapter page
- [ ] **D12 · Optionally record author voiceover and captions** — `TODO`  
  Owner: Jason · Depends: E06 · Pass: Own voice rights and transcript; user-initiated audio playback
- [x] **D13 · Build isolated public chapter export** — `DONE`  
  Owner: Assistant · Depends: D01 · Pass: Build emits landing page, chapter page and two assets; original prose preserved; private notes and provisional family image excluded
- [x] **D14 · Verify local HTTP and responsive layout** — `DONE`  
  Owner: Assistant · Depends: D13 · Pass: 10 source paragraphs preserved; image/audio loaded; memory button updates; no overflow at 390/820/1440px
- [x] **D15 · Prepare manual Pages deployment workflow** — `DONE`  
  Owner: Assistant · Depends: D13 · Pass: Manual Pages workflow configured and successfully run; artifact contains only site/; original manuscript selected
- [x] **D16 · Deploy and verify public HTTPS chapter** — `DONE`  
  Owner: Assistant · Depends: D13,D15,G04 · Pass: Workflow 38878045413 succeeded; https://jasonthedataguy.github.io/json-under-revision/chapters/07/ preserves all original paragraphs; image/audio/landing load; memory control works; no overflow at 390/820/1440px

## Video
- [x] **V01 · Write 5-beat short-form storyboard** — `DONE`  
  Owner: Assistant · Depends: E02 · Pass: Every quote comes from source or labeled editorial paraphrase
- [x] **V02 · Generate 5 visual animatic cards** — `DONE`  
  Owner: Assistant · Depends: V01,A02 · Pass: Consistent keyframe and text safe area
- [x] **V03 · Render vertical animatic MP4** — `DONE`  
  Owner: Assistant · Depends: V02 · Pass: Playable H.264 720x1280 with original room tone
- [ ] **V04 · Authorize depiction of father/child memory** — `NEEDS APPROVAL`  
  Owner: Jason · Depends: A03 · Pass: No inaccurate claims of historical documentation
- [ ] **V05 · Create layered art for true movement** — `BLOCKED`  
  Owner: Artist · Depends: A04,V04 · Pass: Separate foreground/background layers
- [ ] **V06 · Produce required narrator audio from confirmed voice source** — `BLOCKED`  
  Owner: Jason + Audio producer · Depends: E06,V11,V12 · Pass: healwayssmile reference URL recorded in video/NARRATION.md; intended speaker/time range and permitted use clarified; narrator WAV produced and reviewed; room tone does not count
- [ ] **V07 · Final edit, audio mastering and subtitles** — `BLOCKED`  
  Owner: Video editor · Depends: V05,V06 · Pass: Portrait 1080x1920; voice mixed above ambience without clipping; Vietnamese captions timed to actual narration; safe zones verified
- [ ] **V08 · Export 40–70s discovery cut and 15s teaser** — `BLOCKED`  
  Owner: Video editor · Depends: V07 · Pass: Finished exports plus thumbnail and short caption
- [ ] **V09 · Review platform preview and factual claims** — `BLOCKED`  
  Owner: Jason · Depends: V08 · Pass: No false implied recordings, no clipping, legible on phone
- [ ] **V10 · Publish social post with clear chapter CTA** — `BLOCKED`  
  Owner: Jason · Depends: V09,D09 · Pass: Correct live landing page, logged post URLs
- [ ] **V11 · Confirm reference speaker and narration method** — `IN PROGRESS`  
  Owner: Jason · Depends: — · Pass: YouTube reference Q-HcJBSspHQ supplied; timestamp/speaker, voice-use permission where needed, and recording/generation method still pending
- [x] **V12 · Prepare source-based discovery reading script** — `DONE`  
  Owner: Assistant · Depends: E01 · Pass: video/narration-script.txt uses unchanged source excerpts; ending preserved; recording duration and final selection pending

## Git
- [x] **G01 · Commit initial chapter kit locally** — `DONE`  
  Owner: Assistant · Depends: — · Pass: Initial commit 3daa919 on main with GitHub noreply identity
- [x] **G02 · Create remote repository and connect origin** — `DONE`  
  Owner: Jason + Assistant · Depends: G01 · Pass: jasonthedataguy/json-under-revision created; HTTPS origin configured; empty remote inspected
- [x] **G03 · Choose public repository publication scope** — `DONE`  
  Owner: Jason · Depends: G02 · Pass: Author confirmed public repository on 16 October 2026 after disclosure that drafts and production notes are included
- [x] **G04 · Push selected files and verify upstream** — `DONE`  
  Owner: Assistant · Depends: G03 · Pass: main pushed to public origin; upstream configured; 0 ahead and 0 behind after initial push

## Channels
- [x] **C01 · Prepare channel identity and launch copy** — `DONE`  
  Owner: Assistant · Depends: — · Pass: YouTube description, TikTok bio and first-post copy in docs/CHANNEL_LAUNCH.md
- [ ] **C02 · Create book YouTube channel** — `BLOCKED`  
  Owner: Jason + Assistant · Depends: C01 · Pass: Signed in but creation page did not complete; channel handle and URL must be verified
- [ ] **C03 · Create book TikTok account/channel** — `BLOCKED`  
  Owner: Jason + Assistant · Depends: C01 · Pass: Author-controlled sign-in required; handle and URL must be verified

## Release
- [ ] **R01 · Compare source/edit against exported PDF/web/video** — `IN PROGRESS`  
  Owner: Editor + QA · Depends: B01,D01,V03 · Pass: Original prose matches public web candidate; PDF still uses proposed edit; final narrated-video consistency pending
- [ ] **R02 · Run visual QA on PDF and mobile preview** — `IN PROGRESS`  
  Owner: QA · Depends: B01,D01 · Pass: Prior PDF contact sheet inspected; local and live HTTPS page checked at 390/820/1440px with no overflow; final-art, screen-reader and real-device QA pending
- [ ] **R03 · Ask 5 test readers about emotional impact** — `TODO`  
  Owner: Jason · Depends: E03,D01 · Pass: Log feedback without leading respondents
- [ ] **R04 · Run pilot with permissioned/paid intent metrics** — `BLOCKED`  
  Owner: Jason · Depends: B08,D10,V10 · Pass: Measure buyer intent and sales; views alone do not prove demand
- [ ] **R05 · Choose release or revision after feedback** — `BLOCKED`  
  Owner: Jason · Depends: R01,R02,R03 · Pass: Document go/revise/stop decision with evidence

## Core product constraints (strategy deck)

- The physical text is canonical; the archive is optional and must add feeling, context, or contradiction rather than repeat the prose.
- One owned, durable URL per chapter; do not print a QR pointing to a local file or temporary deployment.
- Three hero chapters before full book manufacturing; production-complexity risk is explicitly high.
- Rights, consent and privacy must pass before public release.
- This prototype is not a paid validation, a full print-ready PDF, or the finished film.
