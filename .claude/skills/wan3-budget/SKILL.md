---
name: wan3-budget
description: "WAN 3.0 BUDGET - how not to burn credits on Wan 3.0 / Wan 3.0 Prime in Higgsfield: measured price model, draft ladder (480p, 720p, 1080p), what each tier can validate, re-roll economics, the get_cost preflight rule, Prime vs Standard, smart-duration and count traps, and a spending protocol for sessions that call the Higgsfield tools. Use BEFORE any paid Wan generation and whenever the user says \"сколько стоит\", \"кредиты\", \"дорого\", \"сэкономить\", \"черновик\", \"драфт\", \"бюджет\", \"какое разрешение\", \"720 или 1080\", \"Prime или обычный\", \"30 секунд\", \"перегенерировать\", \"get_cost\", \"unlimited\", or asks what length or resolution a Wan clip should be. Load with wan3-core for every Wan 3 task that will generate; numbers are Higgsfield credits measured 2026-10-14. Not for other models' pricing (use models_explore and get_cost)."
---

# WAN 3.0 BUDGET

Wan 3 is cheap per second and expensive per mistake. On Higgsfield it costs **1.0 / 1.75 / 3.5
credits per second** at 480p / 720p / 1080p (Prime 1.5 / 3 / 6) `[HF]` - roughly **a quarter of
Seedance 2.5 at 720p** (8.75 vs 35 credits for 5 s, same session) - and the time to a usable clip
is dominated by how many generations you waste. This skill is the discipline that keeps the waste
small. Marks as in `wan3-core/references/provenance.md`; every number below is a `get_cost`
reading unless marked.

## §0 - Five rules

**B1 - Price before you press.** `generate_video` with `get_cost: true` returns the price and
submits nothing. It is free. No paid call without it; the number goes in the header line of the
prompt (`Cost: 17.5 cr`). A script gives the same number offline: `scripts/wan3_cost.py`.

**B2 - A generation answers one question.** "Does the camera stay one shot?" "Does Image 1 bind to
the man?" "Is the line lip-synced?" Pick the question, then the **cheapest clip that can answer
it**: the lowest resolution, the shortest duration, the fewest references. A 480p 3 s clip costs
3 credits; the same question asked of a 1080p 15 s clip costs 52.5.

**B3 - There is no seed `[HF]`.** Higgsfield exposes no seed for Wan, so a 480p draft cannot be
"promoted" to the same clip at 1080p the way a Seedance 2.5 Draft can. **A draft validates the
prompt, never the take.** Judge drafts only on what survives a re-roll: structure, camera path,
cut count, action order, audio type, whether the references bound. Never on faces, texture, hands
or a lucky gesture.

**B4 - Price is linear, so there is no bulk saving.** Ten 3 s clips cost the same as one 30 s clip.
Savings come from **not generating the wrong thing**, from editing instead of re-rolling, and
from choosing the right resolution once.

**B5 - Keep a ledger.** Opening balance, every call's cost, running total, what each bought
(answered question / accepted clip / wasted). Stop and re-plan after three failed generations on
one shot or after a quarter of the budget disappears without an accepted clip.

## §1 - Prices `[HF]`  (Plus plan, 2026-10-14; other plans may differ - re-measure)

Credits per clip (Standard, `wan3_0`); Prime in `references/price-table.md`.

| Seconds | 480p | 720p | 1080p |
|---|---|---|---|
| 2 | 2 | 3.5 | 7 |
| 3 | 3 | 5.25 | 10.5 |
| 5 | 5 | 8.75 | 17.5 |
| 10 | 10 | 17.5 | 35 |
| 15 | 15 | 26.25 | 52.5 |
| 30 | 30 | 52.5 | 105 |

Readings: 2 s/480p = 2, 5 s/480p = 5, 5 s/720p = 8.75, 10 s/720p = 17.5, 5 s/1080p = 17.5,
3 s/720p = 5.25, 15 s/480p = 15, 30 s/1080p = 105. Linear in seconds; 720p = 1.75x 480p; 1080p = 2x
720p. `generate_audio` off and `enable_thinking` on **did not change** the preflight - sound and
thinking are free, so decide them on quality, not price.

Traps `[HF]`:

- **`duration: -1` (smart duration) is billed as 10 s.** A three-second idea costs 17.5 credits at
  720p. Always pass a number.
- **`count: 2` preflight returned the single-clip price** `[HF]`. Variants presumably multiply the
  bill `[CRAFT]`; multiply yourself and treat `count > 1` as a deliberate purchase.
