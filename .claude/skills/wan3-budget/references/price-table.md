# Price table - Wan 3.0 on Higgsfield

Measured 2026-10-14 with `generate_video(get_cost: true)` on a Plus plan; nothing was generated.
Rates are credits per second; prices are linear in seconds. Re-measure when a price matters:
the rates moved at least once already (third-party reports cite earlier 6.25/12.5/27.5 per 5 s
for Standard and 17.5/38.5 for Prime at 720p/1080p `[FIELD]`).

## Raw readings `[HF]`

| Model | Resolution | Seconds | Credits |
|---|---|---|---|
| wan3_0 | 480p | 2 | 2 |
| wan3_0 | 480p | 5 | 5 |
| wan3_0 | 480p | 15 | 15 |
| wan3_0 | 720p | 3 | 5.25 |
| wan3_0 | 720p | 5 | 8.75 |
| wan3_0 | 720p | 10 | 17.5 |
| wan3_0 | 720p | -1 (smart) | 17.5 (billed as 10 s) |
| wan3_0 | 1080p | 5 | 17.5 |
| wan3_0 | 1080p | 30 | 105 |
| wan3_0_prime | 480p | 5 | 7.5 |
| wan3_0_prime | 720p | 5 | 15 |
| wan3_0_prime | 1080p | 5 | 30 |
| wan3_0_prime | 1080p | 30 | 180 |
| wan3_0 | 720p | 5, `generate_audio: false` | 8.75 (unchanged) |
| wan3_0 | 720p | 5, `enable_thinking: true` | 8.75 (unchanged) |
| wan3_0 | 720p | 5, `count: 2` | 8.75 (single-clip price) |

Not measured: any call with media attached; edit/extend routing; upscale.

## Derived rates (credits per second)

| Model | 480p | 720p | 1080p |
|---|---|---|---|
| wan3_0 | 1.00 | 1.75 | 3.50 |
| wan3_0_prime | 1.50 | 3.00 | 6.00 |
| Prime / Standard | 1.50x | 1.71x | 1.71x |

## Standard `wan3_0`, credits per clip

| s | 480p | 720p | 1080p |
|---|---|---|---|
| 2 | 2 | 3.5 | 7 |
| 3 | 3 | 5.25 | 10.5 |
| 4 | 4 | 7 | 14 |
| 5 | 5 | 8.75 | 17.5 |
| 6 | 6 | 10.5 | 21 |
| 8 | 8 | 14 | 28 |
| 10 | 10 | 17.5 | 35 |
| 12 | 12 | 21 | 42 |
| 15 | 15 | 26.25 | 52.5 |
| 20 | 20 | 35 | 70 |
| 25 | 25 | 43.75 | 87.5 |
| 30 | 30 | 52.5 | 105 |

## Prime `wan3_0_prime`, credits per clip

| s | 480p | 720p | 1080p |
|---|---|---|---|
| 2 | 3 | 6 | 12 |
| 3 | 4.5 | 9 | 18 |
| 5 | 7.5 | 15 | 30 |
| 10 | 15 | 30 | 60 |
| 15 | 22.5 | 45 | 90 |
| 20 | 30 | 60 | 120 |
| 30 | 45 | 90 | 180 |

## Other models, 5 s, default parameters `[HF]`

| Model | Credits |
|---|---|
| wan2_7 720p | 7.5 |
| wan3_0 480p | 5 |
| wan3_0 720p | 8.75 |
| kling3_0 | 8.75 |
| seedance_2_5 480p | 15 |
| seedance_2_5 720p | 35 |

These are different models, not drafts of one another. The table only tells you where exploration
is cheap.

## Example projects (standard, 720p finals)

| Project | Plan | Credits |
|---|---|---|
| One 30 s continuous take | 1 L1 draft (480p 4 s) + 2 finals 30 s | 4 + 105 = 109 |
| 15 s three-shot scene, p(accept)=0.3 untested | direct: 26.25 / 0.3 | ~88 expected |
| Same, after one 480p 8 s structure draft, p=0.55 | 8 + 26.25 / 0.55 | ~56 expected |
| Product swatch, 5 s final | 1 final | 8.75 (a draft would cost more than it saves) |
| Video edit of a 5 s clip | `get_cost` with the clip attached first | unmeasured |
| Dialogue test in Russian | 480p 4 s | 4 |

Expected values use the `scripts/wan3_cost.py` formulas and guessed acceptance rates; replace the
guesses with the ledger once it exists.
