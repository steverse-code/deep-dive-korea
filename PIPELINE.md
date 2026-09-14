# Daily automated pipeline

This is the source of truth for the unattended `daily-content.yml` agent.
The account is @deep_dive_korea and all audience-facing copy is English.

## 0. Safety gates

- Create at most one item for a KST calendar day.
- Never publish directly and never run `publish.yml` from this workflow.
- If a same-day `pending` or `published` queue item exists, stop.
- Do not revive `held` items or catch up missed days.
- If rights, venue existence, or current operation cannot be verified, stop without
  adding a queue item.

## 1. Choose the weekly slot

Use `TZ=Asia/Seoul date +%u`.

| Day | Format | Topic | Collab |
|---|---|---|---|
| 1 Mon | reel | restaurant | optional |
| 2 Tue | reel | local | candidate |
| 3 Wed | carousel | cafe | optional |
| 4 Thu | reel | bar | optional |
| 5 Fri | reel | restaurant | candidate |
| 6 Sat | carousel | local | optional |
| 7 Sun | reel | cafe | optional |

During restriction recovery, respect the manual ramp flag in the queue or repository
notes: three posts in week 1, four in week 2, then daily. Skipped days stay skipped.

## 2. Research and verification

Read `CONTENT.md`, `scripts/cardnews.py`, and recent same-topic posts. Confirm:

- official venue name and address;
- current operation from an official listing, booking service, or recent source;
- any menu, price, and hours used in copy;
- a useful English search phrase for travelers.

Record source URLs and an as-of date. Never write as if the account visited.

## 3. Acquire media legally

Preferred order:

1. original footage/photo supplied by the account owner;
2. venue/creator media with written permission;
3. licensed stock only for a non-venue-specific editorial Carousel.

Do not scrape venue social photos. Do not use a mood photo as if it depicts the
named place. Store `asset_source`, `rights_confirmed: true`, and a `rights_note`.
If those facts cannot be confirmed, stop.

For a Collab candidate, set `collab_required: true`, `partner_handle`, and keep
`collab_status: requested`. Do not queue it as pending until the partner accepts;
the publisher enforces this.

## 4. Write and render

Create `content/<YYYY-MM-DD>-<slug>.json` with:

- `policy_version: 2`;
- `format: reel|carousel`;
- `pillar`, `handle: "@deep_dive_korea"`, `publish_at`;
- `asset_source`, `rights_confirmed`, `rights_note`;
- `location`, `venue_handle`, `search_keyword`;
- `partner_handle`, `collab_required`, `collab_status`;
- English caption and 5–8 specific hashtags.

Render Carousel slides:

```bash
python3 scripts/cardnews.py content/<slug>.json out
```

For a Reel, render slides and then a 1080×1920 MP4:

```bash
python3 scripts/cardnews.py content/<slug>.json out
python3 scripts/reel.py content/<slug>.json out
```

Confirm all referenced assets exist and the MP4 is 9:16 when applicable.

## 5. Queue and push

Append exactly one entry:

```json
{
  "slug": "<slug>",
  "pillar": "<topic>",
  "format": "reel",
  "publish_at": "<KST ISO timestamp>",
  "status": "pending"
}
```

Commit the content JSON, rendered output, authorized source asset, and queue change.
Push once. The separate publisher runs daily at 19:00 KST and selects only the
newest due item.

## 6. Failure behavior

The publisher changes any failed item to `held` immediately. Instagram action
blocks (including code 4/subcode 2207051) are never retried automatically. The
watchdog may restore a missed content-generation run, but it never starts an
Instagram publish run.

## 7. Report

Report the format, topic, verification sources, rights basis, render result, and
commit SHA. Keep the report concise.