- **Reference videos did not add billed seconds** in the one Higgsfield measurement `[HF]`: a 3 s
  480p clip with a 6 s reference video preflighted at 3 and was charged 3 (some other hosts bill
  output + every reference second `[FIELD]`). An edit with a 7 s source video (`Edit the video ... Video 1`) was charged 7 cr at 480p, i.e. the
  output seconds only `[HF]` (one measurement). Still run `get_cost` with the real media attached and
  trim reference videos to the shortest clip that carries the motion.
- **A preset may be suggested instead of a submission** `[HF]`: `generate_video` can answer with
  `preset_recommendation` (nothing is charged). To generate literally, repeat the call with
  `declined_preset_id` set to the id it names.
- **A rejected combination costs nothing** `[HF]`: the 422 for `start_image` + references came back at
  submission with no charge.
- **Payment happens at submission** `[CRAFT]`, usable or not; whether failed or blocked jobs are
  refunded and whether uploads are free are unmeasured - check `transactions` after the first failure.

Where Wan sits `[HF]` (5 s, default parameters of each model, same session): Wan 3.0 720p **8.75**
· Wan 3.0 480p **5** · Wan 2.7 720p 7.5 · Kling 3.0 8.75 · Seedance 2.5 480p 15 · Seedance 2.5
720p **35**. Wan 3 is the cheap place to explore structure, long takes and reference-heavy briefs;
it is **not** a draft of a Seedance shot - a different model gives a different picture, so a Wan
test predicts nothing about a Seedance take.

## §2 - The ladder

Climb only as far as the question requires.

| Rung | What | Price | Validates |
|---|---|---|---|
| L0 | `get_cost`, `prompt_lint.py`, the pre-send check | 0 | arithmetic, syntax, timecodes, role lines |
| L1 | **480p, 2-4 s**, text only (or one reference) | 2-4 | does the prompt parse: camera treatment, first beat, audio type, cut behaviour at the first boundary |
| L2 | **480p, full length** or one beat per clip | 1 per second | pacing, order of beats, number of cuts, whether references bind, dialogue timing and that the mouth moves (sync is judged at the final tier) |
| L3 | **720p final** | 1.75 per second | faces, hands, texture, light, grain; the take you may keep |
| L4 | **1080p hero** | 3.5 per second | only the shots that will be seen big; check first that 720p was not enough |

What 480p cannot tell you `[CRAFT]`: face likeness, fine skin, hands, small text and logos, grain
and halation, whether a subtle gesture is subtle. These are decided at L3 and cannot be paid for
cheaper. A 480p clip is never the final unless the delivery is small.

Skip rungs when the arithmetic says so: a 5 s clip at 480p costs 5, the same as one L1 draft at
720p/3 s - for a simple shot, go straight to the final tier. `scripts/wan3_cost.py draft ...`
answers "is a draft worth it?" from two numbers you can estimate: how often the prompt works
untested (`p-direct`) and how often it works after a draft (`p-after-draft`). Until calibration logs
exist, guess `p-direct` 0.3 for a new multi-shot prompt, 0.5 for a single shot, 0.7 for an edit
with a clean source `[CRAFT]` and revise from the ledger.

## §3 - Choosing duration and resolution

- **Duration = the shot in the edit + 1 s of handle, rounded up; never `-1`.** A reaction close-up
  is 3-5 s, not 8 "to be safe": every second is 1.75 credits at 720p and one more second for the
  model to drift.
- **A 30 s clip is a product decision.** It costs 30 / 52.5 / 105 credits and gives the model more
  chances to fail `[FIELD]`. Use it when the continuous take *is* the idea; otherwise build the
  scene as 2-3 clips of 8-15 s joined by start-image chaining, or cut together in an editor when the scene is hard-cut coverage
  (same price, independent retries, a fix re-buys 10 s instead of 30).
- **Default final tier: 720p.** `[HF]` default; the official handbook's own clips never exceed
  1080p and only a handful are exactly 1920x1080 (Atlas count `[FIELD]`). Go to 1080p for the
  shots that fill a large screen; for social delivery 720p is usually the whole story.
  Whether upscaling a 720p take (Higgsfield `upscale_video`) beats native 1080p on price and look
  is `[OPEN]` - get its `get_cost` on a real clip before deciding.
- **Aspect ratio is chosen once, before the first paid call.** Regenerating to flip 9:16 to 16:9
  is the most avoidable waste (Venice `[FIELD]`); Higgsfield has no 21:9 for Wan `[HF]`.

## §4 - Re-roll economics

