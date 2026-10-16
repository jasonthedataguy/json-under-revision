# .json — Jason, under revision

A chapter archive with the story, interactive artifacts, and downloadable production media.

- [Read Expected_utility — chapter 04](https://jasonthedataguy.github.io/json-under-revision/chapters/04/)
- [Read Cơm nguội — chapter 07](https://jasonthedataguy.github.io/json-under-revision/chapters/07/)
- [Open the archive](https://jasonthedataguy.github.io/json-under-revision/)

## Selected chapter package

`Expected_utility/` is the author's selected final artifact, imported in full from `Expected_utility_poster_v02_full_chapter` on 16 October 2026. All 37 supplied files are preserved unchanged. Its original review-only labels are historical; the author explicitly authorized push and deployment. See the [release record](docs/chapters/expected-utility/RELEASE.md) and [file inventory](docs/chapters/expected-utility/BUNDLE_INVENTORY.json).

The public chapter keeps the supplied poster design, selected prose and interactive decision tree, with navigation, downloads and small responsive/accessibility fixes. All media is available individually or in the complete chapter ZIP. The PDF is an eight-page A5 layout proof; the video is a 24-second ambient-only animatic. Those formats remain accurately labeled after publication. Social assets are ready to download; platform posts are managed by the author.

Cơm nguội uses the previously selected edit in `content/proposed-edit.md`; the original manuscript is preserved separately. Its existing PDF and ambient-only animatic are linked from the chapter page. Future narrated videos require Jason's actual recording; voice generation remains stopped. A custom domain and print QR are deferred.

## Build and deploy

Python 3.12 is used by CI; the site build has no third-party dependencies.

```sh
python scripts/build_site.py --text proposed-edit
python scripts/check_site.py
python -m http.server 8765 --directory site --bind 127.0.0.1
```

`--text original` selects the Cơm nguội original; pass the same option to `check_site.py`. Expected_utility always uses the author's selected package. The build cleans and recreates only `site/`. Pushes to `main` build, validate and deploy that directory through GitHub Pages. Manual deployment remains available in the Actions workflow.

The supplied media builder, `Expected_utility/scripts/build_v02.py`, is preserved as provenance. It requires Pillow, ReportLab, ffmpeg and the Linux fonts specified in its source. Deploying the website uses the finished media and does not rerender it.

## Production records

- [Current project update](PROJECT_UPDATE.md)
- [Expected_utility release and QA](docs/chapters/expected-utility/RELEASE.md)
- [Earlier project state](docs/history/2026-10-16-before-expected-utility-release.md)
- [Reusable chapter production playbook](docs/CHAPTER_PRODUCTION_PLAYBOOK.md)

The repository is public by author choice, including drafts and production notes. Public access is not a license to reuse the author's prose or artwork. Historical documents describe earlier milestones; the current release record supersedes their pending approval and import statements.
