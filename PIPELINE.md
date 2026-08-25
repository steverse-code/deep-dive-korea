# Daily automated pipeline (cloud-only)

This document is the **exact procedure the agent triggered by
`.github/workflows/daily-content.yml` follows.** Adapted from ig-studio's pipeline
for this account: DeepDive Korea (@deep_dive_korea), an **English-language** account
covering real, verified restaurants/cafes/bars/local spots in Korea.
The agent starts with zero context, so this document alone must be enough to finish
the job end to end.

The big picture:

```
daily-content.yml  09:00 / 15:00 KST  →  research, write, render, commit (this doc)
publish.yml        every 30 min       →  publishes whichever queued post is due
refresh-token.yml                     →  refreshes the Instagram token
```

Assumptions:
- Working directory = this repo's checkout (don't assume a path — confirm with
  `git rev-parse --show-toplevel`)
- The workflow sets `TZ=Asia/Seoul`, so the runner's `date` reads KST. Still,
  **always get today's date/weekday via an explicit `TZ=Asia/Seoul date` call**
  (the runner's raw default is UTC, and using it naively shifts the date by one
  between midnight and 9am KST)
- This agent does **not** publish to Instagram directly. GitHub Actions'
  `publish.yml` drains the queue every 30 minutes (see §7)

---

## 0. Time budget — 20 minutes

Note `date +%s` at the start. Check elapsed time after each research step.

- If 15 minutes pass with no verified material: wrap up with what you have, or write
  a skip note and stop
- Past 20 minutes: stop immediately and write a skip note
- Exception: **if content is already committed, finish the push regardless.** The
  budget is for research, not for cleanup

When skipping, write `SKIPPED.md` at the repo root and commit+push it (local `/tmp`
disappears when the cloud session ends — nobody else will ever see it). Note what was
missing, and record any already-verified material so the next run can pick it up.

## 1. Decide today's subcategory

```
TZ=Asia/Seoul date +%u    # 1=Mon ... 7=Sun
```

| Day | AM | PM |
|---|---|---|
| Mon | restaurant | cafe |
| Tue | bar | local |
| Wed | restaurant | cafe |
| Thu | bar | local |
| Fri | restaurant | cafe |
| Sat | bar | local |
| Sun | restaurant | cafe |

This table must match `CONTENT.md` §1. If they disagree, **trust CONTENT.md**.

## 2. Read the standards before writing anything

- `CONTENT.md` in full — especially §2 tone rules, §3 photography requirement
  (mandatory — see §4 below for the exact workflow), §4 card structure and cover
  schema, §5 caption structure (~250 chars), §6 hashtags
- `scripts/cardnews.py` — exact JSON field names per slide type
- The 2-3 most recent posts in today's subcategory
  (`ls content/`, find same-pillar files with `grep '"pillar": "<subcategory>"' content/*.json`)
  — **including whatever the other slot posted today** — so you don't repeat the
  same place or neighborhood

### ⚠️ Slot-duplication check — do this before writing

This is separate from topic overlap. It checks whether *today's slot* is already
filled — guards against a retry, manual run, or overlapping cron creating a second
post in the same slot.

```
TZ=Asia/Seoul date +%F        # today's date
grep -l "\"pillar\": \"<today's subcategory>\"" content/<today>-*.json 2>/dev/null
```

If today's date + subcategory combination already exists in `content/` and that
slug is `published` or `pending` in `queue.json`, **this slot is already handled.**
Don't write a new post — report "slot already filled — skipping" and exit
immediately.

## 3. Verification rule — no compromises, especially existence

This whole account's credibility rests on "it's real and it's open." For every
post, **verify the place's name, address, and that it's currently operating**
(booking/review platform, official Instagram/website, credible press within the
last 1-2 years — at least one of these). If you're not confident, **do not invent
it** — follow the skip procedure in §0. Recommending a place that doesn't exist is
this account's one fatal failure mode.

Menu items, prices, and hours must also come from real sources only. Don't write as
if you personally visited (this account is research-based — the tone should own
that honestly, per CONTENT.md §2).

If you searched in good faith and found nothing verifiable for today's
subcategory, **do not fabricate** — follow the §0 skip procedure.

