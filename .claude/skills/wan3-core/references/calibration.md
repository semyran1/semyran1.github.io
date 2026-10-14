# Calibration - turning `[OPEN]` and `[FIELD]` into `[EMPIRICAL]` for pennies

This set was written without a single generation: the research channel was documentation and
reports only. The Seedance set became reliable because failed generations were logged and turned
into rules. This file is the shortest route to the same thing for Wan 3 - every test is designed
to be the cheapest clip that can answer one question, at `480p` standard (**1 credit per second**
`[HF]`) unless stated.

Rules of the ledger:

- One question per test, one variable per run, the rest copied byte for byte (R2).
- Before each paid call: `get_cost` (free). After each: record the price actually charged
  (`transactions`) - a mismatch with the preflight is itself a finding.
- A result is logged in the table below with date, model, parameters, prompt id, verdict and the
  rule it changes. A single run is **provisional** (`[EMPIRICAL?]` in the log only).
- No seed on Higgsfield: one run is a sample. A rule is upgraded to `[EMPIRICAL]` in the source file
  only after **two confirming runs**; a rule contradicted once goes back to `[OPEN]`.

## Minimum set (about 30 credits) - run before the first serious project

Status 2026-10-14: C10, C13, C1 done (see the log). Still open: C5 (default audio), C2 (no-cut), C4 (Russian speech) - they need the clips to be listened to / cut-counted by a person or a machine that can download the result.

| Id | Question | Cheapest setup | Credits | Records | Changes |
|---|---|---|---|---|---|
| C10 | Do `start_image` + `image_references` get rejected together? Do `video_references` + `start_image`? | `get_cost` only, three role combinations | 0 | the tool's error or adjustment text | `SKILL.md` §1, `modes-and-references.md` §1 |
| C13 | Are reference-video seconds billed on Higgsfield? | upload a 5 s clip; `get_cost` with and without it | 0 | both prices | `wan3-budget` price table, `limits.md` |
| C1 | Does Higgsfield bind `Image 1` or `@Image1`? | REF, two clearly different people as images; "Image 1 hands a cup to Image 2" vs the `@Image1` form; 3 s each | 6 | who is who in each clip | `SKILL.md` §4 default syntax |
| C5 | What audio appears when sound is not mentioned? Does "no music, no dialogue, only ambient sound" hold? | T2V, a person in a street, 3 s, twice | 6 | music? voice? ambience? | `wan3-sound` defaults |
| C2 | Does `No cut.` plus a camera clause keep a 3-beat take one shot? | T2V, 8 s, three beats, with and without the clauses | 16 | cut times via `count_cuts.py` | `long-form.md` §3 |
| C4 | Is Russian speech usable (intelligibility, accent, does the mouth move)? | T2V, one person, one 8-word line, 4 s | 4 | listen; mouth movement present (sync quality is judged at 720p) | `limits.md`, `wan3-sound` |

## Full set

| Id | Question | Setup | Credits |
|---|---|---|---|
| C3 | Are declared hard cuts obeyed (3 shots, `(Jump Cut)` each)? | T2V 9 s, count cuts | 9 |
| C6 | Does `enable_thinking` change adherence on a multi-shot or multi-reference prompt, and the bill? | same prompt on/off, 6 s; compare `transactions` | 12 |
| C7 | Does a 480p draft predict the 720p/1080p take (composition, blocking, camera, cuts)? | same prompt at 480p, 720p, 1080p, 3 s | 3 + 5.25 + 10.5 |
| C8 | What does `-1` return for a three-beat prompt, and what is charged? | T2V, `duration: -1`, 480p | 10 |
| C9 | Is an edit instruction routed (`Edit the video, remove ... in Video 1`) and how is it billed? Is `Extend video 1 by 3 seconds` routed? | use a clip from C2; 480p; `get_cost` first | ~6 |
| C12 | How much does prompt length matter (45 words vs 250 words, same scene)? | T2V 5 s twice | 10 |
| C14 | What does `aspect_ratio: auto` do with a 9:16 start image? | I2V 3 s | 3 |
| C16 | How different are two runs of the same prompt (value of a re-roll)? | same prompt twice, 3 s | 6 |
| C17 | Is a short sign text legible at 480p vs 720p? | T2V 3 s, a shop sign | 3 + 5.25 |
| C18 | Fractional timecodes in a storyboard-per-frame prompt (`1.48-3s`) | REF, three images, 5 s | 5 |
| C19 | Prime vs Standard on the same prompt: is the 1.71x worth it? | T2V 5 s at 720p, both models | 8.75 + 15 |

## Log

| Date | Id | Model / params | Prompt | Verdict | Mark changed |
|---|---|---|---|---|---|
| 2026-10-14 | C10 | wan3_0, 480p 3 s, `start_image` + `image_references` | submit | **rejected**: 422 "start_image/end_image cannot be combined with reference media"; nothing charged. Preflight (`get_cost`) accepted the same combination, so the preflight does not validate roles | `[HF]` confirmed |
| 2026-10-14 | C13 | wan3_0, 480p 3 s, 2 images + 6 s `video_references` | submit | preflight 3 cr, charged 3 cr (`transactions`): reference-video seconds not billed (one measurement) | `[HF]` provisional |
| 2026-10-14 | C1 | wan3_0, 480p 3 s, REF, ship (Image 1) + dog (Image 2), `Image 1 / Image 2` syntax, dog large in the foreground | 2 clips (one with an extra `Video 1` camera-only reference, 6 s hands-and-watch clip) | both **bound correctly**; the video reference leaked no content (judged by the user) | `Image N` `[EMPIRICAL]` (2 runs); `Video 1` camera-only provisional |
| 2026-10-14 | C1 | same, `@Image1 / @Image2` syntax | 1 clip | **bound correctly** | `@ImageN` provisional (1 run): both syntaxes work, `Image N` stays the default |

Operational notes from the session (not rules about Wan): in a cloud sandbox with a restricted egress policy the presigned upload host and the result CDN of Higgsfield were blocked, so media went in through `media_import_url` from a public URL (the user's own published site) and results could be judged only by the user in the gallery; `scripts/count_cuts.py` needs the clip on a machine that can download it. Spent 9 credits (three 3 s clips); `start_image` + reference media was rejected before billing.

## How to read a result

- **Binding tests** (C1, C18): the person who appears is judged by face, not by clothing.
- **Cut tests** (C2, C3): run `scripts/count_cuts.py clip.mp4 --expect N`; a threshold that is too
  sensitive reports camera whips as cuts, so also look at the first frame after each reported time.
- **Draft predictability** (C7): compare five things only - subject placement, camera path, number
  of cuts, action order, audio type. Texture and faces are expected to differ and prove nothing.
- **Audio tests** (C4, C5): download the file and listen once with the picture, once without.
- **Cost tests**: the preflight is the claim, `transactions` is the fact.
