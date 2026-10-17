# Fashion / 02 — 9+ product-quality release plan
**Status:** Author review + physical-media work required. **Scope:** The chapter is publicly readable; this branch is a proposed immersive upgrade, not a verified commercial release.

## Product definition
Canonical: the author's 17 October 2026 selected manuscript. The printed and digital prose remain identical. The book is the story; the archive is optional context, contradiction or feeling. The chapter must offer a memorable Read → Explore → Revisit → Keep journey without invented memories. The six image excerpts remain illustrations, not photographs of actual possessions.

## What this branch improves immediately
1. **ENTER:** Side A / Then and Side B / Now, supporting the underlying "borrowed identity → lived identity" tension. The original hero poster and author text remain.
2. **READ:** Quiet long-form prose, progress affordance, and visible assurance that the archive is optional. The manuscript checksum and QA still govern its integrity.
3. **EXPLORE:** Six-stage wardrobe with source-verbatim text, provenance annotations, focusable controls, arrow-key navigation, and stage indicators. No quiz or invented personal data.
4. **REVISIT:** Three side-by-side comparisons selected from the actual 16 and 17 October manuscripts. Historical text is not silently represented as the latest.
5. **KEEP:** Two clear home-print choices, additional formats behind a disclosure, share/copy controls, and explicit "not for sale" status.
6. **DISCOVERY:** Native Open Graph metadata, a richer on-page three-act storyboard, and a documented campaign concept.
7. **PRODUCTION:** Source-truth tests and CI regeneration of the chapter's inventory after the offline page is rebuilt.

## Hard quality gates before calling the chapter 9+/10
### Gate A — Editorial truth
- [ ] Author reviews microedits in EDITORIAL_DECISIONS.md. Update canonical source and documented SHA only by explicit approval; retain the previous revision.
- [ ] Verify historical timelines in the fashion chapter and qualify economic causal claims as an opinion, not science.
- [ ] Ask whether any particular garment or father's wardrobe memory described here is a verifiable personal artifact. **Never invent photos, purchases, dialogue, years or provenance.**
- [ ] Human literary read: 3 readers unfamiliar with the author summarize what changed between "Then" and "Now". The ending should work without opening the archive.

### Gate B — Visual original work
- [ ] Original vector or layered hi-res masters for three turning points: THE RULEBOOK, PATINA, HIDDEN GEM. Not extra crops of the existing 1400×795 artwork.
- [ ] Source/artist license for every hero, poster, illustrated brand-mark and borrowed image; decide what can be commercially printed. Review prominent Nike/adidas marks in the existing master.
- [ ] Keep Fashion's pine/pink color as a chapter accent; retain a shared .json family resemblance with the strategy deck (paper, editorial serif, restrained archival labels). Do **not** imitate a living illustrator's signature style.
- [ ] Check mobile hero crop at 320/375/390px; title is embedded in artwork, so preserve an accessible visible text cue.

### Gate C — Immersive media
- [ ] Record Jason's actual 45–60-second reading and the full chapter; no impersonation/synthetic Jason voice.
- [ ] Prepare one three-act film: 00–10 WANT, 10–30 RULES, 30–60 WHAT REMAINS. Recut original art/motion appropriately.
- [ ] Commission or properly license sound. Re-time SRT/VTT to actual spoken words; current tracks represent on-screen card timing.
- [ ] Physically test film captions/safe-zones in TikTok, Instagram Reels and YouTube Shorts on an actual phone.
- [ ] Add real garment photographs to the archive only after the author verifies the object, person, date and publication rights.

### Gate D — Print / collectible
- [ ] Obtain source resolution and print licensing. Select print vendor's trim, bleed, safe area, gutter, ICC profile and PDF/X requirements; current home-print PDFs are not press-certified.
- [ ] Order at least one A5 color press proof and one imposed booklet test; inspect under natural light.
- [ ] Build a **small** physical pilot: A5 mini-zine, art print, Side A/Side B liner note, removable hang-tag. No fake "limited" numbers.
- [ ] Verify cost/COGS with vendors and use preorders only after rights, sample inspection and consumer checkout compliance.

### Gate E — Reader evidence / growth
- [ ] Run a 5-person task test: open from mobile, read, change a wardrobe state by touch and keyboard, find previous version, download an A5, share a link.
- [ ] Record friction, misunderstandings and task success; don't infer engagement from built assets.
- [ ] Measure privacy-safe aggregate events only after selecting a data provider, obtaining consent where required, and documenting retention. Proposed event names: fashion_read_start, fashion_archive_select, fashion_revision_open, fashion_download_a5, fashion_share, fashion_print_interest.
- [ ] Implement a real, privacy-compliant first-party opt-in **only when an endpoint, policy and mailing list are configured**. A nonworking form is worse than no form.
- [ ] Launch Instagram/TikTok/YouTube/FB content as editorial discovery, not a sales ad; record live URLs and true referral traffic.
- [ ] The 21-page strategy recommends a **three-chapter paid pilot**, with a ≥200 paid-preorder gate and target CAC ≤65K. These are hypotheses/gates, not current results or a promise for Chapter Fashion by itself.

## Score target and evidence rubric
| Dimension | Starting audit | 9+ acceptance evidence |
|---|---:|---|
| Prose / narrative | 7.8 | Author approves microedit; independent reader feedback shows emotional clarity |
| Original visual identity | 7.9 | Three new bespoke originals, rights cleared, mobile and print test |
| Interaction / site | 6.8 | Full device/keyboard/screen-reader QA; reader tasks pass |
| Film / audio | 6.4 | Author voice + licensed, edited, captioned narrative short |
| Commercial readiness | 4.8 | Real validated opt-in, press proof, rights and paid-intent evidence |

**Scoring rule:** 9+ is a release target to demonstrate with inspections and reader evidence, not an automatic score assigned when this branch merges. Functional code completion is distinct from artistic and commercial certification.

## Suggested next order
1. Review this branch's web experience.
2. Approve manuscript microedits; answer memory provenance questions.
3. Commission/paint the three unique scenes (not recycled crops), record voice.
4. Recut and retime film, redo campaign exports, print the sample.
5. Run device/reader QA and only then launch the three-chapter commercial pilot.

**Authorship:** All source facts come from the repository's Fashion manuscript, images and existing status docs. Proposed editorial interpretation and visual treatments are labeled as proposals.
