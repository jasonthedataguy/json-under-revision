# First chapter release review — 16 October 2026

## Scope and strategy

Read all 21 pages of the supplied strategy PDF. This folder contains the first delivered prototype, **07 — Cơm nguội**, not chapter 01. The strategy's suggested pilot chapters are 10, 11 and 12 (pages 7 and 18); those manuscripts are absent. Preserve chapter 07's identity until the author decides the book sequence.

The strategy makes the physical book canonical, with optional memory and revision artifacts (pages 3–4). It recommends one lasting URL per chapter (page 8), truthful short videos (page 17), and a three-chapter pilot before manufacturing. Prices, conversion rates and budgets are illustrative assumptions, not validated sales or supplier quotes.

## Editorial findings

The original's emotional progression works: present habit, childhood observation, a protective gesture, then the unchanged final exchange. Keep the ending without an added moral. The proposed edit tightens punctuation and removes some of the narrator's conversational phrasing; that is an author choice. No editorial choice has been inferred as approval.

The sentence about stomach pain is parental dialogue, not medical advice. The provisional apartment window, clothing and city view are invented details. The public candidate omits that image and uses the existing two-bowl illustration, clearly described as an interpretation. The source manuscript and proposed edit remain preserved.

## Prepared for release

- Static export: `python scripts/build_site.py --text original` (or `proposed-edit` after selection).
- Export contains only the landing page and chapter portal with two selected assets. It does not copy manuscripts, private notes, print proofs, previews or the provisional family image.
- Stable path within the site: `chapters/07/`. Repository-prefix hosting is supported through relative links.
- GitHub Pages workflow runs manually and publishes only the generated `site/` folder. Select GitHub Actions as the Pages source first. A private repository may require an eligible GitHub plan for Pages; check this before choosing hosting.
- The repository itself should initially be private because it contains unpublished production materials. A public website and a public source repository are different choices.

## Outstanding release dependencies

1. Git commit author name/email and authenticated GitHub account. No existing repository or commit convention was present.
2. Author's text selection; channel account identity and handle availability.
3. Create remote repository, push, enable Pages, run deployment and verify the live chapter URL.
4. Choose the durable owned URL before printing a QR. The deck's domain is a concept, not evidence of ownership.
5. The existing A5 PDF is an edited-text layout proof with a QR placeholder. It is not press-ready; update only after text selection and live URL, then obtain printer specifications/proof.
6. Existing video remains a 24-second animatic with provisional art. Do not label it as a finished narrated film. Final social release needs approved art and a rendered, checked export; author narration requires an actual recording if wanted.
7. Sign in to YouTube/TikTok to create channels. No channels or uploads have been created by this preparation.

Do not start preorders from the deck's illustrative prices. The remaining manuscripts, consent review, print/fulfillment quotes and refund/checkout arrangements are not supplied.

## Local validation

The original-text candidate was served over local HTTP and opened in a browser. All ten manuscript paragraphs rendered with Vietnamese accents, the two-bowl image loaded, and the second memory button updated its text and pressed state. The skip-link encoding issue found during this check was corrected. Live HTTPS, real-device audio playback and printed QR verification remain pending.

Git was initialized on `main`. The author identified the GitHub account as `jasonthedataguy`; commit attribution uses that account's verified GitHub-provided noreply address. The remote repository is https://github.com/jasonthedataguy/json-under-revision. It was created public, so uploading the full production kit awaits a choice between private source storage and public publication of drafts. Website deployment remains pending.
