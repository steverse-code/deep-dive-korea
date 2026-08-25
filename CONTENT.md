# Content Playbook — DeepDive Korea (@deep_dive_korea)

> "Let's deep dive into the real Korea." An English-language account introducing
> real, verified restaurants, cafes, and bars in Korea to an international audience.
> Same rendering/publishing pipeline as ig-studio (@your_ground_zero), but:
> **all post content is in English**, and **every post uses a real, properly-licensed
> photo** (food is a visual category — a typography-only cover doesn't work here).

---

## 1. Daily AM/PM schedule

| Day | AM | PM |
|---|---|---|
| Mon | restaurant | cafe |
| Tue | bar | local |
| Wed | restaurant | cafe |
| Thu | bar | local |
| Fri | restaurant | cafe |
| Sat | bar | local |
| Sun | restaurant | cafe |

Subcategory definitions:

| key | meaning |
|---|---|
| `restaurant` | Fine dining / distinctive restaurants |
| `cafe` | Cafes with strong atmosphere, coffee, or dessert |
| `bar` | Cocktail bars, wine bars, traditional Korean liquor (makgeolli/soju) bars |
| `local` | Old-school (노포) spots, neighborhood favorites, hidden local gems |

## 2. Tone rules

1. **Verified existence is everything.** Confirm the place's name, address, and that
   it is currently operating (booking platform, official listing, recent press).
   If you're not confident, do not invent it — skip. This account's trust comes
   entirely from "we checked, it's really there."
2. **Don't claim taste as fact.** Frame as "if you want this kind of thing" rather
   than "the best" or "you must go." Taste is acknowledged as subjective, always.
3. **Only write facts you can source.** Menu items, prices, hours — only from real
   sources (official page, booking site). Never write as if you personally visited —
   this account is research-based, and the tone should own that honestly.
4. **End declaratively, politely.** No commands, no exclamation-mark hype, no
   clickbait superlatives.

## 3. Photography — required, not optional

Every post needs a **real, properly-licensed photo** representing the cuisine/venue
type. Source from Unsplash (free license, no attribution required) or an equivalent
CC0/free-license source — never scrape a specific venue's own photos unless you can
verify usage rights. The photo should evoke the right mood/cuisine (e.g. Korean
market food, traditional pancake, cocktail bar ambience) — it does **not** need to
be literally that exact venue's interior unless you have verified rights to a real
photo of it.

Workflow to source a photo:

```
1. WebSearch for a relevant Unsplash photo (e.g. "Korean street food market unsplash")
2. WebFetch the photo's page to confirm it's on images.unsplash.com (free),
   NOT plus.unsplash.com (paid/premium — skip these)
3. curl -sL "<direct images.unsplash.com URL>" -o assets/photos/<slug>.jpg
```

Use the photo in **two places** in the content JSON:
- Cover slide: `"bg_image": "assets/photos/<slug>.jpg"` (full-bleed photo + scrim, per §4)
- Top-level: `"photo": "<slug>.jpg"` (applies a duotone wash of the same photo to the
  other 6 slides, via `scripts/cardnews.py`'s `photo_bases()` — keeps the whole
  carousel visually cohesive instead of just the cover having a photo)

If you truly cannot find a suitable free-license photo after a real search, fall back
to the `anchor` typography treatment (no `bg_image`, no `photo`) rather than using an
unlicensed image — but this should be rare for a food account.

## 4. Card structure (7 slides)

Same renderer as ig-studio (`scripts/cardnews.py`):

```
1  cover    ★ editorial cover — eyebrow + 2-line headline ("line 1 hook / line 2 payoff")
             + subline + REQUIRED bg_image (see §3)
2  stat     one key fact/number (e.g. "since 1945", a ranking, a price point)
3  list     comparison/context
4  point    ★ the real reason this place matters — the non-obvious angle
5  list     practical info (location, tips, what to order/pair)
6  quote    caveat — "taste varies", note the info's as-of date
7  source   sources (booking link/official page/press) + save/follow CTA
```

## 5. Caption structure (~250 chars)

```
line 1     one-sentence hook
para 2     place name + one verified key fact (location/feature/source)
para 3     one-line caveat (subjective taste, info as of a date)
closer     "Sources in the last slide" + save prompt
```

## 6. Hashtags

~20 tags, three tiers, **in English** (this is an English-language account):
large (`#travel` `#foodie` `#korea`) / mid (`#seouleats` `#hiddengem` `#localfood`) /
niche (specific neighborhood/cuisine tags).

## 7. Publishing pipeline

Identical structure to ig-studio (see `PIPELINE.md`) — cloud-only, no local Mac needed:

```
daily-content.yml  09:00 / 15:00 KST  →  research, write, render, commit
publish.yml        every 30 min       →  publishes whichever queued post is due
refresh-token.yml                     →  refreshes the Instagram token
```