Expected cost of one usable clip = price of an attempt / probability an attempt is accepted. At
17.5 credits and p = 0.35 that is 50 credits - not 17.5. Three consequences:

1. **Raise p, not the number of attempts.** Every minute spent on a role line, a no-cut clause or a
   lock sentence is cheaper than another roll. Fix the prompt after at most **one** blind re-roll
   (a second sample shows whether the failure is variance or the prompt).
2. **Split when p is low.** A 15 s three-beat prompt with p = 0.25 costs 105 credits per usable clip
   at 720p; three 5 s clips at p = 0.6 cost 43.75. Split by beat, then chain by start image or, for hard cuts, cut the REF clips together
   (`wan3-core/references/long-form.md` §10).
3. **Repair beats re-roll when the clip is 80% right.** `wan3-edit` fixes one object, one line
   of dialogue or one lighting problem while keeping the rest; run `get_cost` with the clip attached
   to see the price of the repair before comparing it with another roll `[OPEN: calibration C9]`.

After each failure: classify (cut / drift / audio / motion / identity / physics / text), change
**one** thing, say which in the ledger. Rewriting the whole prompt after a failure (Seedance
set R2) turns a 17-credit lesson into a 17-credit lottery ticket.

## §4b - When the expected cost exceeds the budget

`scripts/wan3_cost.py expected|draft ... --budget N` prints whether one attempt, a draft plus a final, or a
retry fits. If the expected cost per usable clip is above the budget (a 15 s dialogue scene with two
references, p = 0.3, costs about 87 credits at 720p against a 40-credit budget), say so before
spending and choose, in order: (1) shorten the clip or cut a shot; (2) spend the budget on one
**L1 structure test** (480p, 3-4 s, same role lines and one line of dialogue) and **one final**, and
accept that a failed final is not retried; (3) lower the final tier to 480p if the delivery allows;
(4) ask for more budget. Never spend the remainder on a second blind roll; tell the user which
questions the money bought.

## §5 - Prime or Standard

Prime is the same feature set, faster `[FIELD]`, and costs **1.5x at 480p and 1.71x at 720p/1080p**
`[HF]`. Quality claims conflict (8.8 vs 8.2 in one vendor benchmark, "no published table" in
another). So: **Standard by default; Prime only when the clock, not the wallet, is the constraint**
(a client waiting, many ratio variants of an approved shot). Never pay Prime for a draft: Prime
480p (7.5 for 5 s) costs nearly Standard 720p (8.75).

## §6 - Free allowances

`models_explore` shows an `unlim` block per model. On 2026-10-14 Wan 3.0 and Prime carry no
`supports_unlim`; Wan 2.7 does, but this account's allowance was not available. If an allowance
appears, `generate_video` returns an `unlim_choice` question instead of spending: answer it
deliberately. A Wan 2.7 clip is **not** a draft of a Wan 3.0 clip.

## §7 - Session protocol (when the Higgsfield tools are available)

1. `balance` at the start; write the opening figure in the ledger. Ask for a budget if none was
   given - a number, not "a bit".
2. Per candidate generation: `get_cost` -> header line -> proceed only inside the budget.
3. **Ask before spending** when one call is above **30 credits**, or the session total would pass
   **100**, or the user has not set a budget - state the price, the question it answers and the
   cheaper alternative. A standing instruction ("spend up to N on this") lifts the ask, up to N.
4. One submission at a time for anything over 10 credits; read the result before the next one. On
   a transport timeout do **not** resubmit (the outcome may be unknown); check `transactions`
   and the job list first.
5. After each result print one ledger line:
   `#7 | 480p 4s T2V c2 | 4 cr | total 31 cr / 150 | answered: cuts=2 (asked 0) -> add No cut to shots 2-3`
6. Report the final ledger and what the money bought. Failed attempts are listed, not hidden.

## §8 - Ledger template

```text
Budget: 150 cr (opening balance 975) | Model: wan3_0 | Final tier: 720p
#  tier     dur  mode  question                             cost  total  verdict
1  480p      3   REF   does Image 1 bind to the man?          3     3    yes (Image 1 syntax)
2  480p      8   T2V   one take with No cut?                  8    11    2 cuts found -> clause moved into each shot
3  720p     10   REF   final shot 1                         17.5  28.5   accepted
```

## §9 - Pre-send items added by this skill

1. A `get_cost` reading exists for exactly these parameters (model, resolution, duration, media)
   and sits in the header; `duration` is not `-1`; `count` is 1 or multiplied by hand.
2. The resolution is the lowest that answers this generation's question, and the question is
   written down.
