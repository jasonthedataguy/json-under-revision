# .json / 07 — Cơm nguội: Production Checklist

**Checkpoint:** 2026-10-16 · Prototype v0.1

Legend: DONE means a draft artifact exists, not release approved. BLOCKED means dependency unmet.

## Definition of done

A complete, approved chapter manuscript; final-resolution illustrated book pages and printer proof; deployed HTTPS archive reachable by a scanned QR; and a released vertical video with legally cleared media, accessible captions and author-approved visuals.


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
- [ ] **D06 · Complete screen reader, keyboard, reduced motion tests** — `TODO`  
  Owner: QA · Depends: D05 · Pass: WCAG-focused manual check on mobile and desktop
- [ ] **D07 · Measure speed, CLS and mobile loading** — `TODO`  
  Owner: Engineer · Depends: D05 · Pass: Real 4G phone load target <3s where feasible
- [ ] **D08 · Confirm privacy and analytics consent decisions** — `TODO`  
  Owner: Jason · Depends: E05 · Pass: No personal data capture without explicit policy
- [ ] **D09 · Publish to a real owned domain** — `BLOCKED`  
  Owner: Engineer · Depends: D06,D07,D08 · Pass: HTTPS and permanent human-readable chapter URL working
- [ ] **D10 · Confirm final chapter permalink and redirects** — `BLOCKED`  
  Owner: Engineer · Depends: D09 · Pass: Permalink documented, backup/redirect behavior checked
- [ ] **D11 · Test archive access from final printed QR** — `BLOCKED`  
  Owner: QA · Depends: B05,D10 · Pass: iOS/Android camera opens exact chapter page
- [ ] **D12 · Optionally record author voiceover and captions** — `TODO`  
  Owner: Jason · Depends: E06 · Pass: Own voice rights and transcript; user-initiated audio playback

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
- [ ] **V06 · Record author narration (optional)** — `TODO`  
  Owner: Jason · Depends: E06 · Pass: Clean self-recorded voice in lossless audio
- [ ] **V07 · Final edit, audio mastering and subtitles** — `BLOCKED`  
  Owner: Video editor · Depends: V05,V06 · Pass: Portrait 1080x1920, licensed audio, captions and safe zones
- [ ] **V08 · Export 40–70s discovery cut and 15s teaser** — `BLOCKED`  
  Owner: Video editor · Depends: V07 · Pass: Finished exports plus thumbnail and short caption
- [ ] **V09 · Review platform preview and factual claims** — `BLOCKED`  
  Owner: Jason · Depends: V08 · Pass: No false implied recordings, no clipping, legible on phone
- [ ] **V10 · Publish social post with clear chapter CTA** — `BLOCKED`  
  Owner: Jason · Depends: V09,D09 · Pass: Correct live landing page, logged post URLs

## Release
- [ ] **R01 · Compare source/edit against exported PDF/web/video** — `TODO`  
  Owner: Editor + QA · Depends: B01,D01,V03 · Pass: All excerpts consistent; no altered final sentence
- [ ] **R02 · Run visual QA on PDF and mobile preview** — `TODO`  
  Owner: QA · Depends: B01,D01 · Pass: No clipped text, low contrast, or broken navigation
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
