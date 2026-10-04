# Skipped days — ongoing media-rights blocker

The media-rights blocker below stops every **Reel** day (Mon/Tue/Thu/Fri/Sun). It
does **not** stop Wed/Sat, which are Carousels: PIPELINE.md §3 option 3 allows
licensed stock on a non-venue-specific editorial Carousel. Each entry below
records one skipped run. Stopped under PIPELINE.md §0 ("If rights ... cannot be
verified, stop without adding a queue item"). As of 2026-10-04 that is **fifteen
consecutive Reel-day skips**, and with the action block withdrawn and the render
path proven it is the only thing holding the account below a daily schedule. The
three possible fixes are editorial and reserved for a human — see the 2026-09-15
entry.

**Both Carousel days since 2026-09-26 produced nothing, and the account is now at
zero posts a week.** 2026-09-30 (Wed) and 2026-10-03 (Sat) are the two unexplained
gaps in this file: Carousel days, the one format the media blocker does **not**
stop, each with no content commit, no queue entry and no skip entry. `git log`
shows commits on 09-29, 10-01 and 10-02 but nothing on 09-30 or 10-03, so the gaps
are not an artefact of a missing log entry. Either those runs did not fire or they
ended without writing anything. **This is now the more urgent of the two problems**
— the media blocker costs five days a week, but a silent Carousel failure costs the
remaining two, and the last successful publish was 2026-09-26. Worth a human look at
the `daily-content.yml` run history. Not caught up here: §0 forbids catching up
missed days.

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
