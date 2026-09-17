# Skipped days — ongoing media-rights blocker

The media-rights blocker below stops every **Reel** day (Mon/Tue/Thu/Fri/Sun). It
does **not** stop Wed/Sat, which are Carousels: PIPELINE.md §3 option 3 allows
licensed stock on a non-venue-specific editorial Carousel. Each entry below
records one skipped run. Stopped under PIPELINE.md §0 ("If rights ... cannot be
verified, stop without adding a queue item").

**As of 2026-09-17 a second, separate blocker applies to all seven days:** the
Instagram account is still action-blocked, so Wed/Sat items now queue but fail at
publish time. See the 2026-09-17 entry. Both need a human.

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
