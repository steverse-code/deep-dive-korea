# Skipped days — ongoing media-rights blocker

The media-rights blocker below stops every **Reel** day (Mon/Tue/Thu/Fri/Sun). It
does **not** stop Wed/Sat, which are Carousels: PIPELINE.md §3 option 3 allows
licensed stock on a non-venue-specific editorial Carousel. Each entry below
records one skipped run. Stopped under PIPELINE.md §0 ("If rights ... cannot be
verified, stop without adding a queue item").

**As of 2026-09-17 a second, separate blocker applies to all seven days:** the
Instagram account is still action-blocked, so Wed/Sat items now queue but fail at
publish time. See the 2026-09-17 entry. Both need a human. Last direct evidence is
the **2026-09-23** Carousel, held at 2026-09-23 23:51 KST with the same code 4 /
subcode 2207051 — the block is still live as of the most recent publish attempt.

**The ffmpeg blocker is withdrawn as of 2026-09-22.** The 2026-09-20 entry called
missing ffmpeg a third independent blocker on Reel days. That overstates it: ffmpeg
is absent from the runner image but installable at runtime, and on 2026-09-22
`sudo apt-get install -y ffmpeg` succeeded and `scripts/reel.py` then produced a
valid 1080×1920 / 22.2s MP4. A run that needs the Reel path can install it itself,
so it is a per-run setup step, not a blocker. Adding it to `daily-content.yml`
would still save the install on every run — see the 2026-09-15 entry for why an
agent cannot push that change. **Only the media blocker stops Reel days.**

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
