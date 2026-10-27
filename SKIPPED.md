# Skipped days — ongoing media-rights blocker

The media-rights blocker below stops every **Reel** day (Mon/Tue/Thu/Fri/Sun). It
does **not** stop Wed/Sat, which are Carousels: PIPELINE.md §3 option 3 allows
licensed stock on a non-venue-specific editorial Carousel. Each entry below
records one skipped run. Stopped under PIPELINE.md §0 ("If rights ... cannot be
verified, stop without adding a queue item"). As of 2026-10-27 that is **thirty-two
consecutive Reel-day skips**, and with the action block withdrawn and the render
path proven it is the only thing standing between the account and a daily
*authoring* schedule — publishing is separately dead on the token below. The
three possible fixes are editorial and reserved for a human — see the 2026-09-15
entry.

**NEW as of 2026-10-25 — a second, self-inflicted publish fault: the caption cap.**
`2026-10-24-korea-address-system-en` (Carousel, the one format that can ship) was
authored and rendered correctly, then **held** at 2026-10-24T22:55:29 KST with
`hold_reason: publish_failed_manual_review` and the error `캡션 2328자 — 상한
2200자를 넘습니다.` Measured this run: the `caption` field alone is **2205**
characters and the 8 hashtags add 123 more, for **2328**. `publish.py:build_caption()`
(`MAX_CAPTION = 2200`, scripts/publish.py:36,65-75) concatenates caption + hashtags
and raises *at publish time*, so the item is lost ~8 hours after it is written.

This matters more than one lost day, because it is the **first hold since 10-10 that
is not the dead token** — the 10-24 item never reached the Graph API at all, so it
produced no new token evidence either (the token blocker below is still last-tested
10-17 and should still be assumed to stand). Two things follow:

- **For the next Carousel run (Wed 2026-10-28): keep `caption` + hashtags under 2200
  characters.** Budget ~2000 for the caption and verify before committing, e.g.
  `python3 -c "import json;d=json.load(open(F));print(len(d['caption'].rstrip())+2+sum(len(t)+1 for t in d['hashtags'])-1)"`.
  This is a drift, not a typo: caption+hashtags across the nine policy-v2 Carousels
  has climbed almost monotonically — 929, 1229, 1374, 1689, 1526, 1572, 1964, 2104,
  2328. The 10-21 post already sat 96 characters under the cap, so the next one over
  the line was predictable and the one after this will be too unless the budget is
  made explicit.
- **Recommended human fix (an agent should not edit the source of truth on its own
  judgment):** state the 2200-character cap in PIPELINE.md §4 and CONTENT.md
  "Editorial rules" — neither currently mentions it — and/or move the
  `build_caption()` length check into an authoring-time preflight so an over-length
  caption fails the content run that can still fix it, not the publish run that
  cannot.

**NEW AND URGENT as of 2026-10-11: the Instagram access token is invalid, and the
monthly refresh cron cannot fix it.** `2026-10-10-seoul-alley-spending-en` — a
Carousel, the one format that can ship — was queued and rendered correctly and then
**held** at 2026-10-11T00:49:06 KST with `hold_reason:
publish_failed_manual_review`:

```
POST .../v24.0/17841435733524806/media → HTTP 400
OAuthException code 190: "Error validating access token: The session has been
invalidated because the user changed their password or Facebook has changed the
session for security reasons."
```

This is **not** the 60-day expiry that `refresh-token.yml` handles. That workflow
calls `graph.instagram.com/refresh_access_token` (`scripts/refresh_token.py:28`),
which extends a token that is still valid; it cannot resurrect a session the
platform has invalidated, so the 1st-of-month cron will simply fail too. **A human
must re-authorize through Instagram Login and reset the `IG_ACCESS_TOKEN` secret**
(see CONNECT-GUIDE.md); an agent cannot, as it has no access to repository secrets.
Until that happens the 19:00 KST publisher will hold every item it picks up,
including anything queued on the next Carousel day (Wed 2026-10-14). Note this is a
*publish*-side blocker: it does not affect today's decision, which is made on §3
media grounds and would be a skip regardless. **Still unresolved as of 2026-10-15**
and not checkable by an agent (the token lives in a repository secret), so assume it
stands.

**CONFIRMED 2026-10-18 — the token is dead, now proven rather than presumed.** The
two entries below said the token blocker was *untested* since 10-10 and should be
assumed to stand. It has now been tested and it stands. Sat 2026-10-17 (Carousel,
local) ran, queued and rendered `2026-10-17-bukchon-visiting-hours-en` (commit
7957fb1), the 19:00 KST publisher picked it up, and it was **held** at
2026-10-17T22:34:30 KST with the identical fault — `hold_reason:
publish_failed_manual_review`, OAuthException **code 190**, "session has been
invalidated" (commit a707112, `fbtrace_id AFD2WVXAyVLXu8xXLJrReZO`). Two readings
follow, and they point opposite ways:

- **The token fix is now the top-priority human action.** It is no longer a
  prediction. Two consecutive Carousels — 10-10 and 10-17, the only two that
  reached the publisher — were authored correctly and lost at the final step. Every
  future Wed/Sat will be lost the same way until `IG_ACCESS_TOKEN` is re-authorized
  through Instagram Login (CONNECT-GUIDE.md). An agent cannot do this; the token is
  a repository secret.
- **`--max-turns 60` is *not* currently blocking.** The 10-17 run produced a
  complete item, so it cleared 60 turns. That is the second data point after 10-07
  on the "lean run clears it" side. The turn cap remains worth raising, but the
  stacked-faults framing below now resolves to a single live publish-side fault.

**Update 2026-10-15 — the Wed 2026-10-14 test of this never happened.** The entry
above predicted that the 2026-10-14 Carousel would be queued, rendered, picked up by
the 19:00 KST publisher and held on the dead token. It was not, because the run never
produced an item: run `38501553280` **failed after 11m52s with `Reached maximum
number of turns (60)`**. So the token blocker is still *untested* since 10-10 — no new
evidence either way, and it should still be assumed to stand. The practical point is
that **two independent faults are now stacked on the only format that can ship**: the
turn cap stops the item being created, and the dead token would stop it being
published if it were. Fixing either one alone still ships nothing.

**`--max-turns` is still unraised, but the 2026-10-07 Carousel shipped anyway.**
The 2026-10-06 entry warned that Wednesday 2026-10-07 would fail the same way as
09-30 and 10-03 unless the one-line workflow fix landed. It did not land —
`.github/workflows/daily-content.yml` still reads `--max-turns 60` — and the
Carousel shipped regardless: `2026-10-07-seoul-cafe-churn-en` is `published`
(media_id 17885158536504317, commit 59fa888, marked posted in c5adce1). So 60
turns is a **marginal** budget for a Carousel, not a hard wall: a lean run clears
it, a thorough one does not. That weakens the diagnosis from "will fail" to "will
fail some of the time," and it does not change the recommendation — raising it is
still the cheapest fix for the only format that can currently ship.

**2026-10-14 (Wed) is the fourth Carousel day lost this way, confirmed 2026-10-15.**
`.github/workflows/daily-content.yml:80` still reads `--max-turns 60`. Run
`38501553280` failed at 11m52s with `Reached maximum number of turns (60)`
(`"subtype": "error_max_turns"` in the action log). No content JSON, no queue entry
and — until this entry — no skip note, exactly like 09-30 and 10-03. The tally is now
09-26 (finished at 74 turns, shipped, step still went red), 09-30, 10-03 and 10-14:
of the last six Carousel days, **three produced nothing at all** because of a
one-line workflow setting. That settles the "marginal, not a wall" reading above in
the pessimistic direction — a thorough run is the common case, not the rare one.
Raising it remains a human-only fix (`workflows: write` is not granted to this
agent).

**The silent Carousel gaps are diagnosed as of 2026-10-05: the runs fired, and they
died on `--max-turns 60`.** Previous entries recorded 2026-09-30 (Wed) and
2026-10-03 (Sat) as unexplained — Carousel days, the one format the media blocker
does **not** stop, each with no content commit, no queue entry and no skip entry —
and asked a human to check the run history. This run checked it. `gh run list
--workflow=daily-content.yml` shows both days **ran and failed**, and
`--log-failed` gives the same cause for each:

| Run | Day | Duration | Error |
|---|---|---|---|
| 36211557490 | 2026-09-26 Wed | 12m25s | `Claude reported a successful result after 74 turns, exceeding the configured maximum of 60` |
| 36661618514 | 2026-09-30 Wed | 13m07s | `Reached maximum number of turns (60)` |
| 37090827232 | 2026-10-03 Sat | 18m33s | `Reached maximum number of turns (60)` |

`.github/workflows/daily-content.yml:79-82` sets `claude_args: --max-turns 60`.
Authoring a Carousel — read the four long policy/notes files, research and verify a
venue, fetch a photo, write the JSON, render and inspect 7 slides, queue, commit,
push — does not fit in 60 turns. A Reel day fits easily because it stops at the §3
media gate after ~5-6 min, which is exactly why **every** successful run in the
history is a skip and **every** failure is a Carousel day. 2026-09-26 is the tell:
it finished the work at 74 turns, so the content committed and published, and the
step still went red. 09-30 and 10-03 hit the wall earlier and wrote nothing.

So the two problems have one shape: **the only format that can ship is the only
format that cannot finish.** The fix is a one-line workflow change — raise
`--max-turns` (120 is a safe starting point; `timeout-minutes: 30` is the real
backstop and no run has come close to it). **A human must apply it**: pushing to
`.github/workflows/` is rejected for an agent because `daily-content.yml` grants
only `contents: write` / `id-token: write`, not `workflows: write` — the same
blocker logged for the ffmpeg step on 2026-09-15. Not caught up here: §0 forbids
catching up missed days.

**The Instagram action-block blocker is withdrawn as of 2026-09-27.** From
2026-09-17 this file carried a second, separate blocker on all seven days: the
account was action-blocked, so Wed/Sat items queued but failed at publish time.
That is no longer true. `2026-09-26-korea-market-price-rules-en` **published
successfully** at 2026-09-26 23:18:57 KST (media_id 18144186298582897, commit
d3b80bf) — the first success since 2026-08-30 and the first after four
consecutive code 4 / subcode 2207051 holds (09-13, 09-16, 09-19, 09-23). The
publish path works end to end again. **Only the media blocker remains, and it
stops Reel days only.** Two consequences for a human, in §1/§0 order:

- PIPELINE.md §1's **ramp flag now actually matters**. While every publish failed
  it constrained nothing. With publishing live, CONTENT.md's recovery ramp (three
  posts in week 1, four in week 2, then daily) is the binding limit — and no ramp
  flag is set in `queue.json` or any repo note. 2026-09-26 is post 1 of week 1.
- The 32 `held` items are **not** revived by this: §0 forbids reviving `held`
  items and forbids catching up missed days. Clearing them is a human decision.

**The ffmpeg blocker is withdrawn as of 2026-09-22.** The 2026-09-20 entry called
missing ffmpeg a third independent blocker on Reel days. That overstates it: ffmpeg
is absent from the runner image but installable at runtime, and on 2026-09-22
`sudo apt-get install -y ffmpeg` succeeded and `scripts/reel.py` then produced a
valid 1080×1920 / 22.2s MP4. A run that needs the Reel path can install it itself,
so it is a per-run setup step, not a blocker. Adding it to `daily-content.yml`
would still save the install on every run — see the 2026-09-15 entry for why an
agent cannot push that change. **Only the media blocker stops Reel days.**

---

## 2026-10-27 (Tue), reel / local — SKIPPED

Thirty-second consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged and was
re-derived mechanically this run rather than inherited from the 2026-10-26 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Tue 2026-10-27 11:46 KST, `%u` = 2 → **reel / local /
  Collab candidate**. The task prompt independently specified `reel`; the two agree.
- §0: **no `pending` or `published` item for 2026-10-27.** `queue.json` holds **49**
  entries (36 `held`, 13 `published`, **0 `pending`**) and contains no `2026-10-27`
  string at all. Nothing to stop on, so the run proceeded.
