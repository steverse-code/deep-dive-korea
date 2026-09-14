# Skipped — 2026-09-14 (Mon), reel / restaurant

No queue item was created. No content JSON, no rendered output, no change to
`queue.json`. Stopped under PIPELINE.md §0 ("If rights ... cannot be verified,
stop without adding a queue item").

Two independent blockers, both introduced by the policy rewrite in 8128750
(2026-09-14 10:12 KST), which this run is the first to execute.

## 1. No compliant media exists for a venue-specific Reel

PIPELINE.md §3 now allows, in order: (1) original media from the account owner,
(2) venue/creator media with written permission, (3) licensed stock **only for a
non-venue-specific editorial Carousel**. CONTENT.md agrees: "Venue-specific Reels
and Collabs must use original or written partner-authorized media."

Monday is reel + restaurant, i.e. venue-specific. In this environment:

- there is no owner-supplied original media. Every file in `assets/photos/` was
  fetched by a previous pipeline run; the only human-added one
  (`cheongildip-en.jpg`, 392aefd) predates the new policy;
- written venue permission cannot be obtained by an unattended run;
- licensed stock is available and legal, but §3 forbids it for this format.

This is a policy change, not a research failure. The previous PIPELINE.md §4
explicitly permitted mood-matched Unsplash stock and said the photo "does not need
to be the literal venue's own interior." 8128750 removed that allowance. Every
existing post relies on it — `rights_note` values in `content/` read "licensed
free-use stock, not <venue> itself." Under the new rules none of those would be
publishable as Reels.

**This blocks every future run too, not just today.** Mon/Tue/Thu/Fri/Sun are all
venue-specific Reels. Only Wed/Sat (Carousel) can proceed, and only on a
non-venue-specific editorial topic.

To unblock, one of:

- drop original photos into `assets/photos/` for the venues to be covered;
- restore a stock allowance for Reels in PIPELINE.md §3 (with the "never presented
  as the actual venue" disclaimer the old posts used);
- move the venue-specific days to Carousel and keep Reels for editorial topics.

## 2. `ffmpeg` is not installed on the runner

PIPELINE.md §4 now requires, for a Reel:

```bash
python3 scripts/reel.py content/<slug>.json out   # -> 1080x1920 MP4
```

`daily-content.yml` installs only pillow. `scripts/reel.py` shells out to `ffmpeg`
and fails:

```
FileNotFoundError: [Errno 2] No such file or directory: 'ffmpeg'
```

Previously the cloud pipeline rendered card-news only and Reels were built locally
— `assets/music/README.md` still documents that ("릴스는 현재 로컬에서 수동으로
만듭니다"). §4 moved MP4 rendering into the cloud without adding the dependency.

Fix: add an ffmpeg install step to `daily-content.yml`, e.g.

```yaml
- name: ffmpeg 설치
  run: sudo apt-get update && sudo apt-get install -y ffmpeg
```

Note `assets/music/*.mp3` is gitignored, so cloud-built Reels will use synthesized
audio rather than the licensed Incompetech tracks.

## What was verified working

- `TZ=Asia/Seoul date` → 2026-09-14 Monday → reel / restaurant (§1).
- No same-day `pending`/`published` queue item (§0). Yesterday's
  `2026-09-13-terarosa-gangneung-en` is still `pending`.
- WebSearch and WebFetch both work. (guide.michelin.com returns empty to WebFetch;
  koreaherald.com works.)
- `scripts/cardnews.py` renders 7 slides at 1080x1350 with no errors.
- No ramp flag is set anywhere in `queue.json` or repo notes, though PIPELINE.md §1
  says to respect one during restriction recovery. Worth setting explicitly —
  everything from 2026-08-30 onward is `held`.
