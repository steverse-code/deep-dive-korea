# Content Playbook — DeepDive Korea (@deep_dive_korea)

English-first, research-based guides to real restaurants, cafes, bars, and local
food in Korea. The objective is discovery without sacrificing trust.

## Publishing rhythm

One post per day. Never catch up missed days by bulk publishing.

| Day | Format | Topic | Partnership |
|---|---|---|---|
| Mon | Reel | restaurant | optional |
| Tue | Reel | local food | Collab candidate |
| Wed | Carousel | cafe guide | optional |
| Thu | Reel | bar | optional |
| Fri | Reel | restaurant | Collab candidate |
| Sat | Carousel | neighborhood guide | optional |
| Sun | Reel | cafe/dessert | optional |

The account ramps up after an Instagram restriction: week 1 publishes three posts,
week 2 publishes four, and week 3 reaches the schedule above. The workflow stays
disabled until a human confirms that Account Status is clear.

## Editorial rules

1. Verify the venue name, address, and current operation from an official listing,
   booking platform, or recent credible source.
2. Do not claim personal experience or subjective taste as fact.
3. Put the venue, neighborhood, dish, and city in natural English copy so Instagram
   search can understand the post.
4. Use 5–8 specific hashtags. Avoid repeating the same broad hashtag block.
5. Include one clear action: save the guide, share it, or follow for the next stop.
6. Add a location tag and venue tag when the publishing interface/API supports it.

## Media and rights

New content uses policy version 2 and must contain:

```json
{
  "policy_version": 2,
  "format": "reel",
  "asset_source": "original",
  "rights_confirmed": true,
  "partner_handle": null,
  "collab_required": false,
  "collab_status": "not_requested"
}
```

Allowed `asset_source` values are `original`, `partner_licensed`, and
`licensed_stock`. Venue-specific Reels and Collabs must use original or written
partner-authorized media. Generic stock must never be presented as the actual venue
and is limited to an occasional editorial Carousel.

For partner content, record the permission source in `rights_note`. A Collab item
must remain held until `collab_status` is `accepted`. The current Instagram Login
integration cannot invite collaborators automatically; this step needs a human
operator or a future migration to Instagram API with Facebook Login.

## Format standards

Reels are 1080×1920 (9:16), hook in the first two seconds, 15–30 seconds total,
English on-screen text, and captions safe for the center area. Use original venue
footage whenever possible.

Carousels are 5–7 slides: promise, context, why it matters, practical details,
caveat, and sources/save CTA. Use concise English and no unsupported superlatives.

## Measurement

Review each post after 48 hours. Prioritize saves, shares, profile visits, follows,
and non-follower reach. Only consider paid promotion for the top 20% of posts by
saves/shares; never use spend to rescue weak creative.
