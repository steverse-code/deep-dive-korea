# Skipped days — ongoing media-rights blocker

The media-rights blocker below stops every **Reel** day (Mon/Tue/Thu/Fri/Sun). It
does **not** stop Wed/Sat, which are Carousels: PIPELINE.md §3 option 3 allows
licensed stock on a non-venue-specific editorial Carousel. Each entry below
records one skipped run. Stopped under PIPELINE.md §0 ("If rights ... cannot be
verified, stop without adding a queue item"). As of 2026-11-26 that is **fifty-three
consecutive Reel-day skips**, and with the action block withdrawn it is the main
thing standing between the account and a daily *authoring* schedule — publishing is
separately dead on the token below. Re-measured 2026-11-19: **no file in `content/`
has ever carried `asset_source: original` or `partner_licensed`** (14 of 54 files
are policy-v2 and all 14 are `licensed_stock`), so the gate has never once been
cleared, and **all 14** photos added since the policy rewrite are pipeline-fetched
Carousel stock. New on 2026-11-19: the repo contains **no video or audio file at
all** — see the 2026-11-19 entry.

**NEW 2026-11-26 — the first test of a *public-sector* venue, and it produces the best
media candidate this ledger has ever recorded — but of the wrong building.** Previous
runs tested unaffiliated photographers (11-20, 11-23) and a non-venue-specific dish
photo (11-24). Thursday's bar pillar allows a different test: a venue whose **own
operator** is a government body that publishes under a public licence. 전통주갤러리
(The Sool Gallery) is run by **MAFRA + aT**, and the ministries' own joint press
release carries **공공누리 제1유형 (KOGL Type 1, attribution only — commercial use and
derivatives permitted)** with no third-party-copyright exclusion, and embeds a
**7360 × 4912** interior photograph. That is a venue-operator-published, free-licence,
full-resolution real photograph — it clears every acceptance criterion 11-20, 11-23
and 11-24 derived, by a wider margin than anything before it. It is still unusable,
for a reason none of the earlier tests hit: **the photo is of the 2015 Insa-dong
premises the gallery has since left.** See the 2026-11-26 entry, which also proposes
a **sixth** and much narrower unblocking option than any on the list.

**NEW 2026-11-26 — Wed 2026-11-25 ran no content at all: the third silent miss, and
the third cancelled token test.** The 11-24 entry named Wed 11-25 as "the next
possible test" of the credential. Like 11-16 and 11-21 it left no commit, no queue
item and no skip note. So the token count is **still eight** code-190 holds, still
last tested **2026-11-18**, and the next possible test is Sat **2026-11-28**. Measured
this run: of the **14** Carousel days since 2026-10-08, **5 produced nothing**
(10-14, 10-28, 11-14, 11-21, 11-25) — and **three of the last four**. The format that
can still ship is now failing to author more often than it ships, which makes raising
`--max-turns` and the §0 skip-note requirement more urgent than the Reel blocker.

**NEW 2026-11-24 — for the first time the media itself is compliant and only the
*format clause* blocks it.** The three pillar tests below all failed on the media
(wrong licence, no file, a trademark). Tuesday's local-food pillar does not:
`File:Korea-Tongyeong_food-Chungmu_gimbap-01.jpg` is **CC BY 3.0**, **2489×1659**,
and a real photograph — it clears every acceptance criterion 11-20 and 11-23
derived. It is honestly *non-venue-specific*, which makes it textbook §3 **option 3**
material; it is barred only because option 3 ends in the word "Carousel". So the
cheapest fix is narrower than the 11-20 amendment: extend option 3 to
non-venue-specific editorial **Reels**. See the 2026-11-24 entry, which also records
a fourth failure mode for the 11-20 amendment (the file's *description* names only
the city — the dish appears only in the filename and categories) and the first
video file this ledger has found (640×360, unusable).

**NEW 2026-11-23 — the free-licence pool is now measured, not guessed, and it is
about twenty files.** `incategory:"Restaurants in Seoul"` returns **8** files under
`haslicense:unrestricted` and **12** under `haslicense:attribution` — twenty in
total for the whole category, of which the identifiable ones are chains
(McDonald's ×2, Bored & Hungry) and most of the rest are unnamed storefronts the
11-20 amendment would not reach anyway. Three pillars have now been tested against
that amendment and all three fail differently: 11-20 found a venue-named photo under
the excluded CC BY-SA, 11-22 found no file at all, and 11-23 found the right licence
on a **142×72 trademark**. If it is adopted it needs two more acceptance criteria —
minimum resolution and "a photograph, not a logo." See the 2026-11-23 entry, which
also records a WebFetch gotcha: `guide.michelin.com` returns an **empty body**
rather than an error.

**NEW 2026-11-22 — Sat 2026-11-21 ran no content at all, the second silent miss in
seven days, and it cancelled the token test two entries were waiting on.** No
commit, no content JSON, no queue item, no skip note — invisible from this repo and
checkable only in the Actions log. So the token count stays at **eight** code-190
holds, last tested **2026-11-18**, and the next possible test is Wed **2026-11-25**.
See the 2026-11-22 entry; it also narrows the 11-20 recommendation below, which
would **not** have unblocked a cafe Reel: Commons has zero freely-licensed photos of
the researched venue, and the venue-named Korean cafe files that do exist are all
CC BY-SA.

**NEW 2026-11-20 — the blocker is the *format rule*, not a shortage of usable
photos.** Earlier entries say "no compliant media exists"; that holds only inside
this repo. This run verified a concrete counter-example in one WebFetch — a
CC BY-SA 4.0 Commons photo whose own description names 안동장, a 1948 Euljiro
restaurant that fits Friday's pillar exactly. It was still skipped, because the only
honest `asset_source` for an unaffiliated photographer's file is `licensed_stock`,
which §3 confines to Carousels. That reframes the fix: see the **fourth option** in
the 2026-11-20 entry, which needs no new photography and no blanket stock
allowance.

**NEW 2026-11-17 — one Reel day is missing from the ledger below, and the run that
lost it reported `success`.** Mon **2026-11-16** ran for 6m50s, went green on every
step, and committed nothing at all: no queue item (correct), but also **no skip
note** (not correct). It is recorded retroactively inside the 2026-11-17 entry, which
is why the count jumps 45 → 47. PIPELINE.md §0 never actually requires a skip note,
so a literal reading permits this; the recommended one-line fix to §0 is in that
entry. Until it is made, **a missing day is only detectable from the Actions log,
not from this repo** — the turn-cap misses at least show `conclusion: failure`,
whereas this one does not. The three possible fixes are
editorial and reserved for a human — see the 2026-09-15 entry.

**The Reel render path is no longer unproven — it was exercised end to end on
2026-11-13 and it works.** Every entry from 2026-11-06 to 2026-11-12 recorded only
that `scripts/reel.py` dies on missing ffmpeg and left "it worked on 2026-09-22" as
the newest positive evidence. This run installed ffmpeg and ran the real §4
two-step, producing a valid **1080×1920 / h264 / 30fps / 666-frame / 22.2s** MP4
with AAC audio. So the *only* thing standing between this pipeline and a Reel is
§3 media — not the renderer. Two mechanical gotchas for whoever
ships the first Reel are recorded in that entry: `reel.py` does **not** render
its own slides, and the MP4 must be probed *after* the process exits.
**Correction added 2026-11-15:** that run installed ffmpeg *ad hoc* in its own
session and the install step was never committed — `daily-content.yml` line 50 is
still only `pillow 설치`, so ffmpeg is **absent on a stock runner** and `reel.py`
would fail today. The renderer is proven; the runner is not provisioned for it.

**Token blocker still live — EIGHT straight code-190 holds, last tested 2026-11-18.**
The 2026-11-17 entry named Wed 11-18 as the next real test of the token. It ran, and
it failed identically: `2026-11-18-korea-coffee-price-en` was authored, rendered and
queued, then **held** at **2026-11-19T03:45:36 KST** on OAuthException **code 190**,
"session has been invalidated" (`fbtrace_id AZnGr_CckiGBGmxpU5BmWy1`, commit
155b9f4). Every Carousel authored since 10-10 has died the same way — 10-10, 10-17,
10-21, 10-31, 11-04, 11-07, 11-11, 11-18 — and `--max-turns 60` did not bite on
11-18, so the authoring side is working and the credential is the whole fault. Last
successful publish is **2026-10-07, 43 days** ago (re-measured 2026-11-19).
**Eight** finished posts have now been thrown away by this one expired credential,
and nine in total since 10-10 counting the 10-24 caption-cap loss.
Re-authorizing `IG_ACCESS_TOKEN` (CONNECT-GUIDE.md) is the top-priority human
action. The next item that could test it is the Sat **2026-11-21** Carousel.

**NEW as of 2026-10-29 — the turn cap, not the caption cap, took Wed 2026-10-28.**
The 2026-10-27 entry warned that the next run was the 10-28 Carousel and told it to
budget the caption under 2200 characters. That advice was never reached: run
**40623623652** failed at **11m42s** with `"subtype": "error_max_turns"` and
`Reached maximum number of turns (60)`, failing step `콘텐츠 작성`. No content JSON,
no queue entry, no skip note — a silent miss, confirmed this run from the Actions
log rather than inferred from the empty tree. **Carousel days lost to `--max-turns 60`
are now 09-30, 10-03, 10-14 and 10-28 — four of the last nine.** So the caption cap
measured on 10-24 is still untested, and the two publish-side faults are now
*queued behind each other*: the turn cap stops the item being authored, the caption
cap would stop a long one being published, and the dead token would stop whatever
survived. Raising `--max-turns` remains the single highest-value human fix, because
it is the only one of the three that blocks the format that can still ship.

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
## 2026-11-26 (Thu), reel / bar — SKIPPED

Fifty-third consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. §0 checked first: `queue.json` holds **54**
items (41 `held`, 13 `published`) and **none is dated 2026-11-25 or 2026-11-26**, so
no same-day `pending`/`published` item existed; no ramp flag is set anywhere
(`grep -rn ramp` outside this file still hits only PIPELINE.md:29 and CONTENT.md:20,
i.e. the rules themselves). §1: `TZ=Asia/Seoul date` → Thu 2026-11-26 14:50 KST,
`%u` = 4 → **reel / bar**, Collab optional, which agrees with the prompt's format.
Stopped at §3 under §0 ("If rights ... cannot be verified, stop without adding a
queue item"). The day was in fact barred **twice over** — see the renderer section.

### NEW — the public-sector venue test: the best media candidate ever found here, of a building the venue no longer occupies

Every previous media test in this ledger probed a *third-party* rightsholder:
11-20 an unaffiliated photographer (CC BY-SA, excluded), 11-23 the right licence on a
142×72 trademark, 11-24 a correctly-licensed but non-venue-specific dish photo.
Thursday's bar pillar allows a test none of them could run, and it goes directly at
§3 **option 2** rather than option 3:

> If the venue's **own operator** is a public body that releases its material under a
> public licence, is the operator's photo of its own premises "venue/creator media
> with written permission"?

**The factual leg checks out, and more convincingly than anything before it.**

- **The venue is public-sector.** 전통주갤러리 (The Sool Gallery) is operated by the
  **Ministry of Agriculture, Food and Rural Affairs (농림축산식품부)** and the **Korea
  Agro-Fisheries & Food Trade Corporation (aT)** — confirmed both in English by
  The Korea Times, 2026-07-09, and in a MAFRA release describing it as "2015년에
  농림축산식품부와 한국농수산식품유통공사가 설립한 우리 술 소통공간".
- **The operators' own press release is KOGL Type 1.** `mcst.go.kr`
  `/site/s_notice/press/pressView.jsp?pSeq=14057` (MAFRA + MCST joint release,
  2015-02-10) states verbatim: *"…저작물은 「공공누리」 1유형(출처표시) 공공저작물
  자유이용허락 조건에 따라 이용할 수 있습니다."* **Type 1 permits commercial use and
  derivative works, requiring only attribution** — so it is strictly more permissive
  than the CC BY-SA file rejected on 11-20, and it carries **no**
  "제3자 저작권 있음" exclusion, which ministry pages often do.
- **The photo is real, and enormous.** The release embeds two images captioned
  "전통주 갤러리 내부 모습" (interior of the gallery). One was downloaded and measured
  with pillow this run: `K20150210143313526_EMB00000d140001.jpg`, **7360 × 4912**,
  **21.9 MB**, JPEG — an un-downsized camera original. Short edge 4912 against the
  ≥1080 minimum the 11-23 entry asked for; a photograph, not a logo or a map, which
  is the other 11-23 criterion. For scale, the best previous candidate (11-24) was
  2489 × 1659.

**And then it fails, on a test no previous entry had to apply: the photo is of the
wrong building.** The 2015 release opens the gallery **in Insa-dong**
("…문체부와 손 잡고 인사동에 '전통주 갤러리' 개소"). The gallery is no longer there.
It now operates at **18 Bukchon-ro, Jongno-gu**, on the ground floor of the
한식문화공간 이음 (Korean Food Culture Space "Eum"), and a **second branch opened
2026-07-10** on **B2 of Doota Mall, Dongdaemun**, opposite the DDP. A MAFRA release
confirms both are current, referring to September tasting-and-sales events at
"북촌(1호), 동대문 두타몰(2호)".

So presenting an eleven-year-old interior of a vacated address as The Sool Gallery
would be precisely the thing §3 exists to forbid — "Do not use a mood photo as if it
depicts the named place" — with the aggravating factor that it is not a mood photo
but a *specific wrong room*. A reader who went to Bukchon expecting it would be
misled. This is a §2/§3 failure on **currency**, and it is a **fifth** distinct
failure mode for the media hunt, after licence (11-20), absence (11-22), subject
(11-23, a trademark) and description (11-24).

**No KOGL-licensed photo of either current location was found this run.** Two
dead ends worth recording so the next run does not repeat them:

- the second embedded image, `K20150210143313526_EMB00000d140008.jpg`, is
  **unretrievable** — `curl` exits **52** (empty reply from server) on both a plain
  and a `-L` request, while its sibling on the identical path downloads fine;
- **MAFRA's press-release board is not searchable by plain GET.**
  `mafra.go.kr/bbs/home/792/artclList.do?srchColumn=sj&srchWrd=<term>` returns
  **HTTP 200** with a well-formed page containing **zero** article rows for both
  "전통주 갤러리" and "두타몰". The listing is evidently built client-side or by POST.
  A `site:mafra.go.kr` WebSearch did surface individual `artclView.do` releases, so
  that is the working route in.

**A classification caveat, in case a current-venue KOGL photo is found later.** Even
then, `asset_source` is a judgment call this agent will not make alone. KOGL Type 1 is
a *blanket public licence*, not a grant to this account; by the same reasoning the
11-20 entry applied to CC BY, labelling it `partner_licensed` would overstate the
relationship, which leaves `licensed_stock` and its Carousel-only clause. The
difference from 11-20 is real and worth weighing, though: there the licensor was a
stranger to the venue, whereas here **the licensor *is* the venue's operator**, which
is the substance §3 option 2 is reaching for.

**Recommended amendment — a sixth option, and the narrowest one yet.** Unlike the
11-24 proposal it does not loosen the stock rule for Reels at all:

> Extend §3 **option 2** from "venue/creator media with written permission" to
> "venue/creator media with written permission, **including a public licence granted
> by the venue's own operator** (e.g. KOGL Type 1, CC BY) **where the media depicts
> the venue's current premises**", recording `asset_source: partner_licensed`, and
> requiring the licence type, the publishing body, the source URL and the photo's
> date in `rights_note` and on the sources slide.

Why this is the safest of the six on the menu: it keeps the blanket prohibition on
stock-as-venue fully intact, it requires an affiliation between licensor and venue
that a stranger's CC BY file can never satisfy, and the explicit **currency** clause
is what today's candidate failed on — without it the amendment would have licensed
exactly the misleading post described above. It unblocks venue-specific Reels for
public-sector and publicly-funded venues (traditional-liquor galleries, municipal
markets, museum cafes, 찾아가는 양조장 breweries), which is a meaningful slice of this
account's beat, with no new photography and no partner negotiation. Still editorial,
so an unattended run will not make it.

### §2 research recorded (venue verified; hours and prices deliberately not)

Subject **The Sool Gallery / 전통주갤러리** — new for this pillar. Prior bar subjects
are Zest, Ahn Makgeolli, Bar Cham, MMS, Charles H., Alice Cheongdam, Soko Hannam,
Le Chamber and Gong Gan, so there is no dedup conflict. As-of date **2026-11-26**.

**Verified, and safe for copy:**

- Official name 전통주갤러리 (The Sool Gallery); **1호점** on the 1st floor of the
  한식문화공간 이음, **18 Bukchon-ro, Jongno-gu, Seoul** (across from the
  Constitutional Court, near Anguk station).
- Operated by **MAFRA + aT**; **established 2015** (MAFRA release; The Korea Times
  2026-07-09).
- **2호점 opened 2026-07-10** on **B2, Doota Mall, Dongdaemun**, opposite the DDP, a
  mall the ministry puts at ~14,000 visitors a day with a high share of foreign
  visitors (The Korea Times 2026-07-09; Newsis 2026-07-09).
- The second branch's stated programme: guided tasting sessions by flavour profile,
  **traditional-liquor cocktail** demonstrations aimed at younger drinkers, and
  pop-ups rotating breweries from around the country.
- Both branches were current as of a MAFRA release scheduling September
  award-winner tastings at "북촌(1호), 동대문 두타몰(2호)".

**Reported but NOT verified to §2 standard — must not appear in copy:**

- **Hours.** Seoul city citizen-reporter pieces give Tue–Sun 10:00–19:00 for the
  Bukchon branch, but the most recent confirmation is 2024/2025 and an older piece
  gives 10:00–20:00 for the previous Gangnam-era location. No official current
  listing was reachable this run.
- **Tasting format and cost.** "Free monthly rotating tasting, five people at a
  ㅁ-shaped bar in the centre of the gallery, reserved online and filling within
  minutes" is consistently reported; a ₩5,000 no-show deposit refunded on
  attendance appears in a 2023 piece only. Reservation is variously said to be via
  Naver (Gangnam era) and via the 한식진흥원 site (current). Unconfirmed.
- The count of liquors shown (≈300 displayed / ≈80 sampled and sold) comes from a
  neighbourhood guide, not the operator.

**A WebFetch gotcha:** `english.visitkorea.or.kr/svc/searchList.do?keyword=...`
returns **HTTP 404**; the English VisitKorea search path used by older notes no
longer resolves. Third-party mirrors expose what look like VisitKorea content IDs
(e.g. `3080695`) but the official detail URL for them was not recovered this run.

Nothing above was written as if the account visited. Useful English search phrase for
travellers: "Sool Gallery Bukchon traditional Korean liquor free tasting reservation".

### §3, re-derived for this subject

Option 1 **original — none.** `git log --name-status -- assets/` shows the newest
media is still `assets/photos/2026-11-18-korea-coffee-price-en.jpg`, added by the
11-18 pipeline run itself (ddd3ca6). The only human-added photo in repo history is
still `cheongildip-en.jpg` (392aefd, 2026-08-25), which predates the policy rewrite
and carries no stated provenance, so it cannot be claimed as `original` either. A
fresh `find` for `*.mp4 *.mov *.m4v *.webm *.mp3 *.wav *.m4a` across the tree still
returns **0 hits** — still no video or audio file in this repo at all.
Option 2 **written permission — unobtainable** by an unattended run, and the
public-licence variant tested above fails on currency (and needs a wording decision
besides). Option 3 **licensed stock — format-barred**: today is a Reel. Of **54**
files in `content/`, **14** are `policy_version: 2`, **all 14** are
`licensed_stock`, **all 14** are Carousels, and **zero** have ever carried
`original` or `partner_licensed`. The §3 gate has still never been cleared.

### The renderer: Carousel path clean, Reel path still dead on this runner

The day was barred twice, and the second bar is worth stating plainly because it
would survive any §3 amendment:

- `python3 scripts/cardnews.py content/2026-11-18-korea-coffee-price-en.json
  /tmp/rendertest` → **exit 0, 7 slides, every one 1080 × 1350**, no errors, pillow
  **13.0.0**. Rendered outside the repo, so nothing was committed. Per the 2026-09-14
  warning that renders must be *looked at* and not merely exit-code checked, slide 01
  was opened and inspected: photo-backed cover, English copy, headline and subline
  inside their boxes, no overflow or collision.
- `python3 scripts/reel.py …` → **`FileNotFoundError: [Errno 2] No such file or
  directory: 'ffmpeg'`, exit 1.** `which ffmpeg ffprobe` → both absent.
  `.github/workflows/daily-content.yml:50-51` is still only `pillow 설치` /
  `pip install --quiet pillow`. The 2026-11-15 correction stands: the Reel renderer
  itself is proven (2026-11-13, a real 1080×1920 / h264 / 22.2s MP4), but **the
  runner has never been provisioned for it**. So even with perfect media, §4's
  two-step would have failed today at step two.

### Publish side: a third cancelled token test, and Carousel days are now the fragile ones

Wed **2026-11-25** was named by the 11-24 entry as the next possible test of
`IG_ACCESS_TOKEN`. `git log --since=2026-11-24` returns exactly one commit — 098c555,
the 11-24 skip note — and `queue.json` has no 2026-11-25 item. So 11-25 produced **no
commit, no content JSON, no queue entry and no skip note**: the **third** silent miss,
after 11-16 and 11-21, and the **third** consecutive cancellation of the token test.
Diagnosable only from the Actions log, which this agent cannot read.

- Token status unchanged: **eight** consecutive code-190 holds (10-10, 10-17, 10-21,
  10-31, 11-04, 11-07, 11-11, 11-18), last tested **2026-11-18**. Last successful
  publish **2026-10-07 — 50 days ago**. Next possible test: Sat **2026-11-28**.
- Measured this run, and it reframes the priorities: of the **14** Carousel days from
  2026-10-08 to 2026-11-25, **9 were authored and 5 produced nothing** (10-14, 10-28,
  11-14 to the turn cap; 11-21 and 11-25 silently) — and **three of the last four**
  Carousel days produced nothing at all. The Reel blocker costs days that were never
  publishable anyway while the token is dead; the Carousel misses cost the only days
  that could have proved the token one way or the other. On current evidence
  **raising `--max-turns` and adding the §0 skip-note requirement are now worth more
  than any §3 amendment.**

### Verified working this run

- `TZ=Asia/Seoul date` → Thu 2026-11-26 14:50 KST, `%u` = 4 (§1).
- **WebSearch works**, English and Korean, standard and extended modes.
- **WebFetch works** on `mcst.go.kr` and `koreatimes.co.kr`. **New gotcha:**
  `english.visitkorea.or.kr/svc/searchList.do` → **HTTP 404**.
- **`curl` egress works** to `mcst.go.kr` and `mafra.go.kr`, including downloading a
  21.9 MB image. Two new gotchas recorded above (curl exit 52 on one sibling image;
  MAFRA's board search returning 200 with no rows).
- **Commons is empty for this pillar**, measured rather than assumed:
  `incategory:"Bars in Seoul"` → **0** files, with and without `haslicense:`;
  `incategory:"Drinking establishments in South Korea"` → **0**. Neither category
  exists; a namespace-14 search finds no Korean bar category at all. `Category:Soju`,
  `Category:Makgeolli` and `Category:Cocktails with soju` do exist, but those are
  drink categories, i.e. 11-24's non-venue-specific case, which is format-barred.
- `scripts/cardnews.py` renders 7 clean slides; `scripts/reel.py` fails on ffmpeg
  (both above).

### Unchanged asks for a human (none actionable by this agent)

1. **Re-authorize `IG_ACCESS_TOKEN`** (CONNECT-GUIDE.md). Eight code-190 holds, last
   tested 2026-11-18, last successful publish 2026-10-07 — **50 days**. Still the
   highest-value action, and three straight attempts to even re-test it have been
   cancelled by silent misses.
2. **Raise `--max-turns`** above 60 (`daily-content.yml:80`) and **add a one-line
   "record a skip note" requirement to §0.** Promoted above the Reel blocker this
   run: three of the last four Carousel days — the only format that can ship —
   produced nothing, and two of those were invisible from this repo.
3. **Unblock Reel days** by one of six now: drop original footage/photos into
   `assets/`; obtain written venue permission; restore a blanket stock allowance for
   Reels; move venue-specific days to Carousel; extend §3 option 3 to
   non-venue-specific editorial Reels (11-24); or **extend §3 option 2 to a public
   licence from the venue's own operator, with a currency clause** (this entry —
   narrowest, and the only one that unblocks *venue-specific* Reels without weakening
   the stock prohibition). Editorial, so an unattended run will not choose. If any is
   adopted, add the matching format check to `publish.py:validate_rights()`, which
   still accepts any `asset_source` for any format.
4. **Add an ffmpeg install step** to `daily-content.yml` (needs `workflows: write`);
   without it the first Reel fails at `reel.py` even with compliant media — verified
   again today.
5. **State the 2200-character caption cap** in PIPELINE.md §4 / CONTENT.md.

---

## 2026-11-24 (Tue), reel / local — SKIPPED

Fifty-second consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. §0 checked first: `queue.json` holds 54 items
(41 `held`, 13 `published`) and none is dated 2026-11-24, so no same-day
`pending`/`published` item existed; no ramp flag is set anywhere (`grep -rn ramp`
outside this file still hits only PIPELINE.md:29 and CONTENT.md:20, i.e. the rules
themselves). §1: `TZ=Asia/Seoul date` → Tue 2026-11-24 16:27 KST, `%u` = 2 →
**reel / local food**, Collab candidate, which agrees with the prompt's format.
Stopped at §3 under §0 ("If rights ... cannot be verified, stop without adding a
queue item").

### NEW — the local-food pillar is the first one where the media is substantively fine, and *only* the format clause blocks it

Three pillars had been tested against the 11-20 CC0/CC-BY amendment and all three
failed on the media itself: 11-20 (restaurant) found the right photo under the
excluded CC BY-SA, 11-22 (cafe) found no file at all, 11-23 (restaurant) found the
right licence on a 142×72 trademark. Tuesday's pillar is different, and the
difference matters for whoever decides the fix.

Measured this run against the Commons search API for 충무김밥 / chungmu gimbap:

- `chungmu gimbap haslicense:unrestricted` → **0** files.
- `chungmu gimbap haslicense:attribution` → **1** file.
- `충무김밥`, any licence → **7** files, including the first **video** file this
  ledger has ever turned up.

The one attribution-licensed file clears every acceptance criterion the previous
three runs derived:

- `commons.wikimedia.org/wiki/File:Korea-Tongyeong_food-Chungmu_gimbap-01.jpg`
- **CC BY 3.0** — attribution only, **not** share-alike, so the 11-20 licence
  filter passes and the adaptation/SA worry from that entry does not arise;
- **2489 × 1659**, short edge 1659, comfortably over the ≥1080 minimum the 11-23
  entry asked for;
- a real **photograph**, not a logo, map or signage crop — the 11-23 criterion;
- author **Junho Jung** (Flickr `phploveme`), source
  `flickr.com/photos/phploveme/3505721145`, dated 2009-05-04.

So for the first time the binding constraint is **not** the licence, the
resolution, or logo-vs-photograph. It is the Carousel-only clause in §3 option 3.

**One honest correction to that, found by WebFetching the file page rather than
trusting the filename.** The file's own *description* reads only "View of Tongyeong,
South Gyeongsang province, South Korea" (Korean: 대한민국 경상남도 통영시 풍경). It
names neither a venue **nor the dish** — "Chungmu gimbap" appears only in the
filename and the category tags. So this file would also fail the 11-20 amendment as
written, whose test is that *the file's own description identifies the named venue*.
That is a **fourth** distinct failure mode, and it suggests the amendment's test
should read "the file's description, filename or categories," because Commons
descriptions are routinely this thin.

But the amendment is the wrong lever for this pillar anyway, which is the actual
finding:

> A dish-focused local-food post does not need a file that names a venue. It needs a
> file that is honestly **not** venue-specific — and this one is exactly that. It
> depicts chungmu gimbap in Tongyeong and claims nothing about any particular shop.

That is textbook §3 **option 3** material: correctly licensed stock for a
non-venue-specific editorial piece, with no risk of the thing §3 actually forbids
(passing a mood photo off as the named place). It is blocked solely because option 3
ends in the word "Carousel" and Tuesday is a Reel. This is the case the 2026-09-15
entry predicted in the abstract — "even a dish-focused editorial angle cannot use
stock, because §3 option 3 permits stock only for a Carousel" — now confirmed
against a specific, verified, fully compliant file.

**So the cheapest fix for Tue/local is narrower than the 11-20 amendment and needs
no new acceptance criteria:**

> Extend §3 option 3 (and CONTENT.md's matching sentence) from "a non-venue-specific
> editorial **Carousel**" to "a non-venue-specific editorial **Carousel or Reel**",
> keeping `asset_source: licensed_stock`, keeping the "never presented as the actual
> venue" prohibition, and requiring author, licence and file URL in `rights_note`
> and on the sources slide.

This unblocks the dish-and-custom half of the Reel schedule (Tue/local, and
editorial angles on other days) without any new photography, any partner
negotiation, or any blanket stock allowance for venue-specific Reels — which should
stay blocked, because that is the prohibition with teeth. Still editorial, so an
unattended run will not make it.

The video file is **not** a usable escape hatch, for the record:
`File:(윰댕) 충무김밥 + 깍두기 꿀조합♥ 먹방♥.webm`, CC BY 3.0, is **640 × 360** — below
even 720p, let alone 1080×1920 — and it is a third-party YouTube mukbang, not
documentary footage of the dish or a venue. It fails the resolution criterion by a
wide margin. Worth noting only because the repo still contains no video at all and
this is the first candidate ever identified.

### §2 research recorded (dish level clears; venue level does not)

Subject **chungmu gimbap (충무김밥)** — new for this pillar. Prior local subjects are
cheongildip, yonggeumok, naeho naengmyeon, gugil ttarogukbap, geuyetnal chodang
sundubu, samdae gwangyang, imun seolnongtang, hankook jib and dongnae halmae
pajeon, plus the nationwide editorial Carousels, so there is no dedup conflict.

- **Carried by an official listing.** `english.visitkorea.or.kr` (VisitKorea,
  `rgnContentsView.do?vcontsId=85867`) covers chungmu gimbap and names Ttungbo
  Halmae Gimbap in Tongyeong's Jungang Traditional Market as a known spot for it.
- **Dish facts that are consistent across sources** and would have been safe in
  copy: Tongyeong was formerly named **Chungmu**, and the dish takes its name from
  the old name; the rice is rolled **plain, with no fillings**, and the toppings —
  seasoned squid and radish kimchi — are served **alongside** rather than inside;
  the standard explanation of why is that fillings spoiled quickly at sea, so
  separating them kept a sailor's meal from going off. Also reported, less firmly:
  a vendor named **Eo Du-i** popularized the dish at a 1980s government festival.
- **Not verified, so it must not appear in copy.** Which shop *originated* the dish
  is **contested** — guides variously credit Ttungbo Halmae Gimbap (325
  Tongyeonghaean-ro) and Chungmu Halmae Gimbap (129-1 Jung-ang-dong). Hours
  conflict (06:00–22:00 vs 06:00–00:00). No price was confirmable at all. A
  venue-specific post would have failed §2 on top of §3; the dish-focused angle is
  what the research actually supports, which is the same angle §3's format clause
  forbids.
- As-of date **2026-11-24**. Useful English search phrase: "Chungmu gimbap Tongyeong
  Jungang Market plain rice rolls squid". Nothing above was written as if the account
  visited.

### §3, re-derived for this subject

Option 1 **original — none.** `git log --name-status -- assets/` shows the newest
media is still `assets/photos/2026-11-18-korea-coffee-price-en.jpg`, added by the
11-18 pipeline run itself (ddd3ca6); no human has added media since the policy
rewrite. A fresh `find` for `*.mp4 *.mov *.m4v *.webm *.mp3 *.wav *.m4a` across the
tree still returns **0 hits** — there is still no video or audio file in this repo.
Option 2 **written permission — unobtainable** by an unattended run; and note the
CC BY grant above is a public licence from an unaffiliated photographer, not a
partner relationship, so labelling it `partner_licensed` would misstate the rights
basis (11-20). Option 3 **licensed stock — substantively satisfied but
format-barred**, as set out above. Of **54** files in `content/`, **14** are
`policy_version: 2`, **all 14** are `licensed_stock`, **all 14** are Carousels, and
**zero** have ever carried `original` or `partner_licensed`.

Tuesday is also a Collab-candidate day, and that path is closed too: §3 says a
Collab item must keep `collab_status: requested` and must not be queued as
`pending` until the partner accepts, while §5 requires `status: pending`. An
unattended run cannot obtain an acceptance, and CONTENT.md requires original or
partner-authorized media for Collabs regardless.

### Verified working this run

- `TZ=Asia/Seoul date` → Tue 2026-11-24 16:27 KST, `%u` = 2 (§1).
- **WebSearch works** (English and mixed English/Korean queries both usable).
- **WebFetch works on `commons.wikimedia.org`** and was decisive this run — it is
  what caught that the description names only the city. The 11-23 Michelin gotcha
  was not re-tested.
- **`curl` egress to the Commons API works**, including `list=search` with
  `haslicense:` and `prop=imageinfo&iiprop=extmetadata|size|url|mime`. The `sleep 2`
  between back-to-back calls and the empty-body tolerance are both still needed.
- **`scripts/cardnews.py` renders cleanly: exit 0, 7 slides, every one 1080×1350,
  no errors** (pillow **13.0.0**, run against
  `content/2026-11-18-korea-coffee-price-en.json` into `/tmp/rendertest` outside the
  repo, so nothing was committed).
- **`scripts/reel.py` still dies on ffmpeg:** `FileNotFoundError: [Errno 2] No such
  file or directory: 'ffmpeg'`, **exit 1**. `which ffmpeg` → not found, and
  `.github/workflows/daily-content.yml:50-51` is still only
  `pip install --quiet pillow`. Renderer proven 2026-11-13; runner still not
  provisioned.
- No silent miss to report: `git log --since=2026-11-23` shows 1d9ff7e, the 11-23
  skip note, and Mon 11-23 is accounted for in the ledger.

### Unchanged asks for a human (none actionable by this agent)

1. **Re-authorize `IG_ACCESS_TOKEN`** (CONNECT-GUIDE.md). Still eight consecutive
   code-190 holds (10-10, 10-17, 10-21, 10-31, 11-04, 11-07, 11-11, 11-18), last
   tested **2026-11-18**; the next possible test is the Wed **2026-11-25** Carousel,
   i.e. tomorrow. Last successful publish **2026-10-07 — 48 days ago**. Highest
   value; not checkable by an agent.
2. **Unblock Reel days.** This run adds a fifth and cheapest option to the menu —
   extend §3 option 3 to non-venue-specific editorial **Reels** (above) — alongside:
   drop original footage/photos into `assets/`; obtain written venue permission;
   restore a blanket stock allowance for Reels; move venue-specific days to
   Carousel; or adopt the 11-20 CC0/CC-BY amendment with the 11-23 resolution and
   photograph-not-logo criteria plus the description/filename widening found today.
   Editorial, so an unattended run will not choose. If any is adopted, add the
   matching format check to `publish.py:validate_rights()`, which still accepts any
   `asset_source` for any format.
3. **Add an ffmpeg install step** to `daily-content.yml` (needs `workflows: write`);
   without it the first Reel fails at `reel.py` even with compliant media.
4. **Raise `--max-turns`** above 60 (`daily-content.yml:80`), and **state the
   2200-character caption cap** in PIPELINE.md §4 / CONTENT.md.
5. **Add a one-line "record a skip note" requirement to §0**, so a no-op day is
   visible from the repo rather than only from the Actions log (11-16 and 11-21).

---

## 2026-11-23 (Mon), reel / restaurant — SKIPPED

Fifty-first consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. §0 checked first: `queue.json` holds 54 items
and none is dated 2026-11-23, so no same-day `pending`/`published` item existed; no
ramp flag is set anywhere (`grep -rn ramp` still hits only PIPELINE.md:29 and
CONTENT.md:20, i.e. the rules themselves). §1: `TZ=Asia/Seoul date` → Mon 2026-11-23
13:34 KST, `%u` = 1 → **reel / restaurant**, Collab optional, which agrees with the
prompt's format. Stopped at §3 under §0 ("If rights ... cannot be verified, stop
without adding a queue item").

### NEW — the first numeric measure of the free-licence pool, and it bounds the 11-20 amendment

The 2026-11-20 entry proposed amending §3 to allow CC0/CC BY third-party media whose
description names the venue, and called it the fix that "unblocks all five Reel
days." 2026-11-22 narrowed that to "necessary but not sufficient" from one cafe
subject. This run measured the pool itself rather than one venue, for Monday's
restaurant pillar, straight against the Commons search API:

- `incategory:"Restaurants in Seoul" haslicense:unrestricted` → **8 files total**.
- `incategory:"Restaurants in Seoul" haslicense:attribution` → **12 files total**.

**Twenty freely-licensed files for the whole Seoul-restaurants category**, and the
contents are worse than the count suggests. Four are an unnamed 2007 set (`August
2007, restaurant in Seoul`, …`2`, …`3`, plus one of its toilets); three more are
unnamed Insadong storefronts (`Seoul-Insadong-Restaurant-01`,
`…-A restaurant entrance-01`, `…-Gruel shop-01`); the clearly identifiable ones are
chains or novelties — `Mcdonalds seoul.JPG`, `McDonald's Delivery Fleet.jpg`,
`Bored & Hungry exterior.jpg`, `Boeing 747 Restaurant Outside.jpg`. An unnamed
storefront is exactly the "mood photo standing in for the named place" that §3
forbids outright, so the amendment would not reach it: the amendment's own test is
that *the file's description identifies the venue*. The named, non-chain residue of
the entire category is roughly two files. That is the ceiling on what the licence
change can deliver for one pillar in one city, and it should be stated plainly to
whoever decides.

### NEW — the restaurant pillar fails the amendment on a *third* distinct ground

Subject chosen for §2 was **우래옥 / Woo Lae Oak**, Jung-gu — the oldest active
Pyongyang-naengmyeon house in Seoul, a Michelin Bib Gourmand listing, open since
1946. Commons holds **exactly one** file for it, and it is instructive:

- `File:우래옥(又來屋).png` — **CC BY 4.0** (`LicenseShortName: CC BY 4.0`,
  `LicenseUrl creativecommons.org/licenses/by/4.0`, `AttributionRequired: true`),
  `Artist: 우래옥`, `Credit: 우래옥 상표`, `DateTimeOriginal: 1969-07-05`. The licence
  is exactly the one the 11-20 amendment asks for, and the description names the
  venue.
- It is **142 × 72 pixels**, and it is a **trademark** — the restaurant's wordmark,
  not a photograph of the restaurant. It cannot fill a 1080×1920 Reel frame (it is
  13% of the frame's width), and a brand mark is not a depiction of the venue in the
  sense §3 means. There is also no evidence the Commons uploader held the rights to
  release a company's trademark, and a CC licence over a mark does not clear
  trademark use in the first place.

Three pillars have now been tested against the proposed amendment and all three
fail, each for a different reason, which is why this is worth recording rather than
repeating:

| Run | Pillar | Venue | Why the amendment would not have helped |
|---|---|---|---|
| 11-20 | restaurant | 안동장 | A real venue-named photo exists, but **CC BY-SA** — the licence 11-20 itself excludes |
| 11-22 | cafe | NUDAKE | **Zero files**; the non-SA fallbacks were 1024×768 or "Now closed" |
| 11-23 | restaurant | 우래옥 | Right licence, names the venue — but a **142×72 trademark**, not a photo |

So the honest recommendation to a human is now narrower still: if the amendment is
adopted, it needs **two acceptance criteria beyond the licence** — a minimum source
resolution (≥1080 on the short edge for a 1080×1920 Reel) and "a photograph of the
place, not a logo, map, menu scan or signage crop." Licence alone has not been the
binding constraint in two of the three tests.

### §2 research recorded (partial clear — see the caveat)

Done to PIPELINE.md §2 standard so the work is not lost. Subject **Woo Lae Oak
(우래옥)**, which is new: the restaurant pillar's prior subjects are onjium (×2),
mingles, le dorer (×2), balwoo gongyang, gogung jeonju, giwakang, yong fu jeju,
gosari express and sosuheon, so there is no dedup conflict.

- **Name and address**, consistent across every source: 우래옥 / Woo Lae Oak,
  **62-29 Changgyeonggung-ro, Jung-gu, Seoul 04546**, about one minute from Euljiro
  4-ga station (Lines 2/5). Phone +82 2-2265-0151.
- **Current operation**: carried by the **Michelin Guide Seoul** listing (Bib
  Gourmand) and by Korean listing/press coverage dated 2026. Opened **1946**;
  Wikipedia records a Pyongyang predecessor, 명월관.
- **Closed Mondays** — agreed by Michelin and the Korean listings, and worth noting
  because Monday is this account's restaurant-Reel slot. A Monday post telling
  travelers to go today would have been wrong on the one fact that matters most.
- **Not verified, so it must not appear in copy.** Hours conflict three ways
  (11:30–21:00 Michelin / 11:20–21:00 a 2026 Korean listing / 11:30–21:30 a 2022
  Seoul city media piece), and the naengmyeon price conflicts between **18,000 won**
  and **16,000 won** in sources of similar date. Reservation policy ("4+ guests, one
  week ahead" vs "two weeks ahead") is equally unsettled.
- **Caveat on the source quality, stated plainly:** `guide.michelin.com` is **not
  fetchable from this runner** — plain `curl` gets **HTTP 202** (bot challenge) and
  **WebFetch returns an empty body** on both the `/en/` and `/kr/ko/` paths. So the
  Michelin facts above come from search-result summaries, not from the page itself,
  and no official Seoul/VisitKorea tourism listing for this venue surfaced at all.
  Had §3 not stopped the run first, this would have needed one more pass on a
  fetchable official or booking source before anything shipped. **New gotcha for
  later runs: WebFetch "works" is not a global property — it works on
  visitseoul/visitgangnam/commons and fails closed, with an empty body rather than
  an error, on Michelin.** An empty body is easy to mistake for a page that says
  nothing.
- As-of date **2026-11-23**. Useful English search phrase: "Woo Lae Oak Euljiro
  Pyongyang naengmyeon Seoul". Nothing above was written as if the account visited.

### §3, re-derived for this subject

Option 1 **original — none.** `git log --name-status -- assets/` shows the newest
media is still `2026-11-18-korea-coffee-price-en.jpg`, added by the 11-18 pipeline
run itself; no human has added media since the policy rewrite. A fresh `find` for
`*.mp4 *.mov *.m4v *.webm *.mp3 *.wav *.m4a` across the tree still returns **0
hits** — there is no video or audio file in this repo. Option 2 **written permission
— unobtainable** by an unattended run. Option 3 **licensed stock — forbidden here**:
§3 confines it to a non-venue-specific editorial Carousel and CONTENT.md says it
"must never be presented as the actual venue." Today is a Reel and the constraint
binds on format, so no re-angling rescues it. Of **54** files in `content/`, **14**
are `policy_version: 2`, **all 14** are `licensed_stock`, **all 14** are Carousels,
and **zero** have ever carried `original` or `partner_licensed`.

### Verified working this run

- `TZ=Asia/Seoul date` → Mon 2026-11-23 13:34 KST, `%u` = 1 (§1).
- **WebSearch works** (English and Korean queries both returned usable results).
- **WebFetch is partial** — see the Michelin finding above.
- **`curl` egress to the Commons API works**, including `list=search` with
  `haslicense:` and `prop=imageinfo&iiprop=extmetadata|size|sha1`. The 11-22 gotcha
  reproduced: a `sleep 2` between back-to-back calls is still needed, and the parse
  must tolerate an empty body.
- **`scripts/cardnews.py` renders cleanly: exit 0, 7 slides, every one 1080×1350,
  no errors** (pillow **13.0.0**, run against
  `content/2026-11-18-korea-coffee-price-en.json` into `/tmp` outside the repo, so
  nothing was committed).
- **`scripts/reel.py` still dies on ffmpeg:** `FileNotFoundError: [Errno 2] No such
  file or directory: 'ffmpeg'`, **exit 1**. `which ffmpeg` → not found, and
  `.github/workflows/daily-content.yml:50-51` is still only
  `pip install --quiet pillow`. Renderer proven 2026-11-13; runner still not
  provisioned.
- No silent miss to report for the last cycle: `git log --since=2026-11-21` returns
  44c7a6a, the 11-22 skip note, and Sun 11-22 was a Reel day with no shippable
  format, so nothing is missing from the ledger between then and now.

### Unchanged asks for a human (none actionable by this agent)

1. **Re-authorize `IG_ACCESS_TOKEN`** (CONNECT-GUIDE.md). Still eight consecutive
   code-190 holds (10-10, 10-17, 10-21, 10-31, 11-04, 11-07, 11-11, 11-18), last
   tested **2026-11-18**, next possible test the Wed **2026-11-25** Carousel. Last
   successful publish **2026-10-07 — 47 days ago**. Highest value; not checkable by
   an agent.
2. **Unblock Reel days**, and note this run narrows the menu: drop original
   footage/photos into `assets/`; obtain written venue permission; restore a stock
   allowance for Reels; move venue-specific days to Carousel; and/or adopt the
   CC0/CC-BY amendment — which, on three pillar tests, needs the resolution and
   photograph-not-logo criteria above and still only reaches a handful of files.
   Editorial, so an unattended run will not choose. If adopted, add the matching
   format check to `publish.py:validate_rights()`, which still accepts any
   `asset_source` for any format.
3. **Add an ffmpeg install step** to `daily-content.yml` (needs `workflows: write`);
   without it the first Reel fails at `reel.py:45` even with compliant media.
4. **Raise `--max-turns`** above 60 (`daily-content.yml:80`), and **state the
   2200-character caption cap** in PIPELINE.md §4 / CONTENT.md.
5. **Add a one-line "record a skip note" requirement to §0**, so a no-op day is
   visible from the repo rather than only from the Actions log (11-16 and 11-21).

---

## 2026-11-22 (Sun), reel / cafe — SKIPPED

Fiftieth consecutive Reel-day skip. No content JSON, no rendered output committed,
no change to `queue.json`. §0 checked first: `queue.json` holds 54 items and none is
dated 2026-11-22, so no same-day `pending`/`published` item existed; no ramp flag is
set anywhere (`grep -rn ramp` hits only PIPELINE.md:29 and CONTENT.md:20, i.e. the
rules themselves). §1: `TZ=Asia/Seoul date` → Sun 2026-11-22 12:54 KST, `%u` = 7 →
**reel / cafe**, Collab optional, which agrees with the prompt's format. Stopped at
§3 under §0 ("If rights ... cannot be verified, stop without adding a queue item").

### NEW AND IMPORTANT — Sat 2026-11-21 is a second silent miss, and it cost the token test

The 2026-11-19 and 2026-11-20 entries both named Sat **2026-11-21** (Carousel /
local — the one format that can still ship) as the next real test of
`IG_ACCESS_TOKEN`. **That run produced nothing at all.** Measured this run:

- `git log --since=2026-11-20` returns exactly one commit, 0470820 (the 11-20 skip
  note). There is no 11-21 commit of any kind.
- `content/` has no `2026-11-21-*` file; `out/` has no 11-21 directory; `queue.json`
  is unchanged at 54 items, newest `2026-11-18-korea-coffee-price-en`.
- No skip note was written either.

So 11-21 is the **second known silent miss** after Mon 2026-11-16, and the first to
fall on a *shippable* day. Consequences, all of which change the state the previous
two entries recorded:

- **The token is still last-tested 2026-11-18**, not 11-21. The count stands at
  **eight** consecutive code-190 holds (10-10, 10-17, 10-21, 10-31, 11-04, 11-07,
  11-11, 11-18), not nine. The next possible test is the Wed **2026-11-25**
  Carousel.
- **Last successful publish is 2026-10-07 — 46 days ago** as of today.
- A Carousel day was lost to something other than the three known publish faults.
  Whether it was the turn cap (`--max-turns 60`, still unraised at
  `.github/workflows/daily-content.yml:80`), a scheduling miss, or a run that went
  green while committing nothing (the 11-16 failure mode) is **not determinable from
  this repo** — only from the Actions log. That is exactly the gap flagged on
  2026-11-17: §0 carries no skip-note requirement, so a no-op day leaves no trace
  here. Two silent misses in seven days moves ask 5 below up the list.

### §2 passed this run — today's failure is purely §3

Research was carried out to PIPELINE.md §2 standard so the work is not lost, and
unlike most entries in this ledger the verification actually cleared. Subject:
**NUDAKE (누데이크), Haus Dosan** — a dessert-led cafe, which fits Sunday's
cafe/dessert pillar.

- Official name and address, from the **Seoul city tourism listing** (official):
  Gentle Monster Haus Dosan, **50 Apgujeong-ro 46-gil, Gangnam-gu, Seoul 06020**,
  with "Nudake Café on B1". Hours **daily 11:00–21:00**, phone 1660-1010, nearest
  station **Apgujeong Rodeo (Suin-Bundang Line) Exit 5, 690 m**. The page was
  published 2023-06-28 and carries an **Edited Date of 2026-08-08**, so current
  operation is confirmed from an official listing within the last four months.
  `english.visitseoul.net/shopping/GentleMonsterHausDosan/ENPozt8oi`
- Corroborated by the **Gangnam district tourism listing** (official), which adds
  the one fact a traveler needs and the city page omits: the cafe is **"closed the
  first Monday of each month."** It names the signature item as the **Peak Cake**
  (matcha cream inside a squid-ink pastry shell) and places Nudake on B1 of House
  Dosan. Phone 070-4128-2125.
  `visitgangnam.net/en/places/nudake-haus-dosan-sweetness-between-art-and-gourmet`
- **Not verified, so it must not appear in copy:** the Peak Cake price (neither
  official listing gives one), and the 070 phone number, which the two Gangnam
  listings give inconsistently (…2125 vs …2126). A third-party aggregator pass on
  Fritz Coffee (Dohwa) was also run first and **discarded**: its hours conflicted
  three ways across trip.com/timeout/tablejourney with no official listing behind
  any of them, which is a §2 failure in its own right. Recorded so the next cafe run
  does not repeat it.
- As-of date **2026-11-22**. Useful English search phrase for travelers:
  "Nudake Haus Dosan Apgujeong dessert cafe". Nothing above was written as if the
  account visited.

As-of this entry the cafe pillar's published subjects are anthracite (×2),
hanyakbang, terarosa (×2), momos, onion anguk, hakrim dabang, suyeonsanbang,
sungsimdang, mido dabang plus six editorial Carousels; Nudake is new, so there is no
dedup conflict.

### NEW — the 2026-11-20 "fourth option" would NOT have unblocked today

This is the substantive correction this run adds. The 2026-11-20 entry proposed
amending §3 to permit third-party media under an irrevocable public licence (CC0 or
CC BY, **not** CC BY-SA) where the file's own description names the venue, and
presented it as the cheap fix that "unblocks all five Reel days." Measured against
an actual cafe-pillar subject, it is **necessary but not sufficient**:

- **For Nudake there is no freely-licensed photo at all.** Commons search returns
  **0 hits** for `Nudake`, **0** for `누데이크`, and **0 relevant** for `Haus Dosan`
  (the three hits are unrelated German-language PDFs). An amended §3 grants nothing
  where no file exists.
- **The venue-named Korean cafe photos that do exist are all the excluded licence.**
  `File:Hakrim Dabang 01.jpg` and `02.jpg` (author **Seefooddiet**, own work,
  2025-01-10, 3024×4032 and 4032×3024) and `File:Sungsimdang 2019.jpg` +
  `File:Sungsimdang display stand.jpg` (author **Trainholic**, own work, 2019-06-08)
  are **all CC BY-SA 4.0** — precisely the licence 11-20 ruled out, and note that
  Hakrim Dabang and Sungsimdang are both already published subjects here.
- **The non-SA, venue-named pool is effectively empty.** A `haslicense:
  attribution-only|unrestricted` sweep surfaced exactly two usable-looking
  candidates, and both fail for non-licence reasons:
  `File:Cafe Pascucci, Apgujeong-dong, Seoul, South Korea.jpg` is **Public domain**
  but is a 2006 chain-franchise photo at **1024×768** — below the 1080×1920 Reel
  frame, so it cannot fill it; and `File:Cafe Seoul 20190324 131853.jpg` is **CC0**
  but its own description ends "**Now closed**", which is a §2 current-operation
  failure before §3 is even reached.

So the honest version of the 11-20 recommendation is narrower: **CC0/CC BY coverage
of named Korean cafes is too thin to carry a venue pillar on its own.** Adopting the
fourth option is still worth doing — it is free and it would unblock the occasional
day where a good file happens to exist — but for the cafe pillar it has to be paired
with option 1 (owner photography) or option 2 (written venue permission), or the
venue days have to move to Carousel. Whoever makes the call should not expect the
licence amendment alone to produce five Reel days a week.

§3 as it stands today, re-derived for this subject: option 1 **original — none**
(`git log --name-status -- assets/` shows the newest photo is
`2026-11-18-korea-coffee-price-en.jpg`, added by the 11-18 pipeline run; no human
has added media since the policy rewrite). Option 2 **written permission —
unobtainable** by an unattended run. Option 3 **licensed stock — forbidden here**,
being limited to a non-venue-specific editorial Carousel; today is a Reel, and the
constraint binds on format, so no re-angling rescues it. Re-measured: of **54**
files in `content/`, **14** are `policy_version: 2`, **all 14** are
`licensed_stock`, **all 14** are Carousels, and **zero** have ever carried
`original` or `partner_licensed`. There is still **no video or audio file anywhere in
the tree** (`find` for `*.mp4 *.mov *.m4v *.webm *.mp3 *.wav *.m4a` → 0 hits).

### Verified working this run

- `TZ=Asia/Seoul date` → Sun 2026-11-22 12:54 KST, `%u` = 7 (§1).
- **WebSearch works.** **WebFetch works** on `english.visitseoul.net` and
  `visitgangnam.net` (both returned full structured listings).
- Plain `curl` egress to the **Commons API works** (`list=search`,
  `prop=imageinfo&iiprop=extmetadata` both returned licence metadata). **New gotcha:**
  called back-to-back in a shell loop it intermittently returns an **empty body**,
  which crashes a naive `json.load`. Put a `sleep 2` between calls and parse
  defensively — three of ten probes failed this way before the sleep was added.
- **`scripts/cardnews.py` renders cleanly: exit 0, 7 slides at 1080×1350, no
  errors** (pillow **13.0.0**, run against `content/2026-11-18-korea-coffee-price-en.json`
  into a scratch directory outside the repo, so nothing was committed).
- **`scripts/reel.py` fails exactly as predicted:** `FileNotFoundError: [Errno 2] No
  such file or directory: 'ffmpeg'` at `scripts/reel.py:45`, **exit 1**. This is the
  first time the stock-runner failure has been reproduced by running it rather than
  inferred from `which ffmpeg`. The 2026-11-15 correction stands:
  `.github/workflows/daily-content.yml:51` is still only `pip install --quiet pillow`,
  so the renderer is proven (2026-11-13) but **the runner is not provisioned** and the
  first Reel would die here even with compliant media in hand.

### Unchanged asks for a human (none actionable by this agent)

1. **Re-authorize `IG_ACCESS_TOKEN`** (CONNECT-GUIDE.md) — eight lost posts, **46
   days** without a publish. Still highest value. Not checkable by an agent; the
   token is a repository secret. Next possible test: Wed **2026-11-25**.
2. **Unblock Reel days.** Now four options, and per the measurement above the
   licence amendment is the cheapest but not self-sufficient: drop original
   footage/photos into `assets/`; get written venue permission; restore a stock
   allowance for Reels; move venue-specific days to Carousel; and/or adopt the
   CC0/CC-BY amendment as a supplement. Editorial, so an unattended run will not
   choose. If the amendment is adopted, also add the matching format check to
   `publish.py:validate_rights()`, which still accepts any `asset_source` for any
   format.
3. **Add an ffmpeg install step** to `daily-content.yml` (needs `workflows: write`),
   without which the first Reel fails at `reel.py:45` even with media.
4. **Raise `--max-turns`** above 60 (`daily-content.yml:80`), and **state the
   2200-character caption cap** in PIPELINE.md §4 / CONTENT.md.
5. **Add a one-line "record a skip note" requirement to §0.** Promoted this run:
   with 11-16 and now **11-21** both invisible from the repo, a no-op day is
   detectable only from the Actions log, and 11-21 silently cancelled the token test
   two entries had been waiting on.

---

## 2026-11-20 (Fri), reel / restaurant — SKIPPED

Forty-ninth consecutive Reel-day skip. No content JSON, no rendered output, no
change to `queue.json`. §0 checked first: `queue.json` holds 54 items and none is
dated 2026-11-20, so no same-day `pending`/`published` item existed. §1: `date +%u`
→ 5 → reel / restaurant / Collab candidate, which agrees with the prompt's format.
Stopped at §3 under §0 ("If rights ... cannot be verified, stop without adding a
queue item").

**NEW — the blocker is the format rule, not media scarcity, and that is now backed
by a verified example rather than asserted.** Every entry from 2026-09-14 onward
says "no compliant media exists." That is true only of *this repo*. Measured this
run: venue-accurate, commercially-reusable, third-party-licensed media of a
qualifying Friday restaurant exists publicly and is verifiable in a single WebFetch.

- `commons.wikimedia.org/wiki/File:Andongjang.jpg` — author **Seefooddiet**, own
  work, dated 2024-07-16, released under **CC BY-SA 4.0**, and the file's own
  description identifies it as 안동장 (安東莊), "a historic chinese restaurant in
  Seoul, South Korea."
- The venue checks out as a §2 subject: 서울 중구 을지로 124, near Euljiro 3-ga
  station, opened **1948**, third generation, and widely credited as the origin of
  굴짬뽕 (oyster jjamppong) — confirmed across siksinhot.com and polle.com listings.
  (Current hours were *not* confirmable from an official listing, which would have
  been its own §2 failure, but §3 decided it first.)

**Why that still does not clear §3, and why the run skipped anyway.** The honest
`asset_source` label for a photo taken by an unaffiliated Commons photographer is
`licensed_stock`: `original` is false, and `partner_licensed` would misstate the
rights basis because there is no partner — not the venue, not the photographer.
CONTENT.md limits `licensed_stock` to "an occasional editorial Carousel" and says it
"must never be presented as the actual venue"; §3 option 3 says the same. §3 option
2 ("venue/creator media with written permission") *could* be read to cover a
standing public CC grant from the media's creator, and that reading would let a Reel
ship today — but it only works by relabelling the single metadata field that exists
to record the rights basis. That defeats the gate instead of passing it, so an
unattended run will not take it. Widening the policy stays a human decision.

Second, narrower point for whoever makes that decision: **CC BY-SA is the wrong
licence to start with.** Share-alike plausibly makes a Reel built from the photo an
adaptation, which would put the post itself under SA. CC0 and CC BY files carry no
such term and Commons holds plenty of both, so this is a filter criterion, not an
obstacle.

**A fourth human fix, cheaper than the three in the 2026-09-15 entry.** Those three
(ship original photos, restore a blanket stock allowance, or move venue days to
Carousel) all assume media must be created, negotiated, or given up on. This one
does not:

> Amend §3 to permit third-party media under an irrevocable public licence (CC0 or
> CC BY — **not** CC BY-SA) on any format, *only* where the file's own description
> identifies the named venue; keep `asset_source: licensed_stock`; and require the
> author, licence and file URL in `rights_note` and on the sources slide.

That leaves both of §3's actual prohibitions intact — nothing is scraped from venue
social media, and no mood photo is passed off as the named place — while unblocking
all five Reel days (Mon/Tue/Thu/Fri/Sun) without the owner photographing anything.
If it is adopted, also add the matching format check to
`publish.py:validate_rights()`, which today accepts any of the three
`asset_source` values regardless of format (noted 2026-09-15 and still true).

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-11-20 Friday → §1 reel / restaurant.
- WebSearch works. WebFetch works on commons.wikimedia.org. Plain `curl` egress
  works (Commons API query returned the `Restaurants in Seoul` category listing).
- `scripts/cardnews.py` renders **7 slides at 1080×1350, exit 0, no errors**
  (re-run this session against `content/2026-11-18-korea-coffee-price-en.json`;
  pillow 13.0.0).

### Still standing, unchanged by this run

- **Token, top priority.** Eight straight code-190 holds; last tested 2026-11-18.
  Next real test is the Sat **2026-11-21** Carousel. Not checkable by an agent.
- **ffmpeg still not provisioned.** `which ffmpeg` → not found, and
  `.github/workflows/daily-content.yml` line 50 is still only `pillow 설치`. The
  renderer itself is proven (2026-11-13); the runner is not. Not re-tested here
  because the §3 gate stopped the run before any Reel needed building.
- `--max-turns 60` unraised; this lean skip run cleared it comfortably.
- §0 still carries no skip-note requirement, so a silent miss like 2026-11-16
  remains invisible from the repo alone.

---

## 2026-11-19 (Thu), reel / bar — SKIPPED

Forty-eighth consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged and still
decisive. Every number below was measured this run, not inherited from the
2026-11-17 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Thu 2026-11-19 13:54 KST, `%u` = 4 → **reel / bar**,
  Collab optional. No ramp flag exists in `queue.json` or any repo note (grepped
  this run: "ramp" appears only in PIPELINE.md:29 and CONTENT.md:20, i.e. the rules
  themselves, never as a set flag).
- §0: no `pending` or `published` queue item for 2026-11-19. Clear to proceed.
- §3 option 1 — **owner-supplied original: none.** `git log --name-status --
  assets/photos/` shows every one of the 14 photos added since the policy rewrite
  (8128750, 2026-09-14) was added by a pipeline run and is Carousel stock. The last
  human-added photo, `cheongildip-en.jpg` (392aefd), predates the policy.
- §3 option 2 — **written venue permission: unobtainable** by an unattended run.
- §3 option 3 — **licensed stock: available and legal, but forbidden here.** Stock
  is permitted only for a non-venue-specific editorial *Carousel*. Today is a Reel,
  so the exemption does not apply. The constraint binds on **format**, so no
  editorial re-angling rescues the day.

Stopped under §0: "If rights ... cannot be verified, stop without adding a queue
item." Re-measured this run and worth stating precisely, because it is the whole
blocker in one line: of the **54** files in `content/`, **14** carry
`policy_version: 2`, **all 14** of those carry `asset_source: licensed_stock`, and
**zero** have ever carried `original` or `partner_licensed`. The §3 gate has never
been cleared in the history of this repo.

**New measurement this run — there is no video or audio file in the repo at all.**
Previous entries established that no compliant *photo* exists. A `find` across the
whole tree for `*.mp4 *.mov *.m4v *.webm *.mp3 *.wav` returns **zero** hits. So the
Reel gap is not "a stock photo we may not use" — it is the total absence of moving
footage, and `assets/music/` is gitignored to `tracks.json` + `README.md`, i.e. the
registered tracks have no files either. A human dropping in photos alone still
leaves `reel.py` synthesizing its audio, as documented on 2026-09-15.

### Renderer: Carousel path verified again; Reel path would fail on this runner

- `python3 scripts/cardnews.py content/2026-11-18-korea-coffee-price-en.json
  <scratch>` → exit 0, **7 slides at 1080×1350**, no errors. Rendered to a scratch
  directory outside the repo, so nothing was committed. pillow 13.0.0.
- **`ffmpeg` and `ffprobe` are both ABSENT** on this runner, re-confirmed this run
  (`which` → nothing). `.github/workflows/daily-content.yml:50-51` is still only
  `pillow 설치` / `pip install --quiet pillow`. The 2026-11-15 correction stands
  unchanged: the Reel renderer is proven (2026-11-13, a real 1080×1920 / h264 /
  22.2s MP4), but **the runner is not provisioned for it**, so §4's two-step would
  die at `scripts/reel.py` today even if media appeared. The one-line workflow fix
  in the 2026-09-15 entry is still unapplied and still needs `workflows: write`,
  which this agent does not have.

### Publish side: the token blocker claimed an eighth item, 2026-11-18

The 2026-11-17 entry named Wed 2026-11-18 as "the next real test" of the token. It
ran, and it failed the same way. `2026-11-18-korea-coffee-price-en` was authored,
rendered and queued `pending` (ddd3ca6), the 19:00 KST publisher picked it up, and
it was **held** at **2026-11-19T03:45:36 KST** with `hold_reason:
publish_failed_manual_review` and OAuthException **code 190**, "session has been
invalidated" (`fbtrace_id AZnGr_CckiGBGmxpU5BmWy1`, commit 155b9f4).

- That is the **eighth consecutive code-190 hold**: 10-10, 10-17, 10-21, 10-31,
  11-04, 11-07, 11-11, 11-18. (10-24 sits inside that run of dates but was the
  caption-cap fault, not the token.)
- **Last successful publish is 2026-10-07 — 43 days ago** as of today. Eight
  finished, correct posts have been thrown away by this credential, nine in total
  since 10-10 counting the 10-24 caption-cap loss.
- `--max-turns 60` did **not** bite on 11-18: the run produced a complete item.
- Re-authorizing `IG_ACCESS_TOKEN` through Instagram Login (CONNECT-GUIDE.md)
  remains the **top-priority human action**. An agent cannot do it; the token is a
  repository secret. Note this is publish-side and does not affect today's
  decision, which is a §3 skip regardless.
- Minor, introduced by that commit: `queue.json` now ends **without a trailing
  newline** (155b9f4 shows `\ No newline at end of file`). Harmless to the parser,
  but it will show as noise in the next queue diff.

### Verified working this run

- `TZ=Asia/Seoul date` → Thu 2026-11-19, `%u` = 4 (§1).
- `WebSearch` works.
- `WebFetch` works, **with a new gotcha worth recording**: `theworlds50best.com`
  now **301-redirects to `the50.com`**, and WebFetch does not follow cross-host
  redirects — it returns the target for a second call. The redirected story page
  fetched fine; `the50.com/bars/best-in-asia/list/1-10` returns **404**, so the
  list-path URLs under the old host no longer resolve on the new one. Use the
  `/stories/News/...` pages, and expect one extra call per 50 Best URL.
- `scripts/cardnews.py` renders 7 slides cleanly (above). `scripts/reel.py` not
  exercised: no ffmpeg, and no media to feed it.

### Research done anyway — a ready bar candidate for whoever shoots first

Thursday is the bar pillar, so §2 research was carried out even though §3 closes
the day. It is recorded here so the work is not lost. **Asia's 50 Best Bars 2026**
was announced 2026-07-28 in Macau; Hope & Sesame (Guangzhou) took No. 1. **Seoul
placed four bars**: **Zest No. 2** (also The Best Bar in Korea, third straight
year), **Alice No. 13**, **Bar Cham No. 33**, **MMS No. 42**. Sources: Korea Times
2026-07-29 (`koreatimes.co.kr/lifestyle/travel-food/20260729/seoul-claims-4-spots-on-asias-50-best-bars-2026-zest-retains-no-2-ranking`),
Herald Corp (`biz.heraldcorp.com/article/10827855`) for the ranks 13/33/42, and the
official Destination Awards page for Best Bar in Korea. As-of date **2026-11-19**;
hours and addresses were **not** verified to §2 standard because the day cannot
ship — do that before use.

Two things follow for a human:

- All four already exist in this repo — `zest-seoul-en` (published 2026-08-25),
  `alice-cheongdam-en`, `bar-cham-en`, `mms-bar-en` (all `held`) — and all four
  photos are pipeline-fetched stock. So the obvious Reel is blocked not for lack of
  a subject but for lack of one authorized frame of any of them.
- The ranking angle would make a strong **non-venue-specific editorial Carousel**
  ("Seoul's four bars on Asia's 50 Best 2026, and what the list actually measures"),
  which §3 option 3 *does* permit. It does not fit Sat 2026-11-21 (local /
  neighborhood) but would fit a Wed cafe-or-bar slot or a human-chosen editorial
  day. Flagged, not queued: changing the weekly slot table is an editorial decision
  and §0 forbids an unattended run from inventing one.

### Unchanged asks for a human (none actionable by this agent)

1. **Re-authorize `IG_ACCESS_TOKEN`** — eight lost posts, 43 days without a
   publish. Highest value.
2. **Unblock Reel days** by one of: dropping original footage/photos into
   `assets/`; restoring a stock allowance for Reels in §3; or moving venue-specific
   days to Carousel. Editorial, so an unattended run will not choose.
3. **Add the ffmpeg install step** to `daily-content.yml` (needs `workflows:
   write`), without which the first Reel fails even with media.
4. **Raise `--max-turns`** above 60, and **state the 2200-character caption cap**
   in PIPELINE.md §4 / CONTENT.md.
5. **Add a one-line "record a skip note" requirement to §0** so a no-op day is
   detectable from the repo rather than only from the Actions log (2026-11-17).

---
## 2026-11-17 (Tue), reel / local — SKIPPED

Forty-seventh consecutive Reel-day skip, and the first entry that has to cover
**two** days: Mon **2026-11-16** was also a Reel day, it ran, it succeeded, and it
left **nothing behind** — no content JSON, no queue change and no skip note (see
below). So the 46th skip is recorded here retroactively and today's is the 47th.
No content JSON, no rendered output committed, no change to `queue.json` this run
either. The §3 media blocker is unchanged. Every number below was measured this
run, not inherited from the 2026-11-15 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Tue 2026-11-17 14:35 KST, `%u` = 2 → **reel / local
  food**, Collab *candidate*. The task prompt independently specified `reel`; the
  two agree.
- §0: **no `pending` or `published` item for 2026-11-17.** `queue.json` holds **53**
  entries (**13** `published`, **40** `held`, **0** `pending`) — unchanged from
  11-15, because nothing has been written since. Grepping the whole serialised
  queue for `2026-11-17` returns **zero** hits, so neither a slug nor a
  `publish_at` claims today, and `content/` has no `2026-11-17-*` file. Still **no
  ramp flag**: the union of all keys across all 53 entries is exactly `error,
  format, held_at, hold_reason, media_id, pillar, publish_at, published_at, slug,
  status`, and the only "ramp" matches in the repo remain the prose at
  CONTENT.md:20 and PIPELINE.md:29 that *describe* the flag §1 says to respect.
- §3 option 1 (owner original): **empty.** Resolved every `assets/photos/`
  reference across all **53** `content/*.json`: **54** on disk, **54** referenced,
  **zero unreferenced** — so not one frame on disk is an unclaimed owner photo.
  (This is a small correction to the 11-15 entry, which reported 53 referenced and
  called `2026-09-16-korea-cup-rules-en.jpg` unreferenced. It *is* referenced —
  by `2026-09-16-korea-cup-rules-en.json`, which uses the `-cover` variant as its
  cover `bg_image` and the plain file elsewhere. The conclusion is unchanged and
  in fact slightly stronger.) `git ls-files` filtered for
  `mp4|mov|m4v|avi|webm|mkv|mp3|wav|m4a|heic|raw|dng|tiff|cr2|arw` returns **zero**
  files, so there is no owner footage for a Reel either, and
  `git status --untracked-files=all` is **clean** — nothing was dropped in for this
  run.
- §3 option 2 (venue/creator media with written permission): **no paperwork
  exists.** Re-measured across all 53 content files: **13** carry policy v2 and
  **all 13** are `format: carousel` + `asset_source: licensed_stock`; the other 40
  predate the policy and carry no `asset_source` at all. The `(format,
  asset_source)` tally is exactly `{(carousel, licensed_stock): 13, (none, none):
  40}`. Zero files have ever carried `original` or `partner_licensed`. No file sets
  a `partner_handle`, and no file has a `collab_status` other than
  `not_requested`. Obtaining real permission means contacting a venue, which an
  unattended run must not do.
- §3 option 3 (licensed stock): **barred for this format.** Stock is limited to "a
  non-venue-specific editorial Carousel". Today is a Reel. Note the bar is on the
  **format**, not only the subject: even a non-venue-specific editorial *Reel*
  could not use stock, so there is no "editorial Reel" escape hatch. And Tuesday is
  a Collab *candidate* day, which CONTENT.md ("Media and rights") restricts to
  original or written-partner media — so today is blocked twice over.

So §0 applies and the run stops without a queue item. The three possible fixes
remain editorial and reserved for a human — see the 2026-09-15 entry.

### NEW — Mon 2026-11-16 ran, succeeded, and wrote nothing: a *silent successful* skip

This is a new failure mode and it is worth separating from the turn-cap misses,
because it does not look like a failure from any angle an automated check can see.
Run **43799347964**, created 2026-11-16T03:38:00Z, finished 03:44:50Z
(**6m50s**), conclusion **`success`**, every step green including `콘텐츠 작성`.
And yet `git log` has no 11-16 commit at all: HEAD is still
**624921a** ("skip: 2026-11-15 …"), measured this run with `git rev-parse HEAD`.
No content JSON, no queue change, **and no SKIPPED.md entry**.

The decision itself was almost certainly correct — 11-16 was a Monday Reel and the
§3 blocker above applied identically — so this is not a bad call, it is an
**unrecorded** call. That distinction matters for three reasons:

- **The skip ledger silently lost a day.** Without this entry the file would have
  jumped from "45th" on 11-15 to "46th" today, and the count of consecutive skips —
  the single number that tells a human how long this blocker has stood — would have
  been permanently one short.
- **It is invisible to every existing check.** The turn-cap misses (09-30, 10-03,
  10-14, 10-28, 11-14) at least show `conclusion: failure` in the Actions list. This
  one shows `success`. The watchdog, which only counts whether a run *exists*
  (watchdog.yml:24-28, see the 11-15 entry), was satisfied twice over.
- **It cost nothing and proves nothing.** Six minutes and fifty seconds of model
  time produced no artifact, so the run cannot be distinguished after the fact from
  one that never reached a decision.

Causes that were **ruled out** this run: not the turn cap (the run succeeded, and
`error_max_turns` appears nowhere in its log); not a push failure (no commit object
exists to have failed to push); not a DRY-RUN flag (the `DRY RUN 여부` env var is
present but **empty** on the 11-16 run's own recorded prompt, identical to today's,
and empty is not `true`). What remains is that the run reached the correct §3 skip
and then simply did not perform the §0 bookkeeping — PIPELINE.md §0 says "stop
without adding a queue item" and never says to write a skip note, so a literal
reading of §0 permits exactly what 11-16 did. **The repo convention of committing a
skip note lives only in `git log` and in this file, not in the source of truth.**

**Recommended human fix (flagged, not done — an agent should not edit the source of
truth on its own judgment):** add one line to PIPELINE.md §0 making the skip note
mandatory, e.g. *"When stopping under this section, append a dated entry to
SKIPPED.md recording which gate stopped the run, and commit it. Do not add a queue
item."* That turns a silent success into a committed artifact and makes a missing
day detectable by looking at the repo instead of the Actions log. A cheap companion
check: have the watchdog require that a Reel day produced *either* a queue item or
a new SKIPPED.md entry.

### Day-loss tally, restated with 11-16 included

Of the last **nine** scheduled content days, **three** produced no artifact of any
kind: 11-14 (Carousel, turn cap, `failure`), 11-16 (Reel, silent success, this
entry), and — for a different and legitimate reason — every Reel day produced no
*queue* item by design. Separating the two kinds of loss:

- **Carousel days lost to `--max-turns 60`: five** — 09-30, 10-03, 10-14, 10-28,
  11-14. `.github/workflows/daily-content.yml:80` still reads `--max-turns 60`.
  Raising it (120 is a safe start; `timeout-minutes: 30` at line 37 is the real
  ceiling and 11-14 used only 14 min) remains the **single highest-value human
  fix**, because it is the only known fault that blocks the format that can still
  ship. Today's run, for calibration, reached its §3 decision in roughly 20 turns.
- **Reel days lost to §3 media: 47 consecutive**, correctly and by design.
- **Days lost to missing bookkeeping: one, new** — 11-16, above.

### Publish side: unchanged, and the next real test is tomorrow

Nothing has been authored since the 11-11 Carousel, so nothing was due at 19:00 KST
on 11-16 and the publish run (**43947573894**, 2026-11-16T20:13:45Z) succeeded with
nothing to pick up — as did 11-15's. So the code-190 tally is still **seven**
(10-10, 10-17, 10-21, 10-31, 11-04, 11-07, 11-11), the newest `held_at` is still
**2026-11-12T02:49:50**, and the last successful publish is still
`2026-10-07-seoul-cafe-churn-en` — now **41 days** ago. Re-authorizing
`IG_ACCESS_TOKEN` through Instagram Login (CONNECT-GUIDE.md) is still the
top-priority human action and still impossible for an agent: it is a repository
secret. The item that will actually test it is whatever survives Wed
**2026-11-18** — tomorrow, a cafe Carousel, with a ready angle handed off below.

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-11-17 (Tue), `%u` = 2.
- `scripts/cardnews.py` renders **7 slides at 1080×1350 with no errors** — run for
  real against `content/2026-11-11-korea-cafe-cup-rules-en.json` into a temp
  directory, so the renderer is proven on this runner without touching the
  committed `out/` tree. Pillow **13.0.0**.
- **WebSearch works. WebFetch works** — WebFetch verified on `segye.com`, which
  returned full article body including figures and quoted sentences.
- **`ffmpeg` is still missing** (`command -v ffmpeg` → nothing), and still not
  committed: `grep -n ffmpeg .github/workflows/daily-content.yml` returns nothing
  and line 50 is still just `pillow 설치`. `scripts/reel.py` would die here. Moot
  today (§3 stops first), but whoever ships the first Reel needs that step
  committed, which needs `workflows: write`.

### Hand-off for Wed 2026-11-18 (cafe Carousel) — the caveat is now closed

The 11-15 entry handed off the cafe contraction/consolidation split with one
load-bearing caveat: both headline counts came *through* outlets citing the NTS,
never from a second independent outlet or from source. **That caveat is now
narrower.** A third outlet, found and fetched this run, carries the same April 2026
figures and adds survival data the earlier pair did not have:

- Segye Ilbo, published **2026-10-09 05:00 KST**:
  [segye.com/newsView/20261009501247](https://www.segye.com/newsView/20261009501247)
  — "전국 커피음료점은 올해 4월 기준 9만3551곳으로 1년 전보다 1699곳 줄었다."
  That is **93,551 as of April 2026, down 1,699 (−1.8%) from 95,250**, a **second
  consecutive annual decline** — digit-for-digit the News1 (2026-06-07) figures,
  from a different outlet on a different date. Two independent outlets now agree on
  the same number, so it is safe to use **attributed to the outlets**.
- **New from the same piece, and a better hook than the raw count:** cafe survival
  rates, attributed to the NTS's *100대 생활업종 생존율* release of April 2025
  (2023 basis) — **1-year 83.5%, 3-year 53.2%, 5-year 34.6%**. The article's own
  framing: "카페 세 곳이 문을 열면 5년 뒤 영업을 이어가는 곳은 한 곳 정도라는
  의미다" — of three cafes that open, about one is still trading five years later.
  This is a *rate*, not a closure count, which is what keeps it clear of the ground
  10-07 (`seoul-cafe-churn`) and 11-11 already covered.

**Still true and still load-bearing:** `tasis.nts.go.kr` was **not** fetched this
run either, so nothing here is verified at source. Attribute to the outlet on the
sources slide, as 10-10 through 11-11 did. The consolidation contrast (big-5
discount chains from under 3,000 stores in 2020 to over 10,000 in 2025; Mega MGC
~4,400 by Aug 2026) is in the 11-15 entry and is still the recommended frame —
**fewer cafes, more cafe chains, one in three surviving five years.** Do not lead
with "cafes are closing."

Also still true: keep `caption` + hashtags under ~2000 characters against
`MAX_CAPTION = 2200` (measure before committing), source a non-venue-specific CC0
photo and verify the licence against the Wikimedia Commons `extmetadata` API for
the exact file, and **do not** build on the Starbucks `cagongjok` equipment ban
(covered by 09-23).

### Topic research for today's slot (not the blocker)

Recorded so the effort is not spent twice. Today's slot was local food, and the
angle that looked most promising is **착한가격업소** — the value-price shops that
local governments designate and list publicly, with set menu prices (kimchi stew
and kalguksu at ₩6,000, doenjang stew at ₩9,000 on Dongdaemun-gu's own 2026 list;
a Seoul city media piece from June 2026 covers a shop where every item is ₩6,000).
This is worth keeping because it is **structurally stock-eligible**: the subject is
a government scheme and a price list, not a venue, so it fits §3 option 3 on a
**Saturday local Carousel** without recommending anywhere. Park it as the backup
for **Sat 2026-11-21**, behind the origin-labelling board from the 2026-11-13 entry,
which is fully verified and still unconsumed. Caveat: the Dongdaemun-gu page is a
single district's list and the Seoul piece is five months old, so prices need
re-checking against the national 착한가격업소 listing before any number goes in
copy. A related inflation hook — kalguksu showing the steepest rise among Seoul
dining-out staples, per Korea Times — was found **undated** in search results and
is **not** usable until the publication date is confirmed.

---
## 2026-11-15 (Sun), reel / cafe — SKIPPED

Forty-fifth consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged. Every
number below was measured this run, not inherited from the 2026-11-13 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Sun 2026-11-15 12:39 KST, `%u` = 7 → **reel /
  cafe-dessert**, Collab *optional*. The task prompt independently specified
  `reel`; the two agree.
- §0: **no `pending` or `published` item for 2026-11-15.** `queue.json` holds **53**
  entries (**13** `published`, **40** `held`, **0** `pending`); grepping the whole
  serialised queue for `2026-11-15` returns **zero** hits, so neither a slug nor a
  `publish_at` claims today, and `content/` has no `2026-11-15-*` file. Still **no
  ramp flag**: the union of all keys across all 53 entries is exactly `error,
  format, held_at, hold_reason, media_id, pillar, publish_at, published_at, slug,
  status`, and the only "ramp" matches in the repo remain the prose at
  CONTENT.md:20 and PIPELINE.md:29 that *describe* the flag §1 says to respect.
- §3 option 1 (owner original): **empty.** Resolved every `assets/photos/`
  reference across all **53** `content/*.json`: **54** on disk, **53** referenced.
  The one unreferenced file is `2026-09-16-korea-cup-rules-en.jpg`, which is itself
  Carousel stock belonging to a policy-v2 item — not an unclaimed owner frame.
  `git ls-files` filtered for
  `mp4|mov|m4v|avi|webm|mkv|mp3|wav|m4a|heic|raw|dng|tiff|cr2|arw` returns **zero**
  files, so there is no owner footage for a Reel either, and
  `git status --untracked-files=all` is **clean** — nothing was dropped in for this
  run.
- §3 option 2 (venue/creator media with written permission): **no paperwork
  exists.** Re-measured across all 53 content files: **13** carry policy v2 and
  **all 13** are `format: carousel` + `asset_source: licensed_stock`. Zero files
  have ever carried `original` or `partner_licensed`. No file sets a
  `partner_handle`, and no file has a `collab_status` other than `not_requested`.
  Obtaining real permission means contacting a venue, which an unattended run must
  not do.
- §3 option 3 (licensed stock): **barred for this format.** Stock is limited to "a
  non-venue-specific editorial Carousel". Today is a Reel, and a Sunday
  cafe/dessert Reel is venue-specific by construction.

So §0 applies and the run stops without a queue item. The three possible fixes
remain editorial and reserved for a human — see the 2026-09-15 entry.

### NEW — Sat 2026-11-14 died on the turn cap, and it was the run that was ready

The fifth Carousel day lost this way, and the most expensive one. The 2026-11-13
entry handed it a **fully primary-verified** angle (the 29-item origin-labelling
board, checked against Seoul's own food-safety portal) precisely so the run would
be cheap. It still failed: run **43554040429**, 2026-11-14T03:55Z, **13m49s**,
failing step `콘텐츠 작성`, `Action failed with error: Claude execution failed:
Reached maximum number of turns (60)`. No content JSON, no queue entry, no skip
note — a silent miss, confirmed from the Actions log this run.

Carousel days lost to `--max-turns 60`: **09-30, 10-03, 10-14, 10-28, 11-14** —
five, against 13 lifetime published posts. `.github/workflows/daily-content.yml:80`
still reads `--max-turns 60`. Raising it (120 is a safe start;
`timeout-minutes: 30` at line 37 is the real ceiling and 11-14 only used 14 min of
it) remains the single highest-value human fix, because it is the only one of the
known faults that blocks the format that can still ship.

### NEW — the watchdog cannot recover a turn-cap failure, by design

Worth recording because it looked like a second failure on 11-14 and is not: the
watchdog *did* run (2026-11-14T07:04Z, after the pipeline had already failed) and
reported success without restoring anything. That is its specification, not a bug.
`.github/workflows/watchdog.yml:24-28` counts `daily-content.yml` runs created
since 00:00 UTC and re-dispatches only `if: steps.check.outputs.count == '0'`. It
tests whether a run **exists**, never whether it **succeeded**, so a run that
fires and dies on the turn cap satisfies it. PIPELINE.md §6's "the watchdog may
restore a missed content-generation run" is therefore true only for a *dropped*
GitHub schedule, not for a failed run.

Consequence: **every turn-cap failure is unrecoverable for that day.** The two
faults compound — the cap kills the Carousel, the watchdog declines to retry it.
The jq filter would need `select(.conclusion == "success")` (or `!= "failure"`)
added at watchdog.yml:27; the job already holds `actions: write`. Flagged, not
done: this agent's token has no `workflows: write`, and changing recovery
behaviour is a human call.

### Publish side: unchanged, and 11-14 produced no new evidence

Because 11-14 wrote nothing, nothing was due at 19:00 KST, and the publish run
(2026-11-14T16:29Z) succeeded in **15s** with nothing to pick up. So the code-190
tally is still **seven** (10-10, 10-17, 10-21, 10-31, 11-04, 11-07, 11-11), the
newest `held_at` is still **2026-11-12T02:49:50** (the 11-11 Carousel), and the
last successful publish is still `2026-10-07-seoul-cafe-churn-en` — now **39 days**
ago. Re-authorizing `IG_ACCESS_TOKEN` through Instagram Login (CONNECT-GUIDE.md)
is still the top-priority human action and still impossible for an agent: it is a
repository secret. The next item that will actually test it is whatever survives
Wed **2026-11-18**.

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-11-15 (Sun), `%u` = 7.
- `scripts/cardnews.py` renders **7 slides at 1080×1350 with no errors** — run for
  real this run against `content/2026-11-11-korea-cafe-cup-rules-en.json` into a
  temp directory, so the renderer is proven on this runner without touching the
  committed `out/` tree.
- **WebSearch works. WebFetch works** on `hankyung.com`; `news1.kr`'s AMP URL
  returns only headline and subheadline, not the article body.
- **`ffmpeg` is missing again.** The 2026-11-13 run proved the Reel path end to end
  only because it installed ffmpeg ad hoc in its own session — **no install step was
  ever committed**: `grep -n ffmpeg .github/workflows/daily-content.yml` returns
  nothing and line 50 is still just `pillow 설치`. `scripts/reel.py` would die here.
  Moot today (§3 stops first), but whoever ships the first Reel needs that step
  committed, which needs `workflows: write`.

### Hand-off for Wed 2026-11-18 (cafe Carousel) — the contraction/consolidation split

Two angles are now ready and neither needs fresh research. **11-21 (Sat, local):**
take the origin-labelling board from the 2026-11-13 entry — it is fully verified
and was never consumed. **11-18 (Wed, cafe):** the cafe-count angle below, which
this run upgraded from the "NOT yet primary-verified" state the 11-09/11-11
hand-offs left it in.

The numbers, all now attached to dated, attributed reports:

- **93,542** coffee/beverage businesses (커피음료점) nationwide **as of June 2026**,
  **down 1.5% YoY**, a **second consecutive annual decline** since June 2024.
  Attributed to 국세청 (NTS) by Hankyung, published **2026-08-31**.
  [hankyung.com/article/202608314344g](https://www.hankyung.com/article/202608314344g)
- **April 2026: 93,551**, down **1,699 (-1.8%)** from 95,250 in April 2025, after a
  **peak of 96,300 in April 2024**. News1, published **2026-06-07**.
  [news1.kr/economy/trend/6189108](https://www.news1.kr/economy/trend/6189108)
- The counter-movement, which is the actual story: the **big-5 low-cost chains went
  from under 3,000 stores in 2020 to over 10,000 in 2025**. As of April 2026 Mega
  MGC ~**4,000** stores (~**4,400** by August 2026), Compose ~**3,000**, 빽다방
  ~**1,800**. Seoul coffee *franchise* outlets were **6,766 in Q4 2025, down 368
  YoY** — so even the chain total fell in Seoul while the discount brands grew.
  Same Hankyung piece.
- Supporting cost pressure: coffee **import prices up 14%** with continued drought
  in Brazil; independent operators quoted that one discount brand opening nearby
  halves their sales. News1 subheadline, 2026-06-07.

**Frame it as the split, not the decline** — Korea has fewer cafes than two years
ago *and* more cafe chains, so the cafe a traveler walks past is likelier to be a
₩1,500 chain counter than it was in 2024. That framing is also what keeps the post
off ground already covered: **10-07 (`seoul-cafe-churn`) and 11-11 already used raw
closure counts**, so a post that leads with "cafes are closing" repeats them. Lead
with the consolidation contrast or drop the angle.

**Caveat, unchanged and load-bearing:** both headline counts still come *through
news outlets citing the NTS*, not from an NTS/TASIS release fetched directly —
`tasis.nts.go.kr` was **not** fetched this run. Re-verify at source before a number
goes in a caption, or attribute to the outlet in the sources slide. This pair
supersedes the 11-09/11-11 hand-off's "95,337 in Q1 2025, down 743 from 96,080",
which is a year older and a different reference period. One trap: a
`thecheck.co.kr` startup-info page carries an impossible "2028년 1분기" figure —
do not use that page.

Also still true: keep `caption` + hashtags under ~2000 characters against
`MAX_CAPTION = 2200` (measure before committing), source a non-venue-specific CC0
photo and verify the licence against the Wikimedia Commons `extmetadata` API for
the exact file, as 10-10 through 11-11 did, and **do not** build on the Starbucks
`cagongjok` equipment ban (covered by 09-23).

---

## 2026-11-13 (Fri), reel / restaurant — SKIPPED

Forty-fourth consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged. Every
number below was measured this run, not inherited from the 2026-11-12 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Fri 2026-11-13 12:57 KST, `%u` = **5** → **reel /
  restaurant**, Collab **candidate**. The task prompt independently specified
  `reel`; the two agree.
- §0: **no `pending` or `published` item for 2026-11-13.** `queue.json` holds **53**
  entries (**13** `published`, **40** `held`, **0** `pending`). Grepping the whole
  serialised queue for `2026-11-13` returns **zero** hits — unlike 11-12, not even a
  `held_at` collision. `content/` has no `2026-11-13-*` file. Still **no ramp flag**
  anywhere: a regex for `"*ramp*"` keys across `queue.json` returns nothing, and the
  only "ramp" matches in the repo remain the prose at CONTENT.md:20 and
  PIPELINE.md:29 that *describe* the flag §1 says to respect.
- §3 option 1 (owner original): **empty.** Resolved every image reference across all
  **53** `content/*.json` against `assets/photos/`: **54** on disk, **54**
  referenced, **unused set = zero**, missing set = zero — no unclaimed frame is
  sitting in the repo. `git ls-files` filtered for
  `mp4|mov|m4v|avi|webm|mkv|mp3|wav|m4a|heic|raw|dng|tiff|tif|cr2|arw` returns
  **zero** files, so there is no owner footage for a Reel either. `git status
  --untracked-files=all` is **clean** — nothing was dropped in for this run. The last
  human-committed photo is still `cheongildip-en.jpg` (392aefd, **2026-08-25**),
  which predates the policy rewrite (8128750, 2026-09-14) by three weeks; every
  photo commit since is a `claude[bot]` Carousel-stock fetch.
- §3 option 2 (venue/creator media with written permission): **no paperwork exists.**
  `git ls-files` filtered for `right|permis|licen|consent|partner|inbox|incoming|
  upload|submission|footage` returns **9** paths, and all 9 are the
  `2026-11-04-korea-cafe-licence-en` slug matching on "licen" — a post *about* licence
  types, not a licence grant. Obtaining real permission means contacting a venue,
  which an unattended run must not do.
- §3 option 3 (licensed stock): **barred for this format, and today doubly so.**
  Stock is limited to "a non-venue-specific editorial Carousel". Today is a Reel, and
  the Friday `restaurant` pillar is a single-venue recommendation by construction, so
  the escape hatch is closed on both counts. Friday is also a **Collab candidate**,
  and §3 is stricter again there: a Collab "must use original or written
  partner-authorized media" (CONTENT.md, Media and rights), and a Collab item must
  stay held until `collab_status: accepted`, which needs a human operator because the
  Instagram Login integration cannot invite collaborators. So the Collab branch is
  not a way around the media gate; it is the same gate plus a second one.
- Rights audit across `content/`: the set of
  `(policy_version, format, asset_source)` triples is exactly
  `{(2, carousel, licensed_stock): 13, (none, none, none): 40}`. **Zero** files at any
  policy version carry `original` or `partner_licensed`, so no compliant Reel *input*
  has ever existed. For today's pillar specifically, the account's last `restaurant`
  Reel was `2026-09-13`; re-running one the pre-8128750 way — a stock photo as the
  cover with a disclosure buried in sources-slide prose, as `2026-09-03-charles-h-en`
  did — is exactly what the policy rewrite withdrew and is not available.

### NEW this run: the Reel render path works, measured end to end

This is the first positive measurement of the Reel path in **52 days** (the previous
newest was 2026-09-22) and it changes the standing framing in the header. Sequence,
exactly as PIPELINE.md §4 prescribes it:

```
sudo apt-get install -y ffmpeg                  → exit 0, ffmpeg 6.1.1-3ubuntu5
python3 scripts/cardnews.py content/2026-11-11-korea-cafe-cup-rules-en.json OUT
                                                → exit 0, 7 slides, all 1080×1350 RGB
python3 scripts/reel.py     content/2026-11-11-korea-cafe-cup-rules-en.json OUT
                                                → exit 0, <slug>_reel.mp4
```

`ffprobe` on the result: **h264, 1080×1920, 30/1 fps, 666 frames, 22.200 s, 7.70 MB**,
plus an **AAC 44.1 kHz mono** track. 9:16 confirmed by measurement, and 22.2 s sits
inside CONTENT.md's 15–30 s window. Audio is the **synthesised** pillar fallback, not
the licensed track: `reel.py` printed `! cafe: tracks.json 에 등록됐지만 파일이
없습니다 → assets/music/cafe.mp3`, which is correct and expected — `.gitignore`
excludes `assets/music/*` so the Incompetech mp3s are never in a fresh checkout. Per
assets/music/README.md a Reel that needs the licensed track must be built where the
mp3 exists; a CI-built Reel will always carry synth audio, which is copyright-safe.

Two mechanical traps found by hitting them, worth writing down because the next
person to ship a Reel will hit both:

1. **`reel.py` does not render its own slides.** Run against a fresh empty output
   directory it fails — with ffmpeg *absent* at `reel.py:45` (`FileNotFoundError:
   'ffmpeg'`, the error all seven previous entries recorded), and with ffmpeg
   *present* at `reel.py:65`, where ffmpeg itself reports `Error opening input file
   .../<slug>_01.jpg`. It consumes the JPGs `cardnews.py` leaves in
   `<out>/<slug>/`, so §4's two commands are a mandatory order into the **same**
   output directory, not a convenience. Earlier entries only ever saw trap 1 because
   ffmpeg was missing first, and so read the crash as the whole story.
2. **Probe the MP4 only after the process exits.** `ffprobe` run while `reel.py` was
   still writing reported `moov atom not found / Invalid data found`, on a file that
   was already 4.98 MB and finished valid at 7.70 MB. A render check that probes
   early will report a corrupt Reel that is in fact fine.

So ffmpeg remains a per-run setup step (2026-09-22 finding, now re-confirmed) and the
renderer is sound. **§3 media is the only thing blocking a Reel.**

### Also verified working this run

- `scripts/cardnews.py` on `content/2026-11-11-korea-cafe-cup-rules-en.json`:
  exit **0**, **7** slides, every one **1080×1350** RGB, opened and measured with
  Pillow afterwards rather than trusted on exit code (the 2026-09-17 lesson).
- **WebSearch works. WebFetch works** — see the Saturday hand-off below, which
  upgraded a fact the 11-12 entry explicitly flagged as unverified.
- `python3` **3.12.16** and Pillow **13.0.0** are present.
- `--max-turns 60` did not fire this run.
  `.github/workflows/daily-content.yml:80` still reads `--max-turns 60`, unraised.

### Publish side: no new evidence, by construction

Nothing shipped to the API since the 11-12 entry and nothing could have: 11-12 and
11-13 were both Reel skip days, so the 19:00 KST publisher had no due item to pick
up either evening. `queue.json` is byte-identical on the publish side — newest
`held_at` is still **2026-11-12T02:49:50** (the 11-11 Carousel), and the code-190
tally is still **seven** (10-10, 10-17, 10-21, 10-31, 11-04, 11-07, 11-11). Last
successful publish remains `2026-10-07-seoul-cafe-churn-en`, now **37 days** ago.
Re-authorizing `IG_ACCESS_TOKEN` through Instagram Login (CONNECT-GUIDE.md) is still
the **top-priority human action** and still not something an agent can do — the token
is a repository secret. Saturday 2026-11-14 is the next item that will actually test
it, and on current evidence it will be the eighth code-190 hold.

### Hand-off for Sat 2026-11-14 (local / neighborhood Carousel)

**The 11-12 hand-off stands and its one open item is now closed.** Angle unchanged:
the origin-labelling board on the restaurant wall. Read the 11-12 entry for the
framing — lead with enforcement scale, not the prison term.

The 11-12 entry said the labelled-item list was "**NOT yet primary-verified, do not
publish as-is**" because secondary guides disagreed and one contradicted itself. It
is now verified against a **government** source — Seoul's official food-safety
portal, [fsi.seoul.go.kr 음식점 원산지 표시](https://fsi.seoul.go.kr/front/M0000067/content/view.do)
— which gives the full list and the fine schedule:

- **29 items = 6 + 3 + 20**, confirming the count the 11-12 entry could not.
- **Livestock (6):** beef, pork, chicken, duck, lamb, goat (incl. dairy goat) —
  covering meat, packaged meat and processed meat products.
- **Agricultural (3):** rice (in 밥/죽/누룽지, incl. glutinous and brown);
  soybeans (두부류 excl. processed tofu and yuba, 콩비지, 콩국수); napa-cabbage
  kimchi, **labelled for both the cabbage and the chilli powder**.
- **Seafood (20):** olive flounder, Korean rockfish, red sea bream, loach, eel,
  webfoot octopus, mackerel, hairtail, pollack (excl. dried 황태/북어), squid,
  swimming crab, yellow croaker, tuna, monkfish, baby octopus, scallop, sea squirt,
  yellowtail, abalone, bluefin croaker. Plus **live seafood held in a tank** for
  cooking, which is covered on top of the 20. The last five were the 2023-07-01
  expansion from 15 species, so **any page still saying 15 or 12 is stale** — and
  several district-office pages are (Gangdong says 15, Seoul's welfare pages say 12,
  a 2013 Gunsan PDF says 16). Do not source the list from a district office.

**One correction to carry into the copy.** The 11-12 entry's "administrative fine up
to 10 million won" is the statutory *ceiling*, not what a restaurant actually faces.
The schedule for non-labelling is **₩300,000 / 600,000 / 1,000,000** by violation
count for each listed item, rising to **₩1m / 2m / 3m** for beef specifically;
labelling-*method* violations run ₩150,000–500,000, and ₩250,000–1.5m for beef. Live
seafood is the only line that reaches ₩10m (₩50,000–10,000,000). False labelling is
the serious one and is unchanged: **up to 7 years or ₩100m**. Two or more violations
in 2 years can also get the business **publicly named online** plus mandatory
education — a good, under-used slide fact.

**One dead link to skip.** The 해양수산부 release on the 15→20 expansion
(`mof.go.kr/doc/ko/selectDoc.do?docSeq=48425`) now **404s**; the expansion is
attested by the fsi.seoul.go.kr list above instead. Also still true from the 11-12
entry: `law.go.kr` serves statute **titles only** (client-rendered), so do not spend
turns there — and the 2026-10-22 delivery-app amendment is still sourced only to a
payments-industry explainer, so verify at 농식품부 or drop it; the post works without.

Carried forward unchanged from 11-12: the 농관원 Chuseok sweep figures (**7–23 Sept
2026**, **13,251** businesses inspected, **256** caught — **104** false labelling
referred for criminal charges, **152** non-labelling fined **₩35.87m** total, release
1 Oct 2026, [mafra.go.kr 579325](https://www.mafra.go.kr/bbs/home/792/579325/artclView.do)
and [578682](https://www.mafra.go.kr/bbs/home/792/578682/artclView.do)) — that is
still the cover stat. Keep `caption` + hashtags under ~2000 characters against
`MAX_CAPTION = 2200`, and source a non-venue-specific CC0 photo (an origin board, a
market meat counter, a generic restaurant interior) verifying the licence against the
Wikimedia Commons `extmetadata` API for the exact file, as 10-10 through 11-11 did.

Also still true from earlier entries: **do not** build on the Starbucks `cagongjok`
equipment ban (covered by 09-23) or on cafe closure counts (covered by 10-07 and
11-11's hand-off).

---

## 2026-11-12 (Thu), reel / bar — SKIPPED

Forty-third consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged. Every
number below was measured this run, not inherited from the 2026-11-10 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Thu 2026-11-12 13:45 KST, `%u` = 4 → **reel / bar**,
  Collab *optional*. The task prompt independently specified `reel`; the two agree.
- §0: **no `pending` or `published` item for 2026-11-12.** `queue.json` holds **53**
  entries (**13** `published`, **40** `held`, **0** `pending`). Grepping the whole
  serialised queue for `2026-11-12` returns exactly **one** hit, and it is the
  `held_at` timestamp of the *11-11* Carousel — **not** a `slug` or a `publish_at`,
  so it is not a same-day item and does not trigger §0. `content/` has no
  `2026-11-12-*` file. Still **no ramp flag** anywhere in the queue or repo notes;
  the only "ramp" matches remain the prose at CONTENT.md:20 and PIPELINE.md:29 that
  *describe* the flag §1 says to respect.
- §3 option 1 (owner original): **empty.** Resolved every image reference across all
  **53** `content/*.json` against `assets/photos/`: **54** on disk, **54**
  referenced, **unused set = zero**, missing set = zero — no unclaimed frame is
  sitting in the repo. `git ls-files` filtered for
  `mp4|mov|m4v|avi|webm|mkv|mp3|wav|m4a|heic|raw|dng|tiff|cr2|arw` returns **zero**
  files, so there is no owner footage for a Reel either. `git status
  --untracked-files=all` is **clean** — nothing was dropped in for this run.
  Separately re-confirmed against history: of the **14** files added to
  `assets/photos/` since the policy rewrite (8128750, 2026-09-14), **all 14** are
  pipeline-fetched editorial stock named for a Carousel slug. The last
  human-committed photo is still `cheongildip-en.jpg` (392aefd, **2026-08-25**),
  which predates the policy by three weeks.
- §3 option 2 (venue/creator media with written permission): **no paperwork exists.**
  `git ls-files` filtered for `right|permis|licen|consent|partner|inbox|incoming|
  upload|submission|footage` returns **9** paths, and all 9 are the
  `2026-11-04-korea-cafe-licence-en` slug matching on "licen" — a post *about* licence
  types, not a licence grant. Obtaining real permission means contacting a venue,
  which an unattended run must not do.
- §3 option 3 (licensed stock): **barred for this format.** Stock is limited to "a
  non-venue-specific editorial Carousel". Today is a Reel, and the Thursday `bar`
  pillar is a single-venue recommendation by construction, so the escape hatch is
  closed on both counts. Swapping the day to a Carousel is one of the three
  editorial fixes in the 2026-09-15 entry and is explicitly reserved for a human.
- Rights audit across `content/`: the set of
  `(policy_version, format, asset_source)` triples is exactly
  `{(2, carousel, licensed_stock): 13, (none, none, none): 40}`. **Zero** files at any
  policy version carry `original` or `partner_licensed`, so no compliant Reel *input*
  has ever existed. Note what this implies for the one `bar` Reel the account has
  authored: `2026-09-03-charles-h-en` ran a stock bar photo as its `bg_image` cover
  and disclosed it only in sources-slide prose ("Cover photo is a licensed stock
  image of a bar, not a photo of this bar"). That disclosure pattern is exactly what
  8128750 withdrew, so re-running today's pillar the old way is not available.

### Verified working this run

- `scripts/cardnews.py` on `content/2026-11-11-korea-cafe-cup-rules-en.json`:
  exit **0**, **7** slides, every one **1080×1350** RGB, opened and measured with
  Pillow afterwards rather than trusted on exit code (the 2026-09-17 lesson).
- **WebSearch works. WebFetch works** — the Wikimedia Commons `extmetadata` API
  re-returned `License: cc0` for the 11-11 cover file, and `mafra.go.kr` article
  579325 returned a full press-release body.
- **New WebFetch datapoint: `law.go.kr` is useless to this pipeline.** Fetching
  `law.go.kr/법령/농수산물의원산지표시등에관한법률` returns the statute *title only* —
  the article text is client-rendered. Statutory figures must therefore be sourced
  from a 농관원/농식품부 press release or a ministry PDF, not from the statute page.
  Worth knowing before a future run burns turns on it.
- `python3` **3.12.16** and Pillow **13.0.0** are present.

### Re-confirmed: `scripts/reel.py` still cannot run here

`python3 scripts/reel.py content/2026-11-11-korea-cafe-cup-rules-en.json
/tmp/reelcheck2` → exit **1**, uncaught `FileNotFoundError: [Errno 2] No such file or
directory: 'ffmpeg'` at `scripts/reel.py:45`. `which ffmpeg` is empty on this runner
image. Identical to the 2026-11-06 / 11-08 / 11-09 / 11-10 measurements. Per the
2026-09-22 finding this is a per-run setup step rather than a true blocker — `sudo
apt-get install -y ffmpeg` succeeds here and `reel.py` then produces a valid
1080×1920 MP4 — but the Reel path has now been unexercised for **forty-three**
consecutive Reel days, so "it worked on 2026-09-22" is still the newest evidence
there is.

### Publish side: NEW evidence today — the seventh code-190 hold

Unlike 11-10, this run *does* carry new publish evidence, because 11-11 was a
Carousel that actually shipped to the API. `2026-11-11-korea-cafe-cup-rules-en` was
authored and rendered correctly off the 11-10 hand-off, then **held** at
**2026-11-12T02:49:50 KST** with `hold_reason: publish_failed_manual_review` and
OAuthException **code 190** (`fbtrace_id AwAKaH9ZaIvG-8NNUDYj2Ia`) — the same
"session has been invalidated because the user changed their password" message.

That makes **seven** code-190 holds (10-10, 10-17, 10-21, 10-31, 11-04, 11-07,
11-11) and moves the token blocker's last-tested date from 2026-11-08 to **today**.
It is not stale and it is not intermittent: **every** Carousel authored since 10-10
has died on it. Last successful publish is still `2026-10-07-seoul-cafe-churn-en`,
now **36 days** ago. Re-authorizing `IG_ACCESS_TOKEN` through Instagram Login
(CONNECT-GUIDE.md) remains the **top-priority human action** and is not something an
agent can do. Note the compounding waste: the authoring side is working — 11-04,
11-07 and 11-11 were all produced on schedule — and all three were thrown away at
19:00 KST by one expired credential.

`--max-turns 60` did not fire again this run;
`.github/workflows/daily-content.yml:80` still reads `--max-turns 60`, unraised.

**Caption cap: no longer drifting.** Measured across all 13 policy-v2 Carousels,
caption + hashtags runs 929, 1229, 1374, 1689, 1526, 1572, 1964, 2104, **2328**,
2051, 2110, 2069, **1915**. The 10-24 breach (2328) is still the only one over
`MAX_CAPTION = 2200`, and the last four runs have held 90–285 characters under it,
so the explicit budget the 10-25 entry asked for is being honoured in practice. The
10-25 recommendation stands anyway: the cap is still **unwritten** in PIPELINE.md §4
and CONTENT.md, so compliance currently depends on each run reading this file.

### Hand-off for Sat 2026-11-14 (local / neighborhood Carousel)

The 11-10 dessert-cycle hand-off was **consumed** by 11-11, so Saturday needs a new
angle. Researched and partly verified this run — a non-venue-specific editorial
topic, so §3 option 3 applies and it can ship:

**"The board on the wall tells you where your meat came from — and lying on it is a
7-year offence."** Korea's 원산지표시법 (Act on Origin Labelling of Agricultural and
Fishery Products) obliges *every* 일반음식점 / 휴게음식점 / 위탁급식소 / 집단급식소 to
post origin for a fixed list of items, which is why that small print board hangs by
the door of restaurants travelers eat in daily. Useful to an English audience
because it is a trust tool they can actually read: the country name is in the board
even when the menu is not.

Facts gathered, with their verification state:

- **Penalties — verified at an official source.** 농관원/농식품부 releases state false
  labelling (거짓표시) carries **up to 7 years' imprisonment or a fine up to 100
  million won**, while non-labelling or wrong-method labelling (미표시·표시방법 위반)
  carries an **administrative fine up to 10 million won**. Sources:
  [mafra.go.kr 579325](https://www.mafra.go.kr/bbs/home/792/579325/artclView.do),
  [mafra.go.kr 578682](https://www.mafra.go.kr/bbs/home/792/578682/artclView.do).
- **Enforcement scale — verified, and the strongest stat for a cover.** In a 17-day
  Chuseok sweep, **7 Sept – 23 Sept 2026**, 농관원 inspected **13,251** businesses and
  caught **256**: **104** for false labelling (referred for criminal charges) and
  **152** for non-labelling (fines totalling **35.87 million won**). Release dated
  1 Oct 2026, same mafra.go.kr/579325 URL above.
- **The labelled item list — NOT yet primary-verified, do not publish as-is.**
  Secondary guides agree on **6 meats** (beef, pork, chicken, duck, lamb, goat
  incl. dairy goat) and **3 agricultural items** (rice; napa-cabbage kimchi, which
  must carry origin for *both* the cabbage and the chilli powder — e.g. "배추김치
  (배추 국내산, 고춧가루 중국산)"; and soybeans for tofu/soy dishes), plus **20
  seafood species** for **29** total. One of those guides contradicts itself on the
  total within the same page. Confirm the list and count against the 농관원 고시 or a
  ministry PDF before it goes in a slide — and per the WebFetch note above, do not
  expect law.go.kr to serve it.
- **A live 2026 change worth one line.** An amendment effective **22 Oct 2026**
  requires delivery-app operators to notify listed restaurants of the origin-labelling
  rules and sanctions; the underlying duty on the restaurant is unchanged. Sourced
  only to a payments-industry explainer
  ([tossplace](https://tossplace.com/story/food_delivery_apps_origin)) — verify at
  농식품부 before using, or drop it, since the post works without it.

Angle guidance: lead with the 13,251-inspected / 256-caught enforcement figure, not
with the prison term — the useful message is "this board is checked", not "Korean
restaurants lie". Keep `caption` + hashtags under ~2000 characters against
`MAX_CAPTION = 2200`, and source a non-venue-specific CC0 photo (a restaurant origin
board, a market meat counter, or a generic Korean restaurant interior) the way 10-10
through 11-11 did, verifying the licence against the Wikimedia Commons `extmetadata`
API for the exact file as 11-11 did.

Also still true from earlier entries: **do not** build on the Starbucks `cagongjok`
equipment ban (covered by 09-23) or on cafe closure counts (covered by 10-07 and
11-11's hand-off).

---

## 2026-11-10 (Tue), reel / local — SKIPPED

Forty-second consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged. Every
number below was measured this run, not inherited from the 2026-11-09 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Tue 2026-11-10 14:04 KST, `%u` = 2 → **reel / local**,
  Collab *candidate*. The task prompt independently specified `reel`; the two agree.
- §0: **no `pending` or `published` item for 2026-11-10.** `queue.json` holds **52**
  entries (**13** `published`, **39** `held`, **0** `pending`); grepping the whole
  serialised queue for `2026-11-10` returns **zero** hits in either `slug` or
  `publish_at`, and `content/` has no `2026-11-10-*` file. Nothing to stop on. Still
  **no ramp flag** anywhere in the queue or repo notes — the only "ramp" matches
  remain the prose at CONTENT.md:20 and PIPELINE.md:29 that *describe* the flag §1
  says to respect.
- §3 option 1 (owner original): **empty.** Resolved every image reference across all
  **52** `content/*.json` against `assets/photos/`: **53** on disk, **53**
  referenced, **unused set = zero**, missing set = zero — no unclaimed frame is
  sitting in the repo. `git ls-files` filtered for
  `mp4|mov|m4v|avi|webm|mkv|mp3|wav|m4a|heic|raw|dng|tiff|cr2|arw` returns **zero**
  files, so there is no owner footage for a Reel either. `git status
  --untracked-files=all` is **clean** — nothing was dropped in for this run.
- §3 option 2 (venue/creator media with written permission): **no paperwork exists.**
  `git ls-files` filtered for `right|permis|licen|consent|partner|inbox|incoming|
  upload|submission|footage` returns **9** paths, and all 9 are the
  `2026-11-04-korea-cafe-licence-en` slug matching on "licen" — a post *about* licence
  types, not a licence grant. Obtaining real permission means contacting a venue,
  which an unattended run must not do.
- §3 option 3 (licensed stock): **barred for this format.** Stock is limited to "a
  non-venue-specific editorial Carousel". Today is a Reel, and the Tuesday
  `local` (local food) pillar is a venue/dish recommendation by construction, so the
  escape hatch is closed on both counts. Swapping the day to a Carousel is one of the
  three editorial fixes in the 2026-09-15 entry and is explicitly reserved for a
  human.
- Rights audit across `content/` is unchanged: the set of
  `(policy_version, format, asset_source)` triples is exactly
  `{(2, carousel, licensed_stock): 12, (none, none, none): 40}`. **Zero** files at any
  policy version carry `original` or `partner_licensed`, so no compliant Reel *input*
  has ever existed.

### Verified working this run

- `scripts/cardnews.py` on `content/2026-11-07-korea-old-shop-plaques-en.json`:
  exit **0**, **7** slides, every one **1080×1350** RGB, opened and measured with
  Pillow afterwards rather than trusted on exit code (the 2026-09-17 lesson).
- **WebSearch works. WebFetch works** on `koreaherald.com` (article 10550038 returned
  a full article body).
- `python3` **3.12.16** and Pillow **13.0.0** are present.

### Re-confirmed: `scripts/reel.py` still cannot run here

`python3 scripts/reel.py content/2026-11-07-korea-old-shop-plaques-en.json
/tmp/reelcheck` → exit **1**, uncaught `FileNotFoundError: [Errno 2] No such file or
directory: 'ffmpeg'` at `scripts/reel.py:45`. `which ffmpeg` is empty on this runner
image. Identical to the 2026-11-06, 11-08 and 11-09 measurements. Per the 2026-09-22
finding this is a per-run setup step rather than a true blocker — `sudo apt-get
install -y ffmpeg` succeeds here and `reel.py` then produces a valid 1080×1920 MP4 —
but the Reel path has now been unexercised for **forty-two** consecutive Reel days,
so "it worked on 2026-09-22" is still the newest evidence there is.

### Publish side: no new evidence today, by construction

`queue.json` carries **0** `pending` entries and 2026-11-09 was itself a Reel-day
skip, so the 19:00 KST publisher had nothing to pick up and produced no new token
evidence. The dead-token blocker stands exactly as last tested on **2026-11-08** (the
11-07 Carousel, held 2026-11-08T01:15:12 KST, OAuthException **code 190**,
`fbtrace_id AHyBd06xD_cDwGNXiT_kZD7`) — the sixth code-190 hold, last successful
publish **2026-10-07**. Re-authorizing `IG_ACCESS_TOKEN` through Instagram Login
(CONNECT-GUIDE.md) remains the **top-priority human action** and is not something an
agent can do. `--max-turns 60` did not fire again this run;
`.github/workflows/daily-content.yml:80` still reads `--max-turns 60`, unraised.

### Hand-off for Wed 2026-11-11 (cafe Carousel) — still the dessert-cycle angle

The 2026-11-08 entry's sourced Carousel angle (Korea's 2025–26 dessert cycle,
non-venue-specific so §3 option 3 applies) is **still unconsumed** — 11-09 and 11-10
both skipped as that entry predicted. Tomorrow is a Carousel, the one format that can
still be authored and rendered end to end. Start from that hand-off rather than
re-researching, re-verify each figure at its primary source, keep `caption` +
hashtags under ~2000 characters against `MAX_CAPTION = 2200`, and source a
non-venue-specific CC0 photo the way 10-10 through 11-07 did.

**One upgrade from this run: the NTS lead the 11-09 entry flagged *unverified* now has
numbers.** National Tax Service TASIS data puts registered coffee/beverage shops at
**95,337 in Q1 2025, down 743** from 96,080 a year earlier — reported as the first
decline since the series began, and the national counterpart to 10-07's Seoul-only
492-closure figure. A later Segye report gives **93,551 as of April 2026, down 1,699
YoY**, i.e. a second consecutive annual fall. **Caveat unchanged and important:** both
figures still came through news outlets citing TASIS, not the NTS release itself — the
primary TASIS table was *not* fetched directly this run, so re-verify at source before
either number goes in a caption, and note the Segye piece carries a 2026-10 publication
date against an April 2026 reference period. Sources:
[newsis](https://www.newsis.com/view/NISX20250526_0003189542),
[insideretail.asia](https://insideretail.asia/2025/05/27/cafe-boom-reverses-for-first-time-in-years-as-market-saturation-bites/),
[segye](https://www.segye.com/newsView/20261009501247).

Also unchanged from the 11-09 entry: **do not** build 11-11 on the Starbucks
`cagongjok` equipment ban — `korea-cafe-seat-time` (09-23) already covers that
seat-economics story.

---

## 2026-11-09 (Mon), reel / restaurant — SKIPPED

Forty-first consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged. Every
number below was measured this run, not inherited from the 2026-11-08 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Mon 2026-11-09 12:30 KST, `%u` = 1 → **reel /
  restaurant**, Collab *optional*. The task prompt independently specified `reel`;
  the two agree.
- §0: **no `pending` or `published` item for 2026-11-09.** `queue.json` holds **52**
  entries (**13** `published`, **39** `held`, **0** `pending`); grepping the whole
  serialised queue for `2026-11-09` returns **zero** hits, so neither a slug nor a
  `publish_at` claims today. Nothing to stop on. Still **no ramp flag**: the union of
  all keys across all 52 entries is exactly `error, format, held_at, hold_reason,
  media_id, pillar, publish_at, published_at, slug, status`, and the only "ramp"
  matches in the repo remain the prose at CONTENT.md:20 and PIPELINE.md:29 that
  *describe* the flag PIPELINE.md §1 says to respect.
- §3 option 1 (owner original): **empty.** Resolved every `photo`/`bg_image` key
  across all **52** `content/*.json` against `assets/photos/`: **53** on disk, **53**
  referenced, **unused set = zero**, missing set = zero — so there is no unclaimed
  frame sitting in the repo waiting to be used. `git ls-files` filtered for
  `mp4|mov|m4v|avi|webm|mkv|mp3|wav|m4a|heic|raw|dng|tiff|cr2|arw` returns **zero**
  files — no owner footage for a Reel either. `git status --untracked-files=all` is
  **clean**, so nothing was dropped in for this run.
- §3 option 2 (venue/creator media with written permission): **no paperwork exists.**
  `git ls-files` filtered for `right|permis|licen|consent|partner|inbox|incoming|
  upload|submission|footage` returns **9** paths, and all 9 are the
  `2026-11-04-korea-cafe-licence-en` slug matching on "licen" — a post about licence
  types, not a licence grant. Obtaining real permission means contacting a venue,
  which an unattended run must not do.
- §3 option 3 (licensed stock): **barred for this format.** Stock is limited to "a
  non-venue-specific editorial Carousel". Today is a Reel, and the Monday
  `restaurant` pillar is a venue recommendation by construction, so the escape hatch
  is closed on both counts.

### Measured this run: the Reel format has never once been produced under policy v2

Worth stating plainly, because forty-one skip entries describe the blocker without
quantifying how total it is. Auditing `policy_version` / `format` / `asset_source` /
`rights_confirmed` across all **52** files in `content/`:

- **40** files (2026-08-25 → 2026-09-13) carry **none** of the four v2 rights keys.
  These are the pre-rewrite posts that relied on the mood-stock allowance 8128750
  removed; as the 2026-09-14 entry notes, none of them would be publishable today.
- **12** files carry `policy_version: 2`, and the set of `(policy_version, format)`
  pairs among them is exactly `{(2, 'carousel')}` — all twelve are Carousels, all
  twelve are `asset_source: licensed_stock`, all twelve `rights_confirmed: true`.
- **Zero** files in the repo, at any policy version, carry `asset_source: original`
  or `partner_licensed`.

So the §3 gate has never been cleared by anything. "The Reel path is unexercised" is
not merely a rendering observation (below) — no compliant Reel *input* has ever
existed either. The three editorial fixes in the 2026-09-15 entry remain the only
ways out, and all three are human decisions.

### Verified working this run

- `scripts/cardnews.py` on `content/2026-11-07-korea-old-shop-plaques-en.json`:
  exit **0**, **7** slides, every one **1080×1350** RGB, opened and measured with
  Pillow afterwards rather than trusted on exit code (the 2026-09-17 lesson).
- **WebSearch works.** **WebFetch works** on `koreaherald.com` — a full article body
  came back (article 10550038, the Starbucks Korea `cagongjok` equipment ban).
- `python3` **3.12.16** and Pillow **13.0.0** are present, as the prompt states.

### Re-confirmed: `scripts/reel.py` still cannot run here

`python3 scripts/reel.py content/2026-11-07-korea-old-shop-plaques-en.json
/tmp/rendercheck` → exit **1**, uncaught `FileNotFoundError: [Errno 2] No such file
or directory: 'ffmpeg'` at `scripts/reel.py:45` (`subprocess.run` inside `run()`,
called from `build_segment` at `reel.py:65`, from `build_reel` at `reel.py:244`).
`which ffmpeg` is empty on this runner image. Identical to the 2026-11-06 and
2026-11-08 measurements.

Per the 2026-09-22 finding this is a per-run setup step, not a true blocker — `sudo
apt-get install -y ffmpeg` succeeds here and `reel.py` then produces a valid
1080×1920 MP4 — but the Reel path has now been unexercised for **forty-one**
consecutive Reel days, so "it worked on 2026-09-22" is still the newest evidence
there is. `run()` should also fail with a readable message ("ffmpeg not found —
install it") instead of a bare traceback; the first run that ever gets past the §3
gate should not have to diagnose this too.

### Publish side: no new evidence today, by construction

Nothing was due at the 19:00 KST publisher on Sun 2026-11-08, because 11-08 was
itself a Reel-day skip and `queue.json` carries **0** `pending` entries. The
publisher therefore had nothing to pick up and produced no new token evidence. The
dead-token blocker stands exactly as last tested on **2026-11-08** (the 11-07
Carousel, held 2026-11-08T01:15:12 KST, OAuthException **code 190**, `fbtrace_id
AHyBd06xD_cDwGNXiT_kZD7`) — the sixth code-190 hold, last successful publish
2026-10-07. Re-authorizing `IG_ACCESS_TOKEN` through Instagram Login
(CONNECT-GUIDE.md) remains the **top-priority human action** and is not something an
agent can do; `refresh-token.yml` cannot help, because `refresh_access_token`
extends a live token rather than resurrecting an invalidated session.

`--max-turns 60` did not fire again this run. `.github/workflows/daily-content.yml:80`
still reads `--max-turns 60`, unraised; it stays worth raising as cheap insurance,
not as the first fix.

### Hand-off: the 2026-11-11 topic is already researched — do not redo it

The 2026-11-08 entry closes with a fully sourced Carousel angle for **Wed
2026-11-11 (cafe)** — Korea's 2025–26 dessert cycle, non-venue-specific so §3
option 3 applies. It is **still unconsumed**, since 11-09 and 11-10 are both Reel
days and will both skip. The 11-11 run should start from that hand-off rather than
re-researching: re-verify each figure at its primary source, keep caption +
hashtags under ~2000 characters against `MAX_CAPTION = 2200`, and source a
non-venue-specific CC0 photo the way 10-10 through 11-07 did.

Checked this run for overlap, since four cafe-pillar Carousels already exist and a
fifth must not repeat them: `korea-cup-rules` (09-16, reusable-cup discounts),
`korea-cafe-seat-time` (09-23, the 91-minute americano — this is the `cagongjok`
seat-economics story, so **the Korea Herald Starbucks-equipment article fetched
above is already covered; do not build 11-11 on it**), `seoul-cafe-churn` (10-07,
492 Seoul closures) and `korea-cafe-licence` (11-04, licence types). The dessert-cycle
angle is clear of all four. One adjacent lead surfaced and is flagged *unverified*:
National Tax Service data reported as the **first nationwide decline** in coffee-shop
count since the series began, which is a national counterpart to 10-07's Seoul-only
figure — if 11-11 prefers it, pull it from the NTS release itself, as the search hits
were aggregators.

---

## 2026-11-08 (Sun), reel / cafe — SKIPPED

Fortieth consecutive Reel-day skip. No content JSON, no rendered output committed,
no change to `queue.json`. The §3 media blocker is unchanged. Every number below was
measured this run, not inherited from the 2026-11-06 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Sun 2026-11-08 12:08 KST, `%u` = 7 → **reel /
  cafe**, Collab *optional*. The task prompt independently specified `reel`; the
  two agree.
- §0: **no `pending` or `published` item for 2026-11-08.** `queue.json` holds **52**
  entries (**13** `published`, **39** `held`, **0** `pending`); no entry has a
  `2026-11-08` slug or `publish_at`. Nothing to stop on. Still **no ramp flag** in
  `queue.json` or repo notes — the only "ramp" matches are the prose at
  CONTENT.md:20 and PIPELINE.md:29 that *describe* the flag.
- §3 option 1 (owner original): **empty.** Resolved every `photo`/`bg_image` key
  across all **52** `content/*.json` against `assets/photos/`: **53** on disk, **53**
  referenced, **unused set = zero**, missing set = zero. `git ls-files` filtered for
  `mp4|mov|m4v|avi|webm|mkv|mp3|wav|m4a|heic|raw|dng|tiff` returns **zero** files —
  no owner footage for a Reel either. `git status --untracked-files=all` is **clean**,
  so nothing was dropped in for this run.
- §3 option 2 (venue/creator media with written permission): **no paperwork exists.**
  `git ls-files` filtered for `right|permis|licen|consent|partner|inbox|incoming|
  upload|submission|footage` returns **9** paths, and all 9 are the
  `2026-11-04-korea-cafe-licence-en` slug matching on "licen" — not a grant.
  Obtaining permission means contacting a venue, which an unattended run must not do.
- §3 option 3 (licensed stock): **barred for this format.** Stock is limited to "a
  non-venue-specific editorial Carousel". Today is a Reel, and the Sunday
  `cafe`/dessert pillar is a venue recommendation by construction, so the escape
  hatch is closed on both counts.

A note on one tempting non-escape, because this run's prompt pre-empted it: a
typography-only Reel cover would clear §3 by using no photograph at all, and it is
**not** an option. This is a food and venue account; the prompt states outright that
a typography-only cover "doesn't work here", and CONTENT.md's format standard asks
for original venue footage. Rendering text over a flat background to dodge the media
gate would satisfy the letter of §3 while producing something the account should not
post. The skip is the correct output.

### Verified working this run

- `scripts/cardnews.py` on `content/2026-11-07-korea-old-shop-plaques-en.json`:
  exit **0**, **7** slides, every one **1080×1350**, opened and measured with Pillow
  afterwards rather than trusted on exit code (the 2026-09-17 lesson).
- **WebSearch works.** **WebFetch works** on `koreatimes.co.kr` — a full article
  body came back, see the topic hand-off below.
- `python3` 3.12.16 and Pillow are present, as the prompt states.

### Re-confirmed: `scripts/reel.py` still cannot run here

`python3 scripts/reel.py content/2026-11-07-korea-old-shop-plaques-en.json
/tmp/rendercheck` → exit **1**, uncaught `FileNotFoundError: [Errno 2] No such file
or directory: 'ffmpeg'` at `scripts/reel.py:45` (`subprocess.run` inside `run()`,
called from `build_segment`, `reel.py:65`). `which ffmpeg` is empty on this runner
image. Identical to the 2026-11-06 measurement.

Per the 2026-09-22 finding this is a per-run setup step, not a true blocker — `sudo
apt-get install -y ffmpeg` succeeds here and `reel.py` then produces a valid
1080×1920 MP4 — but two things are worth a human's attention. First, the Reel path
has now been *unexercised* for forty consecutive Reel days, so "it worked on
2026-09-22" is the newest evidence there is. Second, `run()` should fail with a
readable message ("ffmpeg not found — install it") instead of a bare traceback; the
first run that ever gets past the §3 gate should not also have to diagnose this.

### Publish side: the dead token produced fresh evidence overnight

The token blocker is no longer last-tested 2026-11-04. Yesterday's Carousel,
`2026-11-07-korea-old-shop-plaques-en`, was authored, rendered and queued correctly
by the 11-07 run (commit 4f0d9d2), the 19:00 KST publisher picked it up, and it was
**held** at **2026-11-08T01:15:12 KST** with `hold_reason:
publish_failed_manual_review` and the same OAuthException **code 190** — "The
session has been invalidated because the user changed their password or Facebook has
changed the session for security reasons" (`fbtrace_id AHyBd06xD_cDwGNXiT_kZD7`).
That is the **sixth** code-190 hold (10-10, 10-17, 10-21, 10-31, 11-04, 11-07) and
`queue.json` now carries **39** held items against 13 published, last success
2026-10-07.

So the standing diagnosis holds exactly: re-authorizing `IG_ACCESS_TOKEN` through
Instagram Login (CONNECT-GUIDE.md) remains the **top-priority human action**, it is
not something an agent can do, and `refresh-token.yml` cannot help because
`refresh_access_token` extends a live token rather than resurrecting an invalidated
session. Everything the authoring side is still able to produce — Wed/Sat Carousels
— is being written correctly and then lost eight hours later at the final step.

Two sub-faults are *not* currently firing, which is worth recording so nobody fixes
the wrong thing first:

- **The caption cap is being respected.** `2026-11-07`'s `caption` + 8 hashtags
  measure **2069** characters against `MAX_CAPTION = 2200` — the item reached the
  Graph API and died on the token, not on `build_caption()`. The explicit budget
  recommended on 10-25 is working; keep it.
- **`--max-turns 60` did not fire.** `.github/workflows/daily-content.yml:80` still
  reads `--max-turns 60`, unraised, but the 11-07 Carousel run completed inside it.
  That is now three Carousel days in a row — 10-31, 11-04 and 11-07, each with a
  content commit (77ff22c, b0ef5c0, 4f0d9d2) — that cleared the cap. It stays worth
  raising as cheap insurance, not as the first fix.

### Hand-off: a researched Carousel topic for Wed 2026-11-11 (cafe)

§2 research ran before the §3 gate closed the day, so rather than discard it: the
next Carousel day is **Wed 2026-11-11, cafe pillar**, and Korea's 2025–26 dessert
cycle is a strong *non-venue-specific editorial* angle — it names no venue, so §3
option 3 applies and the day can actually ship. Sources found this run, with the
usual caveat that these are **leads for the 11-11 run to verify, not pre-verified
copy**:

- **The Korea Times / Hankook Ilbo, 14 January 2026** — "dujjonku" (두쫀쿠, Dubai
  chewy cookie) traced from the 2024 Dubai-chocolate trend into convenience stores
  and hotel dining. Fetched in full this run. Figures cited there: CU's kataifi
  chocolate chewy rice cake past **1.8 m units in three months** and Dubai-themed
  lines past **8.3 m** overall; GS25 past **1 m units** at a **97%** sell-through
  since October 2025; 7-Eleven's Kadayif Ball lifting dessert-category sales
  **250%** in 11 days; Emart24's two kataifi mochi lines past **180,000** units a
  month. Pierre Gagnaire à Séoul at Lotte Hotel Seoul served a dujjonku-inspired
  petit four, substituting Pailleté Feuilletine because kataifi had become hard to
  source — a nice concrete detail, and note it is a *past* seasonal menu.
- **Korea Credit Data, Q4 2025 small-business report** (via asiae.co.kr, 9 March
  2026) — bakery and dessert sales **+9.5%**, with an explicit warning that the
  fading dujjonku craze leaves small operators holding inventory. Private data, so
  attribute it to Korea Credit Data rather than presenting it as official.
- **Open Survey, Cafe Trend Report 2025** — over **40%** of consumers name bakery
  and dessert as a cafe-choice factor. Also private data.
- **MAFRA / KREI coffee industry analysis, 21 August 2026** — domestic coffee market
  past **KRW 3.7 trillion**; per Korea JoongAng Daily on the same dataset, roasted
  coffee overtook liquid coffee (KRW 1.1 tn in 2024) for the first time since the
  series began in 2018. This is the **official** anchor; pull the primary report
  from mafra.go.kr rather than relying on the summaries.
- **Rejected as unusable:** gitnux.org (aggregator, figures not traceable to a
  primary source) and the Expert Market Research / travel-blog pages. Do not cite.

The arc writes itself and needs no venue: a craze starts abroad, Korean
convenience-store R&D industrialises it in about ten weeks, hotels cite it, the
ingredient runs short, then the inventory bill arrives — with the official coffee
numbers underneath as the stable baseline. Whoever takes 11-11 should re-verify
every figure at the primary source, keep caption + hashtags under ~2000 characters,
and source the photo as a non-venue-specific CC0 frame the way 10-10 through 11-07
did.

---

## 2026-11-06 (Fri), reel / restaurant — SKIPPED

Thirty-ninth consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged. Every
number below was measured this run, not inherited from the 2026-11-05 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Fri 2026-11-06 13:00 KST, `%u` = 5 → **reel /
  restaurant**, Collab *candidate*. The task prompt independently specified
  `reel`; the two agree.
- §0: **no `pending` or `published` item for 2026-11-06.** `queue.json` holds **51**
  entries (**13** `published`, **38** `held`, **0** `pending`); no entry has a
  `2026-11-06` slug or `publish_at`. Nothing to stop on. Still **no ramp flag** in
  `queue.json` or repo notes — the only "ramp" matches are the prose at
  CONTENT.md:20 and PIPELINE.md:29 that *describe* the flag.
- §3 option 1 (owner original): **empty.** Resolved every `photo`/`bg_image` key
  across all **51** `content/*.json` against `assets/photos/`: **52** on disk, **52**
  referenced, **unused set = zero**, missing set = zero. `git ls-files` filtered for
  `mp4|mov|m4v|avi|webm|mkv|mp3|wav|m4a|heic|raw|dng|tiff` returns **zero** files —
  no owner footage for a Reel either. `git status --untracked-files=all` is **clean**,
  so nothing was dropped in for this run.
- §3 option 2 (venue/creator media with written permission): **no paperwork exists.**
  `git ls-files` filtered for `right|permis|licen|consent|partner|inbox|incoming|
  upload|submission|footage` returns **9** paths, and all 9 are the
  `2026-11-04-korea-cafe-licence-en` slug matching on "licen" — not a grant.
  Obtaining permission means contacting a venue, which an unattended run must not do.
- §3 option 3 (licensed stock): **barred for this format.** Stock is limited to "a
  non-venue-specific editorial Carousel". Today is a Reel, and the `restaurant`
  pillar is inherently venue-specific, so the escape hatch is closed on both counts.

Friday is additionally a **Collab candidate** day, which closes the gap a second
time: even with compliant media, §3 requires `collab_status: requested` and forbids
queueing the item as `pending` until a partner accepts — and an unattended run
cannot solicit that acceptance.

So §0 applies and the run stops without a queue item. The three possible fixes
remain editorial and reserved for a human — see the 2026-09-15 entry.

### Why this run did not ship a stock-photo restaurant Reel

Restating the 2026-11-05 finding because it still holds and nothing in code
prevents the breach: `validate_rights()` (scripts/publish.py:78) accepts
`asset_source: licensed_stock` for **any** `format`, so a stock-photo restaurant
Reel would have passed the publisher. It was not written because it would breach
PIPELINE.md §3 and CONTENT.md's "Generic stock must never be presented as the actual
venue" — it would show a stranger's photo of some other dining room as a named Seoul
restaurant. The policy/enforcement gap is the finding, not a licence to use it.

### Correction to the 2026-09-22 withdrawal: reel.py was exercised this run, and it fails

The 2026-09-22 note above withdrew the ffmpeg blocker and the 2026-11-05 entry could
not test it ("`scripts/reel.py` could not be exercised because there was no compliant
Reel to render"). **This run exercised it anyway**, against the existing
`2026-11-04-korea-cafe-licence-en` content, and recorded the actual failure:

```
File "scripts/reel.py", line 65, in build_segment -> run([...])
File "scripts/reel.py", line 45, in run -> subprocess.run(cmd, ...)
FileNotFoundError: [Errno 2] No such file or directory: 'ffmpeg'
```

`command -v ffmpeg` returns nothing, and `daily-content.yml` installs **pillow only**
(line 50-51) with no ffmpeg step. The 2026-09-22 withdrawal is still *technically*
right — the install is available at runtime — but two things are worth recording:
`reel.py` has **no preflight and no graceful failure**, it dies with a raw
`FileNotFoundError` partway through segment building; and the `ffmpeg 설치` step
requested on 2026-09-15 **still has not landed** in `.github/workflows/`, which an
agent cannot push. So the day media is unblocked, the first Reel run will crash
unless it remembers to `apt-get install -y ffmpeg` first. Cheap human fixes: add the
workflow step, and/or add an ffmpeg check to `reel.py`'s entry point.

### §2 research was done and works; the blocker is media, not facts

Research was carried out before the §3 stop, so the blocker is confirmed to be media
alone. Candidate for whenever a human unblocks media — a **new 2026 Bib Gourmand**
restaurant, none of which this account has covered except Gosari Express
(`2026-09-07-gosari-express-en`):

- **Oilje (오일제)** — perilla-seed seaweed soup (*deulkkae miyeok-guk*) and rice
  cooked to order in a cast-iron/stone pot in an open kitchen. **29 Hangang-daero
  62da-gil, Yongsan-gu, Seoul.** Current operation confirmed by its live Michelin
  Guide listing (an official listing per §2). Michelin's English page states
  "Reservations are not available for this restaurant on our site", so hours are
  **unconfirmed** and must be checked on Naver before any copy claims them.
- Other new 2026 Bib entries in Seoul, uncovered: **Andeok** (beef *naengguksu* and
  *mandutguk*, Jongno-gu), **3rd Samgyetang** (Seocho-gu), **Sobakeeri Suzu** (Korean
  buckwheat soba; neighborhood not given in source).
- Bib Gourmand price cap: a full meal **under 45,000 KRW** (~$31) per person.
- Useful English search phrase for travelers: "Michelin Bib Gourmand Seoul under
  45,000 won".

Sources: Korea JoongAng Daily, "Michelin releases 2026 Bib Gourmand, adds 8 new
Korean restaurants", 2026-02-26; Michelin Guide restaurant listing for Oilje.
As-of date 2026-11-06. Search totals for the 2026 Bib list **conflict across
outlets** (51 Seoul vs. 71 Korea-wide vs. a 77/58 figure from a blog that appears to
predate the final release); the Michelin site/app is authoritative and the count was
deliberately **not** used as a fact here.

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-11-06 Friday → reel / restaurant (§1).
- No same-day `pending`/`published` queue item (§0).
- **WebSearch works.** **WebFetch works** on koreajoongangdaily.com. WebFetch on
  `guide.michelin.com` returned an **empty document** (JS-rendered); the Oilje
  address came from the search index instead. Treat Michelin pages as search-only.
- **`scripts/cardnews.py` works:** re-rendered `2026-11-04-korea-cafe-licence-en` to
  a scratch directory — **7 slides, 1080×1350, exit 0, no errors** (pillow 13.0.0).
  Nothing was committed from this test.
- **`scripts/reel.py` is broken on this runner** — see the ffmpeg correction above.

### Still true: publishing is dead downstream of authoring

Unchanged and not re-tested this run (no item to publish). The last six Carousels
are all `held`; five carry the invalidated-token OAuthException code 190 and
`2026-10-24` carries the 2200-character caption cap. `2026-11-04-korea-cafe-licence-en`
was held 2026-11-05T02:54:43 KST on the same token error. Authoring a Reel today
would not have reached Instagram even if §3 had allowed it.

---

## 2026-11-05 (Thu), reel / bar — SKIPPED

Thirty-eighth consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged. Every
claim below was measured this run, not inherited from the 2026-11-03 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Thu 2026-11-05 13:04 KST, `%u` = 4 → **reel / bar**,
  Collab *optional*. The task prompt independently specified `reel`; the two agree.
- §0: **no `pending` or `published` item for 2026-11-05.** `queue.json` holds **51**
  entries (**13** `published`, **38** `held`, **0** `pending`) and no entry has a
  `2026-11-05` slug or `publish_at`. Nothing to stop on. Still **no ramp flag** in
  `queue.json` or repo notes — the only "ramp" occurrences are the prose at
  CONTENT.md:20 and PIPELINE.md:29 that *describe* the flag.
- §3 option 1 (owner original): **empty.** Resolved every `photo` and slide
  `bg_image` across all **51** `content/*.json` files against `assets/photos/`:
  **52** photos on disk, **52** referenced, **unused set = zero**. `git ls-files`
  filtered for `mp4|mov|m4v|avi|webm|mkv|mp3|wav|m4a|heic|raw|dng|tiff` returns
  **zero** files — no owner footage for a Reel either. The working tree is clean
  with `--untracked-files=all`, so nothing was dropped in for this run.
- §3 option 2 (venue/creator media with written permission): **no paperwork
  exists.** `git ls-files` filtered for `right|permis|licen|consent|partner|inbox|
  incoming|upload|submission|footage` returns **9** paths, and all 9 are the
  `2026-11-04-korea-cafe-licence-en` slug matching on "licen" — not a grant.
  Obtaining permission means contacting a venue, which an unattended run must not do.
- §3 option 3 (licensed stock): **barred for this format.** It is limited to "a
  non-venue-specific editorial Carousel"; today's slot is a Reel, and the `bar`
  pillar is inherently venue-specific.

So §0 applies and the run stops without a queue item. The three possible fixes
remain editorial and reserved for a human — see the 2026-09-15 entry.

### Why this run did not simply ship a stock-photo bar Reel

Worth stating plainly, because nothing in code would have stopped it.
`validate_rights()` (scripts/publish.py:78) accepts `asset_source: licensed_stock`
for **any** `format` — it does not encode §3's Carousel-only limit on stock. A
stock-photo bar Reel would therefore have passed the publisher and shipped. It was
not written because it would breach PIPELINE.md §3 and CONTENT.md's "Generic stock
must never be presented as the actual venue" — i.e. it would show a stranger's
photo of some other room as a named Seoul bar. The gap between the policy and its
enforcement is the finding here, not a licence to use it.

### §2 research was done and works; the blocker is media, not facts

Research was carried out before the §3 stop, so the blocker is confirmed to be
media alone. `Asia's 50 Best Bars 2026` (announced 2026-07-28, Wynn Palace, Macau)
puts **four** Seoul bars on the 1–50 list: **Zest** (No. 2, Cheongdam-dong, best in
Korea three years running), **Alice** (No. 13, Gangnam), **Bar Cham** (No. 33, a
restored hanok in Jongno, down from No. 6) and **M+MS** (No. 42, new entry).
Source: Korea Times, 2026-07-29, as-of date 2026-11-05.

Note for a future bar run: **all four are already covered** by this account —
`2026-08-25-zest-seoul-en`, `2026-09-05-alice-cheongdam-en`, `2026-08-29-bar-cham-en`,
`2026-09-01-mms-bar-en`. One outlet (Korea Stripes) reports eight Seoul bars rather
than four, presumably counting the 51–100 "bubbling under" list; that was not
resolved this run and should be checked against the official list before use.

### Verified working this run

- `TZ=Asia/Seoul date` → 2026-11-05 Thursday → reel / bar (§1).
- No same-day `pending`/`published` queue item (§0).
- **WebSearch works.** **WebFetch works** on koreatimes.co.kr.
- **`scripts/cardnews.py` works:** re-rendered `2026-11-04-korea-cafe-licence-en`
  to a scratch directory — **7 slides, 1080×1350, no errors** (pillow 13.0.0).
  Nothing was committed from this test.
- **ffmpeg is absent from the runner image again** this run (`ffmpeg -version`
  returns nothing). Per the 2026-09-22 withdrawal above this is a per-run install
  step, not a blocker, but `scripts/reel.py` could not be exercised because there
  was no compliant Reel to render in the first place.

### Still true: publishing is dead downstream of authoring

`2026-11-04-korea-cafe-licence-en` — the Carousel authored yesterday, the one format
that can still be written — was **held at 2026-11-05T02:54:43 KST** with the same
invalidated-token error (code 190) that took 10-10, 10-17, 10-21 and 10-31. So the
last successful publish remains **2026-10-07**. Authoring a compliant Carousel still
produces a held item; the token needs a human.

---

## 2026-11-03 (Tue), reel / local — SKIPPED

Thirty-seventh consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged and was
re-derived mechanically this run, not inherited from the 2026-11-02 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Tue 2026-11-03 13:26 KST, `%u` = 2 → **reel / local**,
  Collab *candidate*. The task prompt independently specified `reel`; the two agree.
- §0: **no `pending` or `published` item for 2026-11-03.** `queue.json` holds **50**
  entries (**13** `published`, **37** `held`, **0** `pending`) and the string
  `2026-11-03` does not appear in it. Nothing to stop on. No ramp flag is set in
  `queue.json` or repo notes — the only occurrences of "ramp" are the prose in
  CONTENT.md:20 and PIPELINE.md:29 that *describe* the flag.
- §3 option 1 (owner original): **empty.** All **51** files in `assets/photos/` are
  referenced by one of the **50** `content/*.json` files (resolved every `photo` and
  every slide `bg_image`), so the unused set is **zero**. `git ls-files` filtered for
  `mp4|mov|m4v|avi|webm|mkv|mp3|wav|m4a|heic|raw|dng|tiff` returns **zero** files, so
  there is no owner footage for a Reel either. The newest photos added (2026-10-31,
  10-24, 10-21, 10-17) are all editorial Carousel stock covers.
- §3 option 2 (venue/creator media with written permission): **no paperwork exists.**
  `git ls-files` filtered for `right|permis|licen|consent|partner|inbox|incoming|
  upload|submission|footage` returns **zero** paths. Obtaining permission means
  contacting a venue, which an unattended run must not do.
- §3 option 3 (licensed stock): **barred for this format.** It is limited to "a
  non-venue-specific editorial Carousel"; today's slot is a Reel, and the `local`
  pillar on a Collab-candidate day is venue-specific. Also §3's Collab rule would
  hold the item at `collab_status: requested` regardless.

So §0 applies and the run stops without a queue item. The three possible fixes
remain editorial and reserved for a human — see the 2026-09-15 entry.

### Correction to the 2026-09-15 entry: policy-v2 metadata is no longer unimplemented

That entry recorded that **zero** of the then-40 `content/` files carried
`policy_version`, `asset_source`, `rights_confirmed` or `rights_note`. That is now
stale. Measured this run: **10 of 50** files carry **all four** fields. Every one of
the 10 declares `asset_source: licensed_stock` with `rights_confirmed: true`, a
specific per-photo `rights_note` (named photographer, licence, Wikimedia/Commons
file, verification date), and `format: carousel`.

The practical reading: policy v2 is implemented and being followed correctly, but it
has only ever been exercised in the **one** combination §3 permits — stock on an
editorial Carousel. The Reel blocker is therefore purely **media acquisition**, not
missing plumbing. Nothing in the authoring path needs fixing for a compliant Reel to
be written; the media simply does not exist in the repo.

### The dead token is confirmed fresher than the log claimed

The 2026-10-25 entry said the token blocker was "last-tested 10-17 and should still
be assumed to stand". It has since been tested twice more and still stands:
`2026-10-31-seoul-tourist-zones-en` was held **2026-11-01T00:41:00 KST** with
`hold_reason: publish_failed_manual_review` and OAuthException **code 190**, "The
session has been invalidated because the user changed their password". So the token
is dead as of **2026-11-01**, not 10-17. Re-authorisation remains a human step; the
monthly refresh cron cannot fix an invalidated session.

### The caption-cap drift reversed — the 10-24 lesson was applied

The 2026-10-25 entry predicted the next Carousel would also run over 2200. It did
not. Measured across the ten policy-v2 Carousels (caption + 2 + hashtags):

929, 1229, 1374, 1689, 1526, 1572, 1964, 2104, **2328 (held 10-24)**, **2051 (10-31)**

The 10-31 run came in **149 characters under** the cap, so the explicit budget
worked. The recommended human fix still stands and is still unapplied: neither
PIPELINE.md §4 nor CONTENT.md states the 2200-character cap, so the budget survives
only as advice in this file. `build_caption()` (scripts/publish.py:65-75) still
raises at *publish* time, hours after the run that could have fixed it.

### Still open: publish.py is more permissive than PIPELINE.md §3

Re-verified in source this run. `validate_rights()` (scripts/publish.py:78-93) skips
all rights checks when `policy_version < 2` (40 of 50 files), and for v2 content
accepts any `asset_source` in `{original, partner_licensed, licensed_stock}`
**regardless of `format`**. It does not encode §3's "stock only for a
non-venue-specific editorial Carousel" rule, so a stock-photo Reel would pass the
publisher while violating PIPELINE.md. It does correctly enforce the Collab gate
(`collab_status == "accepted"`).

### Verified working this run — the environment is sound

The blocker is editorial only. Everything mechanical works:

- `TZ=Asia/Seoul date` → 2026-11-03 Tuesday (§1).
- **WebSearch works.** **WebFetch works** (fetched `english.visitkorea.or.kr`
  successfully).
- `python3 scripts/cardnews.py` renders **7 slides at 1080×1350** with no errors
  (pillow 13.0.0).
- **ffmpeg is absent from the runner image but `sudo apt-get install -y ffmpeg`
  succeeded this run** (6.1.1-3ubuntu5), confirming the 2026-09-22 withdrawal of the
  ffmpeg blocker. With it, `scripts/reel.py` produced a valid **1080×1920, 22.2s**
  MP4 end-to-end. The only warning is the expected gitignored-music one
  (`local.mp3` absent → ffmpeg-synthesized audio).

Both renders were written to `/tmp`, not `out/`, to leave the tree clean.

---

## 2026-11-02 (Mon), reel / restaurant — SKIPPED

Thirty-sixth consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged and was
re-derived mechanically this run, not inherited from the 2026-11-01 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Mon 2026-11-02 12:10 KST, `%u` = 1 → **reel /
  restaurant**, Collab optional. The task prompt independently specified `reel`;
  the two agree.
- §0: **no `pending` or `published` item for 2026-11-02.** `queue.json` holds **50**
  entries (**13** `published`, **37** `held`, **0** `pending`) and the string
  `2026-11-02` does not appear in it. Nothing to stop on.
- §3 option 1 (owner original): **empty.** All **51** files in `assets/photos/` are
  referenced by one of the **50** `content/*.json` files (resolved every `photo` and
  every slide `bg_image`), so the unused set is **zero**. `git ls-files` filtered for
  `mp4|mov|m4v|avi|webm|mkv|mp3|wav|m4a|heic|raw|dng|png|tiff` returns **zero** files,
  so there is no owner video for a Reel either. No human commit since **2026-09-14**
  (`git log` by author: 84 claude[bot], 60 github-actions[bot], 14 Steve, none of the
  latter since 09-14), and no human-added photo since `cheongildip-en.jpg` on
  2026-08-25 (392aefd), which predates the policy.
- §3 option 2 (venue/creator media with written permission): **no paperwork exists.**
  `git ls-files` filtered for `right|permis|licen|consent|partner|inbox|incoming|
  upload|submission|original|footage` returns **zero** paths. `git fetch --all` leaves
  `main` level with `origin/main` at 42a3bba, `main` is the only branch, tree clean —
  no new media channel appeared. Obtaining permission means contacting a venue, which
  an unattended run must not do. The Creative-Commons reading of option 2 was tested
  and rejected on 2026-11-01; not re-litigated here.
- §3 option 3 (licensed stock): legal and available, but restricted to a
  **non-venue-specific editorial Carousel**. The restriction binds on **format**, so
  the escape hatch of writing a venue-less editorial restaurant topic is closed too —
  it would still be a Reel. A fresh audit agrees: of 50 content files, **10** carry
  `policy_version: 2` and all ten are `('carousel', 'licensed_stock')`. **Zero** files
  anywhere declare `original` or `partner_licensed`.
- No ramp flag is set in `queue.json` or `.github/` (PIPELINE.md §1), so the ramp
  constrained nothing and the skip is decided on §3 grounds alone.

Stopped under §0: "If rights, venue existence, or current operation cannot be
verified, stop without adding a queue item."

### CORRECTION — the last successful publish is 2026-10-07, not 2026-09-26

The 2026-11-01 entry states the account "has not [shipped] since 2026-09-26." That
is wrong, and it understates the account by one post. `queue.json` has **13**
`published` items and the newest is **`2026-10-07-seoul-cafe-churn-en`**, media_id
**17885158536504317**, posted 2026-10-08T02:22:59 KST. (The 2026-10-18 entry records
this correctly; the 11-01 entry contradicts it.) The 09-26 date is the *first*
success after the action-block run, not the last success.

This matters for the token timeline a human will reconstruct: the token **worked on
2026-10-07** and first failed on **2026-10-10**. So code 190 dates from somewhere in
10-08…10-10, which is consistent with a password change or forced session reset in
that window rather than a long-standing fault. Holds on code 190 since: 10-10,
10-17, 10-21, 10-31 (10-24 was the caption cap, not the token). Five items have been
held since the last success.

### The caption drift broke — the 10-25 budget advice worked, but only just

The 2026-10-25 entry predicted the caption would keep climbing past 2200 unless the
budget was made explicit. Measured across all ten policy-v2 Carousels this run
(`caption` + 2 + hashtags joined by spaces, i.e. what `publish.py:build_caption()`
concatenates):

| Date | total | | Date | total |
|---|---|---|---|---|
| 09-16 | 929 | | 10-10 | 1572 |
| 09-19 | 1229 | | 10-17 | 1964 |
| 09-23 | 1374 | | 10-21 | 2104 |
| 09-26 | 1689 | | 10-24 | **2328 — over** |
| 10-07 | 1526 | | 10-31 | **2051 — under** |

10-31 is the **first decrease since 09-16** and the first Carousel authored after the
cap was documented here, so the advice landed. But 2051 is only **149 characters**
under the limit, which is less headroom than 10-21 had before it went over. The
recommendation from 10-25 therefore still stands unchanged and is still a human fix:
state the 2200-character cap in PIPELINE.md §4 / CONTENT.md, or move
`build_caption()`'s length check into an authoring-time preflight so an over-length
caption fails the run that can still fix it.

### Restaurant-beat research, for whenever §3 opens — and two traps in it

The 2026-10-30 entry listed four uncovered Michelin subjects. Verified and expanded
this run from Asia Economy's English report on the **Michelin Guide Seoul & Busan
2026** announcement (5 March 2026, Signiel Busan), fetched this run:

- Three stars: **Mingles** (second consecutive year) — already covered (08-28).
- Two stars: **Mosu** (returned after a closure) and **Sosuheon** (promoted from one
  star). Ten two-star restaurants were awarded across Seoul and Busan; the article
  names only these two.
- New Seoul one stars: **Collage**, **Giwagang**, **Restaurant San**, **Sushi
  Kanesaka**. Promoted from Michelin-selected: **Gaggan by Choi Junho**,
  **Restaurant Jueun**, **Hakushi**. Busan: **Ledohé**.

Against the 11 existing `pillar: restaurant` posts (Onjium ×2, Mingles, Le DORER ×2,
Balwoo Gongyang, Gogung Jeonju, GiwaKang, Yong Fu Jeju, Gosari Express, Sosuheon),
the uncovered and newly-ranked set is **Mosu, Collage, Restaurant San, Sushi
Kanesaka, Gaggan by Choi Junho, Restaurant Jueun, Hakushi** — seven subjects, all
verifiable from an official listing, which satisfies §2 comfortably. The well is not
dry.

Two traps found while checking Mosu, both of which would have produced a false
statement in a published post:

1. **Mosu has two stars, not three.** A Daum/Hankyung headline still in search
   results calls it "Michelin 3-star Mosu Seoul." The 2026 guide gives it **two**;
   Mingles is Korea's only three-star. Do not take a star count from a headline.
2. **Mosu's Hannam address is stale.** It closed, then reopened in **March 2025** in
   Yongsan-gu — secondary sources give `4 Hoenamu-ro 41-gil, Yongsan-gu, Seoul
   04344`, near Grand Hyatt Seoul, and warn that older listings still show
   Itaewon/Hannam. **This address is not verified** — `guide.michelin.com`'s Mosu page
   returned an empty body to WebFetch this run, so no official listing was read.
   Treat the address as unconfirmed and re-verify from the venue or the Michelin
   listing before it is used in copy. The general lesson for §2: for any venue that
   has closed and reopened, an address found in pre-2025 coverage fails the
   "current operation" test even when the venue itself is fine.

Also unchanged from 10-30: **Sosuheon's existing 09-09 post predates its two-star
promotion** and may state the wrong star count. Worth a human check before reuse.

### Verified working this run

- `scripts/cardnews.py` renders **7 slides**, exit 0, each **1080×1350** — run on
  `content/2026-10-31-seoul-tourist-zones-en.json` into `/tmp/rendercheck`, outside
  the repo. **Nothing was committed from it.**
- `pillow` **13.0.0** present without installing anything.
- **WebSearch works.** **WebFetch works** on `asiae.co.kr` (returned the full 2026
  Michelin rating list). **WebFetch returned an empty body for
  `guide.michelin.com`** — a new data point; the Carousel days have relied on
  `commons.wikimedia.org`, which was last proven 2026-11-01.
- **`ffmpeg` still absent** from the runner image (`which ffmpeg` → nothing), and the
  `ffmpeg 설치` step requested on 2026-09-15 still has not landed in
  `daily-content.yml`. Per 2026-09-22 this is a per-run install, not a blocker; it was
  not installed today because the §3 gate fails upstream of §4, so `scripts/reel.py`
  was **not** exercised. Treat the MP4 path as last-proven 2026-10-29.
- `--max-turns 60` is still at `daily-content.yml:80`. This run stayed well inside it
  by batching each audit into a single `python3`/`git` call. **The next run that can
  produce anything is Wed 2026-11-04 (Carousel, cafe)** — it faces the turn cap, then
  the 2200-character caption budget, then the dead token.

### One note on this run's invocation

The operator prompt's `DRY RUN 여부:` field again arrived **empty** (same as
2026-11-01). Treated as not true, i.e. a live run, so this skip note is committed. No
content, queue or asset change was made either way. The prompt also instructed the
run to render seven slides and commit them alongside a content JSON; PIPELINE.md is
the stated source of truth and its §0/§3 gate fails before §4, so no content was
authored and nothing was rendered into the repo. The render path was proven
separately, to a temp directory, as recorded above.

---

## 2026-11-01 (Sun), reel / cafe — SKIPPED

Thirty-fifth consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged and was
re-derived from the repo this run, not inherited from the 2026-10-30 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Sun 2026-11-01 12:00 KST, `%u` = 7 → **reel / cafe**,
  Collab optional.
- §0: no `pending` or `published` queue item for 2026-11-01. 50 queue entries, the
  newest being the 10-31 Carousel (`held`). Nothing to stop on there.
- §3 option 1 (owner original): still nothing. `git log --author=steve.seil.oh`
  shows **no human commit since 2026-09-14** and no human-added media since
  `assets/photos/cheongildip-en.jpg` on 2026-08-25 (392aefd), which predates the
  policy. All 51 files in `assets/photos/` were fetched by pipeline runs.
- §3 option 2 (venue/creator media with written permission): unobtainable by an
  unattended run — see the new finding below for the one route that looked open.
- §3 option 3 (licensed stock): legal and available, but limited to a
  **non-venue-specific editorial Carousel**. Today is a Reel, so it is closed.
  CONTENT.md "Media and rights" agrees independently: "Venue-specific Reels and
  Collabs must use original or written partner-authorized media."

### NEW — the Creative Commons route was checked properly and does not open §3

Previous entries asserted option 2 was unobtainable without testing it. This run
tested the strongest version of it: a third-party photo under a standing public
license, which is arguably "written permission" already granted. Searched
Wikimedia Commons and government open-license galleries. What exists:

- `File:Coffee_Prince_interior.JPG` on Commons — interior of the first Coffee
  Prince shop, Hongdae, Mapo-gu. **CC BY-SA 3.0 Unported**, author "Michaela den"
  (own work), shot **2012-09-20**.
- Mapo-gu's tourism gallery (600+ photos) is **KOGL/Public Nuri Type 1** — free
  commercial use with attribution. Busan's tourism archive has Type 0 images.
  Both are real, usable licenses.

So compliant *licensing* is genuinely obtainable. It still fails, for two
independent reasons, and the second is the load-bearing one:

1. **This candidate also fails §2.** A 2012 interior photo cannot honestly
   illustrate the venue in 2026, and Coffee Prince's current operation was not
   verified. §2 requires current operation; §3 forbids presenting a photo as a
   place it no longer depicts.
2. **A stranger's CC photo is option 3, not option 2.** "Venue/creator media with
   written permission" most plausibly means media from the venue or a creator the
   account has an exchange with. A Commons upload or a district tourism gallery is
   third-party licensed media — exactly what option 3 describes, and option 3 is
   Carousel-only. Reading it into option 2 would route around the restriction the
   owner added deliberately: 8128750 (2026-09-14) **removed** the previous §4
   allowance for mood-matched Unsplash stock. An unattended run reinstating that
   by reinterpretation would be overriding the source of truth on its own
   judgment, which §0 and CONTENT.md both forbid.

**For a human this is the cheapest of the three fixes in the 2026-09-15 entry.**
KOGL Type 1 and CC BY are commercially usable with attribution, and the pipeline
already renders an attribution line on the sources slide. If the intent is that
publicly licensed media which *genuinely and currently depicts the named venue*
is acceptable for a Reel, then **say so in PIPELINE.md §3 as a fourth option**
with the two guards that matter — the photo must depict the named venue, and it
must be recent enough to still be true — and Reel days unblock immediately
without reopening the mood-photo loophole. That edit is one paragraph and it is
the only one of the three fixes that needs no new assets and no human photography.

### The token is still dead, and the publisher's commit message hides it

Fourth confirmation, and the most misleading one yet. The 10-31 Carousel
(`2026-10-31-seoul-tourist-zones-en`) was authored and rendered correctly, picked
up by the 19:00 KST publisher, and **held** at 2026-11-01T00:41:00 KST with the
same OAuthException **code 190** "session has been invalidated"
(`fbtrace_id AUUIJ0wwDxsBQWmFFGZT4C5`). Holds on this fault: 10-10, 10-17, 10-21,
10-31. The 10-24 hold was the caption cap, not the token.

**The commit that recorded this is titled `publish: mark posted` (f397f80).** Its
only change is `status: pending` → `status: held` with a code 190 error. A human
skimming `git log` sees "publish: mark posted" on 11-01 and reasonably concludes
the account is shipping; it is not, and has not since 2026-09-26. Worth fixing in
`scripts/publish.py` so the message reflects the outcome — this is the kind of
fault that stays invisible precisely because the log claims success.

`IG_ACCESS_TOKEN` must be re-authorized through Instagram Login by a human
(CONNECT-GUIDE.md). An agent cannot: it is a repository secret, and
`refresh-token.yml` only extends still-valid tokens.

### Verified working this run

- `scripts/cardnews.py` renders 7 slides at 1080×1350, exit 0, no errors
  (smoke-tested on the 10-31 content JSON to a temp dir, not committed).
- WebSearch works. WebFetch works on `commons.wikimedia.org`.
- pillow 13.0.0 present. **ffmpeg still absent** from the runner image — per the
  2026-09-22 entry it is installable at runtime, so it remains a per-run setup
  step rather than a blocker, and it was not needed today.

### One note on this run's invocation

The operator prompt's `DRY RUN 여부:` field arrived **empty**. Treated as not
true, i.e. a live run, so this skip note is committed; no content, queue or asset
change was made either way, so the two readings differ only in whether this
paragraph exists. If the field was meant to carry `true`, the dry-run contract was
still honoured in substance.

---

## 2026-10-30 (Fri), reel / restaurant — SKIPPED

Thirty-fourth consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged and was
re-derived mechanically this run rather than inherited from the 2026-10-29 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Fri 2026-10-30 12:21 KST, `%u` = 5 → **reel /
  restaurant / Collab candidate**. The task prompt independently specified `reel`;
  the two agree.
- §0: **no `pending` or `published` item for 2026-10-30.** `queue.json` holds **49**
  entries (**13** `published`, **36** `held`, **0** `pending`) and the string
  `2026-10-30` does not appear in it. Nothing to stop on, so the run proceeded.
- §3: a Reel needs option 1 (owner original) or option 2 (venue/creator media with
  written permission). Option 3 (licensed stock) is restricted to a
  non-venue-specific editorial **Carousel** — the restriction binds on **format**,
  and CONTENT.md "Media and rights" says the same independently ("limited to an
  occasional editorial Carousel"). So the Friday escape hatch of writing an
  editorial restaurant topic with no named venue is closed too: it would still be a
  Reel.
- **Neither option 1 nor option 2 exists in the repo.** All **50** files in
  `assets/photos/` are referenced by one of the **49** `content/*.json` files
  (checked by resolving every `photo` and every slide `bg_image`), so the unused set
  is **empty**. `git ls-files` filtered for
  `mp4|mov|m4v|avi|webm|mkv|mp3|wav|m4a|heic|raw|dng|png` returns **zero** files, so
  there is no owner video for a Reel either.
- A fresh audit of all 49 content files: **9** carry `policy_version: 2` and all nine
  are `asset_source: licensed_stock` on a `carousel`. **Zero** files anywhere in the
  repo declare `original` or `partner_licensed`.
- No rights paperwork exists to support option 2: `git ls-files` filtered for
  `right|permis|license|consent|partner` returns **zero** paths. Obtaining written
  permission would mean contacting a venue, which an unattended run must not do.
- No new media channel appeared: `git fetch --all` leaves `main` level with
  `origin/main` at 375c240, `main` is the only branch, the tree is clean, and no
  `inbox/`, `incoming/`, `uploads/`, `media/`, `submissions/`, `originals/` or
  `footage/` path exists. No human has added media since 2026-08-25.
- No ramp flag is set in `queue.json` or `.github/` (PIPELINE.md §1), so the ramp
  constrained nothing and the skip is decided on §3 grounds alone.

Stopped under §0: "If rights, venue existence, or current operation cannot be
verified, stop without adding a queue item."

### Verified working this run

- `scripts/cardnews.py` renders **7 slides**, exit 0, each **1080×1350** — run on
  `content/2026-10-24-korea-address-system-en.json` into `/tmp/rendercheck`, outside
  the repo. **Nothing was committed.**
- `pillow` **13.0.0** is present without installing anything.
- **WebSearch works** and **WebFetch works** (`koreajoongangdaily.com` returned the
  Michelin Seoul & Busan 2026 star list; `commons.wikimedia.org`'s `api.php`
  returned `extmetadata` with a parseable `LicenseShortName` / `AttributionRequired`
  pair, which is the licence-verification path the Carousel days depend on).
- **`ffmpeg` is still absent from the runner** (`which ffmpeg` → nothing) and the
  `ffmpeg 설치` step requested on 2026-09-15 still has not landed in
  `daily-content.yml`. Per the 2026-09-22 note this is a per-run install, not a
  blocker, and it was **not** installed this run because the §3 gate fails upstream
  of §4 — so `scripts/reel.py` was not exercised today. Treat the MP4 path as
  last-proven on 2026-10-29.
- `--max-turns 60` is still in `daily-content.yml:80`, so the Carousel-day risk
  recorded on 2026-10-29 (four of the last nine Carousels lost to the turn cap) is
  unchanged. This run stayed well inside it by batching the audit into single
  `python3`/`git` calls.

### Worth knowing before the next restaurant day: the Michelin well is not dry

Unlike the bar beat (2026-10-29 found all eight ranked Seoul bars already covered),
the restaurant beat still has unused verified subjects. The **11** existing
`pillar: restaurant` posts are Onjium (twice, 08-26 and 09-11), Mingles, Le DORER
(twice, 08-30 and 09-13), Balwoo Gongyang, Gogung Jeonju, GiwaKang, Yong Fu Jeju,
Gosari Express and Sosuheon.

From **Michelin Guide Seoul & Busan 2026**, announced 5 March 2026 (Korea JoongAng
Daily, fetched this run, article modified 11 March 2026): the two Seoul two-star
promotions were **Mosu** and **Sosuheon**, and the four Seoul one-star debuts were
**GiwaKang**, **SAN**, **Sushi Kanesaka** and **Collage**. Of those six, GiwaKang and
Sosuheon are already covered — so **Mosu, SAN, Sushi Kanesaka and Collage are
uncovered, newly-ranked, and verifiable from an official listing**, which satisfies
§2 comfortably. Note also that Sosuheon's existing 09-09 post predates the promotion
and may describe it at the wrong star count; worth a human check before it is reused.

None of this was verified to full §2 standard (address and current operation were not
confirmed) because there was no point: the gate that fails is upstream, and no amount
of verified venue fact produces a publishable Reel without compliant media. It is
recorded so that whoever supplies original photos knows **which four venues to shoot
first** — that is the single action that converts this backlog into posts.

**Not done, deliberately:** the format was not swapped to Carousel to get a post out.
PIPELINE.md §1 assigns Friday a Reel and the task prompt says `reel`; moving venue
days to Carousel is one of the three fixes listed in the 2026-09-15 entry and is an
editorial decision for a human. A stock photo was not used on a Reel, and a
typography-only cover was not used either — the task prompt rules it out for this
account, and §3 would reject the first. Also not done: setting `collab_required` on a
speculative Friday Collab (§3 forbids queueing one as pending before a partner
accepts, and no partner has been contacted), reviving any of the 36 `held` items
(§0), catching up 2026-10-28 or any other missed day (§0), and editing PIPELINE.md /
CONTENT.md / `daily-content.yml` — those are changes to the source of truth and to a
workflow file, and are reserved for a human.

---

## 2026-10-29 (Thu), reel / bar — SKIPPED

Thirty-third consecutive Reel-day skip. No content JSON, no rendered output
committed, no change to `queue.json`. The §3 media blocker is unchanged and was
re-derived mechanically this run rather than inherited from the 2026-10-27 entry.

### The §3 decision, re-derived this run

- §1: `TZ=Asia/Seoul date` → Thu 2026-10-29 12:19 KST, `%u` = 4 → **reel / bar /
  Collab optional**. The task prompt independently specified `reel`; the two agree.
- §0: **no `pending` or `published` item for 2026-10-29.** `queue.json` holds **49**
  entries (**13** `published`, **36** `held`, **0** `pending`) and the string
  `2026-10-29` does not appear in it. Nothing to stop on, so the run proceeded.
- §3: a Reel needs option 1 (owner original) or option 2 (venue/creator media with
  written permission). Option 3 (licensed stock) is restricted to a
  non-venue-specific editorial **Carousel**, and CONTENT.md "Media and rights" says
  the same independently. This binds on **format**, so the Thursday/bar escape — a
  drink or a cocktail style as the subject rather than one venue — is closed too.
- **Neither option 1 nor option 2 exists in the repo.** All **50** files in
  `assets/photos/` are referenced by one of the **49** `content/*.json` files, so the
  unused set is **empty**. `git ls-files` filtered for
  `mp4|mov|m4v|avi|webm|mkv|mp3|wav|m4a|heic|raw|dng|png` returns **zero** files, so
  there is no owner video for a Reel either.
- A fresh audit of all 49 content files: **9** carry `policy_version: 2` and all nine
  are `asset_source: licensed_stock` on a `carousel`. **Zero** files anywhere in the
  repo declare `original` or `partner_licensed`.
- Primary evidence that the existing bar photos are the forbidden case, read this run
  from the file rather than from an earlier entry: the sources slide of
  `content/2026-09-10-le-chamber-en.json` ends "Photo: Unsplash License (Adam Jaime)
  — a representative classic cocktail, **not Le Chamber itself**". That is precisely
  §3's "Do not use a mood photo as if it depicts the named place." The same pattern
  covers all nine `pillar: bar` posts, so none of their photos can be reused today.
- No new media channel appeared: `git fetch --all` leaves `main` level with
  `origin/main` at f1e947d, `main` is the only branch, the tree is clean, and no
  `inbox/`, `incoming/`, `uploads/`, `media/`, `submissions/`, `originals/` or
  `footage/` path exists. No human has added media since 2026-08-25.
- No ramp flag is set in `queue.json`, `.github/` or `scripts/` (PIPELINE.md §1), so
  the ramp constrained nothing and the skip is decided on §3 grounds alone.

Stopped under §0: "If rights, venue existence, or current operation cannot be
verified, stop without adding a queue item."

### Verified working this run — the whole render path, including the MP4

This is the first entry to prove **both** §4 render steps in one run, which isolates
§3 as the only remaining blocker on a Reel day:

- `scripts/cardnews.py` renders **7 slides**, exit 0, each **1080×1350**.
- `sudo apt-get install -y ffmpeg` **succeeds on this runner** (exit 0,
  `/usr/bin/ffmpeg`), and with it `scripts/reel.py` produced a valid
  **1080×1920, 22.20s** MP4 — 9:16 confirmed by `ffprobe`, not by filename. Before
  the install, `reel.py` fails with `FileNotFoundError: 'ffmpeg'` at
  `scripts/reel.py:45`; note it exits **0** on that traceback, so a caller that
  checks only the exit status would read the failure as success.
- Both were run on `content/2026-10-24-korea-address-system-en.json` into
  `/tmp/rendertest`, outside the repo. **Nothing was committed.**
- The `ffmpeg 설치` step requested on 2026-09-15 still has not landed in
  `daily-content.yml`; it costs each run an install but blocks nothing.
- **WebSearch works** and **WebFetch works** (`korea.stripes.com` returned the
  Asia's 50 Best Bars 2026 Seoul set). Recorded as a tool check — see below for the
  one editorially useful fact that fell out of it.

### Worth knowing before the next bar day: the bar beat is fully covered

Not a blocker, but it changes what a human should supply media for. The eight Seoul
entries on **Asia's 50 Best Bars 2026** are Zest No. 2, Alice No. 13, Bar Cham
No. 33, M+MS No. 42, Space No. 74, Charles H. No. 87, Le Chamber No. 88 and Soko
No. 89 (`korea.stripes.com`, fetched this run). **All eight already have posts** —
and note that "Space" is 공간/**Gong-Gan**, covered on 2026-09-12 at the same No. 74,
so the two names are one venue and the set really is exhausted. Mr. Ahn's Craft
Makgeolli, the obvious non-ranked candidate, was covered on 2026-08-27.

So the next bar Reel needs either a venue off that list or a fresh angle on a covered
one, and the ranked-list well is dry. Candidates that surfaced but were **not
verified to §2 standard** and must not be used as-is: Damotori, Neulin Maeul Brewery
(Euljiro) and Juan Makgeolliano — all three appeared only in blogs and travel
aggregators, with no official listing or credible recent source behind them. Full
§2 verification was not attempted, because the gate that fails is upstream: no amount
of verified venue fact produces a publishable Reel without compliant media.

**Not done, deliberately:** the format was not swapped to Carousel to get a post out.
PIPELINE.md §1 assigns Thursday a Reel and the task prompt says `reel`; moving venue
days to Carousel is one of the three fixes listed in the 2026-09-15 entry and is an
editorial decision for a human. Also not done: reviving any of the 36 `held` items
(§0), catching up 2026-10-28 or any other missed day (§0), and editing PIPELINE.md /
CONTENT.md to document the caption cap or raise `--max-turns` — those are changes to
the source of truth and to a workflow file, and are likewise reserved for a human.

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