- §3: a Reel needs option 1 (owner original) or option 2 (venue/creator media with
  written permission). Option 3 (licensed stock) is restricted to a
  non-venue-specific editorial **Carousel**; CONTENT.md "Media and rights" says the
  same independently ("Venue-specific Reels and Collabs must use original or written
  partner-authorized media"). Note this binds on **format**, so even a
  dish-as-subject editorial angle — the obvious Tuesday/local escape — cannot use
  stock today.
- **Neither option 1 nor option 2 exists in the repo.** All **50** files in
  `assets/photos/` are referenced by one of the **49** `content/*.json` files, so the
  unused set is **empty**. `git ls-files` filtered for
  `mp4|mov|m4v|avi|webm|mkv|mp3|wav|m4a|heic|raw|dng` returns **zero** files, so
  there is no owner video for a Reel either.
- A fresh audit of all 49 content files: **9** carry `policy_version: 2` and all nine
  are `asset_source: licensed_stock` on a `carousel`. **Zero** files anywhere in the
  repo declare `original` or `partner_licensed`. The one human-added photo,
  `assets/photos/cheongildip-en.jpg` (392aefd, 2026-08-25), remains rejected for the
  reasons set out on 2026-10-25.
- No new media channel appeared: `git fetch --all` leaves `main` level with
  `origin/main` at ed4f7ec, `main` is the only branch, the tree is clean, and no
  `inbox/`, `incoming/`, `uploads/`, `media/`, `submissions/`, `originals/` or
  `footage/` path exists. Every `assets/` addition since the policy-v2 rewrite is a
  `claude[bot]` content commit fetching stock for that day's Carousel; no human has
  added media since 2026-08-25.
- No ramp flag is set in `queue.json`, `.github/` or `scripts/` (PIPELINE.md §1), so
  the ramp constrained nothing and the skip is decided on §3 grounds alone.

Stopped under §0: "If rights, venue existence, or current operation cannot be
verified, stop without adding a queue item." Venue research was not carried out,
because the gate that fails is upstream of it: no amount of verified venue fact
produces a publishable Reel without compliant media.

### Verified working this run

- `scripts/cardnews.py` renders **7 slides** with no error, exit 0, each 1080×1350
  RGB (run on `content/2026-10-24-korea-address-system-en.json` into
  `/tmp/render-check`, outside the repo; nothing committed). Slide 04 — the most
  text-heavy `list` slide — was opened and inspected by eye: all four item titles and
  bodies sit inside the text column with no collision and no clipping, per the
  2026-09-14 note that `fit()` overflows silently and exit 0 proves nothing.
- **WebSearch works** (MICHELIN Guide Seoul & Busan 2026 Bib Gourmand query returned
  current results). **WebFetch works** on koreajoongangdaily.com, which confirmed the
  2026 Bib Gourmand detail: announced 26 Feb 2026, 71 restaurants (51 Seoul / 20
  Busan), ceiling KRW 45,000 per person, 8 new entries. Recorded only as a tool
  check — **no content was authored from it.**
- **ffmpeg is still absent from the runner image** (`which ffmpeg` → not found), so
  §4's `scripts/reel.py` step would need `sudo apt-get install -y ffmpeg` first. Not
  a blocker (installable per-run) and moot today, but the `ffmpeg 설치` step
  requested on 2026-09-15 still has not landed in `daily-content.yml`.

### The publish-side faults, re-checked (all still open)

- **The caption cap is still undocumented, and the run it threatens is tomorrow.**
  `scripts/publish.py:36` still sets `MAX_CAPTION = 2200` and raises at publish time;
  a grep for `2200` across PIPELINE.md and CONTENT.md still returns nothing. The
  drift was re-measured from source this run, not inherited — caption + hashtags
  across the nine policy-v2 Carousels: 929, 1229, 1374, 1689, 1526, 1572, 1964, 2104,
  **2328** (2026-10-24, the one that was held). **The next Carousel run is Wed
  2026-10-28 — the very next run after this one.** It must budget the caption
  itself: aim at ~2000 total, and verify before committing with
  `python3 -c "import json;d=json.load(open(F));print(len(d['caption'].rstrip())+2+sum(len(t)+1 for t in d['hashtags'])-1)"`.
- **`--max-turns 60` is still unraised** (`.github/workflows/daily-content.yml:80`;
  `timeout-minutes: 30` at `:37`). Unchanged and still human-only to fix.
- The dead `IG_ACCESS_TOKEN` (OAuthException code 190) was not re-tested this run —
  nothing was queued, so nothing reached the publisher — and remains last-proven
  2026-10-17. Assume it stands. Note what this means for tomorrow: even a
  correctly-budgeted Carousel on 10-28 will be `held` on the token, so fixing the
  caption cap buys a valid item, not a published one.

**Not done, deliberately:** the format was not swapped to Carousel to get a post
out. PIPELINE.md §1 assigns Tuesday a Reel and the task prompt says `reel`; moving
venue days to Carousel is one of the three fixes listed in the 2026-09-15 entry and
is an editorial decision for a human. Also not done: reviving any of the `held`
items (§0), catching up the missed days (§0), and editing PIPELINE.md / CONTENT.md
to document the caption cap — that is a change to the source of truth and is
likewise reserved for a human.

---

## 2026-10-26 (Mon), reel / restaurant — SKIPPED

Thirty-first consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged and was
re-derived mechanically this run rather than inherited from the 2026-10-25 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Mon 2026-10-26 11:09 KST, `%u` = 1 → **reel /
  restaurant / Collab optional**. The task prompt independently specified `reel`;
  the two agree.
- §0: **no `pending` or `published` item for 2026-10-26.** `queue.json` holds **49**
  entries (36 `held`, 13 `published`) and contains no `2026-10-26` string at all.
  Nothing to stop on, so the run proceeded.
- §3: a Reel needs option 1 (owner original) or option 2 (venue/creator media with
  written permission). Option 3 (licensed stock) is restricted to a
  non-venue-specific editorial **Carousel**; CONTENT.md "Media and rights" says the
  same independently ("Venue-specific Reels and Collabs must use original or written
  partner-authorized media").
- **Neither option 1 nor option 2 exists in the repo.** All **50** files in
  `assets/photos/` are referenced by one of the **49** `content/*.json` files, so the
  unused set is **empty**. A repo-wide `git ls-files` filter for
  `mp4|mov|m4v|avi|webm|mkv|mp3|wav|m4a|heic|raw|dng` returns **zero** files, so
  there is no owner video for a Reel either.
- A fresh audit of all 49 content files (not inherited): **9** carry
  `policy_version: 2` and all nine are `asset_source: licensed_stock` on a
  `carousel`. **Zero** files anywhere in the repo declare `original` or
  `partner_licensed`. The one human-added photo, `assets/photos/cheongildip-en.jpg`
  (392aefd, 2026-08-25), remains rejected for the reasons set out on 2026-10-25: it
  predates the policy-v2 rewrite and its post records no rights metadata, so
  "supplied by the owner" cannot be verified — and it is the wrong pillar besides.
- No new media channel appeared: `git fetch --all` leaves `main` level with
  `origin/main` at 06bb749, `main` is the only branch, the tree is clean, and no
  `inbox/`, `incoming/`, `uploads/`, `media/`, `submissions/`, `originals/` or
  `footage/` path exists.
- No ramp flag is set in `queue.json`, `.github/` or `scripts/` (PIPELINE.md §1), so
  the ramp constrained nothing and the skip is decided on §3 grounds alone.

Stopped under §0: "If rights, venue existence, or current operation cannot be
verified, stop without adding a queue item." Research was not carried out, because
the gate that fails is upstream of it: no amount of verified venue fact produces a
publishable Reel without compliant media.

### Verified working this run

- `scripts/cardnews.py` renders **7 slides** with no error, exit 0, each 1080×1350
  (run on `content/2026-10-24-korea-address-system-en.json` into a scratch dir
  outside the repo; nothing committed). Slide 04 — the most text-heavy `list` slide —
  was opened and inspected by eye: all four item titles and bodies sit inside the
  text column with no collision and no clipping, per the 2026-09-14 note that `fit()`
  overflows silently and exit 0 proves nothing.
- **WebSearch works** (MICHELIN Guide Seoul & Busan 2026 query returned current
  results). **WebFetch works** on korea.stripes.com.
- **ffmpeg is still absent from the runner image** (`which ffmpeg` → not found), so
  §4's `scripts/reel.py` step would need `sudo apt-get install -y ffmpeg` first. Not
  a blocker (installable per-run) and moot today, but the `ffmpeg 설치` step
  requested on 2026-09-15 still has not landed in `daily-content.yml`.

### The two publish-side faults, re-checked (both still open)

- **The caption cap is still undocumented.** `scripts/publish.py:36` still sets
  `MAX_CAPTION = 2200` and raises at publish time (`:73-74`), and a grep of
  PIPELINE.md and CONTENT.md for `2200` still returns nothing. The 2026-10-25 header
  note's recommendation stands unactioned, so **the next Carousel run (Wed
  2026-10-28) must budget the caption itself**: keep `caption` + hashtags under 2200,
  aim at ~2000, and verify before committing with the one-liner in that note.
- **`--max-turns 60` is still unraised** (`.github/workflows/daily-content.yml:80`;
  `timeout-minutes: 30` at `:37`). Unchanged and still human-only to fix.
- The dead `IG_ACCESS_TOKEN` (OAuthException code 190) was not re-tested this run —
  nothing was queued, so nothing reached the publisher — and remains last-proven
  2026-10-17. Assume it stands.

**Not done, deliberately:** the format was not swapped to Carousel to get a post
out. PIPELINE.md §1 assigns Monday a Reel and the task prompt says `reel`; moving
venue days to Carousel is one of the three fixes listed in the 2026-09-15 entry and
is an editorial decision for a human. Also not done: reviving any of the `held`
items (§0) and catching up the missed days (§0).

---

## 2026-10-25 (Sun), reel / cafe — SKIPPED

Thirtieth consecutive Reel-day skip. No content JSON, no rendered output committed,
no change to `queue.json`. The §3 media blocker is unchanged and was re-derived
mechanically this run rather than inherited from the 2026-10-23 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Sun 2026-10-25 11:08 KST, `%u` = 7 → **reel /
  cafe-dessert / Collab optional**. The task prompt independently specified `reel`;
  the two agree.
- §0: **no `pending` or `published` item for 2026-10-25.** `queue.json` holds **49**
  entries and contains no `2026-10-25` string at all. Nothing to stop on, so the run
  proceeded.
- §3: a Reel needs option 1 (owner original) or option 2 (venue/creator media with
  written permission). Option 3 (licensed stock) is restricted to a
  non-venue-specific editorial **Carousel**; CONTENT.md "Media and rights" says the
  same independently ("Venue-specific Reels and Collabs must use original or written
  partner-authorized media").
- **Neither option 1 nor option 2 exists in the repo.** All **50** files in
  `assets/photos/` are referenced by one of the **49** `content/*.json` files, so the
  unused set is **empty**. A repo-wide `git ls-files` filter for
  `mp4|mov|m4v|avi|webm|mkv|mp3|wav|m4a|heic|raw|dng` returns **zero** files, so
  there is no owner video for a Reel either.
- No new media channel appeared: `git fetch --all` leaves `main` level with
  `origin/main` at cc50134, `main` is the only branch, the tree is clean, and no
  `inbox/`, `incoming/`, `uploads/`, `media/`, `submissions/` or `originals/` path
  exists.
- No ramp flag is set in `queue.json`, `.github/` or `scripts/` (PIPELINE.md §1), so
  the ramp constrained nothing and the skip is decided on §3 grounds alone.

Stopped under §0: "If rights, venue existence, or current operation cannot be
verified, stop without adding a queue item."

### Checked and rejected this run: the one human-added photo

Earlier entries assert that the only human-added asset predates policy v2. That was
re-checked directly this run, because if it qualified under §3 option 1 ("original
footage/photo supplied by the account owner") a Reel could in principle proceed.
It does not qualify:

- `assets/photos/cheongildip-en.jpg` was committed by Steve
  (`steve.seil.oh@gmail.com`) in 392aefd on 2026-08-25, "content: English +
  photo-required pivot; first English test post" — i.e. **before** the policy-v2
  rewrite in 8128750 (2026-09-14).
- Its post, `content/2026-08-25-cheongildip-en.json`, carries **no** rights metadata
  at all: `policy_version`, `asset_source`, `rights_confirmed` and `rights_note` are
  all absent. Nothing records the photo as owner-shot rather than sourced, so
  "supplied by the owner" cannot be distinguished from "committed by the owner",
  and §0 forbids proceeding on rights that cannot be verified.
- It is also the wrong pillar (that post is `local`, today is `cafe`) and the venue
  is already covered.

An audit of all 49 content files found **9** with `policy_version: 2`, and all nine
are `asset_source: licensed_stock` on a `carousel`. **Zero** policy-v2 Reels exist,
and no `original` or `partner_licensed` asset exists anywhere in the repo.

### Verified working this run

- `scripts/cardnews.py` renders **7 slides** with no error (run on
  `content/2026-10-24-korea-address-system-en.json` into a scratch dir outside the
  repo; nothing committed). A sample slide was opened and inspected — text inside
  its box, no collision — per the 2026-09-14 note that `fit()` overflows silently
  and exit 0 proves nothing.
- WebSearch works. WebFetch works on koreaherald.com.
- **ffmpeg is again absent from the runner image** (`which ffmpeg` → not found), so
  §4's `scripts/reel.py` step would need `sudo apt-get install -y ffmpeg` first, as
  on 2026-09-22. Not a blocker (installable per-run) and moot today, but the
  `ffmpeg 설치` step requested on 2026-09-15 still has not landed in
  `daily-content.yml`.

**Not done, deliberately:** the format was not swapped to Carousel to get a post
out. PIPELINE.md §1 assigns Sunday a Reel and the task prompt says `reel`; moving
venue days to Carousel is one of the three fixes listed in the 2026-09-15 entry and
is an editorial decision for a human. Also not done: reviving any of the `held`
items (§0) and catching up the missed days (§0).

---

## 2026-10-23 (Fri), reel / restaurant — SKIPPED

Twenty-ninth consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged and was
re-derived mechanically this run rather than inherited from the 2026-10-22 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Fri 2026-10-23 11:24 KST, `%u` = 5 → **reel /
  restaurant / Collab candidate**. The task prompt independently specified `reel`;
  the two agree.
- §0: **no `pending` or `published` item for 2026-10-23.** `queue.json` still holds
  **48** entries and contains no `2026-10-23` string at all. Nothing to stop on, so
  the run proceeded to §2.
- §3: a Reel needs option 1 (owner original) or option 2 (venue/creator media with
  written permission). Option 3 (licensed stock) is restricted to a
  non-venue-specific editorial **Carousel**, and CONTENT.md "Media and rights" says
  the same independently.
- **Neither option 1 nor option 2 exists in the repo.** Re-checked mechanically:
  all **49** files in `assets/photos/` are referenced by one of the **48**
  `content/*.json` files, so the unused set is **empty** — unchanged from 10-22, and
  no asset has been added since `2026-10-21-korea-no-kids-zones-en.jpg`. A repo-wide
  `git ls-files` filter for `mp4|mov|m4v|avi|webm|mkv|mp3|wav|m4a|heic|raw|dng`
  returns **zero** files, so there is no owner video for a Reel either.
- No new media channel appeared: `git fetch --all` leaves `main` level with
  `origin/main` at 80fb3af, `main` is the only branch, the working tree is clean,
  and no `inbox/`, `incoming/`, `uploads/`, `media/`, `submissions/` or `originals/`
  path exists.
- No ramp flag is set in `queue.json` or any repo note (PIPELINE.md §1) — the only
  `ramp` hits are prose in CONTENT.md, PIPELINE.md and this file — so the ramp
  constrained nothing and the skip is decided on §3 grounds alone.

Stopped under §0: "If rights, venue existence, or current operation cannot be
verified, stop without adding a queue item."

**Not done, deliberately: the format was not swapped to Carousel to get a post out,**
and no licensed-stock Reel was attempted. Friday is a Reel in PIPELINE.md §1 and
nothing in §0–§7 authorises substituting a format to dodge a blocked day; §3 option 3
says *Carousel*, and CONTENT.md repeats that stock is "limited to an occasional
editorial Carousel". Both changes are editorial decisions for a human.

### §2 research — the restaurant slot now has a strong, unused 2026 hook

**As-of date 2026-10-23.** As with the bar slot on 10-22, research is not the
constraint for the restaurant pillar; the photo is.

- **Michelin Guide Seoul & Busan 2026 Bib Gourmand**, announced **26 February 2026**
  ahead of the star reveal in Busan on 5 March 2026: **8 new entries** across both
  cities, of which **5 are in Seoul**. Bib Gourmand means a full meal under
  **45,000 won** per person. New Seoul names reported: **3rd Samgyetang** (Seocho;
  same family since 1973), **Gosari Express** (Sindang-dong Jungang Market; gosari
  oil sauce), **Sobakeeri Suzu** (Korean-buckwheat soba), **Andeok** (beef naengguksu,
  mandutguk) and **Oilje** (perilla-seed miyeok-guk).
  **Verification status, stated plainly: this came from a single standard WebSearch
  pass and the primary sources were not fetched this run.** The 8-entry total and the
  45,000-won ceiling were consistent across sources, but **Oilje's location was not
  confirmed as Seoul**. Before any of this is written up, fetch the Michelin release
  directly (`guide.michelin.com/.../korea-bib-gourmand-2026`) and corroborate with
  Korea JoongAng Daily (`/lifestyle/michelin-releases-2026-bib-gourmand-adds-8-new-korean-restaurants/12491521`).
  **Note for whoever uses this:** the repo already has `content/2026-09-07-gosari-express-en.json`
  and a photo for it — but that photo is stock, so it does **not** unblock a Reel.
- The **affordability** angle is the honest one here: a Michelin-listed meal with a
  published price ceiling is checkable, non-subjective and useful to a traveller,
  which suits CONTENT.md's "no unsupported superlatives" rule.

### Correction for Saturday: the full 서울미식 100선 list *is* readable after all

The 10-20 and 10-22 entries recorded that text sources only ever name the **25 new**
venues and that the full 100 "appears only as images and on the festival site". That
is now out of date, and it matters for the next post that can ship:

- `tasteofseoul.visitseoul.net` **was reachable this run**, from the same tooling that
  got `ECONNREFUSED 115.68.17.176:443` on 10-19 and 10-22. So the site is confirmed
  **intermittent across days** — treat reachability as a coin flip, not as fixed
  either way.
- `tasteofseoul.visitseoul.net/restaurants/list` serves the **full 100선 as a
  paginated, filterable list** — "100개의 지점이 검색되었습니다", pages 1–9, filters for
  all seven categories (한식·양식·아시아·그릴·채식·바&펍·디저트&카페) and all 25
  districts. Page 1 alone named 12 venues (9 디저트&카페, 3 한식). A run that needs
  venue names beyond the new 25 **can** get them here — but only while the site is up,
  so capture them in the content JSON when it is.
- The festival index now lists **8 programs**, not the 4 in the press release:
  서울레스토랑위크, 서울미식마켓, 서울미식투어, **서울미식클래스** (the release called
  it 워크숍), **서울미식어워즈**, 서울 바비큐 페스티벌, 도곡시장 푸드컬처 페스타,
  마장동 한우바비큐 체험.
- **Per-program dates are still unpublished even on day 1.** The index carries no
  dates, and the city's line is unchanged: schedules release 순차적으로 on the site and
  `instagram.com/tasteofseoul_official`. So the gap the 10-22 entry hoped would close
  by Saturday has **not** closed. Do not invent a schedule; the festival window
  (**23–29 October 2026, DDP and citywide**) is the only date fact confirmed by the
  city itself (mediahub.seoul.go.kr/archives/2019580).
- Separately confirmed and still unused: **디저트 50선** is a distinct list of 50 cafes
  and dessert spots, **presented separately for the first time this year**, judged on
  drink/dessert quality, the space, popular appeal and accessibility for foreign
  tourists. It is *not* the 9 디저트&카페 entries inside the 100선. That is a clean
  editorial Carousel topic for a future cafe slot.

### Note for the next slot that can ship — Sat 2026-10-24 (Carousel, local)

The 10-22 recommendation still stands and is now better supported: 서울미식주간 will be
**day 2 of 7** on Saturday, it is editorial and non-venue-specific, and it clears §3
option 3 on licensed stock with no venue photo. Two honest hooks, both verified above:
the official 100선 list *is* now readable in full on the city's site, while the
**per-program schedule for a festival already running is still not published** — the
city opened the week without telling people when its own programs happen.

### Verified working this run

- **WebSearch works** (2 queries, standard, both returned results). **WebFetch works**
  — `koreaherald.com`, `mediahub.seoul.go.kr`, `tasteofseoul.visitseoul.net/` and
  `tasteofseoul.visitseoul.net/restaurants/list` all returned full text. **No fetch
  failed this run**, which is itself the evidence for the intermittency finding above.
- **`python3 scripts/cardnews.py` works.** Rendered
  `content/2026-10-21-korea-no-kids-zones-en.json` into `/tmp` → **7 slides, exit 0**,
  no errors. Rendered to `/tmp` and **not committed**, since §3 produced no new content
  to render.
- `ffmpeg` is still **absent** from the runner image (installable at runtime per the
  2026-09-22 entry). Moot today: the Reel never reached §4, so `scripts/reel.py` was
  not exercised.
- The dead-token publish blocker is unchanged and **not checkable by an agent**
  (`IG_ACCESS_TOKEN` is a repository secret); the three confirmations recorded in the
  10-22 entry (10-10, 10-17, 10-21, all OAuthException **code 190**) stand, and no new
  evidence arrived because nothing was queued since. Re-authorizing `IG_ACCESS_TOKEN`
  through Instagram Login (CONNECT-GUIDE.md) remains the top-priority human action —
  **Saturday's Carousel will be lost the same way unless it happens first.** Nothing
  was queued this run, so no item was exposed to it today.
- `--max-turns 60` did not bite: a Reel-day run stops at the §3 gate well inside budget.

---

## 2026-10-22 (Thu), reel / bar — SKIPPED

Twenty-eighth consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged and was
re-derived mechanically this run rather than inherited from the 2026-10-20 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Thu 2026-10-22 11:18 KST, `%u` = 4 → **reel / bar /
  Collab optional**. The task prompt independently specified `reel`; the two agree.
- §0: **no `pending` or `published` item for 2026-10-22.** `queue.json` now holds
  **48** entries (**35 `held`**, 13 `published`) — one more than the 2026-10-20
  entry recorded, which is yesterday's Carousel being added and then held. The only
  `2026-10-22` string in the file is the `held_at` timestamp of
  `2026-10-21-korea-no-kids-zones-en` (held 2026-10-22T00:00:14 KST), which is not a
  same-day item. Nothing to stop on, so the run proceeded to §2.
- §3: a Reel needs option 1 (owner original) or option 2 (venue/creator media with
  written permission). Option 3 (licensed stock) is restricted to a
  non-venue-specific editorial **Carousel**, and CONTENT.md "Media and rights" says
  the same independently.
- **Neither option 1 nor option 2 exists in the repo.** Re-checked mechanically this
  run: all **49** files in `assets/photos/` are referenced by an existing
  `content/*.json` (48 content files), so the unused set is **empty**. A repo-wide
  `git ls-files` filter for `mp4|mov|m4v|avi|webm|mkv|mp3|wav|m4a|heic|raw|dng`
  returns **zero** files, so there is no owner video for a Reel either.
- No new media channel appeared: `git fetch --all` leaves `main` level with
  `origin/main` at b8e8031, `main` is the only branch, the working tree is clean, and
  no `inbox/`, `incoming/`, `uploads/`, `media/`, `submissions/` or `originals/` path
  exists.
- No ramp flag is set in `queue.json` or any repo note (PIPELINE.md §1), so the ramp
  constrained nothing — the skip is decided on §3 grounds alone.

Stopped under §0: "If rights, venue existence, or current operation cannot be
verified, stop without adding a queue item."

**Not done, deliberately: the format was not swapped to Carousel to get a post out.**
A Carousel would clear §3 on option 3, but PIPELINE.md §1 fixes Thursday as a Reel
and nothing in §0–§7 authorises substituting a format to dodge a blocked day.
Changing the weekly slot is an editorial decision for a human, so this run skipped
rather than quietly rewriting the schedule.

### §2 research — the bar slot is fully researched; only media is missing

**As-of date 2026-10-22.** Worth recording plainly: for the *bar* pillar the research
is no longer the constraint. Two independent 2026 rankings cover the exact venues the
repo already has content files for, and the only thing that has ever stopped these
posts is the photo.

- **Asia's 50 Best Bars 2026**, announced at the Macau ceremony on **28 July 2026**
  (extended 51–100 list published **14 July 2026**), by UK publisher William Reed on
  votes from bartenders, bar owners and drinks writers across Asia. Seoul entries as
  reported by The Korea Times, 29 July 2026: **Zest No. 2** (Cheongdam-dong; also
  **The Best Bar in Korea for a third consecutive year**; zero-waste, seasonal local
  ingredients), **Alice No. 13**, **Bar Cham No. 33**, **MMS No. 42**, plus four more
  in the 51–100 band — **Charles H No. 87** is confirmed by name in the William Reed
  release, and **eight Seoul bars** are in the top 100 in total.
  **Caveat for whoever writes this up:** sources disagree on one 51–100 name — one
  list gives **Gonggan at No. 74** where another gives "Space". Do not print that one
  without the official list. Tokyo also took four of the 51–100 places.
- **2026 서울미식 100선** (Seoul Metropolitan Government, press release **6 October
  2026**): seven categories — Korean 27, Western 23, Asian 15, Grill 10, Café &
  Dessert 9, Vegetarian 8, **Bar & Pub 8** (sums to 100). Selected by **60 domestic
  food experts** (food journalists, food travel writers, academic researchers, chefs,
  tourism specialists); each recommended three venues per category (21 each),
  recommendations were rank-weighted, and the city chose the final 100 on
  세계성·전문성·화제성 (global standing, expertise, buzz). **25 venues are new**, of
  which the four new Bar & Pub entries are **백곰막걸리 (Baekgom Makgeolli), 앨리스
  청담 (Alice Cheongdam), 장생건강원 (Jangsaeng Geonganwon), 참 제철 (Cham Jecheol)**.
  **The other four Bar & Pub names are not in any text source** — the city's release,
  Wikitree and the city mediahub article all name only the new four, and the full 100
  appears only as images and on the festival site. Do not guess them.
  *Unverified observation, flagged as such:* 앨리스 청담 and 참 제철 look like the
  same businesses as Alice (No. 13) and Bar Cham (No. 33) on the 50 Best list, which
  would be a strong hook — "newly official at home, long ranked abroad" — but the
  identity of 참 제철 with Bar Cham was **not** confirmed this run and must be checked
  before it is written.
- **서울미식주간 2026 runs Fri 2026-10-23 → Thu 2026-10-29** at DDP and across Seoul,
  with four programs (서울레스토랑위크, 서울미식마켓, 서울미식투어, 서울미식워크숍).
  **Per-program dates are still unpublished** as of this run — the city's own release
  says they will be released in stages (순차적으로 공개) on the festival site and
  `instagram.com/tasteofseoul_official`. The 미식마켓 theme is reported as 집밥
  (home cooking). The festival opens **tomorrow**.

### Correction to the 2026-10-20 entry: the official site is intermittent, not fixed

The 2026-10-20 entry recorded `tasteofseoul.visitseoul.net` as **reachable again**
after being down on 10-19, and told future runs to source the lists from it directly.
**That does not hold.** Both `https://tasteofseoul.visitseoul.net/` and
`https://tasteofseoul.visitseoul.net/restaurants/list` failed this run with
`connect ECONNREFUSED 115.68.17.176:443` — the same error as 10-19, from the same IP.
So the site is **intermittent across days**, not recovered, and a run that needs the
full 100선/50선 lists cannot count on it. `mediahub.seoul.go.kr` and
`seoul.go.kr/news/news_report.do` both served full text this run and are the reliable
fallback, at the cost of only ever naming the 25 new venues rather than all 100.

### Note for the next slot that can ship — Sat 2026-10-24 (Carousel, local)

Wed 2026-10-21 used the cafe slot on no-kids zones, so the 카페·디저트 50선 angle
recommended by the 10-19 and 10-20 entries is still unused. For Saturday's *local*
Carousel the stronger option is **서울미식주간 itself**, which will be mid-run on
10-24 (day 2 of 7): it is editorial, non-venue-specific and city-sourced, so it clears
§3 option 3 on licensed stock with no venue photo. By then the per-program schedules
should have been released, which is the one thing missing today. Note the honest hook
is the same one that made 10-21 work — an official list that the public cannot
actually read in full, because the site serving it keeps refusing connections.

### Verified working this run

- **WebSearch works** (4 queries, standard and extended, all returned results).
  **WebFetch works** — `mediahub.seoul.go.kr`, `seoul.go.kr/news/news_report.do`,
  `wikitree.co.kr` and `kyodonewsprwire.jp` all returned full text. Two failures were
  the remote's fault, not the tool's: `tasteofseoul.visitseoul.net` ECONNREFUSED (see
  above) and an `epicureasia.com` article URL that 404s.
- **`python3 scripts/cardnews.py` works.** Rendered
  `content/2026-10-21-korea-no-kids-zones-en.json` into a temp dir → **7 slides,
  all 1080×1350, exit 0**, pillow 13.0.0. Rendered to `/tmp` and **not committed**,
  since §3 produced no new content to render.
- `ffmpeg` is still **absent** from the runner image (installable at runtime per the
  2026-09-22 entry). Moot today: the Reel never reached §4, so `scripts/reel.py` was
  not exercised.
- The dead-token publish blocker is unchanged and **not checkable by an agent**
  (`IG_ACCESS_TOKEN` is a repository secret). It now has a **third** confirmation
  without any agent action: `2026-10-21-korea-no-kids-zones-en` was queued and
  rendered correctly yesterday and was **held** at 2026-10-22T00:00:14 KST with the
  identical fault — `hold_reason: publish_failed_manual_review`, OAuthException
  **code 190**, "session has been invalidated" (`fbtrace_id AQcvjaPt8uL-8QcaTKLYmYA`).
  **Three consecutive Carousels — 10-10, 10-17, 10-21 — have now been authored
  correctly and lost at the final step.** Re-authorizing `IG_ACCESS_TOKEN` through
  Instagram Login (CONNECT-GUIDE.md) remains the top-priority human action; until it
  happens, Saturday's Carousel will be lost the same way. Nothing was queued this
  run, so no item was exposed to it today.
- `--max-turns 60` did not bite: `.github/workflows/daily-content.yml` is unchanged,
  but a Reel-day run stops at the §3 gate and stays well inside the budget.

---

## 2026-10-20 (Tue), reel / local — SKIPPED

Twenty-seventh consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged and was
re-derived mechanically this run rather than inherited from the 2026-10-19 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Tue 2026-10-20 11:29 KST, `%u` = 2 → **reel / local /
  Collab candidate**. The task prompt independently specified `reel`; the two agree.
- §0: **no `pending` or `published` item for 2026-10-20.** `queue.json` holds the
  same 47 entries as yesterday (34 `held`, 13 `published`); a string search for
  `2026-10-20` across the file returns nothing. Nothing to stop on, so the run
  proceeded to §2.
- §3: a Reel needs option 1 (owner original) or option 2 (venue/creator media with
  written permission). Option 3 (licensed stock) is restricted to a
  non-venue-specific editorial **Carousel**, and CONTENT.md "Media and rights" says
  the same independently.
- **Neither option 1 nor option 2 exists in the repo.** Re-checked mechanically this
  run: all **48** files in `assets/photos/` are referenced by an existing
  `content/*.json`, so the unused set is **empty** (47 content files). A repo-wide
  `git ls-files` filter for `mp4|mov|m4v|mp3|wav|heic|avi|webm` returns **zero**
  files, so there is no owner video for a Reel either.
- No new media channel appeared: `git fetch --all` leaves `main` level with
  `origin/main` at 0c9d9a4, `main` is the only branch, and no `inbox/`, `incoming/`,
  `uploads/`, `media/` or `submissions/` path exists.
- No ramp flag is set in `queue.json` or any repo note (PIPELINE.md §1), so the ramp
  constrained nothing — the skip is decided on §3 grounds alone.

Stopped under §0: "If rights, venue existence, or current operation cannot be
verified, stop without adding a queue item."

### §2 research — the official 미식주간 site is reachable again

**As-of date 2026-10-20.** The 2026-10-19 entry recorded
`tasteofseoul.visitseoul.net` as **unreachable** (`ECONNREFUSED 115.68.17.176:443`)
and told future runs to source the lists from the mediahub press article instead.
**That has changed: the site now responds and serves the lists directly.** This is
the one materially new fact this run.

- **`https://tasteofseoul.visitseoul.net/cafe/list` works.** It is the official
  **서울 카페·디저트 50선** list, paginated 5 pages × 12, header count **50**. Page 1
  fetched cleanly: 고호재 (Jung-gu), 기욤 청담점, 김씨부인 (Seocho-gu), 김영모과자점
  강남구청점, 껠끄쇼즈, 누데이크 하우스 노웨어 도산, 당옥, 더 라운지 파크 하얏트 서울,
  동병상련 (Jongno-gu), 떼헤브 (Gangseo-gu), 띠띠빵빵, 라뜰리에 이은 — nine of the
  twelve in Gangnam-gu. The 100선 equivalent is
  `https://tasteofseoul.visitseoul.net/restaurants/list`.
- Selection criteria for the 50선, quoted from the city's own article: "음료와
  디저트의 완성도를 비롯해 공간에서의 경험, 대중적 인기, **외국인 관광객의 접근성** 등을
  종합적으로 고려해 선정." The selecting body is not named (the 60 expert panel is
  attributed only to the 100선). Published 2026-10-06 17:13 KST.
  Source: https://mediahub.seoul.go.kr/archives/2019580
- **서울미식주간 2026 runs 2026-10-23 → 10-29** at DDP and across Seoul, with four
  programs: 서울레스토랑위크, 서울미식마켓, 서울미식투어, 서울미식워크숍. Per-program
  dates were still unpublished as of this run; the city says they appear on the
  누리집 and `instagram.com/tasteofseoul_official`.
- **Note for Wed 2026-10-21 (Carousel, cafe) — the next slot that can ship.** The
  50선 remains the strongest available cafe topic and the recommendation from
  2026-10-19 stands, now with a working primary source and a sharper angle: the list
  was built partly on *foreign-visitor accessibility*, it is the city's first, and it
  lands **two days before** the festival opens. It is editorial and
  non-venue-specific, so it clears §3 option 3 on licensed stock and needs no venue
  photo. Whoever runs it should pull all 5 pages for a district breakdown — the
  Gangnam concentration visible on page 1 is a real, checkable hook, but page 1 alone
  is not evidence for the full 50.

### Verified working this run

- WebSearch works. WebFetch works — `mediahub.seoul.go.kr` and
  `tasteofseoul.visitseoul.net/cafe/list` both returned full text (the latter a
  change from yesterday, see above).
- `python3 scripts/cardnews.py content/2026-10-17-bukchon-visiting-hours-en.json`
  into a temp dir → **7 slides, 1080×1350, exit 0**, pillow 13.0.0. Rendered to
  `/tmp` and not committed, since §3 produced no new content to render.
- `ffmpeg` is still **absent** from the runner image (installable at runtime per the
  2026-09-22 entry). Moot today: the Reel never reached §4.
- The dead-token publish blocker is unchanged and **not checkable by an agent**
  (`IG_ACCESS_TOKEN` is a repository secret). Nothing was queued this run, so no item
  was exposed to it. It remains the top-priority human action — see the header.

---

## 2026-10-19 (Mon), reel / restaurant — SKIPPED

Twenty-sixth consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged and was
re-derived mechanically this run rather than inherited from the 2026-10-18 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Mon 2026-10-19, `%u` = 1 → **reel / restaurant /
  Collab optional**. The task prompt independently specified `reel`; the two agree.
- §0: **no `pending` or `published` item for 2026-10-19.** `queue.json` holds the
  same 47 entries as yesterday (34 `held`, 13 `published`); a string search for
  `2026-10-19` across the file returns nothing. Nothing to stop on, so the run
  proceeded to §2.
- §3: a Reel needs option 1 (owner original) or option 2 (venue/creator media with
  written permission). Option 3 (licensed stock) is restricted to a
  non-venue-specific editorial **Carousel**, and CONTENT.md "Media and rights" says
  the same independently.
- **Neither option 1 nor option 2 exists in the repo.** Checked mechanically: all
  **48** files in `assets/photos/` are referenced by an existing `content/*.json`
  (`photo` or `slides[].bg_image`), so the unused set is **empty**.
  `git log --author=Steve -- assets/photos/` returns exactly one human-supplied
  file, `cheongildip-en.jpg` (392aefd, 2026-08-25) — it predates policy v2 and is
  already consumed by `2026-08-25-cheongildip-en`. The other 46 are `claude[bot]`
  pipeline commits, all third-party stock (Unsplash / Wikimedia CC0) whose own
  sources slide states the photo is not the venue, so none can be promoted.
- No new media channel appeared: `git fetch --all` leaves `main` level with
  `origin/main` at 90597d7, `main` is the only branch, and no `inbox/`, `incoming/`,
  `uploads/`, `media/` or `submissions/` path exists. A repo-wide search for
  `*.mp4 *.mov *.m4v *.mp3 *.wav *.heic` returns **zero** files, so there is no
  owner video for a Reel either (`assets/music/*` is gitignored by design).
- No ramp flag is set in `queue.json` or any repo note (PIPELINE.md §1), so the ramp
  constrained nothing — the skip is decided on §3 grounds alone.

Stopped under §0: "If rights, venue existence, or current operation cannot be
verified, stop without adding a queue item."

### §2 research — tooling works, and the restaurant pillar has a live hook

Recorded for the next run that can actually ship. **As-of date 2026-10-19.**

- Seoul city's **2026 서울미식 100선** was published **2026-10-06** on the city's own
  mediahub (official source, fetched this run): 한식 27 / 양식 23 / 아시안 15 /
  그릴 10 / 채식 8 / 카페&디저트 9 / 바&펍 8, with **25 newly selected** venues
  (한식 10, 아시안 5, 양식 4, 그릴 1 = 몽탄, 채식 1 = 고사리 익스프레스, 바&펍 4 =
  백곰막걸리 / 앨리스 청담 / 장생건강원 / 참제철). Newly selected 한식: 리북방,
  면서울, 산초, 서령, 수퍼판, 유록, 품서울, 하모, 한식공간 소반, 해남천일관.
  Source: https://mediahub.seoul.go.kr/archives/2019580
- **서울미식주간 (Taste of Seoul) runs 2026-10-23 → 10-29** at DDP and across Seoul
  (서울레스토랑위크 / 미식마켓 / 미식투어 / 미식워크숍), same source. Note for
  whoever runs **Wed 2026-10-21 (Carousel, cafe)**: the first-ever **서울 카페·디저트
  50선** published alongside the 100선 is an *editorial, non-venue-specific* cafe
  topic that lands two days before the festival opens — it needs no venue photo and
  so clears §3 option 3. That is the strongest available use of the next Carousel
  slot.
- **Caveat on the official site:** `https://tasteofseoul.visitseoul.net/` is
  **unreachable from this runner** — `connect ECONNREFUSED 115.68.17.176:443`, not a
  404. The 50선 full list lives there per the city article, so a future run should
  expect to source it from the mediahub/press release instead.
- Venue candidate checked for the restaurant pillar: **해남천일관** (Haenam
  Cheonilgwan), a newly-selected 한식 entry. Michelin Guide Korea has an official
  listing (`guide.michelin.com/kr/ko/.../restaurant/haenam-cheonilgwan`) giving hours
  as Mon–Fri 11:30–14:30 / 17:30–21:30, Sat 10:00–14:30 / 17:30–21:00, closed
  Sunday. **Not fully §2-verified:** the Michelin page itself renders via JS and came
  back empty to WebFetch (hours above are from the search index, not the page), the
  address conflicts across aggregators (서초구 반포대로39길 36-1 vs. a 역삼동 branch
  claim), and no 천일코스 price could be confirmed. So even with media in hand this
  venue would need address and price nailed down before it could be written up.

### Verified working this run

- WebSearch works (4 queries, Korean and English). WebFetch works — mediahub.seoul.go.kr
  returned full text; `tasteofseoul.visitseoul.net` ECONNREFUSED and the Michelin
  venue page returned a blank body (JS-rendered), both noted above.
- `python3 scripts/cardnews.py content/2026-10-17-bukchon-visiting-hours-en.json`
  into a temp dir → **7 slides, 1080×1350, exit 0**, pillow 13.0.0. Rendered to
  `/tmp` and not committed, since §3 produced no new content to render.
- `ffmpeg` is still **absent** from the runner image (installable at runtime per the
  2026-09-22 entry). Moot today: the Reel never reached §4.
- The dead-token publish blocker is unchanged and **not checkable by an agent**
  (`IG_ACCESS_TOKEN` is a repository secret). Nothing was queued this run, so no item
  was exposed to it.

---

## 2026-10-18 (Sun), reel / cafe — SKIPPED

Twenty-fifth consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged and was
re-derived mechanically this run, not inherited from the 2026-10-16 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Sun 2026-10-18, `%u` = 7 → **reel / cafe / Collab
  optional**. The task prompt independently specified `reel`, so the two agree.
- §0: **no `pending` or `published` item for 2026-10-18** in `queue.json` (47
  entries: 34 `held`, 13 `published`; newest is 2026-10-17, `held`). Nothing to
  stop on, so the run proceeded to §2.
- §3: a Reel needs option 1 (owner original) or option 2 (partner media with
  written permission). Option 3 (licensed stock) is restricted to a
  non-venue-specific editorial **Carousel**. CONTENT.md "Media and rights" says the
  same independently: "Venue-specific Reels and Collabs must use original or
  written partner-authorized media. Generic stock ... is limited to an occasional
  editorial Carousel."
- **Neither option 1 nor option 2 exists in the repo.** Checked mechanically rather
  than assumed: all **48** files in `assets/photos/` are already referenced by an
  existing `content/*.json` (`photo` or `slides[].bg_image`), so the unused set is
  **empty**. `git log -- assets/photos/` attributes every one of them to a
  `claude[bot]` pipeline commit; no human-supplied asset has landed. Every existing
  photo is third-party licensed stock (Unsplash / Wikimedia CC0) whose own sources
  slide states it is not the venue, so none can be promoted to a Reel asset.
- No new media channel appeared: `git fetch --all` leaves `main` level with
  `origin/main` at a707112, there is no other branch, and no `inbox/`, `incoming/`,
  `uploads/`, `media/` or `submissions/` path exists for owner uploads.
- No ramp flag is set in `queue.json` or any repo note (PIPELINE.md §1), so the ramp
  constrains nothing this run — the skip is decided on §3 grounds alone.

Stopped under §0: "If rights, venue existence, or current operation cannot be
verified, stop without adding a queue item."

### The §2 research passed — the stop is purely at §3

Worth recording because it is the strongest cafe-pillar topic to appear in weeks and
it is **editorial, not venue-specific**, so it would need no venue photo at all on a
Carousel day:

- Seoul city announced **「2026 서울미식 100선」** on **2026-10-06**, and alongside it
  the first-ever **「서울 카페·디저트 50선」**, a separate list aimed explicitly at
  tourists who travel to Seoul for coffee and desserts.
- The 100 list breaks down as 한식 27 / 양식 23 / 아시안 15 / 그릴 10 / 채식 8 /
  카페·디저트 9 / 바·펍 8, judged by ~60 domestic food experts; **25 venues are new
  this year**.
- **서울미식주간 (Seoul Gourmet Week) runs 2026-10-23 → 10-29** at DDP and across
  Seoul, with 서울레스토랑위크, 서울미식마켓, 서울미식투어 and 서울미식워크숍.
- Useful English search phrase: "Seoul Cafe and Dessert 50" / "Seoul Gourmet Week
  2026".

Sources (as of 2026-10-18): <https://mediahub.seoul.go.kr/archives/2019580>
(Seoul city media hub, published 2026-10-06 17:13, fetched and verified this run);
corroborated by <https://www.wikitree.co.kr/articles/1164258>. Supporting trend
context from <https://en.fnnews.com/news/202602151316437950> (2026-02-17: A Twosome
Place's signature cake sold ~3.2M units, +~30% YoY; Open Survey "Cafe Trend Report
2025" found >40% of consumers weigh bakery/dessert when choosing a cafe).

The individual 50-venue list was **not** confirmed from a primary source this run,
so no specific cafe was named — and naming one would have re-triggered the §3 venue
photo requirement anyway.

### Deliberately not done

Switching the slot to an editorial Carousel would have unlocked §3 option 3 and
shipped the topic above today. **Not done, and an agent should not do it.** §1
assigns Sunday a Reel, §0 forbids catching up missed days, and PIPELINE.md contains
no format-substitution rule; reformatting the slot to dodge the media gate is the
editorial call reserved for a human in the 2026-09-15 entry. Writing a stock-photo
Reel is also technically possible — `validate_rights()` (`scripts/publish.py:78`)
would pass it, see the permissiveness note below — and is a straight §3 violation.
Not done. A typography-only cover was likewise not used: the task prompt rules it
out for this account, and it would not satisfy §3 regardless.

### Verified working this run

The whole render path, including the Reel-only MP4 step, was exercised end to end on
existing content in a temp dir (nothing committed — there is no new item to render):

- `python3 scripts/cardnews.py content/2026-10-17-bukchon-visiting-hours-en.json
  <tmp>` → **7 slides, all 1080×1350, exit 0**, no errors. Pillow 13.0.0.
- `sudo apt-get install -y ffmpeg` succeeded, then `python3 scripts/reel.py ... <tmp>`
  → **1080×1920, 22.200s MP4, exit 0** (ffmpeg 6.1.1), confirmed 9:16 via `ffprobe`.
  Only the known benign warning: `! local: tracks.json 에 등록됐지만 파일이 없습니다`
  (`assets/music/*.mp3` is gitignored, so cloud Reels use synthesized audio).
- **So there is no technical obstacle to a Reel today.** The blocker is the §3
  rights rule alone — if a compliant asset existed, this run would have shipped.
- WebSearch works (returned the 2026-10-06 Seoul list and current cafe-trend
  coverage). WebFetch works (`mediahub.seoul.go.kr` and `en.fnnews.com` both
  fetched and verified).
- `queue.json` parses; 47 entries.

### Still blocked for a human (unchanged, re-checked)

- **The Instagram access token is confirmed dead**, no longer merely presumed — see
  the header. This is now the highest-value fix: it is the only thing stopping the
  one format that can ship, and two consecutive correct Carousels have been lost to
  it. Needs re-authorization through Instagram Login and a new `IG_ACCESS_TOKEN`
  secret. It did not affect today's decision, which is a §3 call either way.
- **The §3 media gate** needs one of the three editorial fixes in the 2026-09-15
  entry (drop in original photos / allow disclaimed stock on Reels / move
  venue-specific days to Carousel). Twenty-five Reel days lost so far.
- **`--max-turns 60`** is still unraised at `.github/workflows/daily-content.yml:80`,
  but the 10-17 run cleared it, so it is not the live fault. Still worth raising.
- **`ffmpeg` is still absent from the runner image** (`which ffmpeg` → nothing until
  installed). Per the 2026-09-22 note this is a per-run setup step, not a blocker.
- **Next real chance to ship is Wed 2026-10-21, a Carousel day** (§1 day 3, cafe) —
  and the 「서울 카페·디저트 50선」 topic above is a ready-made fit for that slot and
  pillar. It will still be **held at publish** unless the token is fixed first. Not
  queued here: §0 allows at most one item per KST day and forbids working ahead.

---

## 2026-10-16 (Fri), reel / restaurant — SKIPPED

Twenty-fourth consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged and was
re-verified from scratch this run rather than inherited from the 2026-10-15 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Fri 2026-10-16, `%u` = 5 → **reel / restaurant /
  Collab candidate**.
- §0: no `pending` or `published` item for 2026-10-16 in `queue.json` (46 entries,
  newest is 2026-10-10, `held`). Nothing to stop on.
- §3: a venue-specific Reel needs option 1 (owner original) or option 2 (partner
  media with written permission). Option 3 (licensed stock) is restricted to a
  non-venue-specific editorial **Carousel**, which today is not. CONTENT.md
  "Media and rights" says the same thing independently: "Venue-specific Reels and
  Collabs must use original or written partner-authorized media."
- **Neither option 1 nor option 2 exists in the repo.** Checked mechanically, not
  assumed: all **47** files in `assets/photos/` are already referenced by an
  existing `content/*.json` (`photo` or `slides[].bg_image`) — the unused set is
  **empty**. So no owner-supplied or partner-licensed asset has arrived. Every
  existing photo is third-party licensed stock (Unsplash / Wikimedia CC0) whose
  own sources slide says it is not the venue, so none of them can be promoted to
  a Reel asset either.
- No new media channel appeared: `git fetch --all` leaves `main` level with
  `origin/main` at b9fac80, there is no other branch, and no inbox/manifest path
  exists for owner uploads.
- No ramp flag is set in `queue.json` or any repo note (PIPELINE.md §1), so the
  ramp constrains nothing this run — the skip is decided on §3 grounds alone.

Stopped under §0: "If rights, venue existence, or current operation cannot be
verified, stop without adding a queue item."

### Deliberately not done

The one thing that would have shipped today is switching the format to an editorial
Carousel to unlock §3 option 3. **Not done, and it should not be done by an agent.**
§1 assigns Friday a Reel, §0 forbids catching up missed days, and PIPELINE.md has no
format-substitution rule. Reformatting the slot to dodge the media gate is the
editorial call reserved for a human in the 2026-09-15 entry. Writing a stock-photo
Reel is also technically possible — `validate_rights()` (scripts/publish.py:78)
would pass it, see the "publish.py is more permissive than PIPELINE.md" note below —
and is a straight §3 violation. Not done.

### Verified working this run

- `python3 scripts/cardnews.py content/2026-10-10-seoul-alley-spending-en.json
  <tmp>` → **7 slides, all 1080×1350, exit 0**, no errors. Rendered to a temp dir,
  not committed, since there is no new content item to render. Pillow 12.3.0.
- WebSearch works (MICHELIN Guide Seoul & Busan 2026 Bib Gourmand additions
  returned current results). WebFetch works — the Wikimedia Commons API still
  reports `License: cc0` / `AttributionRequired: false` for the 2026-10-10 cover
  photo, so that post's recorded rights basis re-verifies.
- `queue.json` parses; 46 entries.

### Still blocked for a human (unchanged, re-checked)

- **`ffmpeg` is absent from this runner** (`which ffmpeg` → nothing), so
  `scripts/reel.py` could not have produced the 9:16 MP4 today without a runtime
  `apt-get install`. Per the 2026-09-22 note this is a per-run setup step, not a
  blocker, but `.github/workflows/daily-content.yml` still has no install step.
- **`--max-turns 60` is still unraised** at `.github/workflows/daily-content.yml:80`.
  Unchanged since the 10-15 entry; it is what lost Wed 2026-10-14.
- **The Instagram access token is still presumed invalid** (code 190, session
  invalidated — see the header). Not checkable by an agent; assume it stands. It
  did not affect today's decision, which is a §3 media call either way.
- **Next real chance to ship is Sat 2026-10-17, a Carousel day** (§1 day 6, local).
  It needs the token fixed to actually publish, and a lean enough run to clear 60
  turns. Not queued here — §0 allows at most one item per KST day and forbids
  working ahead.

---

## 2026-10-15 (Thu), reel / bar — SKIPPED

Twenty-third consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged and was
re-verified from scratch rather than inherited. **New this run: the 2026-10-14
Carousel gap is diagnosed (see the header) — it died on `--max-turns 60`, so the
one format that can ship lost a fourth day.**

`TZ=Asia/Seoul date` → Thursday 2026-10-15 11:13 KST, `+%u` → 4 → §1 row 4 → reel /
bar, Collab **optional**; the run prompt set the same format. Working tree clean at
start (`git status --porcelain --untracked-files=all` → 0 lines). `queue.json` holds
46 items — 33 `held`, 13 `published`, **zero** `pending`. No ramp flag (§1): still
only prose in CONTENT.md, PIPELINE.md and this file.

**§0 same-day check passes.** No `2026-10-15` string appears anywhere in
`queue.json`, so there is no same-day `pending` or `published` item. Nothing has
landed in the repo since the 2026-10-13 skip commit (b9037bd), whose only change was
to this file — note that this means **2026-10-14 left no trace in the repo at all**,
which is how the turn-cap failure stayed silent again.

### Blocking: no compliant media for a venue-specific Reel

PIPELINE.md §3 allows, in order: (1) original media from the account owner,
(2) venue/creator media with written permission, (3) licensed stock **only for a
non-venue-specific editorial Carousel**. Re-checked this run:

- **No owner-supplied original media exists.** A `find` across the repo for
  `*.mp4`/`*.mov`/`*.heic`/`*.dng`/`*.m4v`/`*.webm`/`*.mp3`/`*.wav`/`*.png` outside
  `.git` returns **nothing** — still not one frame of video in a repo for a Reel-led
  account. A `find` for `*inbox*`/`*incoming*`/`*upload*`/`*owner*`/`*original*`/
  `*partner*` directories also returns nothing.
- **`assets/photos/` holds 47 files; 46 are agent-added stock.** Re-audited per file
  with `git log --diff-filter=A`: 46 of 47 were added by `claude[bot]` in `content:`
  pipeline commits between 2026-08-25 and 2026-10-10, all under the pre-2026-09-14
  policy that permitted mood-matched stock.
- **The one human-added file fails on three independent grounds today.**
  `cheongildip-en.jpg` (Steve, 392aefd, 2026-08-25):
  - **(a) Wrong pillar.** It is a `local` subject and today is the `bar` slot. The
    2026-10-13 entry noted this ground lapses on `local` Tuesdays; today it applies
    again.
  - **(b) Wrong venue.** It depicts Cheongildip, already published 2026-08-25
    (media_id 17966641104247745). §3 forbids using a photo "as if it depicts the
    named place" for any other venue, so it cannot carry a Reel about a bar.
  - **(c) No rights record, and the file argues against "owner-shot."** Re-confirmed
    this run: `content/2026-08-25-cheongildip-en.json` has **no** `policy_version`,
    `asset_source`, `rights_confirmed` or `rights_note` (its only keys are `slug`,
    `pillar`, `handle`, `publish_at`, `photo`, `slides`, `caption`, `hashtags`), and
    the image is 1600×939 progressive JPEG with **zero EXIF tags** — the signature of
    a web-delivered stock image, not a camera original. §3 requires those facts to be
    *confirmed*; the evidence points the other way.
- **Option 2 is unavailable.** No partner permission record exists anywhere in the
  repo, and an unattended run cannot obtain written permission from a venue.
- **Option 3 does not reach this format.** §3 limits licensed stock to a
  non-venue-specific editorial *Carousel*; the restriction is on the **format**, and
  CONTENT.md closes it from the other side ("limited to an occasional editorial
  Carousel"). §1 fixes Thursday as a Reel.

A typography-only cover is not an escape hatch either: this is a food/venue account
and the run brief requires a real licensed photo on every post.

### Not blocking: the bar pillar has verifiable material

Checked so the media finding is not confounded with "nothing to write about."
**Asia's 50 Best Bars 2026** (announced in Macau, reported 2026-07-29) puts four
Seoul bars in the top 50 — **Zest** No. 2 in Cheongdam-dong (Korea's best bar for a
third straight year), **Alice** No. 13 in Gangnam, **Bar Cham** No. 33 in a restored
hanok in Jongno, and **M+MS** No. 42, a newcomer — with Gonggan, Charles H, Le
Chamber and Soko in the 51–100 band. Source:
`koreatimes.co.kr/.../20260729/seoul-claims-4-spots-on-asias-50-best-bars-2026-zest-retains-no-2-ranking`
(WebFetch, as of 2026-10-15).

Two caveats for whoever picks this up. First, **all four top-50 Seoul bars are
already covered** by this account (`2026-08-25-zest-seoul-en`,
`2026-09-05-alice-cheongdam-en`, `2026-08-29-bar-cham-en`, `2026-09-01-mms-bar-en`),
as are all four of the 51–100 entries, so a venue-specific bar Reel would need either
a new venue or an explicit "2026 list moved" angle. Second, the one angle that is
genuinely new — the ranking shuffle itself — is **non-venue-specific editorial**,
which is exactly the shape §3 option 3 permits for a Carousel and forbids for a Reel.
That is worth noting to a human: the available material and the available media
licence point at opposite formats.

### Verified working this run

- WebSearch works. WebFetch works on `koreatimes.co.kr`.
- `scripts/cardnews.py` renders 7 slides at 1080×1350, exit 0, re-run this session
  against `content/2026-10-10-seoul-alley-spending-en.json` into a scratch directory
  (not committed). Output dimensions checked per file, not just the exit code.
- The Reel MP4 path still needs `sudo apt-get install -y ffmpeg` at runtime; not
  exercised this run, as there was no compliant media to build from.

---

## 2026-10-13 (Tue), reel / local — SKIPPED

Twenty-second consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. **New this run: today's pillar is `local`,
which is the first time the slot pillar has matched the one human-added photo in the
repo.** Yesterday's entry rejected that file on three grounds, one of which was
"wrong pillar" — that ground lapses today, so grounds (a) and (b) were re-examined
directly rather than inherited. They hold, and new technical evidence strengthens
(a). Detail below.

`TZ=Asia/Seoul date` → Tuesday 2026-10-13 13:22 KST, `+%u` → 2 → §1 row 2 → reel /
local, **Collab candidate**; the run prompt set the same format. Working tree clean
at start (`git status --porcelain --untracked-files=all` → 0 lines). `queue.json`
holds 46 items — 33 `held`, 13 `published`, **zero** `pending`. No ramp flag (§1):
still only prose in CONTENT.md, PIPELINE.md and this file.

**§0 same-day check passes.** Zero queue items carry a `publish_at` on 2026-10-13,
and there is no `2026-10-13` string anywhere in `queue.json`. No same-day `pending`
or `published` item exists. Nothing has landed in the repo since the 2026-10-12 skip
commit (3d69f75), whose only change was to this file.

### Blocking: no compliant media for a venue-specific Reel

PIPELINE.md §3 allows, in order: (1) original media from the account owner,
(2) venue/creator media with written permission, (3) licensed stock **only for a
non-venue-specific editorial Carousel**. Re-checked from scratch:

- **No owner-supplied original media exists.** Working tree clean. A `find` across
  the repo for `*.mp4`/`*.mov`/`*.heic`/`*.dng`/`*.m4v`/`*.webm`/`*.mp3`/`*.wav`
  outside `.git` returns **nothing** — still no video footage of any kind in a repo
  for a Reel-led account. A `find` for `*inbox*`/`*incoming*`/`*upload*`/`*owner*`/
  `*original*`/`*partner*`/`*submit*` directories also returns nothing.
- **`assets/photos/` holds 47 files; 46 are agent-added stock.** Re-audited per file
  this run with `git log --diff-filter=A`: 46 of 47 were added by `claude[bot]` in
  `content:` pipeline commits between 2026-08-25 and 2026-10-10, all under the
  pre-2026-09-14 policy that permitted mood-matched stock.
- **The one human-added file still does not qualify — and the provenance gap is now
  evidenced, not just unrecorded.** `cheongildip-en.jpg` (Steve, 392aefd,
  2026-08-25). Today it clears the pillar test — it is a `local` subject and this is
  the `local` slot — so the other two grounds carry the decision alone, and each is
  independently sufficient:
  - **(a) No rights record, and the file itself argues against "owner-shot."**
    `content/2026-08-25-cheongildip-en.json` carries no `asset_source`,
    `rights_confirmed` or `rights_note` (confirmed by reading it in full this run).
    New this run, the image was inspected rather than just its metadata record:
    **1600×939, progressive JPEG, zero EXIF** — no camera make/model, no capture
    timestamp, no lens or exposure data. That is the signature of a web-delivered
    stock image, not a camera original, whose EXIF would normally survive into a
    committed file. So the honest reading is not "owner media missing its
    paperwork"; it is "probably the same category of stock as the other 46, selected
    by a human under the old policy." §3 requires those facts to be *confirmed*, and
    the evidence points the wrong way.
  - **(b) Wrong venue.** It depicts Cheongildip, published 2026-08-25
    (media_id 17966641104247745). §3 forbids using a photo "as if it depicts the
    named place" for any other venue, so it cannot carry a Reel about a different
    local spot. Re-running Cheongildip itself is not a fix either: it would be a
    duplicate of a published post, and (a) would still block it.
- **Option 2 is unavailable.** No partner permission record exists anywhere in the
  repo, and an unattended run cannot obtain written permission from a venue.
- **Option 3 does not reach this format.** §3 limits licensed stock to a
  non-venue-specific editorial *Carousel*; the restriction is on the **format**, and
  CONTENT.md closes it from the other side ("limited to an occasional editorial
  Carousel"). §1 fixes Tuesday as a Reel.

### The Collab path does not unblock Tuesday either

Tuesday is the week's first **Collab candidate** slot (§1 row 2), which the Monday
entries above never had to address. It does not create a route to shipping, for two
independent reasons:

1. **It still needs compliant media first.** §3's Collab paragraph is additive to the
   media rules, not an alternative to them — CONTENT.md is explicit that "Venue-
   specific Reels **and Collabs** must use original or written partner-authorized
   media." A Collab item with `rights_confirmed: true` cannot be written today for
   exactly the reasons above, and writing one with `rights_confirmed: false` is not
   a schema the policy permits.
2. **Even a well-formed Collab item could not be queued today.** §3 says to keep
   `collab_status: requested` and "do not queue it as pending until the partner
   accepts," and CONTENT.md notes the current Instagram Login integration "cannot
   invite collaborators automatically; this step needs a human operator." So the
   best case for a Collab Tuesday is a non-pending item awaiting a human — not a
   post. §0's instruction to stop without adding a queue item reaches the same place.

### Not blocking: the local pillar has verifiable material

Checked so the media finding is not confounded with "nothing to write about." The
**KTO "K-Local Food 33"** program is a well-sourced, genuinely English-audience local
topic that this account has not covered. Verified by WebFetch against two Korea Times
articles:

- `koreatimes.co.kr/.../20250924/kto-launches-campaign-showcasing-koreas-hidden-culinary-gems`
  (published 2025-09-24, updated 2025-09-25): the Korea Tourism Organization runs
  "K-Local Food Trip: 33 Must-Try Destinations," co-curated with the Ministry of
  Culture, Sports and Tourism, covering 33 local food destinations; launched at
  Pyongyangok, a century-old eatery in Seoul's Seodaemun District; names Andong
  (North Gyeongsang) with jjimdak and Andong soju.
- `koreatimes.co.kr/.../20260826/food-hunters-sparks-enthusiasm-for-k-food-with-10-mil-views-on-social-media`
  (published 2026-08-26): the 2026 "K-Local Food Hunters 33" run drew 33 creators
  from 13 countries (~29M combined followers) on a five-day, four-night trip through
  Gangwon, Jeolla and Gyeongsang, producing ~900 posts and 10M+ cumulative views;
  top item was hanwoo mungtigi at ~447k views. KTO plans an official 33-dish list on
  VISITKOREA in four languages.

**Caveat for whoever writes this up:** the full official 33-item list was **not**
found on an official source this run — the per-city pairings in circulation come
from commercial travel sites (e.g. seoulstart.com, last updated 2026-06-05, which
lists Chuncheon/dakgalbi, Suwon/wanggalbi, Jeonju/bibimbap, Andong/jjimdak,
Busan/dwaeji gukbap and others) and sources disagree on details. §2 requires an
official listing, so the city-dish pairings would need confirmation against
VISITKOREA before going in copy; the program-level facts above are solidly sourced.
Note also that this is a **non-venue-specific editorial** topic — i.e. exactly the
shape §3 option 3 permits on a **Carousel**. It is a strong candidate for Wed
2026-10-14 or Sat 2026-10-17, not for today.

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-10-13 Tuesday → §1 row 2 → reel / local.
- §0 same-day gate: no `pending`, no same-day `publish_at`.
- **WebSearch works** (2 queries returned results). **WebFetch works** — fetched both
  Korea Times articles above and seoulstart.com in full, with datelines.
- **`scripts/cardnews.py` renders 7 slides at 1080×1350 with no errors** (exit 0),
  run against `content/2026-10-10-seoul-alley-spending-en.json` into a scratch dir.
- **`scripts/reel.py` renders a valid 9:16 MP4** — `ffprobe` confirms 1080×1920,
  h264 + aac, 22.2s. `ffmpeg` was again **absent** from the runner image;
  `sudo apt-get install -y ffmpeg` succeeded (6.1.1) and the Reel leg then worked,
  re-confirming the 2026-09-22 finding that this is a per-run setup step, not a
  blocker. Audio is ffmpeg-synthesized because `assets/music/*.mp3` is gitignored
  (`! local: tracks.json 에 등록됐지만 파일이 없습니다`).
- One trap worth recording for future runs: the MP4 is **not** valid until `reel.py`
  exits. Probing it mid-write gives `moov atom not found`, which looks like a
  renderer failure but is just an unfinalized file — the render takes ~53s. Wait for
  exit before `ffprobe`.
- `pillow` 12.3.0, `python3` present. Render verification output was written to
  `/tmp`, **not** committed, since there is no publishable item today.

So the environment is fully healthy and the render path is proven end to end on both
formats. Nothing technical stopped this run; the §3 media rule did.

---

## 2026-10-12 (Mon), reel / restaurant — SKIPPED

Twenty-first consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. Every gate re-checked against the runner and
the repo this run rather than inherited from the entries below. One blocker survives
the re-check and it is decisive: media. **New this run: the single human-added photo
in the repo was examined directly and ruled out on three independent grounds (see
below) — the first time that file has been assessed rather than waved past as
"predates the policy."**

`TZ=Asia/Seoul date` → Monday 2026-10-12 12:06 KST, `+%u` → 1 → §1 row 1 → reel /
restaurant, Collab optional; the run prompt set the same format. Working tree clean
at start (`git status --porcelain --untracked-files=all` → 0 lines). `queue.json`
holds 46 items — 33 `held`, 13 `published`, **zero** `pending`. No ramp flag (§1):
a repo-wide search for "ramp" still returns only prose in CONTENT.md, PIPELINE.md
and this file.

**§0 same-day check passes.** Checking `publish_at` specifically rather than
grepping the file (per the 2026-10-11 entry's recommendation): zero queue items
carry a `publish_at` on 2026-10-12, and there is no `2026-10-12` string anywhere in
`queue.json`. No same-day `pending` or `published` item exists.

### Blocking: no compliant media for a venue-specific Reel

PIPELINE.md §3 allows, in order: (1) original media from the account owner,
(2) venue/creator media with written permission, (3) licensed stock **only for a
non-venue-specific editorial Carousel**. CONTENT.md agrees: "Venue-specific Reels
and Collabs must use original or written partner-authorized media." Re-checked from
scratch:

- **No owner-supplied original media exists.** Working tree clean, so nothing was
  dropped in. `assets/` still holds only `fonts/`, `music/`, `photos/`. A `find`
  across the repo for `*.mp4`/`*.mov`/`*.heic`/`*.dng`/`*.m4v`/`*.webm`/`*.mp3`/
  `*.wav` outside `.git` returns **nothing** — there is still no video footage in
  this repo at all, which for a Reel account is the whole problem. A `find` for
  `*inbox*`/`*incoming*`/`*upload*`/`*owner*`/`*original*`/`*partner*`/`*submit*`
  directories also returns nothing.
- **`assets/photos/` holds 47 files; 46 are agent-added stock.** Audited per file
  this run with `git log --diff-filter=A` rather than by sampling the recent adds:
  every one of the 46 was added by `claude[bot]` in a `content:` pipeline commit
  between 2026-08-25 and 2026-10-10, all under the pre-2026-09-14 policy that
  permitted mood-matched stock.
- **The one human-added file does not qualify.** `cheongildip-en.jpg` was committed
  by Steve (392aefd, 2026-08-25, "content: English + photo-required pivot"). It
  fails on three counts, any one of which is sufficient: (a) **no rights record** —
  its content JSON (`content/2026-08-25-cheongildip-en.json`) carries no
  `asset_source`, `rights_confirmed` or `rights_note`, so there is nothing
  establishing it as owner-shot rather than stock Steve selected under the old
  policy, and §3 requires those facts to be confirmed; (b) **wrong venue** — it
  depicts Cheongildip, already published on 2026-08-25, and §3 forbids using it "as
  if it depicts the named place" for any other venue; (c) **wrong pillar** — it is a
  local/street-food subject, not today's restaurant slot. So the provenance gap is
  real, not merely a paperwork technicality.
- **Option 2 is unavailable.** No partner permission record exists anywhere in the
  repo, and an unattended run cannot obtain written permission from a venue.
- **Option 3 does not reach this format.** §3 limits licensed stock to a
  non-venue-specific editorial *Carousel*. The restriction is on the **format**, not
  merely on venue-specificity, so "a stock-photo editorial Reel" is not a loophole —
  CONTENT.md closes it from the other side too ("limited to an occasional editorial
  Carousel"). Converting Monday to a Carousel instead is fix option 3 in the
  2026-09-15 entry: an editorial decision, explicitly reserved for a human, and §1
  fixes Monday as a Reel.

The per-run restatement of the §3/publish.py mismatch still holds: `validate_rights`
(`scripts/publish.py:78`) would accept `asset_source: licensed_stock` on a Reel,
because it checks the value against `{original, partner_licensed, licensed_stock}`
without consulting `format`. The publisher is more permissive than the policy, so
the policy is enforced only here, by the authoring run declining to write the file.

### Not blocking: the restaurant pillar has verifiable material

Checked so the media finding is not confounded with "nothing to write about." The
2026 Michelin Bib Gourmand selection gives a well-sourced restaurant pool, verified
by WebFetch against Korea JoongAng Daily (`koreajoongangdaily.com/lifestyle/
michelin-releases-2026-bib-gourmand-adds-8-new-korean-restaurants/12491521`,
published 2026-02-26): 71 restaurants total, 51 in Seoul and 20 in Busan, threshold
"a full meal under 45,000 won per person", with eight new entries. Three Seoul
additions are uncovered by this account and would suit a Monday restaurant slot:

- **3rd Samgyetang** — Seocho District; samgyetang with a multi-ingredient broth
  topped with mung bean and pine nut purées and mugwort paste; founded 1973.
- **Andeok** — Jongno District; beef naengguksu and mandutguk.
- **Oilje** — Yongsan District; perilla seed miyeok-guk, rice cooked in a cast-iron
  pot in an open kitchen.

(The fourth new Seoul entry, **Gosari Express**, is already covered —
`2026-09-07-gosari-express-en`.) A separate long-running candidate, **Mijin**
(Jongno), surfaced as a cold-buckwheat-noodle specialist whose Michelin listing gives
Jongno-gu Jongno 19, Le Meilleur Jongno Town, and describes it as serving the
Gwanghwamun area since 1952 with its own noodle and broth factory in the basement —
but its **hours could not be confirmed from an official listing** and the unit number
differs between sources, so it would not clear §2 as written without further work.
The three Bib Gourmand entries above have no such gap at the pillar level.

That caveat is secondary: §2 is fixable by more research within a run, §3 is not
fixable by an agent at all. Had media been available, this run would have had a
publishable Monday restaurant topic.

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-10-12 Monday → §1 row 1 → reel / restaurant.
- §0 same-day gate: no `pending`, no same-day `publish_at`.
- **WebSearch works** (3 queries returned results). **WebFetch works** — fetched the
  Korea JoongAng Daily article above in full with its dateline and figures, and
  `en.wikipedia.org` returned content. Two URLs failed for their own reasons, not
  the tool's: `guide.michelin.com` returns an **empty body** (client-rendered, so
  Michelin listings are unusable via WebFetch — worth knowing, since it is the
  natural §2 source for award facts), and `asianews.network` returns **HTTP 403**.
- **`scripts/cardnews.py` renders 7 slides at 1080×1350 with no errors** (exit 0),
  run against `content/2026-10-10-seoul-alley-spending-en.json` into a scratch dir.
- **`scripts/reel.py` renders a valid 9:16 MP4** — `ffprobe` confirms 1080×1920,
  22.2s. `ffmpeg` was **absent** from this runner image; `sudo apt-get install -y
  ffmpeg` succeeded (6.1.1) and the Reel leg then worked, re-confirming the
  2026-09-22 finding that this is a per-run setup step and not a blocker. Audio is
  ffmpeg-synthesized because `assets/music/*.mp3` is gitignored (`! local:
  tracks.json 에 등록됐지만 파일이 없습니다`).
- `pillow` 12.3.0, `python3` present. Render verification output was written to
  `/tmp`, **not** committed, since there is no publishable item today.

So the environment is fully healthy and the render path is proven end to end on both
legs. The blocker is editorial input, not tooling.

### Unchanged, still needing a human

- **The Instagram token is still dead** (see the header). Not checkable from here;
  the next Carousel day, Wed 2026-10-14, will be held unless it is reset first.
- **`--max-turns` is still 60.** `.github/workflows/daily-content.yml:80` re-checked
  this run and unchanged; `timeout-minutes: 30` at line 37. An agent cannot push it
  (no `workflows: write`).
- The prompt's `DRY RUN 여부:` line was **blank** again, consistent with the
  `schedule` trigger as diagnosed in the 2026-10-11 entry, so this was read as a
  real (non-dry) run and this entry is committed.

---

## 2026-10-11 (Sun), reel / cafe — SKIPPED

Twentieth consecutive Reel-day skip. No content JSON, no rendered output committed,
no change to `queue.json`. Every gate re-checked against the runner and the repo
this run rather than inherited from the entries below. One blocker survives the
re-check and it is decisive: media. **New this run: the publish-side token is dead
(see the header) and the cafe pillar's candidate pool is healthy** — so, as on
2026-10-09 for restaurants, the media gate rather than topic exhaustion is what
stops Sunday.

`TZ=Asia/Seoul date` → Sunday 2026-10-11 11:42 KST, `+%u` → 7 → §1 row 7 → reel /
cafe, Collab optional; the run prompt set the same format. Working tree clean at
start (`git status --porcelain --untracked-files=all` → 0 lines). `queue.json` holds
46 items — 33 `held`, 13 `published`, **zero** `pending`. No ramp flag (§1): a
repo-wide search of `*.json`/`*.yml`/`*.yaml` for "ramp" still returns nothing, so
the only hits remain prose in CONTENT.md, PIPELINE.md and this file.

**§0 same-day check passes.** No queue item carries a `publish_at` on 2026-10-11.
`grep -c 2026-10-11 queue.json` returns 1, but that single hit is the **`held_at`**
of the 2026-10-10 item (held just after midnight), not a same-day post — exactly
the scheduled-vs-actual ambiguity the 2026-10-08 entry asked a human to fix in §0's
wording. Checking `publish_at` specifically rather than grepping the file resolves
it; the gate is clean either way, but the wording is still worth tightening.

### Blocking: no compliant media for a venue-specific Reel

PIPELINE.md §3 allows, in order: (1) original media from the account owner,
(2) venue/creator media with written permission, (3) licensed stock **only for a
non-venue-specific editorial Carousel**. CONTENT.md agrees: "Venue-specific Reels
and Collabs must use original or written partner-authorized media." Re-checked
from scratch:

- **No owner-supplied original media exists.** `git status --porcelain
  --untracked-files=all` returns 0 lines, so nothing has been dropped in. `assets/`
  still holds only `fonts/`, `music/`, `photos/`. A `find` across the repo for
  `*.mp4`/`*.mov`/`*.heic`/`*.dng`/`*.m4v`/`*.avi`/`*.webm`/`*.mp3`/`*.wav` outside
  `.git` returns **nothing** — there is no video footage in this repo at all, which
  for a Reel account is the whole problem. A `find` for
  `*inbox*`/`*incoming*`/`*upload*`/`*owner*`/`*submit*`/`*original*`/`*partner*`
  directories also returns nothing.
- **`assets/photos/` holds 47 files, all agent-added stock.** `git log` on that
  path shows the five most recent adds (adda1cb 10-10, 59fa888 10-07, 0d38369
  09-26, ffe577d 09-23, b1863f5 09-19) are every one of them `claude[bot]` Carousel
  stock. Nothing owner-supplied has ever been added, on any day.
- **Option 2 is unavailable.** No partner permission record exists anywhere in the
  repo, and an unattended run cannot obtain written permission from a venue.
- **Option 3 does not reach this format.** §3 limits licensed stock to a
  non-venue-specific editorial *Carousel*. The restriction is on the **format**,
  not merely on venue-specificity, so "a stock-photo editorial Reel" is not a
  loophole — CONTENT.md closes it from the other side too ("limited to an
  occasional editorial Carousel"). Converting Sunday to a Carousel instead is fix
  option 3 in the 2026-09-15 entry: an editorial decision, explicitly reserved for
  a human, and §1 fixes Sunday as a Reel.

The per-run restatement of the §3/publish.py mismatch still holds: `validate_rights`
(`scripts/publish.py:78`) would accept `asset_source: licensed_stock` on a Reel,
because it checks the value against `{original, partner_licensed, licensed_stock}`
without consulting `format`. The publisher is more permissive than the policy, so
the policy is enforced only here, by the authoring run declining to write the file.

### Not blocking: the cafe pillar has verifiable material

Checked so the media finding is not confounded with "nothing to write about." There
is a current, well-sourced cafe/dessert angle: the 2026 tteok dessert boom.
Verified by WebFetch against The Korea Herald (`mbiz.heraldcorp.com/article/10846414`,
dated 2026-08-20) — national tteok sales 929.1bn won in 2024, up 65% from 564.1bn
in 2018; E-mart frozen tteok +171.2% YoY for Aug 1-18; Shinsegae Sweet Park +31.1%
YoY Jul 1-Aug 17; Lotte main branch dessert +60% Aug 1-18; named brands Changuk
Tteok (pop-up at The Hyundai Seoul, Yeouido, from Aug 14; flagship in Gwangju),
Hanjeong-seon, Gyeonggi Tteokjip, Gyeonghoeru, Golden Piece, 1994 Seoul. Jaha
(Jongno, Gyeonghuigung 2-gil 7) surfaced as a tteok-cafe candidate, though its
address came from a review aggregator and **its hours could not be confirmed from
an official listing**, so it would not clear §2 as written without further work.

That caveat is secondary: §2 is fixable by more research within a run, §3 is not
fixable by an agent at all. Had media been available, this run would have had a
publishable Sunday cafe topic.

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-10-11 Sunday → §1 row 7 → reel / cafe.
- §0 same-day gate: no `pending`, no same-day `publish_at`.
- **WebSearch works** (3 queries returned results). **WebFetch works** on
  `mbiz.heraldcorp.com` — returned the full article with dateline and statistics.
- **`scripts/cardnews.py` renders 7 slides at 1080×1350 with no errors**, run
  against `content/2026-10-10-seoul-alley-spending-en.json` into a scratch dir.
- **`scripts/reel.py` renders a valid 1080×1920 (9:16) 22.2s MP4**; `ffmpeg` was
  already present on this runner image at `/usr/bin/ffmpeg` (6.1.1), so no install
  was needed this run. As documented, audio is ffmpeg-synthesized because
  `assets/music/*.mp3` is gitignored (`! local: tracks.json 에 등록됐지만 파일이
  없습니다`).
- Render verification output was written to `/tmp`, **not** committed, since there
  is no publishable item today.

So the environment is fully healthy and the render path is proven end to end on
both legs. The blocker is editorial input, not tooling.

### Note on the dry-run flag

The prompt's `DRY RUN 여부:` line was **blank**, not `true`/`false`. That is the
`schedule` trigger: `daily-content.yml` interpolates `${{ inputs.dry_run }}`, which
is the empty string on a cron run, whereas `workflow_dispatch` would render the
literal `false` from its default. Read as a real (non-dry) run, which is why this
entry is committed. Worth making explicit in the workflow (`${{ inputs.dry_run ||
'false' }}`) so a future run does not have to infer it.

---

## 2026-10-09 (Fri), reel / restaurant — SKIPPED

Nineteenth consecutive Reel-day skip. No content JSON, no rendered output committed,
no change to `queue.json`. Every gate re-checked against the runner and the repo
this run rather than inherited. One blocker survives the re-check — media — and it
alone is decisive. **New this run: the restaurant pillar's candidate pool is
healthy, which is the opposite of what 2026-10-08 found for bars** — so the media
gate, not topic exhaustion, is what is stopping Friday.

`TZ=Asia/Seoul date` → Friday 2026-10-09 12:30 KST, `+%u` → 5 → §1 row 5 → reel /
restaurant, Collab **candidate**; the run prompt set the same format. Working tree
clean at start (`git status --porcelain --untracked-files=all` → 0 lines).
`queue.json` holds 45 items — 32 `held`, 13 `published`, **zero** `pending`. No ramp
flag (§1): a repo-wide search of `*.json`/`*.yml`/`*.yaml` for "ramp" still returns
nothing, so the only hits remain prose in CONTENT.md, PIPELINE.md and this file.

**§0 same-day check passes cleanly.** No queue item carries a `publish_at` on
2026-10-09, and `grep -c 2026-10-09 queue.json` returns 0 — so unlike 2026-10-08,
the scheduled-vs-actual ambiguity that entry flagged did not even arise this run.
That ambiguity is still unresolved in §0's wording and still worth a human fix.

### Blocking: no compliant media for a venue-specific Reel

PIPELINE.md §3 allows, in order: (1) original media from the account owner,
(2) venue/creator media with written permission, (3) licensed stock **only for a
non-venue-specific editorial Carousel**. CONTENT.md agrees: "Venue-specific Reels
and Collabs must use original or written partner-authorized media." Re-checked:

- **no owner-supplied original media exists.** `git status --porcelain
  --untracked-files=all` returns 0 lines, so nothing has been dropped in; `assets/`
  still holds only `fonts/`, `music/` and `photos/`; a `find` for
  `*inbox*`/`*incoming*`/`*upload*`/`*owner*`/`*submitted*`/`*original*` directories
  and for any `.mp4`/`.mov`/`.heic`/`.dng`/`.m4v`/`.avi`/`.webm` outside `.git`
  returns nothing. `assets/photos/` still holds **46** files, unchanged since
  2026-10-07; the three newest adds (59fa888 10-07, 0d38369 09-26, ffe577d 09-23)
  are all `claude[bot]` Carousel stock. **Nothing owner-supplied has ever been
  added, and nothing at all for 13 days;**
- **written venue permission cannot be obtained by an unattended run;**
- **licensed stock is available and legal, but §3 forbids it for this format.** The
  constraint binds on format, not only on venue-specificity, so an editorial
  Korean-fine-dining angle does not escape it either. Friday is a Reel, so option 3
  is closed.

Friday is additionally a **Collab candidate** day, which tightens the same gate
rather than loosening it: §3 requires a Collab to use original or partner-authorized
media and to stay `collab_status: requested` until a partner accepts, and an
unattended run can neither obtain the media nor solicit the acceptance.

Reusing an existing `assets/photos/` file would violate the rule twice — stock on a
Reel, and stock standing in for a named venue. Deliberately did **not** write
`asset_source: "licensed_stock"` + `rights_confirmed: true` for a Reel: that still
passes `validate_rights()` (scripts/publish.py has no format check; gap first logged
2026-09-15, **still open**) while violating §3. A typography-only cover with no
photo was also rejected — the run prompt independently ruled it out for this
food/venue account, matching §3/§4. The CC/KOGL public-licence reading of §3 option
2, raised and rejected on 2026-09-24 and 2026-09-25, is not reopened: loosening a
rights rule on a live account is outward-facing and not a call for an unattended
run. Switching Friday to a Carousel to dodge the gate is the same kind of editorial
decision and was likewise not taken.

### New: the restaurant pillar still has a well-documented candidate pool

The 2026-10-08 entry recorded that the **bar** pillar had exhausted its best-
documented candidates (all eight Seoul entries on Asia's 50 Best Bars 2026 already
covered). Checked the equivalent for restaurants this run, and the picture is the
reverse. Asia's 50 Best Restaurants 2026 (announced Hong Kong, 2026-03-25) put six
Seoul restaurants in the top 50: Mingles (4), Onjium (14), Eatanic Garden (26), Mosu
(41), Bium (43), 7th Door (49); San, a Gangnam restaurant opened 2024, took "One to
Watch", and Onjium's Cho Eun-hee took Asia's Best Female Chef 2026. Of those, only
**Mingles and Onjium** are already covered in `content/`. **Eatanic Garden, Mosu,
Bium, 7th Door and San are all unused** — five verified, currently-operating,
English-searchable restaurant subjects sitting ready.

So Friday is not short of subjects; it is short of one photo per subject. If a human
drops original or partner-licensed media into `assets/photos/` for any one of those
five, a Friday Reel can be authored immediately with no other change to the repo.

### Verified working this run

- `scripts/cardnews.py` rendered **7/7** slides at 1080×1350 from existing content,
  exit 0, and slide 1 was **opened and visually inspected** — English copy, no
  overflow, no collision, correct branding. (Per the 2026-09-16 lesson: `cardnews.py`
  clips silently and exits 0, so renders must be looked at, not exit-code checked.)
- `scripts/reel.py` produced a valid **1080×1920, 22.2s** MP4 (ffprobe-confirmed),
  exit 0, using synthesized audio — `assets/music/restaurant.mp3` is registered in
  `tracks.json` but gitignored and absent, as documented.
- **ffmpeg is still absent from the runner image** and was installed at runtime again
  (`sudo apt-get install -y ffmpeg` → 6.1.1-3ubuntu5, exit 0). Per-run setup step,
  not a blocker; adding it to `daily-content.yml` would still save the install.
- **WebSearch works. WebFetch works** (korea.stripes.com returned usable content).
  Two routing notes for future runs: `theasian50best.com` does **not** resolve
  (ENOTFOUND), and `theworlds50best.com/asia/...` now 301-redirects to `the50.com`,
  which then returns **404** — use a news source or the rebuilt site's own
  navigation rather than the old deep links.
- `.github/workflows/daily-content.yml:80` still reads `--max-turns 60`, and line
  25-27 still grants only `contents: write` / `id-token: write` — **no `workflows:
  write`**, so an agent still cannot raise it or add the ffmpeg step. Unchanged.

---

## 2026-10-08 (Thu), reel / bar — SKIPPED

Eighteenth consecutive Reel-day skip. Every gate re-checked against the runner and
the repo this run rather than inherited from the entries below. No content JSON, no
rendered output committed, no change to `queue.json`. One blocker survives the
re-check — media — and it alone is decisive. Both render paths were exercised end to
end this run and both work. **Two new things this run: the bar pillar has exhausted
its best-documented candidate pool (all eight Seoul entries on Asia's 50 Best Bars
2026 are already covered), and the 2026-10-07 Carousel shipped despite `--max-turns
60` never being raised — see the header.**

`TZ=Asia/Seoul date` → Thursday 2026-10-08 12:25 KST, `+%u` → 4 → §1 row 4 → reel /
bar, Collab **optional**; the run prompt set the same format. Working tree clean at
start (`git status --porcelain --untracked-files=all` → 0 lines). `queue.json` now
45 items — 32 `held`, 13 `published`, **zero** `pending`. No ramp flag (§1): a
repo-wide search of `*.json`/`*.yml`/`*.yaml` for "ramp" still returns nothing, so
the only hits remain prose in CONTENT.md, PIPELINE.md and this file.

**§0 same-day check, with a wrinkle worth recording.** No queue item whose
`publish_at` falls on 2026-10-08, so the gate passes. But `grep -c 2026-10-08
queue.json` returns 1, because `2026-10-07-seoul-cafe-churn-en` carries
`published_at: 2026-10-08T02:22:59+09:00` — the publisher posted it **after
midnight KST**, seven hours past its 18:30 slot. Read literally, §0's "if a
same-day `pending` or `published` queue item exists, stop" would consume today on
an item scheduled for yesterday. This run reads §0 as keyed on the **scheduled**
day (`slug`/`publish_at`), consistent with every entry below. It made no
difference today — the media gate stops this run anyway — but on a Wednesday or
Saturday it would decide whether a shippable Carousel gets written, so a human
should either tighten §0's wording or find out why the 19:00 KST publisher is
running past midnight.

### Blocking: no compliant media for a venue-specific Reel

PIPELINE.md §3 allows, in order: (1) original media from the account owner,
(2) venue/creator media with written permission, (3) licensed stock **only for a
non-venue-specific editorial Carousel**. CONTENT.md agrees: "Venue-specific Reels
and Collabs must use original or written partner-authorized media." Re-checked this
run:

- **no owner-supplied original media exists.** `git status --porcelain
  --untracked-files=all` returns 0 lines, so no file has been dropped in; `assets/`
  still holds only `fonts/`, `music/` and `photos/`; a `find` for
  `*inbox*`/`*incoming*`/`*upload*`/`*owner*`/`*submitted*` directories and for any
  `.mp4`/`.mov`/`.heic`/`.dng`/`.m4v`/`.avi` outside `.git` returns nothing.
  Provenance re-derived this run with `git log --diff-filter=A` over all **46** files
  in `assets/photos/`: every file has an add-commit (`comm` against the add-list
  returns empty), spread over 45 commits — 44 by `claude[bot]`, and the sole
  human-added one (`cheongildip-en.jpg`, 392aefd, Steve, 2026-08-25) predates the
  policy rewrite and is itself stock, with **no** `policy_version`, `asset_source`,
  `rights_confirmed` or `rights_note` field in its JSON, so it carries no documented
  rights basis and cannot stand in as owner-original media. The newest two adds are
  59fa888 (10-07) and 0d38369 (09-26), both bot-fetched Carousel stock. **No
  owner-supplied file has ever been added, and nothing at all for 12 days;**
- **written venue permission cannot be obtained by an unattended run;**
- **licensed stock is available and legal, but §3 forbids it for this format.** The
  constraint binds on format, not only on venue-specificity, so an editorial
  drinking-culture angle does not escape it either. Thursday is a Reel, so option 3
  is closed.

Reusing an existing file from `assets/photos/` would violate the same rule twice:
stock on a Reel, and stock standing in for a named venue. Deliberately did **not**
write `asset_source: "licensed_stock"` + `rights_confirmed: true` for a Reel — that
still passes `validate_rights()` (scripts/publish.py has no format check; gap first
logged 2026-09-15, still open) while violating §3. The CC/KOGL public-licence reading
of §3 option 2, raised and rejected on 2026-09-24 and 2026-09-25, is not reopened:
loosening a rights rule on a live account is outward-facing and not a call for an
unattended run. Switching Thursday to a Carousel to escape the gate is the same kind
of call — it is fix 3 for a human, not taken here.

### New: the bar pillar has run out of verifiable candidates

Done to prove §2 works; **not** written up as copy, because the media gate stops the
post before copy matters. This is a weaker research block than the entries below,
and the reason is itself the finding.

**Every Seoul bar on Asia's 50 Best Bars 2026 is already covered.** The list is
where this account has sourced its bar pillar, and it is now exhausted. Four in the
top 50 — **Zest** No. 2 (also Best Bar in Korea for the third straight year),
**Alice** No. 13, **Bar Cham** No. 33, **M+MS** No. 42 (debut) — and four on the
extended 51–100 list — **Gong-Gan** No. 74, **Charles H** No. 87, **Le Chambre**
No. 88, **Soko** No. 89. All eight have a `content/` file and a queue entry. Note
the account's Gong-Gan post already cites "No. 74 on Asia's 50 Best Bars 2026," and
the one source conflict here is on that slot: Herald Biz names Gong-Gan at 74 while
Korea Stripes names "Space." Unresolved from search snippets; the official 51–100
list would settle it, and a human should check it before that post is ever reused.
**No Busan bar appears anywhere on the 2026 list** — the bar pillar is Seoul-only by
construction, unlike the restaurant and local pillars, which the Bib Gourmand cycle
spreads across both cities.

**Three uncovered candidates were tried and all three failed §2, not §3.** Worth
recording because it means the bar pillar would stall on verification even if the
media gate were lifted tomorrow:

- **Dormer (도머), Haeundae-gu, Busan** — attic cocktail bar working with Korean
  ingredients, picked up by Fodor's Busan nightlife guide; Instagram `@dormer_haeundae`.
  **Rejected: address conflicts and no hours.** One result gives 11-2 Gunam-ro,
  Haeundae-gu; another places it in U-dong; a third address on Gunam-ro (17-1)
  belongs to a different bar, TBR. No Naver Place or DiningCode profile surfaced, so
  current operation is unverified. §2 requires address and current operation.
- **Don't Tell Mama (돈텔마마), Seoul** — the Le Chamber team's 2026 opening, signature
  Snow Cabin (basil-infused vodka, yogurt wash, Pinot Noir), 9PM–5AM. Good hook, and
  Le Chamber itself is already covered (2026-09-10), which makes the sequel angle
  natural. **Rejected: no address anywhere.** `diningcode.com/list.dc?query=돈텔마마`
  returns "2곳" in the page title and nothing else — the listing is client-side
  rendered, same site shape as `guide.michelin.com`.
- **Bar Namsan (바 남산), Seoul** — Kim Min-hong, World Class Korea 2023 winner;
  Wed–Mon 7PM–2AM; signature Sunbeam Doodles. **Rejected: the name collides with
  Namsan the mountain**, so search returns tourist pages and a Banyan Tree hotel bar
  that may or may not be the same venue. No address, no confirmation of the
  bartender's record.

Two further leads a human with Naver Map access could close quickly, both from the
same GQ Korea piece: **Tricycle (트라이싸이클)**, Yeonnam-dong, 6PM–2AM, by Kim Seo-yun
and Byun Sang-hyun; and **Hand in Hand (핸드인핸드)**, a Nonhyeon-dong alley, 7PM–3AM
(2AM Sundays), by Park Tae-woo, Campari Red Hands Korea 2024 winner. Also unverified
here: Esquire Korea ran a May-2026 feature on five Seoul *yajang* serving makgeolli,
yakju and soju-based cocktails from Euljiro to Oksu-dong — a traditional-liquor angle
the bar pillar has only touched once (Ahn Makgeolli, 2026-08-27) — but the article's
venue names did not surface in snippets.

- **Sources read this run:** The Korea Times, "Seoul claims 4 spots on Asia's 50 Best
  Bars 2026, Zest retains No. 2 ranking," 2026-07-29; Herald Biz article 10827855 (the
  Seoul Metropolitan Government list graphic); GQ Korea, "챔피언 바텐더들이 오픈한, 나만
  알고 싶은 서울 신상 바 4," 2026-06-05 (`gqkorea.co.kr/?p=381245`) — **fetched in
  full**, source of all four new-bar details above; GQ Korea's Macau ceremony report,
  2026-08-31; Fodor's "16 Best Bars in Busan"; DiningCode (`list.dc?query=돈텔마마`).

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-10-08 Thursday, `+%u` → 4 → reel / bar (§1); §0 gates
  pass (see the wrinkle above).
- **WebSearch works.** Five queries run, English and Korean, two in `extended` mode.
  The English queries carried the ranking; the Korean ones surfaced the new-bar leads.
- **WebFetch works.** `gqkorea.co.kr` returned the full article. `diningcode.com`
  returned a **title-only** body for `list.dc` (a search-results page) — note this is
  narrower than the 2026-10-06 result, where a DiningCode `profile.php` page fetched
  in full. Profile pages are server-rendered and work; list/search pages are not.
  Same client-side-rendering shape as `guide.michelin.com`, which has failed on
  2026-09-25, 10-02, 10-05 and 10-06. Not a tool failure.
- `scripts/cardnews.py` renders **7 slides at 1080×1350, exit 0**, from
  `content/2026-09-12-gong-gan-en.json` (bar pillar, matching today's slot). Slide 01
  was opened and **visually inspected** per the 2026-09-16 note about `fit()`
  overflowing silently: the three headline lines and the two-line subline sit inside
  the box, no collision with the `DEEP_DIVE_KOREA` wordmark or the seven pagination
  dots, no run-off at the canvas edge.
- `scripts/reel.py` renders a **1080×1920 (9:16) MP4, 22.200s, h264 + aac, exit 0**
  in 48s, confirmed with `ffprobe`, after `sudo apt-get install -y ffmpeg` (exit 0,
  ffmpeg 6.1.1-3ubuntu5). It warns `! bar: tracks.json 에 등록됐지만 파일이 없습니다`
  and synthesizes audio, because `assets/music/*.mp3` is gitignored. Unchanged from
  2026-09-22.
- Nothing was published and `publish.yml` was not invoked (§0).

### Still open for a human

1. **Raise `--max-turns` in `daily-content.yml` — still unapplied, now demoted from
   first to second place.** `.github/workflows/daily-content.yml:79-80` still reads
   `claude_args: |` / `--max-turns 60`. The 2026-10-07 Carousel shipped under that
   budget (see the header), so this is a flake, not a wall — but 09-30 and 10-03
   wrote nothing because of it, and it still costs a Carousel every few weeks. One
   line. An agent cannot push it (no `workflows: write`).
2. **The media blocker is the top item and has not moved in 24 days.** Three fixes,
   unchanged since 2026-09-15: drop original photos into `assets/photos/`; restore a
   stock allowance for Reels in §3; or move venue-specific days to Carousel and keep
   Reels for editorial topics. Five of seven days are Reels, so this is ~71% of the
   schedule.
3. **New: the bar pillar needs a candidate source.** Asia's 50 Best Bars 2026 is
   exhausted for Seoul and lists no Busan bar. Even with media solved, Thursday and
   the bar pillar will stall on §2 until someone with Naver Map access confirms a
   next venue — Tricycle and Hand in Hand above are the two closest to ready.
4. Unchanged from 2026-09-15: `publish.py`'s `validate_rights()` accepts
   `licensed_stock` regardless of format, so it does not enforce §3's Carousel-only
   restriction; and no ramp flag exists anywhere despite §1 saying to respect one.
   With publishing live again, CONTENT.md's recovery ramp is the binding limit —
   2026-09-26, 2026-10-07 are the only two posts in 38 days, so the ramp is not
   currently binding in practice, but nothing encodes it.
5. While here: `daily-content.yml` could also carry the `sudo apt-get install -y
   ffmpeg` step, saving the per-run install. Same `workflows: write` blocker.

---

## 2026-10-06 (Tue), reel / local — SKIPPED

Seventeenth consecutive Reel-day skip. Every gate re-checked against the runner and
the repo this run rather than inherited from the entries below. No content JSON, no
rendered output committed, no change to `queue.json`. One blocker survives the
re-check — media — and it alone is decisive. Both render paths were exercised end to
end this run and both work, and §2 research was verified against a listing platform
and a local daily. **New this run: the Feb-2026 Bib Gourmand announcement-date
discrepancy flagged on 2026-10-05 is resolved — see "Research a human can pick up".**

`TZ=Asia/Seoul date` → Tuesday 2026-10-06 12:42 KST, `+%u` → 2 → §1 row 2 → reel /
local, Collab **candidate**; the run prompt set the same format. No same-day
`pending` or `published` queue item (§0): `grep -c 2026-10-06 queue.json` → 0, and no
item whose `publish_at` starts with that date. Working tree clean at start
(`git status --porcelain --untracked-files=all` empty). `queue.json` unchanged at 44
items — 32 `held`, 12 `published`, **zero** `pending`. No ramp flag (§1): a repo-wide
search of `*.json`/`*.yml`/`*.yaml` for "ramp" still returns nothing, so the only
hits remain prose in CONTENT.md, PIPELINE.md and this file.

### Blocking: no compliant media for a venue-specific Reel

PIPELINE.md §3 allows, in order: (1) original media from the account owner,
(2) venue/creator media with written permission, (3) licensed stock **only for a
non-venue-specific editorial Carousel**. CONTENT.md agrees: "Venue-specific Reels
and Collabs must use original or written partner-authorized media." Re-checked this
run:

- **no owner-supplied original media exists.** `git status --porcelain
  --untracked-files=all` returns 0 lines, so no file has been dropped in; `assets/`
  still holds only `fonts/`, `music/` and `photos/`; a `find` for
  `*inbox*`/`*incoming*`/`*upload*`/`*original*`/`*owner*`/`*submitted*` directories
  and for any `.mp4`/`.mov`/`.heic`/`.dng`/`.m4v`/`.avi` outside `.git` returns
  nothing. Provenance re-derived this run with `git log --diff-filter=A` over all 45
  files in `assets/photos/`: 44 came from `claude[bot]` pipeline commits, and the
  sole human-added one (`cheongildip-en.jpg`, 392aefd, Steve, 2026-08-25) predates
  the policy rewrite — its JSON has **no** `policy_version`, `asset_source`,
  `rights_confirmed` or `rights_note` field at all, so it carries no documented
  rights basis and cannot stand in as owner-original media. `git log --since=
  2026-09-20 -- assets/` returns two commits, both bot-fetched Carousel stock (0d38369
  09-26, ffe577d 09-23). **Nothing has been added for 10 days;**
- **written venue permission cannot be obtained by an unattended run;**
- **licensed stock is available and legal, but §3 forbids it for this format.** The
  constraint binds on format, not only on venue-specificity, so an editorial local-food
  angle does not escape it either. Tuesday is a Reel, so option 3 is closed.

Reusing an existing file from `assets/photos/` would violate the same rule twice:
stock on a Reel, and stock standing in for a named venue. Deliberately did **not**
write `asset_source: "licensed_stock"` + `rights_confirmed: true` for a Reel — that
still passes `validate_rights()` (scripts/publish.py has no format check; gap first
logged 2026-09-15, still open) while violating §3. The CC/KOGL public-licence reading
of §3 option 2, raised and rejected on 2026-09-24 and 2026-09-25, is not reopened:
loosening a rights rule on a live account is outward-facing and not a call for an
unattended run. Switching Tuesday to a Carousel to escape the gate is the same kind
of call — it is listed below as fix 3 for a human, not taken here.

### Research a human can pick up

Done to prove §2 works; **not** written up as copy, because the media gate stops the
post before copy matters. Tuesday is local food, and 9 local-pillar items are already
queued or published (Cheongildip, Yonggeumok, Naeho Naengmyeon, Gugil Ttarogukbap,
Geuyetnal Chodang, Samdae Gwangyang, Imun Seolnongtang, Hankook Jib, Dongnae Halmae
Pajeon) plus two local-pillar editorial Carousels (Chuseok guide, market price rules).

**Moemiljip (뫼밀집), Marine City, U-dong, Haeundae-gu, Busan — uncovered, and the
strongest local-food hook left in the 2026 Bib Gourmand cycle.** `grep -ril
moemil content/` returns nothing; nothing in `content/` mentions makguksu or memil,
and the only buckwheat item is Naeho Naengmyeon (2026-08-29), a different dish and
a different province.

- **Hook:** a noodle house that mills **100% Korean buckwheat in-house** and serves
  it three ways, named a **new Bib Gourmand in the MICHELIN Guide Seoul & Busan
  2026** — one of three Busan rookies out of 20 Busan Bib Gourmands (71 total, 51
  Seoul). The angle writes itself against the usual Busan noodle story: this is memil,
  not milmyeon.
- **Dish detail:** MICHELIN's cited line is that the simple preparations — deulgireum
  (perilla-oil) memil and mul (cold-broth) memil — are what show the grain; the bibim
  version leads with chilli instead. House-made mandu and pyeonyuk (sliced boiled
  beef) are the side order.
- **Prices (DiningCode, checked 2026-10-06):** perilla-oil buckwheat noodles ₩17,000;
  water buckwheat ₩16,000; bibim buckwheat ₩16,000; red-bean buckwheat ₩16,000;
  handmade mandu 4pc ₩11,000; pyeonyuk ₩17,000 (taster ₩9,000). Consistent with the
  Bib Gourmand threshold of a full meal under ₩45,000 per person.
- **Address:** 23 Marine City 3-ro, Haeundae-gu, Busan 48118 — Byeoksan E Orange Plaza,
  **2nd floor**. Old-style form: U-dong 1435, Haeundae-gu. Phone 0507-1458-9948.
  Two hours' free parking in the building. The 2F detail matters for a traveler and
  should survive into copy.
- **Hours — two sources agree, still confirm on Naver Place before publishing.**
  Tue–Fri 11:30–20:30, Sat–Sun 11:00–20:30, break 15:30–17:00, last orders 15:00 and
  20:00, **closed Mondays**. DiningCode and the Michelin-derived search listing agree
  on the weekday figures; only DiningCode gives the weekend 11:00 open.
- **English search phrase for travelers:** "Moemiljip Haeundae buckwheat noodles" /
  "Busan memil guksu Michelin Bib Gourmand".
- **Sources read this run:** The Korea Herald, "Meet Bib Gourmand rookies in Michelin
  Guide Seoul & Busan 2026" (koreaherald.com/article/10684029) — **fetched in full**,
  gives all eight rookies and the ₩45,000 threshold. Busan Ilbo, 2026-02-26
  (mobile.busan.com, code 2026022609444186161) — **fetched in full**, gives the 20
  Busan Bib Gourmands, the three rookies, and places Moemiljip in Haeundae-gu's U-dong.
  DiningCode profile `xTJKwtUlMnwU` — **fetched in full**, gives address, phone, hours,
  full menu prices and no closure notice, i.e. current operation.
- **Discrepancy from the 2026-10-05 entry — RESOLVED.** That entry could not reconcile
  Korea JoongAng Daily dating the Bib Gourmand announcement 2026-02-26 against The
  Korea Herald's 2026-02-27. The Korean press settles it: Busan Ilbo and Kookje Shinmun
  both carry the story under **2026-02-26** datelines (article codes `20260226...`),
  so **2026-02-26 is the announcement date** and 2026-02-27 is the Herald's own
  publication date. Safe for copy.
- **Other uncovered Busan rookies, if Moemiljip does not suit:** **Songheonjip**
  (charcoal tteokgalbi with doenjang-jjigae in a renovated house) and **Pyongyangjip**
  (handmade mandu and nokdujeon in clear beef broth). Seoul rookies researched on
  earlier runs: Oilje (2026-10-05), Andeok, Sobakeeri Suzu, 3rd Samgyetang (2026-09-25).
  Note **Gosari Express is already published** — it is a 2026 rookie and the repo
  covered it on 2026-09-07.

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-10-06 Tuesday, `+%u` → 2 → reel / local (§1); §0 gates
  all pass.
- **WebSearch works.** Four queries run, in English and Korean; the Korean-language
  queries are what resolved the address, hours and announcement date.
- **WebFetch works.** `koreaherald.com`, `mobile.busan.com` and `diningcode.com` all
  returned full articles/listings. `guide.michelin.com` again returned an **empty
  body** (the Bib Gourmand ceremony article this time) — unchanged from 2026-09-25,
  2026-10-02 and 2026-10-05, and still a site-shape problem (client-side rendering),
  not a tool failure. MICHELIN's own pages remain reachable from this runner only via
  search snippets.
- `scripts/cardnews.py` renders **7 slides at 1080×1350, exit 0**, from
  `content/2026-09-12-dongnae-halmae-pajeon-en.json` (local pillar, matching today's
  slot). Slide 01 was opened and **visually inspected** per the 2026-09-16 note about
  `fit()` overflowing silently: the three headline lines and the two-line subline sit
  inside the box, no collision with the `@deep_dive_korea` handle or the seven
  pagination dots, no run-off at the canvas edge.
- `scripts/reel.py` renders a **1080×1920 (9:16) MP4, 22.200s, h264 + aac, exit 0**,
  confirmed with `ffprobe`, after `sudo apt-get install -y ffmpeg` (exit 0, ffmpeg
  6.1.1-3ubuntu5). It warns `! local: tracks.json 에 등록됐지만 파일이 없습니다` and
  synthesizes audio, because `assets/music/*.mp3` is gitignored. Unchanged from
  2026-09-22.
- Nothing was published and `publish.yml` was not invoked (§0).

### Still open for a human

1. **Raise `--max-turns` in `daily-content.yml` — still the top item, still unapplied.**
   Re-checked this run: `.github/workflows/daily-content.yml:79-80` still reads
   `claude_args: |` / `--max-turns 60`, and `timeout-minutes: 30` at line 37 is still
   the real backstop. See the header for the diagnosis: this is the sole cause of the
   09-30 and 10-03 silent Carousel gaps and of the red check on the otherwise-successful
   09-26 run. One line, and it unblocks the only format that can currently ship. An
   agent cannot push it (no `workflows: write`). **The next Carousel day is Wednesday
   2026-10-07 — tomorrow — and it will fail the same way unless this lands today.**
2. The media blocker's three fixes are editorial and unchanged: drop original photos
   into `assets/photos/`; restore a stock allowance for Reels in §3; or move
   venue-specific days to Carousel and keep Reels for editorial topics.
3. Unchanged from 2026-09-15: `publish.py`'s `validate_rights()` accepts
   `licensed_stock` regardless of format, so it does not enforce §3's Carousel-only
   restriction; and no ramp flag exists anywhere despite §1 saying to respect one.
   With publishing live again, CONTENT.md's recovery ramp is the binding limit and
   nothing encodes it.
4. While here: `daily-content.yml` could also carry the `sudo apt-get install -y
   ffmpeg` step, saving the per-run install. Same `workflows: write` blocker.

---

## 2026-10-05 (Mon), reel / restaurant — SKIPPED

Sixteenth consecutive Reel-day skip. Every gate re-checked against the runner and
the repo this run rather than inherited from the entries below. No content JSON, no
rendered output committed, no change to `queue.json`. One blocker survives the
re-check — media — and it alone is decisive. Both render paths were exercised end to
end this run and both work. **The one new thing this run: the silent Carousel
failures are diagnosed — see the header. They are `--max-turns 60` exhaustion, not
runs that failed to fire.**

`TZ=Asia/Seoul date` → Monday 2026-10-05 11:51 KST, `+%u` → 1 → §1 row 1 → reel /
restaurant, Collab **optional**; the run prompt set the same format. No same-day
`pending` or `published` queue item (§0): `grep -c 2026-10-05 queue.json` → 0, and
no item whose `publish_at` starts with that date. Working tree clean at start
(`git status --porcelain --untracked-files=all` empty). `queue.json` unchanged at 44
items — 32 `held`, 12 `published`, **zero** `pending`. No ramp flag (§1): a repo-wide
search of `*.json`/`*.yml`/`*.yaml` for "ramp" still returns nothing, so the only
hits remain prose in CONTENT.md, PIPELINE.md and this file.

### Blocking: no compliant media for a venue-specific Reel

PIPELINE.md §3 allows, in order: (1) original media from the account owner,
(2) venue/creator media with written permission, (3) licensed stock **only for a
non-venue-specific editorial Carousel**. CONTENT.md agrees: "Venue-specific Reels
and Collabs must use original or written partner-authorized media." Re-checked this
run:

- **no owner-supplied original media exists.** `git status --porcelain
  --untracked-files=all` returns nothing, so no file has been dropped in; `assets/`
  still holds only `fonts/`, `music/` and `photos/`; a `find` for
  `*inbox*`/`*incoming*`/`*upload*`/`*original*`/`*owner*` directories and for any
  `.mp4`/`.mov`/`.heic`/`.dng`/`.m4v` outside `.git` returns nothing. Provenance
  re-derived this run with `git log --diff-filter=A` over all 46 files in
  `assets/photos/`: 45 came from `claude[bot]` pipeline commits, and the sole
  human-added one (`cheongildip-en.jpg`, 392aefd, Steve, 2026-08-25) predates the
  policy rewrite and is itself stock. The three newest adds are 0d38369 (09-26),
  ffe577d (09-23) and b1863f5 (09-19) — all bot-fetched Carousel stock. **Nothing
  has been added for 9 days;**
- **written venue permission cannot be obtained by an unattended run;**
- **licensed stock is available and legal, but §3 forbids it for this format.** The
  constraint binds on format, not only on venue-specificity, so an editorial
  restaurant angle does not escape it either. Monday is a Reel, so option 3 is
  closed.

Reusing an existing file from `assets/photos/` would violate the same rule twice:
stock on a Reel, and stock standing in for a named venue. Deliberately did **not**
write `asset_source: "licensed_stock"` + `rights_confirmed: true` for a Reel — that
still passes `validate_rights()` (scripts/publish.py has no format check; gap first
logged 2026-09-15, still open) while violating §3. The CC/KOGL public-licence
reading of §3 option 2, raised and rejected on 2026-09-24 and 2026-09-25, is not
reopened: loosening a rights rule on a live account is outward-facing and not a call
for an unattended run.

### Research a human can pick up

Done to prove §2 works; **not** written up as copy, because the media gate stops the
post before copy matters. Monday is restaurant, and 11 restaurant-pillar items are
already queued or published (Onjium ×2, Mingles, Le Dorer ×2, Balwoo Gongyang,
Gogung Jeonju, Giwakang, Yong Fu Jeju, Gosari Express, Sosuheon).

**Oilje (오일제), Samgakji, Yongsan-gu — uncovered, and the best remaining hook from
the 2026 Bib Gourmand cycle.** `grep -ril oilje content/` returns nothing.

- **Hook:** a one-dish shop that cooks perilla-seed *miyeok-guk* (seaweed soup) and
  little else, named a **new Bib Gourmand in the MICHELIN Guide Seoul & Busan
  2026**. One of eight rookies — five Seoul, three Busan — out of 71 Bib Gourmands
  total (51 Seoul, 20 Busan).
- **Dish detail (search-level):** first-harvest seaweed from Geogeum Island, Korean
  beef broth, perilla seed powder from Gangjin; rice cooked in a cast-iron pot in an
  open kitchen; reportedly ~50 bowls a day.
- **Price frame:** Bib Gourmand in Korea means a full meal under ₩45,000 per person.
  Treat as the Bib threshold, **not** as this shop's menu price — the actual price
  was not verified this run.
- **Address (aggregator-level):** 29 Hangang-daero 62da-gil, Yongsan-gu, Seoul
  04382. A second aggregator gives 180-1 Hangangno 1-ga, Yongsan-gu — these are the
  new-style and old-style forms of the same lot, but **confirm on Naver Place before
  either reaches copy.**
- **Hours — NOT verified, do not publish as-is.** The only figures found (Mon–Fri
  10:00–13:30, closed Sat/Sun) come from aggregators, which is below §2's bar.
- **English search phrase for travelers:** "Oilje Samgakji miyeokguk" / "perilla
  seaweed soup Seoul Michelin Bib Gourmand".
- **Sources read this run:** Korea JoongAng Daily, "Michelin releases 2026 Bib
  Gourmand, adds 8 new Korean restaurants" (koreajoongangdaily.com/.../12491521) —
  **fetched in full**, confirms all eight rookies, the districts, the signature
  dishes and the 71/51/20 counts. The official MICHELIN listing for Oilje exists and
  is indexed (`guide.michelin.com/us/en/seoul-capital-area/kr-seoul/restaurant/oilje`)
  but **could not be fetched** — see below — so current operation rests on the
  JoongAng article plus search snippets of that listing, not on the listing itself.
- **One discrepancy worth resolving:** Korea JoongAng Daily dates the Bib Gourmand
  announcement **2026-02-26**; The Korea Herald, read on the 2026-09-25 run, dates it
  **2026-02-27**. Pin this before it reaches copy.

Other uncovered rookies, if Oilje does not suit: **Andeok** (Jongno-gu, beef
naengguksu and mandutguk), **Sobakeeri Suzu** (Korean-buckwheat soba), **3rd
Samgyetang** (Seocho-gu, 1973 — researched in full on the 2026-09-25 entry).

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-10-05 Monday, `+%u` → 1 → reel / restaurant (§1); §0
  gates all pass.
- **WebSearch works.** Queried the 2026 Bib Gourmand announcement and Oilje.
- **WebFetch works.** `koreajoongangdaily.com` returned the full article.
  `guide.michelin.com` again returned an **empty body** on both URLs tried (the Bib
  Gourmand article and the Oilje restaurant listing) — unchanged from 2026-09-25 and
  2026-10-02, and still a site-shape problem (client-side rendering), not a tool
  failure. MICHELIN's own pages remain reachable from this runner only via search
  snippets.
- `scripts/cardnews.py` renders **7 slides at 1080×1350, exit 0**, from
  `content/2026-09-09-sosuheon-en.json`. Slide 01 was opened and **visually
  inspected** per the 2026-09-16 note about `fit()` overflowing silently: headline
  and all four body paragraphs sit inside the box, no collision with the
  `@deep_dive_korea` handle or the pagination dot, no run-off at the canvas edge.
- `scripts/reel.py` renders a **1080×1920 (9:16) MP4, 22.200s, h264, exit 0**,
  confirmed with `ffprobe`, after `sudo apt-get install -y ffmpeg` (exit 0, ffmpeg
  6.1.1-3ubuntu5). It warns `! restaurant: tracks.json 에 등록됐지만 파일이 없습니다`
  and synthesizes audio, because `assets/music/*.mp3` is gitignored. Unchanged from
  2026-09-22.
- Nothing was published and `publish.yml` was not invoked (§0).

### Still open for a human

1. **Raise `--max-turns` in `daily-content.yml` — this is now the top item.** See
   the header: it is the sole cause of the 09-30 and 10-03 silent gaps and of the
   red check on the otherwise-successful 09-26 run. One line, and it unblocks the
   only format that can currently ship. An agent cannot push it (no `workflows:
   write`).
2. The media blocker's three fixes are editorial and unchanged: drop original photos
   into `assets/photos/`; restore a stock allowance for Reels in §3; or move
   venue-specific days to Carousel and keep Reels for editorial topics.
3. Unchanged from 2026-09-15: `publish.py`'s `validate_rights()` accepts
   `licensed_stock` regardless of format, so it does not enforce §3's Carousel-only
   restriction; and no ramp flag exists anywhere despite §1 saying to respect one.
   With publishing live again, CONTENT.md's recovery ramp is the binding limit and
   nothing encodes it.
4. While here: `daily-content.yml` could also carry the `sudo apt-get install -y
   ffmpeg` step, saving the per-run install. Same `workflows: write` blocker.

---

## 2026-10-04 (Sun), reel / cafe — SKIPPED

Fifteenth consecutive Reel-day skip. Every gate re-checked against the runner and
the repo this run rather than inherited from the entries below. No content JSON, no
rendered output committed, no change to `queue.json`. One blocker survives the
re-check — media — and it alone is decisive. Both render paths were exercised end to
end this run and both work, and §2 research was verified against an official listing.

`TZ=Asia/Seoul date` → Sunday 2026-10-04 12:15 KST, `+%u` → 7 → §1 row 7 → reel /
cafe, Collab **optional**; the run prompt set the same format. No same-day `pending`
or `published` queue item (§0): zero occurrences of `2026-10-04` in `queue.json` and
no item whose `publish_at` starts with that date. Working tree clean at start
(`git status --porcelain --untracked-files=all` empty). `queue.json` unchanged at 44
items — 32 `held`, 12 `published`, **zero** `pending`. No ramp flag (§1): a repo-wide
search of `*.json`/`*.yml`/`*.yaml` for "ramp" still returns nothing, so the only
hits remain prose in CONTENT.md, PIPELINE.md and this file.

### Blocking: no compliant media for a venue-specific Reel

PIPELINE.md §3 allows, in order: (1) original media from the account owner,
(2) venue/creator media with written permission, (3) licensed stock **only for a
non-venue-specific editorial Carousel**. CONTENT.md agrees: "Venue-specific Reels
and Collabs must use original or written partner-authorized media." Re-checked this
run:

- **no owner-supplied original media exists.** Nothing is untracked anywhere in the
  checkout, so no file has been dropped in; `assets/` still holds only `fonts/`,
  `music/` and `photos/`; a `find` for `*inbox*`/`*incoming*`/`*upload*`/`*original*`
  directories and for any `.mp4`/`.mov`/`.heic`/`.dng` outside `.git` returns
  nothing. Provenance was re-derived this run with `git log --diff-filter=A` over all
  46 files in `assets/photos/`: 45 were introduced by `claude[bot]` pipeline commits,
  and the sole human-added one (`cheongildip-en.jpg`, 392aefd, Steve, 2026-08-25)
  predates the policy rewrite and is itself stock. `git log --since=2026-09-14 --
  assets/` returns exactly four commits, all of them the Carousel stock photos of
  09-16, 09-19, 09-23 and 09-26. **Nothing has been added for 8 days;**
- **written venue permission cannot be obtained by an unattended run;**
- **licensed stock is available and legal, but §3 forbids it for this format.** The
  constraint binds on format, not only on venue-specificity, so an editorial cafe
  angle does not escape it either. Sunday is a Reel, so option 3 is closed.

Reusing an existing file from `assets/photos/` — including the eleven cafe photos
already in the repo — would violate the same rule twice: stock on a Reel, and stock
standing in for a named venue.

### Research a human can pick up

Done to prove §2 works; **not** written up, because the media gate stops the post
before copy matters. Sunday is cafe/dessert, and 13 cafe items are already queued or
published: Anthracite (Seoul and Hapjeong), Hanyakbang, Terarosa (Seoul and
Gangneung), Momos, Onion Anguk, Hakrim Dabang, Suyeonsanbang, Sungsimdang, Mido
Dabang, plus the two editorial Carousels (cup rules, cafe seat time). Two uncovered
leads, in descending order of how well they verify:

**1. Fritz Coffee Company, Dohwa — best verified, and the strongest handoff here.**
Unlike the Michelin problem logged on 2026-10-02, this one verifies against a
genuinely official source. The company's **own store directory** (`fritz.co.kr/store.html?cate_no=125`)
fetches cleanly and lists seven operating branches as of 2026-10-04 KST: 1st Dohwa
(17 Saechang-ro 2-gil, Mapo-gu, Seoul), 2nd Wonseo (83 Yulgok-ro, Jongno-gu), 3rd
Yangjae (24-11 Gangnam-daero 37-gil, Seocho-gu), 4th HYBE Fritz (42 Hangang-daero,
Yongsan-gu), 5th Seongsan (222 Ilchul-ro, Seongsan-eup, Seogwipo-si, Jeju), 6th
Dongnimmun (1F, 24-1 Tongil-ro 12-gil, Jongno-gu), 7th Jangchung (11 Dongho-ro
24-gil, Jung-gu). The site shows no closure notice and lists a staffed line,
02-3275-2047 (Mon–Fri 09:00–17:00). **Caveat for whoever writes it up:** the official
directory gives addresses but **no opening hours**. The widely-repeated Dohwa hours
(Mon–Fri 08:00–22:00, Sat–Sun 10:00–22:00) come only from aggregators — Tripadvisor,
trip.com, brewatlas — which is below §2's bar. Confirm hours on Naver Place or by
phone before any hour reaches copy. The Dohwa branch occupying a hanok is likewise
an aggregator claim, not an official one.

**2. Wi Seung Chan and nuruk — a good story, but stale.** korea.net (articleId
255035, fetches cleanly) reports that Wi Seung Chan won the **World Coffee in Good
Spirits Championship** in Copenhagen, 27–29 June 2024, using **nuruk**, the
traditional Korean fermentation starter for makgeolli and cheongju — distinct from
Japanese koji in that the grain germinates and ferments at once. He has worked at
Ediya Coffee Lab in Seoul since 2017. It is a genuinely good Sunday hook, but it is
a 2024 result, so it needs a current peg before it runs. Two candidates: Korea's
2026 showing at World of Coffee Brussels (Ethan Junseong Park, 5th in the World
Brewers Cup — Korea took no podium) and **Café Show Seoul, 11–14 November 2026**,
which hosts the 2026 Korean Barista Championship and the Korean Brewers Cup. Both of
those are editorial rather than venue-specific, so they suit a **Carousel** — which
is the format that can actually ship.

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-10-04 Sunday, `+%u` → 7 → reel / cafe (§1); §0 gates
  all pass.
- **WebSearch works.** Queried Korea's 2026 specialty-coffee scene, the 2026 World
  Coffee Championships results and Fritz's Dohwa branch.
- **WebFetch works, including on an official source.** `korea.net` and both
  `fritz.co.kr` pages (landing and store directory) returned full content. Noted for
  contrast with 2026-10-02, where all three `guide.michelin.com` URLs returned empty
  because the site is client-side rendered — that remains a site-shape problem, not a
  tool failure.
- `scripts/cardnews.py` renders **7 slides at 1080×1350, exit 0**, from
  `content/2026-09-11-mido-dabang-en.json`. Slide 04 was opened and **visually
  inspected** per the 2026-09-16 note about `fit()` overflowing silently: all four
  body paragraphs sit inside the box, no collision with the `@deep_dive_korea` handle
  or the pagination dots, no run-off at the canvas edge.
- `scripts/reel.py` renders a **1080×1920 (9:16) MP4, 22.200s, h264 video + aac
  audio, exit 0**, after `sudo apt-get install -y ffmpeg` (exit 0, ffmpeg
  6.1.1-3ubuntu5). It warns `! cafe: tracks.json 에 등록됐지만 파일이 없습니다` and
  synthesizes audio, because `assets/music/*.mp3` is gitignored. Unchanged from
  2026-09-22.

### Still open for a human

1. **The silent Carousel gaps are now the priority** — see the header. 2026-09-30
   (Wed) and 2026-10-03 (Sat) both produced nothing, the last publish was
   2026-09-26, and Carousel is the only format that can currently ship. The three
   fixes in item 2 do not matter much if the two days that *can* run keep failing
   silently.
2. The media blocker's three fixes are editorial and unchanged: drop original photos
   into `assets/photos/`; restore a stock allowance for Reels in §3; or move
   venue-specific days to Carousel and keep Reels for editorial topics.
3. Unchanged from 2026-09-15: `publish.py`'s `validate_rights()` accepts
   `licensed_stock` regardless of format, so it does not enforce §3's
   Carousel-only restriction; and no ramp flag exists anywhere despite §1 saying to
   respect one.

---

## 2026-10-02 (Fri), reel / restaurant — SKIPPED

Fourteenth consecutive Reel-day skip. Every gate re-checked against the runner and
the repo this run rather than inherited from the entries below. No content JSON, no
rendered output committed, no change to `queue.json`. One blocker survives the
re-check — media — and it alone is decisive. Both the Carousel and the Reel render
paths were exercised end to end this run and both work.

`TZ=Asia/Seoul date` → Friday 2026-10-02 11:59 KST, `+%u` → 5 → §1 row 5 → reel /
restaurant, Collab **candidate**; the run prompt set the same format. No same-day
`pending` or `published` queue item (§0): zero occurrences of `2026-10-02` in
`queue.json` and no item whose `publish_at` starts with that date. Working tree
clean at start. `queue.json` unchanged at 44 items — 32 `held`, 12 `published`,
**zero** `pending`. No ramp flag (§1): a repo-wide search of `*.json`/`*.yml`/
`*.yaml` for "ramp" still returns nothing, so the only hits remain prose in
CONTENT.md, PIPELINE.md and this file.

### Blocking: no compliant media for a venue-specific Reel

PIPELINE.md §3 allows, in order: (1) original media from the account owner,
(2) venue/creator media with written permission, (3) licensed stock **only for a
non-venue-specific editorial Carousel**. CONTENT.md agrees: "Venue-specific Reels
and Collabs must use original or written partner-authorized media." Re-checked this
run:

- **no owner-supplied original media exists.** `git status --porcelain
  --untracked-files=all` returns nothing at all, so no file has been dropped into
  the checkout; `assets/` still holds only `fonts/`, `music/` and `photos/`, and a
  `find` for `*inbox*`/`*incoming*`/`*upload*` directories and for any `.mp4`/
  `.mov`/`.heic` outside `.git` returns nothing. Provenance was re-derived this run
  with `git log --diff-filter=A` over all 46 files in `assets/photos/`: 45 were
  introduced by `claude[bot]` pipeline commits, and the sole human-added one
  (`cheongildip-en.jpg`, 392aefd, Steve, 2026-08-25) predates the policy rewrite
  and is itself stock. Since 8128750 (2026-09-14 10:12 KST) the only additions to
  `assets/` are the four Carousel stock photos of 09-16, 09-19, 09-23 and 09-26;
- **written venue permission cannot be obtained by an unattended run;**
- **licensed stock is available and legal, but §3 forbids it for this format.**
  The constraint binds on format, not only on venue-specificity, so an editorial
  restaurant angle (e.g. what a Korean tasting-menu `hanjeongsik` course actually
  consists of, rather than one dining room) does not escape it either. Friday is a
  Reel, so option 3 is closed.

Reusing an existing file from `assets/photos/` — including the eleven restaurant
photos from the pre-policy era — would violate the same rule twice: stock on a
Reel, and stock standing in for a named venue.

One reading was considered and rejected this run, for the record: a CC BY / CC0
photo carries a *written* licence from its creator, which could be argued to
satisfy §3 option 2 ("venue/creator media with written permission"). It does not.
`asset_source` is constrained to `original | partner_licensed | licensed_stock`,
and a Wikimedia photographer is not a partner who authorised this account —
CONTENT.md says "written **partner-authorized** media". The four published
Carousels all classify exactly this kind of media as `licensed_stock`. Loosening a
rights rule is an editorial decision and is not one an unattended run should make.

### Research a human can pick up

Done to prove §2 works; **not** written up, because the media gate stops the post
before copy matters. Unlike Thursday's bar slot (see 2026-10-01, where the ranked
-list well is dry), Friday's restaurant slot has fresh, uncovered supply: the
MICHELIN Guide Seoul & Busan **2026** edition — the 10th-anniversary edition, 233
restaurants, 46 starred, 10 newly awarded Stars — added several Seoul one-stars.
Named by search as new one-stars: **Bicena, Exquisine, Gigas, GiwaKang, JUEUN**,
plus Goryori Ken and SAN. Of those, **GiwaKang is already covered**
(`2026-09-04-giwakang-en.json`), and the eleven restaurant posts to date cover
Onjium (×2), Mingles, Le Doré (×2), Balwoo Gongyang, Gogung Jeonju, Yong Fu Jeju,
Gosari Express and Sosuheon. The rest are uncovered.

Best-verified candidate: **JUEUN (주은 / Restaurant Jueun)**, one star in the 2026
guide, Korean/classic cuisine, chef Park Ju-eun, **8F Gyeonghuidang, 36
Gyeonghuigung-gil, Jongno-gu, Seoul 03175**, behind Gyeonghuigung Palace. Listed as
starred in the current guide as of 2026-10-02 KST. Note it is Jongno-gu, not
Gangnam — an early search framing had that wrong.

**A sourcing caution for whoever writes this up.** `guide.michelin.com` is
client-side rendered: WebFetch against both the "All the Stars" and the
"highlights" articles, and against the individual JUEUN listing, returned an
*empty* document every time — not an error, just nothing. Michelin facts here came
from WebSearch snippets, which is weaker than §2's "official listing". Worse, the
obvious-looking aggregator `seoultourism.org/seoul-michelin-restaurants/` **fetches
fine but is not trustworthy**: it lists "Le Chamber" as a two-star *Modern
French-Korean restaurant*, when Le Chamber is a Cheongdam cocktail bar this account
has already covered as a bar (Asia's 50 Best Bars No. 88). Anything from that page
needs independent confirmation before it reaches copy. A human with a browser
should confirm star level, address and current operation directly on Michelin or
the restaurant's own booking channel.

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-10-02 Friday → reel / restaurant (§1); §0 gates all
  pass.
- **WebSearch works.** Queried the MICHELIN Guide Seoul & Busan 2026 star list and
  JUEUN's listing.
- **WebFetch works, but not everywhere.** `seoultourism.org` returned full content;
  all three `guide.michelin.com` URLs returned empty (JS-rendered). Not a tool
  failure — a site-shape problem worth knowing before relying on Michelin pages.
- `scripts/cardnews.py` renders **7 slides at 1080×1350, exit 0**, from
  `content/2026-09-13-le-dorer-en.json`. Slide 04 was opened and **visually
  inspected** per the 2026-09-16 note about `fit()` overflowing silently: body copy
  sits inside its box, no collision with the handle or the pagination dots, no
  run-off at the canvas edge.
- `scripts/reel.py` renders a **1080×1920 (9:16) MP4, 22.200s, video + audio
  streams, exit 0**, after `sudo apt-get install -y ffmpeg` (exit 0, ffmpeg
  6.1.1-3ubuntu5). It warns `! restaurant: tracks.json 에 등록됐지만 파일이 없습니다`
  and synthesizes audio, because `assets/music/*.mp3` is gitignored. Unchanged from
  2026-09-22.

### Still open for a human

Unchanged from 2026-10-01 and repeated only because nothing has moved: the media
blocker's three possible fixes are editorial (drop original photos into
`assets/photos/`; restore a stock allowance for Reels in §3; or move venue-specific
days to Carousel). The **2026-09-30 (Wed, carousel) silent gap** noted in the
header is still unexplained and still the more urgent of the two — Carousel is the
one format that can ship, and no run has fired on a Carousel day since.

---

## 2026-10-01 (Thu), reel / bar — SKIPPED

Thirteenth consecutive Reel-day skip. Every gate re-checked against the runner and
the repo this run rather than inherited from the entries below. No content JSON, no
rendered output committed, no change to `queue.json`. One blocker survives the
re-check — media — and it alone is decisive. The full Carousel **and** Reel render
paths were exercised end to end this run and both work.

`TZ=Asia/Seoul date` → Thursday 2026-10-01 11:56 KST, `+%u` → 4 → §1 row 4 → reel /
bar, Collab optional; the run prompt set the same format. No same-day `pending` or
`published` queue item (§0): zero occurrences of `2026-10-01` in `queue.json` and no
item whose `publish_at` starts with that date. Working tree clean at start.
`queue.json` unchanged at 44 items — 32 `held`, 12 `published`, **zero** `pending`.
No ramp flag (§1): a repo-wide search of `*.json`/`*.yml` for "ramp" still returns
nothing, so the only hits remain prose in CONTENT.md, PIPELINE.md and this file.

### Blocking: no compliant media for a venue-specific Reel

PIPELINE.md §3 allows, in order: (1) original media from the account owner,
(2) venue/creator media with written permission, (3) licensed stock **only for a
non-venue-specific editorial Carousel**. CONTENT.md agrees: "Venue-specific Reels
and Collabs must use original or written partner-authorized media." Re-checked this
run:

- **no owner-supplied original media exists.** `git status --untracked-files=all`
  reports nothing untracked anywhere in the repo, and `assets/` still holds only
  `fonts/`, `music/` and `photos/` — there is no inbox directory. Every file in
  `assets/photos/` was introduced by a `content: … (daily pipeline…)` commit; the
  sole human-added one, `cheongildip-en.jpg` (392aefd, 2026-08-25), predates the
  policy rewrite and is itself stock. Nothing has been added since 8128750;
- **written venue permission cannot be obtained by an unattended run;**
- **licensed stock is available and legal, but §3 forbids it for this format.**
  The constraint binds on format, not only on venue-specificity, so an editorial
  bar angle (e.g. nogari-and-beer alleys as a drinking custom rather than one bar)
  does not escape it either. Thursday is a Reel, so option 3 is closed.

Reusing an existing file from `assets/photos/` — including the bar photos from the
pre-policy era — would violate the same rule twice: stock on a Reel, and stock
standing in for a named venue.

### Correction to the 2026-09-15 entry: policy-v2 metadata is no longer unimplemented

That entry states "**zero** of the 40 files in `content/` carry `policy_version`,
`asset_source`, `rights_confirmed` or `rights_note`." That is now out of date. Of
44 files, **4** carry all four fields — the Carousels of 09-16, 09-19, 09-23 and
09-26. All four are `format: carousel`, `asset_source: licensed_stock`,
`rights_confirmed: true`, with a `rights_note` that names the file, the licence
(CC0 or CC BY 2.0), the Wikimedia Commons API verification date, and an explicit
"used under PIPELINE.md section 3 option 3 — licensed stock on a non-venue-specific
editorial Carousel" clause. The 40 pre-policy files still carry none of it.

So the v2 path is implemented and proven in production — but only along the one
branch a Carousel can take. No file in the repo demonstrates a compliant Reel,
because none can be produced here.

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-10-01 Thursday → reel / bar (§1); §0 gates all pass.
- **WebSearch works.** Queried Asia's 50 Best Bars 2026 for the Seoul entries.
- **WebFetch works.** Fetched the VisitKorea English listing for Euljiro Nogari
  Alley (`english.visitkorea.or.kr`, vcontsId 176867) and got back official name,
  address and transit detail.
- `scripts/cardnews.py` renders 7 slides at 1080×1350, exit 0, from
  `content/2026-09-12-gong-gan-en.json`. Slide 04 was opened and **visually
  inspected** per the 2026-09-16 note about `fit()` overflowing silently — text
  sits inside its box, no collision with the CTA, handle present.
- `scripts/reel.py` renders a 1080×1920 (9:16) MP4, 22.2s, video + audio streams,
  exit 0, after `sudo apt-get install -y ffmpeg` (exit 0, ffmpeg 6.1.1). It warns
  `! bar: tracks.json 에 등록됐지만 파일이 없습니다` and synthesizes audio, because
  `assets/music/*.mp3` is gitignored. Unchanged from 2026-09-22.

### Research that a human can pick up

Done to prove §2 works; **not** written up, because the media gate stops the post
before copy matters. Thursday's bar slot has an exhaustion problem worth knowing
about: all eight Seoul bars on Asia's 50 Best Bars 2026 are already covered by this
account — Zest (No. 2), Alice (13), Bar Cham (33), M+MS (42) in the top 50, and
Gong Gan (74), Charles H (87), Le Chamber (88), Soko (89) on the 51–100 extended
list. The obvious ranked-list well is dry; future bar days need either a different
source or an editorial angle.

One verified, uncovered candidate: **Euljiro Nogari Alley (을지로 노가리골목)**,
Eulji-ro 129, Jung-gu, Seoul; Euljiro 3-ga Station (Line 3) Exit 3; a nogari
(dried young pollack) and golbaengi beer alley, hours "varies by store", listed as
operating by VisitKorea as of 2026-10-01 KST. It suits a Thursday bar slot and, as
a public street rather than one business, it is unusually friendly to a compliant
photo. A caution for whoever writes it: an alley is not a venue, so if it is ever
run as a Carousel the stock photo must still not be passed off as that alley.

---

## 2026-09-29 (Tue), reel / local — SKIPPED

Twelfth consecutive Reel-day skip. Every gate re-checked against the runner and the
repo this run rather than inherited from the entry below. No content JSON, no
rendered output, no change to `queue.json`. One blocker survives the re-check —
media — and it alone is decisive. The full Reel render path was exercised
end to end again this run and works.

`TZ=Asia/Seoul date` → Tuesday 2026-09-29 12:09 KST, `+%u` → 2 → §1 row 2 → reel /
local, Collab **candidate**; the run prompt set the same format. No same-day
`pending` or `published` queue item (§0): `grep -c 2026-09-29 queue.json` → 0, and
no item's `publish_at` starts with `2026-09-29`. Working tree clean at start.
`queue.json` unchanged at 44 items — 32 `held`, 12 `published`, **zero** `pending`.
No ramp flag (§1): a repo-wide search of `*.json`/`*.yml` for "ramp" returns
nothing, so the only hits remain prose in CONTENT.md, PIPELINE.md and this file.

### The standing escalation, restated because it is now the whole story

With the action block withdrawn and the render path proven, **media rights are the
only thing keeping this account to two posts a week.** Five of seven slots
(Mon/Tue/Thu/Fri/Sun) are Reels and every one of them has been unreachable since
2026-09-14. The fixes remain the three listed in the 2026-09-15 entry, all
editorial decisions reserved for a human:

- drop owner-original photos into `assets/photos/` for venues to be covered;
- restore a stock allowance for Reels in §3, with a not-the-venue disclaimer;
- move venue-specific days to Carousel and keep Reels for editorial topics.

### Blocking: no compliant media for a Reel (re-verified from scratch)

- **§3 option 1 (owner original) — none.** `git log --diff-filter=A` over
  `assets/photos/` lists 45 files: 44 authored by `claude[bot]` pipeline commits,
  one by a human — `cheongildip-en.jpg` (392aefd, Steve, 2026-08-25 13:02 KST).
  That file predates policy v2 (8128750, 2026-09-14 10:12 KST) and is already
  spent on `content/2026-08-25-cheongildip-en.json`. Tree clean, so no
  un-committed drop either.
- **§3 option 2 (venue/creator media with written permission) — none.** A repo-wide
  file search for `permission|rights|licen|consent` returns no record of any grant,
  and none is obtainable by an unattended run.
- **§3 option 3 (licensed stock) — closed by format.** Permitted only for a
  non-venue-specific editorial *Carousel*. Tuesday is a Reel. The constraint binds
  on **format**, so an editorial local-food angle could not rescue the day either —
  and §2 below found a venue-specific subject in any case.

Stopped under §0. Deliberately did **not** write `asset_source: "licensed_stock"` +
`rights_confirmed: true` for a Reel. Re-read `validate_rights()`
(`scripts/publish.py:78`) this run: it returns early for `policy_version < 2`, then
checks only that `asset_source` is in `{original, partner_licensed, licensed_stock}`
and that a Collab is `accepted`. **There is still no format check**, so a stock Reel
would sail through the publisher while violating §3. Gap first logged 2026-09-15,
still open.

Did not render a typography-only cover as a substitute — the run prompt rules it out
explicitly for this account, and §3 rules out presenting a non-venue image as the
venue. Did not switch Tuesday to Carousel to reach option 3: §1 fixes Tuesday as a
Reel and the run prompt set reel. The CC-licensed-venue-photo reading raised
2026-09-24 and rejected on 09-25, 09-27 and 09-28 stays rejected on the same
grounds — CONTENT.md glosses option 2 as "original or written **partner**-authorized
media", the `asset_source` enum has no slot for a Commons photographer, and
loosening a rights rule on a live account is outward-facing and hard to reverse.
Moot again today, since option 3's format bar applies whatever the licence.

Collab handling (§3) is moot for the same reason: Tuesday is a Collab *candidate*,
but no item was created, so nothing was queued with `collab_status: requested`.

### §2 research passed — a verified, uncovered local-food subject is ready to ship

Media alone stopped this run, so the research is written up for a human. Tuesday's
pillar is local food.

**Ttungbo Halmae Gimbap (뚱보할매김밥)** — Jungang Market, Tongyeong,
Gyeongsangnam-do. New to the account: no file in `content/` names it, and it is
distinct from the ten local-pillar posts already published.

- **The hook:** chungmu gimbap is the one Korean gimbap deliberately built
  *unrolled* — rice-only finger rolls with the filling served beside them, because
  filled rolls spoiled on a fishing boat. This house is Tongyeong's best-known
  chungmu gimbap shop.
- **Naming precision — do not write "the originator" flatly.** KTO's VisitKorea
  page gives the origin as fishermen packing rice and sides separately to keep them
  fresh at sea, and English Wikipedia's `Chungmu-gimbap` gives the same account
  ("a wife prepared a gimbap for her husband, a fisherman who went out to sea from
  Chungmu Port … to prevent the food from spoiling, she packed the rolls and side
  dishes separately"). **Neither source names this shop, and Wikipedia does not
  mention it at all.** The 원조 claim comes from Korean travel/listing write-ups,
  not from an official source. Safe copy: "Tongyeong's best-known chungmu gimbap
  house, in Jungang Market" — attribute any 원조 or generation claim, or drop it.
- Official name 뚱보할매김밥 / Ttungbo Halmae Gimbap. Address 경상남도 통영시
  통영해안로 325 (325 Tongyeonghaean-ro, Tongyeong-si, Gyeongsangnam-do); lot
  address 통영시 중앙동 129-3. Phone 055-645-2619 / +82-55-645-2619. By Jungang
  Market and Gangguan harbour.
- **Hours: 06:00–22:00.** VisitKorea and DiningCode agree exactly, and VisitKorea
  gives closed days as "N/A (Open all year round)" — unusually, no discrepancy to
  resolve, unlike the 09-28 subject. A 06:00 open is itself a usable detail for a
  market post.
- **Price: chungmu gimbap ₩7,000 per portion** (DiningCode menu, checked
  2026-09-29 KST). A portion is commonly described as eight rolls served with
  seokbakji radish kimchi and a squid-and-fishcake muchim.
- **Current operation:** DiningCode shows the listing as 영업 중 with recent
  reviews and visitor photos; the KTO VisitKorea English page is live with the same
  address, phone and hours. Two independent current sources, one official.
- Suggested `search_keyword`: "Tongyeong chungmu gimbap Jungang Market".
- **Caveats for copy:** the ₩7,000 price and the eight-roll portion come from
  listing platforms, not the shop, so date them; the "1인 1주문", prepay-first and
  two-portion takeout minimum rules appear in Korean travel write-ups but were
  **not** corroborated by an official source this run and should be left out or
  attributed; nothing may be written as a visit.
- **Sources, as-of 2026-09-29 KST:** Korea Tourism Organization, VisitKorea English
  (`english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=85867`) — name,
  address, phone, 06:00–22:00, open year round, origin account; DiningCode profile
  `0otucYRjw9Q2` — road and lot address, phone, hours, ₩7,000 menu price, 영업 중
  status; English Wikipedia, `Chungmu-gimbap` — dish composition, rice-only rolls,
  kolddugi-muchim and radish kimchi sides, Chungmu/Tongyeong origin account.

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-09-29 Tuesday → reel / local (§1); §0 same-day gate
  clear; tree clean; no ramp flag; zero `pending` items.
- **WebSearch works** (English and Korean queries both returned usable results).
  **WebFetch works** on `english.visitkorea.or.kr`, `diningcode.com` and
  `en.wikipedia.org`. Two failures worth recording for future runs: Tongyeong
  city's own tourism site `utour.go.kr` **refuses the connection**
  (`ECONNREFUSED 27.101.75.57:443`), and `telltrip.com` returns **HTTP 403**. Add
  these to the 09-28 note that `guide.michelin.com` returns an empty body. KTO
  VisitKorea is the most reliable official listing source found so far.
- `scripts/cardnews.py` renders **7 slides, all 1080×1350, exit 0**, verified by
  re-rendering `2026-09-12-dongnae-halmae-pajeon-en` to a scratch dir and checking
  every slide's pixel size with pillow 12.3.0. Per the 2026-09-16 note, exit 0 is
  not proof on its own — the cover was also **opened and looked at**, and composes
  correctly (eyebrow, three-line headline, subline, handle, 7-dot pager, no
  overflow, no collision).
- **The full Reel path is confirmed working this run.** ffmpeg is still absent from
  the runner image and still absent from `.github/workflows/`, but
  `sudo apt-get install -y ffmpeg` succeeded (6.1.1-3ubuntu5) and `scripts/reel.py`
  then produced a **1080×1920, 30fps, 22.20s MP4 with an audio stream, exit 0**
  (ffprobe-verified, 8.4 MB). Only warning is the expected
  `! local: tracks.json 에 등록됐지만 파일이 없습니다` — `assets/music/*.mp3` is
  gitignored, so cloud Reels use ffmpeg-synthesized audio. **Media rights, not
  tooling, is what stops a Reel day.** The one-line `daily-content.yml` ffmpeg fix
  from the 2026-09-15 entry is still unapplied and still unappliable by an agent
  (`contents: write` / `id-token: write` only).
- The Instagram action block stays **withdrawn** (see header). Nothing has been due
  since 2026-09-26, so the publish path was not re-exercised, but no new block
  evidence appeared and no item moved to `held`. Ramp status unchanged: 2026-09-26
  is still post 1 of week 1, since this run adds nothing.

---

## 2026-09-28 (Mon), reel / restaurant — SKIPPED

Eleventh consecutive Reel-day skip. Every gate re-checked against the runner and
the repo this run rather than inherited from the entry below. No content JSON, no
rendered output, no change to `queue.json`. One blocker survives the re-check —
media — and it alone is decisive. Everything else in the pipeline was exercised
this run and works, including the full Reel render path.

`TZ=Asia/Seoul date` → Monday 2026-09-28 11:24 KST, `+%u` → 1 → §1 row 1 → reel /
restaurant, Collab **optional**; the run prompt set the same format. No same-day
`pending` or `published` queue item (§0): `grep -c 2026-09-28 queue.json` → 0, and
no item's `publish_at` starts with `2026-09-28`. Working tree clean at start.
`queue.json` unchanged at 44 items — 32 `held`, 12 `published`, **zero** `pending`.
No ramp flag in `queue.json`, `.github/` or any repo note (§1); a repo-wide search
of `*.json`/`*.yml` for "ramp" returns nothing, so the only hits remain prose in
CONTENT.md, PIPELINE.md and this file.

### Blocking: no compliant media for a Reel (re-verified from scratch)

- **§3 option 1 (owner original) — none.** `git log --diff-filter=A` over
  `assets/photos/` attributes 44 of the 45 files to `claude[bot]` pipeline commits.
  The single human-added file is still `cheongildip-en.jpg` (392aefd, Steve,
  2026-08-25, "content: English + photo-required pivot"), which predates policy v2.
  Nothing human-added since; tree clean, so no un-committed drop either.
- **§3 option 2 (venue/creator media with written permission) — none.** No
  permission record exists anywhere in the repo, and none is obtainable unattended.
- **§3 option 3 (licensed stock) — closed by format.** Permitted only for a
  non-venue-specific editorial *Carousel*. Monday is a Reel. The constraint binds on
  **format**, so an editorial angle (tacos/mole in Korea, say) could not rescue the
  day either — and §2 below found a venue-specific subject in any case.

Stopped under §0. Deliberately did **not** write `asset_source: "licensed_stock"` +
`rights_confirmed: true` for a Reel — re-read `validate_rights()` in
`scripts/publish.py` this run and it still has no format check, so such an item
would pass the publisher while violating §3. That gap was first logged 2026-09-15
and is still open. Policy-v2 metadata still exists in exactly four content files,
all Carousels: 09-16, 09-19, 09-23, 09-26, each `licensed_stock` /
`rights_confirmed: true`.

Also did not render a typography-only cover as a substitute. The run prompt rules
it out explicitly for this account, and §3 rules out presenting a non-venue image
as the venue.

The CC-licensed-venue-photo reading raised 2026-09-24 and rejected on 09-25 and
09-27 stays rejected, unchanged reasoning: CONTENT.md glosses §3 option 2 as
"original or written **partner**-authorized media", the `asset_source` enum has no
slot for a Commons photographer, and loosening a rights rule on a live account is
outward-facing and hard to reverse. Moot again today — option 3's format bar
applies whatever the licence.

Did not switch Monday to Carousel to reach option 3. §1 fixes Monday as a Reel and
the run prompt set reel; "move the venue-specific days to Carousel" is listed in
the 2026-09-15 entry as an editorial fix reserved for a human.

### §2 research passed — a verified, uncovered restaurant is ready to ship

Media alone stopped this run, so the research is written up for a human. Monday's
pillar is restaurant.

**Escondido (에스콘디도)** — Hannam-dong, Seoul. New to the account: no post in
`content/` names it, and none of the MICHELIN Seoul & Busan 2026 starred names
checked (Bicena, Collage, Eatanic Garden, Escondido, Exquisine, GAGGEN) appear
anywhere in `content/`.

- **The hook, stated precisely:** Escondido is **Asia's first Mexican restaurant to
  earn a MICHELIN star**, and it holds 1 star in the MICHELIN Guide South Korea
  2026. **Correction to carry into copy:** the star was awarded in the **Seoul &
  Busan 2025** edition and retained for 2026 — it is *not* a new-for-2026 star. An
  early WebSearch summary this run listed it among 2026's new one-stars; the
  MoneyToday interview contradicts that directly, so copy must say "first
  MICHELIN-starred Mexican restaurant in Asia" and not "new star".
- Chef **Jin Woo-beom (진우범)**, 32 at the time of the interview. Studied
  architecture at UC Berkeley, went to Mexico in 2017 to train, including under
  Enrique Olvera. Escondido had been open under a year when the star landed. He
  also runs El Molino (Seongsu-dong), Pescadería, and La Caye (Sindang-dong, near
  Jungang Market) under the "Molino Project" F&B brand.
- Official name 에스콘디도 / Escondido. Address 서울 용산구 한남대로20길 61-7
  지하 1층 (lot address 용산구 한남동 32-48); the MICHELIN listing renders the same
  address in English as B1, 61-7 Hannam-daero 20-gil, Yongsan-gu, Seoul 04419.
  Phone 02-2038-8994.
- **Hours: 17:15 onward, Tuesday–Saturday, closed Sunday and Monday.** Reservation
  only, by phone. One private room; valet parking; wine/mezcal/tequila pairings;
  corkage permitted.
  **Unresolved discrepancy — do not write a closing time.** DiningCode's profile
  gives 17:15–22:30; a search snippet for the same venue gave 17:15–23:00. Opening
  time and closed days agree across both. A future run should settle this from one
  source before putting a closing time on screen.
- **Price:** dinner course **₩210,000** per person, described as seasonally
  variable. Counter-style service where the chef explains each dish.
- **Current operation:** DiningCode profile shows an active, reservation-only
  listing, and the MICHELIN Guide restaurant page is live — an official listing per
  §2.
- Suggested `search_keyword`: "Seoul Michelin Mexican restaurant Hannam".
- **Caveats for copy:** the ₩210,000 course price is season-dependent; the
  restaurant is closed Mondays and Sundays, which is worth saying plainly to
  travelers; the DiningCode listing also claims a 흑백요리사 (Culinary Class Wars)
  appearance, which was **not** corroborated by a second source this run and should
  be left out; and nothing may be written as a visit.
- **Sources, as-of 2026-09-28 KST:** MoneyToday interview with Jin Woo-beom,
  2026-03-26, mt.co.kr/living/2026/03/26/2026032509135633487 — star edition, "Asia's
  first", chef background, sister restaurants; DiningCode profile `e1nbttyqArIH` —
  both addresses, phone, hours, closed days, course price, reservation-only status,
  1-star listing; MICHELIN Guide restaurant page
  guide.michelin.com/kr/en/seoul-capital-area/kr-seoul/restaurant/escondido — 2026
  1-star status and the English address (via search result; the domain itself is not
  fetchable, see below).

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-09-28 Monday → reel / restaurant (§1); §0 same-day
  gate clear; tree clean; no ramp flag.
- **WebSearch works** (English and Korean queries both returned usable results).
  **WebFetch works** on mt.co.kr and diningcode.com. **`guide.michelin.com` returns
  empty content to WebFetch** — both an article URL and the ceremony highlights URL
  came back with no body, so Michelin facts had to be triangulated from search
  snippets plus Korean press. Consistent with the 09-25 entry's note that
  `guide.michelin.com` could not be fetched directly. Use DiningCode/Naver/Korean
  press for listing data.
- `scripts/cardnews.py` renders **7 slides, all 1080×1350, exit 0**, verified by
  re-rendering `2026-09-26-korea-market-price-rules-en` to a scratch dir and
  checking every slide's pixel size with pillow (12.3.0). Per the 2026-09-16 note,
  exit 0 alone is not proof — slide sizes were checked, not just the return code.
- **The full Reel path is confirmed working this run.** ffmpeg is still absent from
  the runner image and still absent from every file in `.github/workflows/`, but
  `sudo apt-get install -y ffmpeg` succeeded (6.1.1-3ubuntu5), and
  `scripts/cardnews.py` + `scripts/reel.py` on `2026-09-13-le-dorer-en` then
  produced a **1080×1920, 22.2s MP4, exit 0** (ffprobe-verified). Only warning is
  the expected `! restaurant: tracks.json 에 등록됐지만 파일이 없습니다` —
  `assets/music/*.mp3` is gitignored, so cloud Reels use ffmpeg-synthesized audio.
  So a Reel day is fully renderable today; **media rights, not tooling, is what
  stops it.** The one-line `daily-content.yml` fix from the 2026-09-15 entry is
  still unapplied and still unappliable by an agent (`contents: write` /
  `id-token: write` only).
- The Instagram action block stays **withdrawn** (see header). Nothing was due since
  2026-09-26, so the publish path has not been re-exercised, but no new block
  evidence appeared and no item moved to `held`. Ramp status unchanged: 2026-09-26
  is still post 1 of week 1, since this run adds nothing.

---

## 2026-09-27 (Sun), reel / cafe — SKIPPED

Tenth consecutive Reel-day skip, and the first since the account unblocked. Every
gate re-checked against the runner and the repo this run rather than inherited. No
content JSON, no rendered output, no change to `queue.json`. One blocker survives
the re-check — media — and it alone is decisive. The other standing blocker is
**withdrawn**: see the header, and the section below.

`TZ=Asia/Seoul date` → Sunday 2026-09-27 11:20 KST, `+%u` → 7 → §1 row 7 → reel /
cafe, Collab **optional**. No same-day `pending` or `published` queue item (§0):
`grep -c 2026-09-27 queue.json` → 0. Working tree clean at start. `queue.json` is
at 44 items — 32 `held`, 12 `published`, **zero** `pending`. No ramp flag in
`queue.json`, `.github/` or any repo note (§1); the only "ramp" hits repo-wide are
prose in CONTENT.md, PIPELINE.md and this file.

### New this run: the account is publishing again

`2026-09-26-korea-market-price-rules-en` went out at 2026-09-26 23:18:57 KST with
`media_id` 18144186298582897 (`publish: mark posted`, d3b80bf). That is the first
successful publish since 2026-08-30 and it breaks a run of four straight
`instagram_action_blocked` holds (09-13, 09-16, 09-19, 09-23), so the action block
logged from 2026-09-17 is resolved rather than merely untested. The header is
updated accordingly, and the ramp-flag consequence is recorded there — that is now
the live question for a human, not the block.

This does **not** change today's outcome. The two blockers were always independent:
the account being healthy makes a Reel publishable, not sourceable.

### Blocking: no compliant media for a Reel (re-verified from scratch)

- **§3 option 1 (owner original) — none.** `git log --diff-filter=A` over
  `assets/photos/` lists 45 files. 44 were added by `content: … (daily pipeline…)`
  commits authored by `claude[bot]`; the single human-added file is still
  `cheongildip-en.jpg` (392aefd, Steve, 2026-08-25 13:02 KST), which predates
  policy v2. Nothing human-added since — the newest additions are the bot's
  Carousel covers (0d38369 on 2026-09-26, ffe577d, b1863f5, 853fff6). Tree clean,
  so no un-committed drop either.
- **§3 option 2 (venue/creator media with written permission) — none.** No
  permission record exists anywhere in the repo, and none is obtainable unattended.
- **§3 option 3 (licensed stock) — closed by format.** Permitted only for a
  non-venue-specific editorial *Carousel*. Sunday is a Reel. The constraint binds on
  **format**, so an editorial cafe angle could not rescue the day either — and the
  §2 research below found a venue-specific subject in any case.

Stopped under §0. Deliberately did **not** write `asset_source: "licensed_stock"` +
`rights_confirmed: true` for a Reel — that still passes `validate_rights()`
(`scripts/publish.py`, still no format check; gap first logged 2026-09-15, still
open after re-reading the function this run) while violating §3.

Did not switch Sunday to Carousel to reach option 3. §1 fixes Sunday as a Reel, the
run prompt set the format to reel, and "move the venue-specific days to Carousel" is
listed in the 2026-09-15 entry as one of the editorial fixes reserved for a human.
Picking it unilaterally would be an unattended agent rewriting the content calendar.

The CC-licensed-venue-photo reading raised on 2026-09-24 and rejected again on
2026-09-25 stays rejected, for the recorded reason: CONTENT.md glosses §3 option 2
as "original or written **partner**-authorized media", the `asset_source` enum has
no slot for a Commons photographer, and loosening a rights rule on a live account
is outward-facing and hard to reverse. It is also moot today — see §3 option 3
above, which binds on format regardless of licence.

### §2 research passed — a verified, uncovered cafe is ready to ship

Media alone stopped this run, so the research is written up for a human to use as
soon as media is unblocked. Sunday's pillar is cafe/dessert.

**Ruli Coffee (루리커피)** — No. 51 on The World's 100 Best Coffee Shops 2026, and
the only Seoul entry on that list. The other Korean entry, Momos Coffee (No. 22,
Busan), is already covered (`2026-08-31-momos-coffee-en`), and every previously
covered cafe was checked against `content/` — Ruli is new to the account.

- Official name 루리커피 / RULI COFFEE. Address 서울 중구 퇴계로20길 31 1층
  (lot address 중구 남산동2가 18-9), a few minutes from Myeongdong. Phone
  0507-1420-9976.
- Hours 11:30–18:30, last order 18:15, closed every Wednesday. Basement parking.
- Currently operating — DiningCode listing shows active status, and it is in the
  2026 Blue Ribbon Seoul guide.
- The hook: 100+ Panamanian coffees including 20+ ultrapremium auction lots
  (Best of Panama, Geisha), filter coffee from ₩10,000 to ₩80,000+ a cup, served
  in Riedel wine glasses. Split layout — takeout bar on the right, tasting room on
  the left. Founded by the operator of the Korean community site Ruliweb, so the
  interior carries gachapon machines and anime merchandise against the tasting-room
  format.
- Suggested `search_keyword`: "Seoul geisha coffee tasting room Myeongdong".
- Sources, as-of 2026-09-27 KST: The Korea Herald, 9 Apr 2026, "From craft to
  rarity, two Korean cafes redefining the cup of joe"
  (koreaherald.com/article/10713588) — ranking, prices, format, Ruliweb link;
  DiningCode profile AAqmRY8O5kbK — name, both addresses, phone, hours, last
  order, closed day, operating status, price band, Blue Ribbon listing.
- Caveat to carry into copy: the ₩80,000 figure is the top of the auction-lot
  range, not a typical cup, and nothing here may be written as a visit.

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-09-27 Sunday → reel / cafe (§1); §0 same-day gate
  clear; no ramp flag.
- WebSearch works. WebFetch works on koreaherald.com and diningcode.com;
  tripadvisor.com returns HTTP 403 (use DiningCode or Naver for listing data).
- `scripts/cardnews.py` renders 7 slides at 1080×1350, exit 0, verified by
  re-rendering `2026-09-26-korea-market-price-rules-en` to a scratch dir and
  checking every slide's pixel size. pillow 12.3.0.
- **ffmpeg is still absent from the runner** and still absent from every file in
  `.github/workflows/`. Per the header this is a per-run install, not a blocker,
  but a Reel day must still run `sudo apt-get install -y ffmpeg` first. The
  one-line fix to `daily-content.yml` from the 2026-09-15 entry is still unapplied
  and still unappliable by an agent (`contents: write` / `id-token: write` only).

---

## 2026-09-25 (Fri), reel / restaurant — SKIPPED

Ninth consecutive Reel-day skip. Every gate re-checked against the runner and the
repo this run rather than inherited. No content JSON, no rendered output, no change
to `queue.json`. One blocker survives the re-check — media — and it alone is
decisive.

`TZ=Asia/Seoul date` → Friday 2026-09-25 11:20 KST, `+%u` → 5 → §1 row 5 → reel /
restaurant, Collab **candidate**. No same-day `pending` or `published` queue item
(§0): `grep -c 2026-09-25 queue.json` → 0, and the file is unchanged at 43 items
(32 `held`, 11 `published`, **zero** `pending`). Working tree clean at start. No
ramp flag in `queue.json` or any repo note (§1) — the only "ramp" hits repo-wide are
prose in CONTENT.md, PIPELINE.md and this file.

### §2 research passed; the stop is once more at §3

A verified, previously-uncovered restaurant was available, so media alone stopped
this run. Research written up below so a human can ship it quickly once media is
unblocked.

### Blocking: no compliant media for a Reel (re-verified from scratch)

- **§3 option 1 (owner original) — none.** `git log --diff-filter=A` over
  `assets/photos/` lists 45 files; 44 were added by `content: … (daily pipeline…)`
  commits, and the single human-added file is still `cheongildip-en.jpg` (392aefd,
  Steve, 2026-08-25 13:02 KST), which predates policy v2. Nothing human-added since.
  Tree clean, so no un-committed drop either.
- **§3 option 2 (venue/creator media with written permission) — none.** No
  permission record exists anywhere in the repo, and none is obtainable unattended.
- **§3 option 3 (licensed stock) — closed by format.** Permitted only for a
  non-venue-specific editorial *Carousel*. Friday is a Reel. The constraint binds on
  **format**, so an editorial samgyetang angle could not rescue the day either.

Stopped under §0. Deliberately did **not** write `asset_source: "licensed_stock"` +
`rights_confirmed: true` for a Reel — that still passes `validate_rights()`
(scripts/publish.py has no format check; gap first logged 2026-09-15, still open)
while violating §3.

Also checked, and worth recording: `cheongildip-en.jpg` is the one owner-committed
photo, so it is the closest thing in the repo to §3 option 1. It cannot serve. The
post that ships it, `content/2026-08-25-cheongildip-en.json`, carries **no**
`asset_source`, `rights_confirmed` or `rights_note` — like all 43 files in
`content/`, it has zero policy-v2 metadata — so nothing in the repo actually
evidences that it is owner-original rather than stock fetched under the pre-v2
policy. It is also already published, and depicts a different venue and pillar.

### The CC-licensed-venue-photo reading: still rejected, and moot again today

The 2026-09-24 entry raised and rejected reading §3 option 2 ("venue/creator media
with written permission") to cover a public licence such as CC BY / CC BY-SA /
KOGL Type 1. That rejection stands for the same reason: CONTENT.md glosses the rule
as "original or written **partner**-authorized media", the `asset_source` enum has
no slot for a Commons photographer, and loosening a rights rule on a live account is
outward-facing and hard to reverse — not a call for an unattended run.

Re-tested for today's pillar, and it is moot a second time. Commons has plenty of
*samgyetang* imagery (`incategory:"Samgyetang"` → 81 files, e.g.
`File:Korean soup-Samgyetang-08.jpg`, `File:Samgye-tang 2.jpg`), but every one is a
photo of the dish somewhere else, not of the venue below. Using one on a
venue-specific Reel is precisely what §3 forbids — "Do not use a mood photo as if it
depicts the named place" — so even the permissive reading yields nothing shippable.
Venue-level supply is as thin as it was for bars: `incategory:"Restaurants in
Seoul"` → 78 files, mostly unrelated interiors and dishes, none of them this
restaurant.

### Topic research (not the blocker) — one ready angle

**3rd Generation Samgyetang** (3대삼계탕 / listed by MICHELIN as "3rd Samgyetang"),
Seocho-dong, Seoul. New to the account: `content/` has no samgyetang post, and
`grep -ril samgyetang content/` returns nothing, so this is not a repeat.

- **Hook:** a 1973 family samgyetang shop, now third generation, named a **new Bib
  Gourmand in the MICHELIN Guide Seoul & Busan 2026** — announced 2026-02-27, one of
  eight new Bib Gourmands (five Seoul, three Busan).
- **Dish:** samgyetang whose broth is built from 40+ ingredients, finished with
  finely ground mung bean, pine nuts and mugwort paste; three samgyetang variants
  are the signature.
- **Price frame:** Bib Gourmand means a full meal under ₩45,000 per person. Treat as
  the Bib threshold, **not** as this shop's menu price — the actual price was not
  verified this run.
- **Address (from the MICHELIN listing, via search snippet):** 서초구 반포대로28길
  56-3, Seoul 06646.
- **Current operation:** supported by the active MICHELIN Guide listing (an official
  listing per §2). **Hours were not verified** — no source this run gave them, and
  `guide.michelin.com` could not be fetched directly (see below). A run that
  publishes this must verify hours and price before writing them into copy.
- **English search phrase for travelers:** "samgyetang Seocho Michelin Bib
  Gourmand" / "3rd Generation Samgyetang Seoul".
- **Sources fetched and read this run:** The Korea Herald, "Meet Bib Gourmand
  rookies in Michelin Guide Seoul & Busan 2026" (koreaherald.com/article/10684029)
  — fetched in full, confirms the eight rookies, the 2026-02-27 date, and the 1973 /
  third-generation / 40-ingredient facts. Search-level corroboration only for the
  Bib totals (71 Bib Gourmand: 51 Seoul, 20 Busan) and the address.

**Background context, search-level only, not individually verified:** the MICHELIN
Guide Seoul & Busan 2026 was announced 2026-03-05 at Signiel Busan, its 10th Korean
edition — 233 restaurants (178 Seoul, 55 Busan), 46 starred (1 three-star, 10
two-star, 35 one-star), Mingles holding Korea's only three stars for a second year,
Sosuheon promoted to two. Mingles, Sosuheon and Onjium all already have posts in
`content/`, and `2026-09-07-gosari-express-en.json` already covers another of the
eight Bib rookies — so 3rd Generation Samgyetang is the freshest unused hook from
this cycle.

### Verified working this run

- WebSearch works. WebFetch works on koreaherald.com (full article text returned).
  WebFetch returns an **empty body for every `guide.michelin.com` URL** tried (the
  2026 highlights, Bib Gourmand and restaurant-listing pages) and koreadaily.com
  returned HTTP 410 — so MICHELIN's own pages are reachable only via search
  snippets from this runner.
- `scripts/cardnews.py` renders 7 slides at 1080×1350, exit 0 (re-rendered
  `2026-08-25-cheongildip-en` to a scratch dir). Slide 4 was **opened and looked
  at**, not just exit-code checked: text sits inside the canvas, no box collision.
- **The full Reel path works.** `sudo apt-get install -y ffmpeg` succeeded (6.1.1)
  and `scripts/reel.py` then produced a 1080×1920 / 22.2s MP4, exit 0, dimensions
  confirmed with `ffprobe`. Audio is ffmpeg-synthesized because `assets/music/*.mp3`
  is gitignored (`! local: tracks.json 에 등록됐지만 파일이 없습니다`). ffmpeg is
  still absent from the runner image and from every file in `.github/workflows/`;
  `daily-content.yml` still grants only `contents: write` / `id-token: write`, so an
  agent still cannot push the install step.
- The Instagram action block was **not** re-tested — an unattended run must never
  publish (§0). Latest evidence in the repo is unchanged: `2026-09-23-korea-cafe-
  seat-time-en` held 2026-09-23 23:51 KST, code 4 / subcode 2207051.

---

## 2026-09-24 (Thu), reel / bar — SKIPPED

Eighth consecutive Reel-day skip. Every gate re-checked against the runner and the
repo this run rather than inherited. No content JSON, no rendered output, no change
to `queue.json`. One blocker survives the re-check — media — and it alone is
decisive.

`TZ=Asia/Seoul date` → Thursday 2026-09-24 11:02 KST, `+%u` → 4 → §1 row 4 → reel /
bar, Collab optional. No same-day `pending` or `published` queue item (§0): no
`2026-09-24` string in `queue.json`, which is unchanged at 43 items and still has
**zero** `pending`. Working tree clean at start. No ramp flag in `queue.json` or any
repo note (§1) — `grep -rn -i ramp queue.json .github/` returns nothing.

### §2 research passed; the stop is once more at §3

A verified bar topic was available, so media alone stopped this run. See "Topic
research" below — the research is written up in full so a human can ship it quickly
once media is unblocked.

### Blocking: no compliant media for a Reel (re-verified from scratch)

- **§3 option 1 (owner original) — none.** `git log --diff-filter=A --name-only --
  assets/photos/` shows all 45 files were added by `content: … (daily pipeline…)`
  commits; the most recent, `2026-09-23-korea-cafe-seat-time-en.jpg`, came from
  yesterday's Carousel run. The only human-added file, `cheongildip-en.jpg`
  (392aefd), predates policy v2. Nothing human-added since. Tree clean, so no
  un-committed drop either.
- **§3 option 2 (venue/creator media with written permission) — none.** No
  permission record exists anywhere in the repo, and none is obtainable unattended.
- **§3 option 3 (licensed stock) — closed by format.** Permitted only for a
  non-venue-specific editorial *Carousel*. Thursday is a Reel. The constraint binds
  on **format**, not only venue-specificity, so an editorial bar angle (the pub-
  closure story below would make a strong one) cannot rescue the day either.

Stopped under §0. Deliberately did **not** write `asset_source: "licensed_stock"` +
`rights_confirmed: true` for a Reel — that still passes `validate_rights()`
(scripts/publish.py has no format check; gap first logged 2026-09-15, still open)
while violating §3.

### New this run: the CC-licensed-venue-photo reading, considered and rejected

Worth recording because it is the one avenue earlier entries did not test, and a
future run will probably think of it again.

§3 option 2 reads "venue/creator media with written permission." A public licence
(CC BY, CC BY-SA, KOGL Type 1) *is* a written grant from the creator permitting
commercial reuse, and a photo that genuinely depicts the named venue commits
neither harm §3 names — it is not a scraped social photo, and it is not a mood
photo passed off as the place. On that reading a CC-licensed photo of a real Seoul
bar would qualify for a Reel.

**Not acted on, for two reasons.**

1. *The text does not clearly support it.* CONTENT.md glosses the same rule as
   "original or written **partner**-authorized media", and the `asset_source` enum
   offers only `original` / `partner_licensed` / `licensed_stock`. A Commons
   photographer is not a partner and has authorized nobody in particular. The
   reading is arguable, not plain — and loosening a rights rule on a live account
   is outward-facing and hard to reverse. Seven prior runs read §3 strictly and
   escalated it as an editorial decision; an unattended run should not quietly
   settle it the other way.
2. *It is moot today anyway.* Commons has essentially no usable Korean bar imagery.
   `incategory:"Bars in South Korea"`, `"Bars in Seoul"`, `"Pubs in South Korea"`
   and `"Cocktails in South Korea"` all return **0** files. `"Drinking
   establishments in South Korea"` returns 2: `File:Suwon Gamaekjip - Outside.jpg`
   (CC BY-SA 3.0, shot 2011 — 15 years stale, cannot evidence current operation)
   and `File:Jeju cute bar sign woljeongri jeju korea.jpg` (CC BY-SA 4.0, a sign,
   not a venue). Neither is publishable even under the permissive reading.

So the question is live for a human to settle, but settling it would not have
unblocked today.

### Verified working this run

- WebSearch works. WebFetch works (koreaherald.com returned full article text).
- `scripts/cardnews.py` renders 7 slides at 1080×1350, exit 0 (re-rendered
  `2026-09-23-korea-cafe-seat-time-en` to a scratch dir).
- **The full Reel path works.** `sudo apt-get install -y ffmpeg` succeeded (6.1.1),
  and `scripts/reel.py` then produced a valid 1080×1920 / 22.2s MP4 with
  synthesized audio, exit 0 — confirming the 2026-09-22 withdrawal of the ffmpeg
  blocker. Still absent from the runner image and from every file in
  `.github/workflows/`; `daily-content.yml` still grants only `contents: write` /
  `id-token: write`, so an agent still cannot push the install step.

### Topic research (not the blocker) — two ready angles

**Angle A — venue-specific, needs option-1/2 media.** Asia's 50 Best Bars 2026 was
announced 2026-07-29 at Wynn Palace, Macao. Four Seoul bars on the main list: Zest
No. 2 (Gangnam-gu; Best Bar in Korea for a fourth straight year; zero-waste, makes
sodas and spirits in-house; Jeju Garibaldi uses freshly squeezed hallabong juice
with the peels repurposed to infuse the house gin), Alice No. 13 (Cheongdam-dong),
Bar Cham No. 33 (Seochon, Jongno-gu; hanok; Korean spirits, soju-forward), M+MS
No. 42 (Gangnam-gu; **first-time entry**; cafe by day, cocktails by night, in-house
brewery and fermentation; the Yama is made with sour kimchi and tuna). Extended
51–100: Gong Gan No. 74, Charles H No. 87, Le Chamber No. 88, Soko No. 89.
Source: The Korea Herald, 29 Jul 2026 (koreaherald.com/article/10824797), fetched
and read in full this run. **Caveat: all eight already have posts in `content/`** —
M+MS's first-time entry is the freshest hook, but `2026-09-01-mms-bar-en.json`
exists, so a genuinely new bar needs sourcing beyond this list.

**Angle B — editorial, non-venue-specific; would fit a Carousel day.** Korea's
neighbourhood drinking scene is contracting hard, which is a better story than
another ranking. Casual pubs and beer houses fell to 28,178 in March 2026 from
52,302 in 2018, a ~46% contraction; the year to March 2026 alone lost 2,998 pubs
(−9.6%, ~8 closures a day), split into ganee jujeom −10.2% (8,894 → 7,985) and hof
pubs −9.4% (22,282 → 20,193). Alcohol consumption fell at its fastest pace in seven
years in early 2026. Reported by Seoul Economic Daily (24 May, 13 Apr and 14 Aug
2026) and The Drinks Business (Jun 2026). **These figures are from search-result
summaries only and were not individually fetched and verified this run** — a run
that uses them must re-verify each against the primary article before publishing.
Saved as a lead, not as checked copy.

---

## 2026-09-22 (Tue), reel / local — SKIPPED

Seventh consecutive Reel-day skip. Every gate re-checked against the runner and
the repo this run rather than inherited from the entry below. No content JSON, no
rendered output, no change to `queue.json`. One blocker survives the re-check —
media — and it alone is decisive.

`TZ=Asia/Seoul date` → Tuesday 2026-09-22 11:15 KST, `+%u` → 2 → §1 row 2 → reel /
local, Collab **candidate**. No same-day `pending` or `published` queue item (§0):
no `2026-09-22` string in `queue.json`, which is unchanged at 42 items — 31 `held`,
11 `published`, **zero** `pending`. Working tree clean at start. No ramp flag is
set in `queue.json` or repo notes (§1); the only "ramp" mentions are the prose in
CONTENT.md, PIPELINE.md and this file.

### §2 research passed; the stop is once more at §3

The candidate was **Jeonju Waengi Kongmulgukbap Specialty Restaurant**
(전주 왱이콩나물국밥전문점), a Jeonju house that serves one dish only — kongnamul
gukbap, bean-sprout rice soup. Verified this run against the Korea Tourism
Organization's official English site (`english.visitkorea.or.kr/svc/contents/
contentsView.do?vcontsId=228776`, fetched this run): currently listed at **88
Dongmun-gil, Wansan-gu, Jeonju-si, Jeonbuk-do**, phone **+82-63-287-6980**, hours
**07:00–21:00** (last order 20:30), **open all year round**, next to Dongmun Art
Street, broth described as anchovy and seafood. Not previously covered by this
account — the only Jeonju item so far is `2026-09-02-gogung-jeonju-en`
(bibimbap, `held`).

Two gaps that would have shaped the copy under §2, had it got that far: the
official page lists **no prices**, so no price claim could have been made from it
without a second source; and "open all year round" needs a listing-platform
cross-check before being printed as fact about a small family house. Neither was
pursued, because §3 stops the run regardless.

### Blocking: no compliant media for a venue-specific Reel

All three §3 options re-tested this run:

- **§3 option 1 (owner original) — none.** `assets/photos/` still holds 43 tracked
  files, unchanged since 2026-09-19. `git log --format=%an -- assets/photos` over
  *all* commits returns 41 by `claude[bot]` and exactly 1 by a human; per-file
  attribution confirms the single human file is `cheongildip-en.jpg` (Steve), which
  depicts a different, already-published venue — reusing it for a Jeonju gukbap
  house would itself breach §3's "do not use a mood photo as if it depicts the
  named place". There are **no video or footage assets in the repo at all**
  (`git ls-files` matches zero `.mp4/.mov/.m4v/.webm`), so even option 1 could only
  ever have supplied a still. `git status --porcelain --ignored` shows no untracked
  drop either.
- **§3 option 2 (partner media with written permission) — none.** No permission
  record exists anywhere in `assets/` or `content/`. The strings that match a
  `licen|permission|authoriz` grep are sources-slide prose, not rights metadata —
  e.g. "Used under PIPELINE.md section 3 option 3 — licensed stock on a
  non-venue-specific editorial Carousel." Only two of the 30 files in `content/`
  carry rights fields at all (`2026-09-16`, `2026-09-19`), both Carousels, both
  `licensed_stock`. No channel exists to obtain permission unattended.
- **§3 option 3 (licensed stock) — not available on a Reel.** §3 scopes option 3 to
  "a non-venue-specific editorial **Carousel**", and CONTENT.md § Media and rights
  states "Venue-specific Reels and Collabs must use original or written
  partner-authorized media." The constraint binds on **format**, so even a
  dish-level editorial angle (kongnamul gukbap as a dish) cannot use stock today.

The free-licensed-photo-of-the-actual-venue question, open since 2026-09-20, was
re-tested and is again moot for this candidate: Wikimedia Commons MediaSearch for
`왱이콩나물국밥` / `Waengi Kongnamul Gukbap Jeonju` returns **zero** results. The
underlying policy question still stands for a future candidate: a CC BY photo of
the named venue by an unrelated photographer is a written license from the
photographer but is neither owner-original nor venue/partner-authorized, so §3 as
written does not clearly admit it. An unattended run will not stretch §3 to cover
it.

Today was additionally a **Collab candidate** day (§1 row 2). That path is no
escape hatch: §3 requires `collab_status: requested` and forbids queueing as
pending until the partner accepts, and CONTENT.md notes the current Instagram
Login integration cannot invite collaborators at all without a human operator.

### Not re-testable this run: the account block

No Instagram credential is present in this environment — only GitHub tokens
(`GH_TOKEN`, `GITHUB_TOKEN`) are set — so `scripts/status.py` could not be run
against the Graph API. The last direct evidence remains
`2026-09-19-chuseok-2026-guide-en`, held at 22:50 KST on 2026-09-19 with
OAuthException code 4 / subcode 2207051, matching 2026-09-16 and 2026-09-13.
Everything from 2026-08-30 onward is `held`; the last successful publish was
`2026-08-30-le-dorer-en` at 12:54 KST on 2026-08-30 — now 23 days ago.

### Verified working this run

- `TZ=Asia/Seoul date` → Tuesday 2026-09-22; `+%u` → 2 → reel / local (§1).
- §0 gates: no same-day queue item, clean working tree, zero `pending`.
- **WebSearch works.** **WebFetch works** on `english.visitkorea.or.kr` and
  `commons.wikimedia.org`.
- `scripts/cardnews.py` renders **7 slides, exit 0** (1080×1350).
- `sudo apt-get install -y ffmpeg` **succeeds** (6.1.1); `scripts/reel.py` then
  renders a **1080×1920, 22.2s** MP4, exit 0. Licensed music falls back to
  synthesized audio as documented (`! local: tracks.json 에 등록됐지만 파일이
  없습니다`) because `assets/music/*.mp3` is gitignored.

So the whole toolchain is healthy end to end. The pipeline is blocked on an
editorial input — rights-cleared media for the named venue — not on code.

### To unblock Reel days, a human needs to pick one

1. drop owner-original photos (or footage) into `assets/photos/` for the venues to
   be covered, and record `asset_source: original` / `rights_confirmed: true`;
2. restore a stock allowance for Reels in PIPELINE.md §3, with the "never
   presented as the actual venue" disclaimer the pre-8128750 posts used;
3. move venue-specific days to Carousel and keep Reels for editorial topics;
4. or decide explicitly whether a CC BY photo of the named venue satisfies §3, and
   write that into §3 either way.

Note that unblocking media alone does not restore publishing — the account block
is separate and still unresolved. See the 2026-09-17 entry.

---

## 2026-09-21 (Mon), reel / restaurant — SKIPPED

Sixth consecutive Reel-day skip. All three blockers re-checked against the runner
and the repo this run rather than inherited from the entry below. No content JSON,
no rendered output, no change to `queue.json`.

`TZ=Asia/Seoul date` → Monday 2026-09-21 11:10 KST → §1 row 1 → reel / restaurant,
Collab optional. No same-day `pending` or `published` queue item (§0): `grep
2026-09-21 queue.json` returns nothing, the queue is unchanged at 42 items — 31
`held`, 11 `published`, **zero** `pending` — and the working tree was clean at
start.

### §2 research passed again; the stop is once more at §3

The candidate was **Hwangsaengga Kalguksu** (황생가칼국수) in Samcheong-dong, a
kalguksu house serving hand-cut noodles and nine-vegetable dumplings in beef
broth. Verified this run against the Seoul Metropolitan Government's official
English tourism site (`english.visitseoul.net/restaurants/Hwangsaengga-Kalguksu/
ENP003496`, fetched this run): currently listed and operating at **78 Bukchon-ro
5-gil, Jongno-gu, Seoul 03053**, phone **+82-2-739-6339**, hours **11:00–21:30**
(last order 20:30), **open 365 days a year**, price range around **₩10,000**. Not
previously covered by this account. So §2's venue existence, address, current
operation and price checks were all satisfiable from an official listing.

One claim was deliberately **not** carried forward: the restaurant's Bib Gourmand
status appeared only in search-result summaries. `guide.michelin.com` returned an
empty body to WebFetch on both the `/us/en/` and `/en/` paths this run, so the
distinction and its guide year were never confirmed at source and would have been
left out of the copy under §2.

### Blocking 1: no compliant media for a venue-specific Reel (unchanged)

- **§3 option 1 (owner original) — none.** `assets/photos/` still holds 43 tracked
  files, unchanged since 2026-09-19. `git log --format=%an -- assets/photos` over
  *all* commits, not just additions, returns 41 by `claude[bot]` and exactly 1 by a
  human: `cheongildip-en.jpg` (392aefd, Steve, 2026-08-25 13:02 KST), which predates
  the policy-v2 rewrite 8128750 (2026-09-14 10:12 KST) and depicts a different,
  already-posted venue. Reusing it for a kalguksu house would itself breach §3's
  "do not use a mood photo as if it depicts the named place". Working tree clean, so
  no un-committed drop either.
- **§3 option 2 (partner media with written permission) — none.** `grep -ril` over
  `assets/` and `content/` finds no permission record; the only two files carrying
  rights fields at all are the 2026-09-16 and 2026-09-19 Carousels, both
  `licensed_stock`. No channel exists to obtain permission unattended.
- **§3 option 3 (licensed stock) — not available on a Reel.** §3 scopes option 3 to
  "a non-venue-specific editorial **Carousel**", and CONTENT.md § Media and rights
  states that "Venue-specific Reels and Collabs must use original or written
  partner-authorized media."

The free-licensed-photo-of-the-actual-venue question raised on 2026-09-20 was
re-tested and is moot for this candidate in any case: Wikimedia Commons MediaSearch
for `Hwangsaengga Kalguksu` / `황생가칼국수` returns **zero** results this run. The
policy question itself still stands unchanged for a future candidate.

### Blocking 2: the account is still action-blocked (not re-testable this run)

Stated more narrowly than the entry below, because this run could not verify it
directly. No Instagram credential is present in this environment — only GitHub
tokens are set — so `scripts/status.py` could not be run against the Graph API. The
last direct evidence remains `2026-09-19-chuseok-2026-guide-en`, held at 22:50 KST
on 2026-09-19 with OAuthException code 4 / subcode 2207051, matching 2026-09-16 and
2026-09-13. No publish has been attempted since, so there is no newer signal either
way. Everything from 2026-08-30 onward is `held`; the last successful publish
remains **2026-08-30**. Per §6 these are never retried automatically. No ramp flag
is set in `queue.json` or any repo note, so §1's ramp imposed no constraint.

### Blocking 3 (Reel days only): ffmpeg is still missing

Re-confirmed, not assumed. `which ffmpeg` → not found.
`python3 scripts/reel.py content/2026-09-19-chuseok-2026-guide-en.json /tmp/...`
exits 1 with `FileNotFoundError: [Errno 2] No such file or directory: 'ffmpeg'`.
`grep -rn ffmpeg .github/workflows/` returns nothing, and `daily-content.yml` still
grants only `permissions: contents: write` / `id-token: write`, so this agent still
cannot add the install step itself. The fix is unchanged from the 2026-09-15 entry:
add `workflows: write`, or commit the `sudo apt-get install -y ffmpeg` step by hand
after the pillow install. §4 requires a 1080×1920 MP4 for a Reel, so even with
compliant media this run could not have produced one.

### Verified working this run

- WebSearch works. WebFetch works on `english.visitseoul.net` and
  `commons.wikimedia.org`; `guide.michelin.com` returns an empty body on both
  locale paths and is unusable as a source from this runner.
- `scripts/cardnews.py` renders 7 slides at 1080×1350, exit 0, verified this run
  against the 2026-09-19 content file into a scratch directory outside the repo.
  Nothing was written to `out/`.
- `scripts/reel.py` remains the only broken link in the toolchain, and only for
  want of ffmpeg — see Blocking 3.

---

## 2026-09-20 (Sun), reel / cafe — SKIPPED

Fifth consecutive Reel-day skip. Both standing blockers re-verified from source
this run rather than inherited, plus a third that is specific to Reel days. No
content JSON, no rendered output, no change to `queue.json`.

`TZ=Asia/Seoul date` → Sunday 2026-09-20 → §1 row 7 → reel / cafe. No same-day
`pending` or `published` queue item (§0): `grep 2026-09-20 queue.json` returns
nothing, and the queue now holds 42 items, 31 `held` and 11 `published`, with
**zero** `pending`. Working tree clean.

### The §2 research actually passed — this is a pure §3 stop

Worth recording, because it isolates the blocker. The candidate was **Fritz
Coffee Company, Wonseo branch**, a hanok-set cafe next to the Arario Museum in
Space. Verified against the company's own English site
(`en.fritz.co.kr/contact.html`, fetched this run): the branch is listed as
currently operating at **83 Yulgok-ro, Jongno-gu, Seoul**, hours **9:00–19:30**,
one of seven branches. Not previously covered by this account. So venue
existence, address and current operation under §2 were all satisfiable from an
official source. The run stopped one step later, at §3, for want of a photo.

### Blocking 1: no compliant media for a venue-specific Reel (unchanged)

- **§3 option 1 (owner original) — none.** `assets/photos/` now holds 43 tracked
  files. `git log --diff-filter=A` attributes exactly one to a human —
  `cheongildip-en.jpg` (392aefd, Steve, 2026-08-25) — and that commit predates the
  policy-v2 rewrite in 8128750 (2026-09-14 10:12 KST). The other 42 were fetched
  by `content: … (daily pipeline)` commits. Count rose 42 → 43 only because
  2026-09-19 added its own. Working tree is clean, so no un-committed drop either.
  The one human-supplied file also depicts a different, already-posted venue, so
  reusing it for Fritz would itself violate §3's "do not use a mood photo as if it
  depicts the named place".
- **§3 option 2 (partner media with written permission) — none.** No permission
  record anywhere in the repo, and no channel exists to obtain one unattended.
- **§3 option 3 (licensed stock) — not available on a Reel.** This is the letter of
  both documents, not an inference: §3 scopes option 3 to "a non-venue-specific
  editorial **Carousel**", and CONTENT.md § Media and rights is explicit that
  "Venue-specific Reels and Collabs must use original or written partner-authorized
  media."

**A question for the human, surfaced by this run's search.** I checked whether a
genuinely free-licensed photo *of the actual venue* exists, which would be a
different case from the mood-photo problem §3 is written against. It does not, for
Fritz — the nearest Commons hit, `File:Cafe CNow interior.jpg`, is CC BY 4.0 and
depicts a cafe at Budi Luhur University in **Indonesia**, verified through the
Commons API this run. But the general question stands: if a CC0/CC-BY photo that
truthfully depicts the named cafe were found, current policy would still bar it
from a Reel, because option 3 is scoped by *format* rather than by whether the
image honestly depicts the subject. That may be intended. If it is not, the fix is
a §3 wording change, and it would unblock five days a week.

### Blocking 2: the account is still action-blocked (unchanged)

`2026-09-19-chuseok-2026-guide-en` was queued `pending` for 18:30 KST by the
previous run. Last night's publisher attempted it and **held** it at 22:50 KST with
`instagram_action_blocked`, OAuthException code 4 / subcode 2207051 — the same
signature as 2026-09-16 and 2026-09-13. So the Wed/Sat escape hatch still produces
a publishable artifact and still does not produce a published post. Everything from
2026-08-30 onward is `held`; the last successful publish remains **2026-08-30**.
This is §6's designed behaviour, not a new fault, and it needs a human. No ramp
flag is set in `queue.json` or any repo note, so §1's ramp imposed no constraint.

### Blocking 3 (Reel days only): ffmpeg is still missing from the runner

Re-confirmed, not assumed: `which ffmpeg` → not found, and
`python3 scripts/reel.py content/2026-09-19-chuseok-2026-guide-en.json /tmp/...`
exits 1 with `FileNotFoundError: [Errno 2] No such file or directory: 'ffmpeg'`.
§4 requires a Reel to render a 1080×1920 MP4, so even with compliant media today's
run could not have produced one. `.github/workflows/daily-content.yml` still has no
ffmpeg install step and still grants only `permissions: contents: write`, so this
agent cannot add the step itself — it needs `workflows: write` added, or the step
committed by hand after the pillow install, as the 2026-09-15 entry sets out.

### Verified working this run

- WebSearch works. WebFetch works — `en.fritz.co.kr` returned all seven branches
  with addresses and hours, and the Wikimedia Commons API returned full
  `extmetadata` (`LicenseShortName: CC BY 4.0`, `AttributionRequired: true`) for
  programmatic licence checking.
- `scripts/cardnews.py` renders 7 slides at 1080×1350, exit 0, verified this run
  against the 2026-09-19 content file into a scratch directory. Nothing was written
  to `out/`.
- `scripts/reel.py` is the only broken link in the toolchain, and only for want of
  ffmpeg — see Blocking 3.

---

## 2026-09-19 (Sat), carousel / local — QUEUED, not skipped

Second run to take the Wed/Sat escape hatch. Queued
`2026-09-19-chuseok-2026-guide-en`, a non-venue-specific editorial Carousel on the
Chuseok 2026 holiday (Thu 24 – Sat 26 Sep) — what opens, what closes, and how the
travel week actually works. Names no venue as its subject, so §2's venue checks do
not apply and §3 option 3 is available.

Photo is `File:Songpyeon.jpg` from Wikimedia Commons, CC0 1.0, verified through the
Commons API this run (`LicenseShortName: CC0`, `AttributionRequired: false`,
`Restrictions:` empty, `Categories` includes CC-Zero) rather than assumed — same
method as 2026-09-16. It depicts the dish the post is actually about, so §3's "do
not use a mood photo as if it depicts the named place" rule is satisfied on the
merits, not just by the absence of a named venue.

### Two source conflicts, both disclosed on the quote slide rather than resolved

- **Palace free-entry window.** The Korea Times (18 Sep 2026) says Thursday through
  *Sunday*; VisitKorea frames the holiday itself as Thursday to *Saturday*. Slide 6
  says to treat Sunday the 27th as likely but worth checking.
- **28 Sep.** Not a temporary holiday, and not under official review, as of
  Seoul Economic Daily 13 Sep 2026. Stated with its as-of date so it ages honestly.

**Rejected during research:** Korea Herald article 10575897 turned up in search as a
Chuseok toll-waiver source. It is about Chuseok **2025** (tolls 4–7 Oct, published
15 Sep 2025). Likewise `korea.net` articleId 258260, which search surfaced for 2026
palace free entry, is a 2024 article. Neither was used. Aggregator blogs asserting
2026 KTX booking windows (3–11 Sep) were also dropped — no primary source found, so
slide 5 gives the tourism office's generic sell-out warning instead of dates.

**Still open for a human — unchanged and still blocking publication:** the account
remains action-blocked. Everything from 2026-08-30 on is `held`; last successful
publish 2026-08-30; 2026-09-16 was held at 23:46 KST with code 4 / subcode 2207051.
This item is `pending` for 18:30 KST, so tonight's 19:00 publisher will attempt it
and, if the block is still live, will hold it — §6's designed behaviour, not a new
fault. No ramp flag is set in `queue.json` or any repo note, so §1's ramp imposed no
constraint. The Reel-day media blocker (Mon/Tue/Thu/Fri/Sun) is also unchanged.

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-09-19 Saturday → carousel / local (§1). No same-day
  `pending`/`published` queue item (§0).
- WebSearch works. WebFetch works (koreatimes.co.kr, en.sedaily.com,
  english.visitkorea.or.kr all returned usable text). WebFetch correctly flagged
  both the 2025 and 2024 articles above as off-year — worth trusting on dates.
- Wikimedia Commons API reachable for programmatic licence verification.
- `scripts/cardnews.py` renders 7 slides at 1080×1350, exit 0. **All seven were
  opened and inspected**, per the 2026-09-16 note that `fit()` overflows silently —
  no overflow or CTA collision this time.

---

## 2026-09-18 (Fri), reel / restaurant — SKIPPED

Fourth consecutive Reel-day skip. Same two blockers, both re-verified from source
this run rather than inherited. No content JSON, no rendered output, no change to
`queue.json`.

### Blocking 1: no compliant media for a venue-specific Reel

- **§3 option 1 (owner original) — none.** `assets/photos/` now holds 42 files.
  `git log --diff-filter=A` attributes exactly one to a human — `cheongildip-en.jpg`
  (392aefd, Steve, 2026-08-25) — and that commit *predates* the policy-v2 rewrite
  in 8128750. Every other file was fetched by a `content: … (daily pipeline)` commit.
  (The count rose 40 → 42 only because 2026-09-16 added its own two.) Working tree
  is clean, so there is no un-committed drop either.
- **§3 option 2 (written venue permission) — unobtainable unattended.** Grepped the
  whole repo for permission records: the only `rights_note` in `content/` is the one
  on 2026-09-16, and it documents a stock licence, not a venue grant.
- **§3 option 3 (licensed stock) — closed by format.** Stock is permitted only for a
  non-venue-specific editorial *Carousel*. Friday is a Reel.

**Checked this run and rejected: an openly-licensed photo that really does depict the
venue.** A Wikimedia Commons CC0/CC-BY shot of the actual restaurant would satisfy
§3's accuracy rule ("do not use a mood photo as if it depicts the named place") — but
accuracy is not the binding constraint. The repo already has a precedent for how such
a photo classifies: 2026-09-16 used a Commons CC0 image and recorded
`asset_source: "licensed_stock"`. `licensed_stock` on a Reel violates §3, and
CONTENT.md is independently explicit — "Venue-specific Reels and Collabs must use
original or written partner-authorized media." So this path is closed too.

Note the constraint binds on **format**, not only venue-specificity: §3 option 3 names
Carousel, so even a dish-level or editorial Reel angle cannot use stock.

Stopped under §0. Deliberately did **not** write `asset_source: "licensed_stock"` +
`rights_confirmed: true` for a Reel — that still passes `validate_rights()`
(scripts/publish.py has no format check; the gap logged on 2026-09-15 is still open)
while violating §3. The policy remains enforced only here.

### Blocking 2: Instagram account still action-blocked

Unchanged. Every item from 2026-08-30 onward is `held` — 2026-09-16, the post
designed to be publishable via the Wed/Sat hatch, was held at 2026-09-16 23:46 KST
with code 4 / subcode 2207051. Last successful publish is still 2026-08-30. No ramp
flag is set in `queue.json` or any repo note, and CONTENT.md says the workflow "stays
disabled until a human confirms that Account Status is clear."

### ffmpeg: still missing, still not fixable from here

`which ffmpeg` → not found on this runner, and `grep -rn ffmpeg .github/workflows/`
returns nothing, so the install step recommended on 2026-09-15 has still not been
applied. This run cannot apply it either: `daily-content.yml` grants only
`contents: write` / `id-token: write`, so pushing a workflow change is rejected.
Secondary to the media blocker — without media there is nothing to encode — but any
future Reel day needs a human to add it.

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-09-18 Friday → reel / restaurant, Collab candidate (§1).
- No same-day `pending`/`published` queue item (§0). No ramp flag set.
- WebSearch works. WebFetch works (koreatimes.co.kr returned full article text).
  `guide.michelin.com` fetches 200 but renders empty — client-side content; use a
  news mirror for that source.
- `scripts/cardnews.py` renders 7 slides at 1080×1350, exit 0 (re-rendered
  2026-09-16-korea-cup-rules-en to a scratch dir).
- `scripts/reel.py` not exercised — no ffmpeg and no compliant media.

### Topic research (not the blocker)

A verified restaurant topic was available, so media alone stopped this run. The
MICHELIN Guide Seoul & Busan **2027** pre-release (announced ~Aug 2026, full reveal
spring 2027) added six restaurants, featuring regional Italian cooking in Seoul and
local flavours in Busan; entries are flagged "New" in the Guide's Korea app and site.
Worth noting for reuse: the 2026 edition's six pre-release additions — Doori, Bium,
GiwaKang, Gosari Express, Onyva, Sobakeeri Suzu — are a year old now, and GiwaKang
and Gosari Express already have posts in `content/`.

---

## 2026-09-17 (Thu), reel / bar — SKIPPED

Third consecutive Reel-day skip, same decisive blocker. No content JSON, no
rendered output, no change to `queue.json`.

### Blocking: no compliant media for a venue-specific Reel (unchanged)

Re-verified from scratch this run rather than inherited from the entries below:

- **§3 option 1 (owner original) — none.** `git log --diff-filter=A --name-only
  -- assets/photos/` shows every one of the 40 files was added by a `content: …
  (daily pipeline…)` commit. Nothing has been human-added since policy v2 landed
  in 8128750. Working tree is clean, so no un-committed drop either.
- **§3 option 2 (written venue permission) — unobtainable unattended.** No
  permission record exists anywhere in the repo.
- **§3 option 3 (licensed stock) — closed by format.** Permitted only for a
  non-venue-specific editorial *Carousel*. Thursday is a Reel, so no editorial
  angle rescues it.

Stopped under §0. Deliberately did **not** write `asset_source:
"licensed_stock"` + `rights_confirmed: true` for a Reel: that combination passes
`validate_rights()` (scripts/publish.py:78 has no format check — see the open gap
noted on 2026-09-15) while violating §3. The policy is only enforced here.

### New this run: the Wed/Sat escape hatch also failed to reach Instagram

The header of this file says the blocker "does not stop Wed/Sat." That is still
true of the *media* rule, but it no longer means a Wed/Sat post publishes.
`2026-09-16-korea-cup-rules-en` — the first post to take that hatch — was held at
2026-09-16 23:46 KST with the same `instagram_action_blocked` (code 4, subcode
2207051, "Application request limit reached").

So **every** item since 2026-08-30 is now `held`, including the one designed to be
publishable. The last successful publish remains 2026-08-30. Queuing anything
today would only have added a 41st held item.

### Escalation for a human — the pipeline is now blocked end to end

Two independent faults, neither fixable by an unattended run:

1. **Media rights (blocks 5 of 7 days).** Mon/Tue/Thu/Fri/Sun are Reels and have
   had no legal media source since 8128750. Unblock by one of: dropping original
   photos into `assets/photos/`; restoring a stock allowance for Reels in §3;
   or moving venue-specific days to Carousel. This is an editorial decision.
2. **Instagram account status (blocks all 7 days).** The account is still
   action-blocked. CONTENT.md says the workflow "stays disabled until a human
   confirms that Account Status is clear," and §1 expects a manual ramp flag on
   recovery — no ramp flag is set in `queue.json` or any repo note.

Until at least one of these is cleared, further runs will keep skipping (Reel
days) or queueing items that fail at 19:00 KST (Carousel days).

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-09-17 Thursday → reel / bar (§1). No same-day
  `pending`/`published` queue item (§0). No ramp flag set.
- WebSearch works. WebFetch works (koreaherald.com; theworlds50best.com 301s to
  the50.com and succeeds on retry at the redirect URL).
- `scripts/cardnews.py` renders 7 slides at 1080×1350, exit 0.
- **ffmpeg is still missing from the runner** and still absent from every file in
  `.github/workflows/`. `sudo apt-get install -y ffmpeg` succeeds ad hoc (6.1.1),
  but the fix from the 2026-09-15 entry was never applied, and this run still
  cannot apply it: `daily-content.yml` grants only `contents: write` /
  `id-token: write`, so pushing a workflow change is rejected. Any future Reel
  day needs a human to add the install step.

### Topic research (not the blocker)

A verified topic was available, so media alone stopped this run. Asia's 50 Best
Bars 2026 (announced 2026-07-28, Macau) lists eight Seoul bars — Zest No. 2,
Alice No. 13, Bar Cham No. 33, M+MS No. 42, Gong Gan No. 74, Charles H No. 87,
Le Chamber No. 88, Soko No. 89. All eight already have posts in `content/`, so a
fresh bar would need sourcing beyond that list next time.

---

## 2026-09-16 (Wed), carousel / cafe — PUBLISHED TO QUEUE, not skipped

First run to take the Wed/Sat escape hatch the 2026-09-15 entry identified. Queued
`2026-09-16-korea-cup-rules-en`, a non-venue-specific editorial Carousel on Korea's
September 2026 reusable-cup pact. Names no venue as its subject, so §2's venue
checks do not apply and §3 option 3 is available.

Cover photo is CC0 1.0 (public domain) from Wikimedia Commons, licence verified
programmatically via the Commons API (`LicenseShortName: CC0`, `Restrictions:`
empty) rather than assumed — see `rights_note` in the content JSON. This is the
first file in `content/` to actually carry policy-v2 metadata
(`policy_version`/`asset_source`/`rights_confirmed`/`rights_note`), so it is also
the first that `publish.py:validate_rights()` checks rather than waves through.

**Still open for a human:** the account remains action-blocked. Everything from
2026-08-30 on is `held`; the last successful publish was 2026-08-30, and
2026-09-13 was held with subcode 2207051. This item is queued `pending` for 18:30
KST, so tonight's 19:00 publisher will attempt it. If the block is still live it
will fail and be set to `held` — that is PIPELINE.md §6's designed behaviour, not
a new fault. No ramp flag is set anywhere in `queue.json` or repo notes, so §1's
ramp imposed no constraint on this run.

**Rendering note for future runs:** `cardnews.py`'s `fit()` silently overflows
when text exceeds a box at its minimum font size — it does not raise. The first
render of this post ran off the canvas on the `point` slide and collided the
`source` list with the CTA box, and exited 0 both times. Renders must be looked
at, not just exit-code checked.

---

## 2026-09-15 (Tue), reel / local — SKIPPED

Second consecutive skip. No content JSON, no rendered output, no change to
`queue.json`.

The media blocker from 2026-09-14 is unchanged and remains decisive. The ffmpeg
blocker is **resolved** — see below.

### Still blocking: no compliant media for a venue-specific Reel

PIPELINE.md §3 allows, in order: (1) original media from the account owner,
(2) venue/creator media with written permission, (3) licensed stock **only for a
non-venue-specific editorial Carousel**. CONTENT.md agrees: "Venue-specific Reels
and Collabs must use original or written partner-authorized media."

Tuesday is reel + local food + Collab candidate. In this environment:

- no owner-supplied original media exists. Every file in `assets/photos/` was
  fetched by a previous pipeline run; the only human-added one
  (`cheongildip-en.jpg`, 392aefd) predates the new policy. Nothing has been added
  since the policy change;
- written venue permission cannot be obtained by an unattended run;
- licensed stock is available and legal, but §3 forbids it for this format.

Note the constraint binds on **format**, not only on venue-specificity. Even a
dish-focused editorial angle (e.g. chungmu gimbap as a dish rather than one
restaurant) cannot use stock, because §3 option 3 permits stock only for a
Carousel. Tuesday is a Reel, so that escape hatch is closed.

**This blocks every future run except Wed/Sat.** Mon/Tue/Thu/Fri/Sun are all
Reels. Only Wed/Sat (Carousel) can proceed, and only on a non-venue-specific
editorial topic.

To unblock, one of:

- drop original photos into `assets/photos/` for the venues to be covered;
- restore a stock allowance for Reels in PIPELINE.md §3 (with the "never presented
  as the actual venue" disclaimer the old posts used);
- move the venue-specific days to Carousel and keep Reels for editorial topics.

This is an editorial/policy decision, so an unattended run will not make it.

### Two corrections to the 2026-09-14 entry

1. **ffmpeg is installable and the Reel path works.** `sudo apt-get install -y
   ffmpeg` succeeds on the runner. With it installed, `scripts/reel.py` produced a
   valid 1080×1920, 22.2s MP4 from existing content with no errors. So this is a
   missing dependency, not a broken script.

   **A human must apply the fix** — this run could not. Pushing a change to
   `.github/workflows/` is rejected: `refusing to allow a GitHub App to create or
   update workflow .github/workflows/daily-content.yml without 'workflows'
   permission`. `daily-content.yml` grants only `contents: write` and
   `id-token: write`. Either add `workflows: write` to that block, or commit this
   step by hand after `pillow 설치`:

   ```yaml
   - name: ffmpeg 설치
     run: sudo apt-get update && sudo apt-get install -y ffmpeg
   ```

   As documented, cloud-built Reels use ffmpeg-synthesized audio, because
   `assets/music/*.mp3` is gitignored (`! local: tracks.json 에 등록됐지만 파일이
   없습니다`).

2. **No content file has `rights_note`.** The previous entry said `rights_note`
   values in `content/` read "licensed free-use stock, not <venue> itself". Those
   strings are real but they live in the **sources slide** text, not in a rights
   field. In fact **zero** of the 40 files in `content/` carry `policy_version`,
   `asset_source`, `rights_confirmed` or `rights_note` — policy v2 metadata is
   entirely unimplemented in existing content, and `cardnews.py` does not read it.

### Related gap: publish.py is more permissive than PIPELINE.md

`validate_rights()` (scripts/publish.py:78) skips all rights checks when
`policy_version < 2`, which is every existing file. For v2 content it accepts
`asset_source` in `{original, partner_licensed, licensed_stock}` **regardless of
format** — it does not encode §3's "stock only for a non-venue-specific editorial
Carousel" rule. A stock-photo Reel would therefore pass the publisher while
violating PIPELINE.md. Worth closing if §3 is meant to be enforced in code.

### Also worth a human decision: the account is still action-blocked

`2026-09-13-terarosa-gangneung-en` was held on 2026-09-14 with
`instagram_action_blocked` (OAuthException code 4, subcode 2207051). Everything
from 2026-08-30 onward is `held`; the last successful publish was 2026-08-30.

CONTENT.md says the workflow "stays disabled until a human confirms that Account
Status is clear" and that recovery ramps 3 posts in week 1, 4 in week 2. No ramp
flag is set anywhere in `queue.json` or repo notes, though PIPELINE.md §1 says to
respect one. Queuing new items now would feed the 19:00 KST publisher into an
actively blocked account.

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-09-15 Tuesday → reel / local (§1).
- No same-day `pending`/`published` queue item (§0).
- WebSearch works. WebFetch works on koreaherald.com; namu.wiki returns HTTP 403.
- `scripts/cardnews.py` renders 7 slides at 1080×1350 with no errors.
- `scripts/reel.py` renders 1080×1920 MP4 once ffmpeg is present.

---

## 2026-09-14 (Mon), reel / restaurant — SKIPPED

First run to execute the policy rewrite in 8128750 (2026-09-14 10:12 KST).
Stopped for two reasons: no compliant media for a venue-specific Reel (unchanged,
see above), and `ffmpeg` missing from the runner (since fixed).

The previous PIPELINE.md §4 explicitly permitted mood-matched Unsplash stock and
said the photo "does not need to be the literal venue's own interior". 8128750
removed that allowance. Every existing post relies on it — under the new rules
none of them would be publishable as Reels.