## 4. Photography — required (see CONTENT.md §3 for the full rule)

Source a real, properly-licensed photo (Unsplash free-license or equivalent —
`images.unsplash.com`, never `plus.unsplash.com`) matching the cuisine/venue mood.
It does not need to be the literal venue's own interior unless you have verified
rights to a real photo of it.

```
mkdir -p assets/photos
curl -sL "<direct images.unsplash.com URL>" -o assets/photos/<slug>.jpg
```

Then reference it in the content JSON:
- Cover slide: `"bg_image": "assets/photos/<slug>.jpg"`
- Top level: `"photo": "<slug>.jpg"` (duotone-washes the same photo across the other
  6 slides — see `photo_bases()` in `scripts/cardnews.py`)

Only fall back to the `anchor`-typography-only cover (no photo at all) if a real
search genuinely turns up nothing usable — this should be rare.

## 5. Write and render

Write `content/<YYYY-MM-DD>-<short-slug>.json`:

- `pillar` = today's subcategory key, `handle` = `"@deep_dive_korea"`
- `publish_at` = now (`TZ=Asia/Seoul date +%Y-%m-%dT%H:%M:%S+09:00`)
- **All post text — headline, subline, stat labels, body copy, caption, hashtags —
  is in ENGLISH.** This is an English-language account.
- 7 slides: cover / stat / list / point / list / quote / source (exact field names
  from `scripts/cardnews.py`; cover = eyebrow + 2-line headline ("line 1 hook /
  line 2 payoff") + subline + `bg_image` per §4)
- Caption ~250 chars (CONTENT.md §5's 4-part structure)
- ~20 hashtags in English, 3 tiers (CONTENT.md §6)

Then render it yourself and confirm all 7 slides come out with no errors:

```
pip install --quiet pillow      # only if missing
python3 scripts/cardnews.py content/<slug>.json out
```

**You must commit the rendered images (`out/<slug>/`) yourself.** `render.yml`
reacts to `content/**.json` pushes, but a push made with `GITHUB_TOKEN` from inside
GitHub Actions doesn't trigger other workflows (recursion guard) — so `render.yml`
won't backstop this run. No images committed means no URL for Instagram to fetch at
publish time.

(When a human pushes locally, `render.yml` runs normally.)

## 6. Register in the queue and push

Append to the `queue.json` array (keep it valid JSON):

```json
{"slug": "<slug>", "pillar": "<subcategory>", "publish_at": "<now, +09:00 ISO>", "status": "pending"}
```

```
git add content/<slug>.json out/<slug>/ assets/photos/<slug>.jpg queue.json
git commit -m "content: <slug> (daily pipeline, am|pm)"
git pull --rebase && git push
```

If the push fails, stop and **report why**. If the commit never reaches the
remote, the publish workflow can't see it.

## 7. Publishing is the cron's job — the agent never fires it directly

`publish.yml` runs **every 30 minutes**, finds the oldest `status: "pending"` entry
in `queue.json` whose `publish_at` has passed, publishes it, and commits the queue
back as `published`.

So once §6's push lands, you're done — it auto-publishes within 30 minutes, as
long as §5's images were committed too.

If you have time, it's worth checking the result (skip if `gh` isn't authenticated):

```
gh run list -R steverse-code/deep-dive-korea --workflow=publish.yml --limit 3 \
  --json status,conclusion,createdAt,url
```

**Don't run `gh workflow run publish.yml` directly.** It can overlap with the cron
and double-publish. Only use it as an exception if you're sure the cron hasn't run
in over 30 minutes.

## 8. On failure

Meta-side limits — `Application request limit reached` (code 4, subcode 2207051) or
`API access blocked` (OAuthException code 200) — are rate limits this pillar's
sibling account (ig-studio) has hit before, usually from posting too fast on a new
account. **Don't retry.** The content is already committed and queued, so the next
cron run will publish it once the limit clears. Same for any other error — report
it plainly, don't loop retrying.

## 9. Report

Under 200 chars: which subcategory and place you picked, what you used to verify
existence, whether you found a usable photo, render result, commit/push status, and
that publishing is left to the cron.
