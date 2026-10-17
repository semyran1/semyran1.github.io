# Model facts - limits, inputs, output, scope

Marks as in `provenance.md`. Higgsfield facts are `[HF]` (catalog read and preflights run
2026-10-14); re-run `models_explore(action:"get", model_id:"wan3_0")` when a value matters, the
platform changes.

## Models on Higgsfield `[HF]`

| Id | Name | Note |
|---|---|---|
| `wan3_0` | Wan 3.0 | the default; text-to-video, first/last frame, multimodal reference-to-video, native audio |
| `wan3_0_prime` | Wan 3.0 Prime | same feature envelope; faster tier `[FIELD]`; **1.71x the price at 720p** (`wan3-budget`) |
| `wan2_7` | Wan 2.7 | previous generation; `start_image`/`end_image`/`audio_references` only; 2-15 s; eligible for free-trial unlimited generations when the account holds an allowance (`supports_unlim`), not available on this account on 2026-10-14 |

Wan 3.0 is an API-hosted model `[FIELD]`; open weights and 4K are claimed by one blog and denied by
the others, treat as false.

## Parameters exposed `[HF]`

| Parameter | Values | Default | Notes |
|---|---|---|---|
| `duration` | 2-30 (integer), or -1 | 5 | **-1 = model chooses the length, billed as 10 s** |
| `resolution` | `480p`, `720p`, `1080p` | 720p | no 4K |
| `aspect_ratio` | `auto`, `16:9`, `9:16`, `1:1`, `4:3`, `3:4` | - | no 21:9, no 2.39:1; `auto` is listed (that it follows the media is `[FIELD]`, C14) |
| `generate_audio` | bool | true | native audio track; price unchanged in the preflight |
| `enable_thinking` | bool | false | "reason about the prompt before generating (slower, better adherence)"; price unchanged in the preflight |
| `seed` | - | - | **not exposed**: no way to reproduce or promote a draft |
| `count` | 1-4 | 1 | variants of the same prompt; preflight returned the single-clip price for `count: 2` |
| `medias[].role` | `start_image`, `end_image`, `image_references`, `video_references`, `audio_references` | - | |

Output frame rate 30 fps `[FIELD]`. Prompt length: **at most 5,000 characters on Higgsfield** `[HF]`
(422 `string_too_long` at submit, nothing charged; the third-party figure of 20,000 is the raw API and wrong
here; the preflight does not check it). Chinese, English and Japanese `[FIELD]`; Russian prompts are not documented - write the model-facing prompt in English
(the handbook itself is Chinese, its English versions are translations that still work as
templates).

## Reference inputs `[FIELD]` `[DOC-2]`

| Material | Limit |
|---|---|
| Images | up to 10 |
| Videos | up to 5, 1-15 s each, 15 s in total |
| Audio | up to 5, 15 s in total; WAV or MP3, <= 15 MB `[FIELD]` |
| Overall | 20 assets; the handbook's omni-reference mode also names documents and web pages (API; not exposed on Higgsfield) |
| First/last frame | one `start_image`, one `end_image`; **cannot be combined with reference media** `[HF]` (422 at submission, no charge) |
| Video input for extension | input + new output <= 30 s `[DOC-2]` |

Reference videos are billed as extra seconds on some hosts (RunComfy: "counted seconds" = output +
every reference video) `[FIELD]`. **On Higgsfield they were not**: a 3 s 480p generation with a 6 s
reference video attached preflighted at 3 credits and was charged 3 `[HF]` (one measurement; a longer
reference may behave differently). Still run `get_cost` with the real media attached, and trim
reference videos to the shortest clip that carries the motion.

## What Wan 3 does well, and what it does not `[FIELD]` (vendors, directional)

| Reported strong | Reported weak |
|---|---|
| camera commands behave "like a parameter"; smooth long moves | uncommanded cuts inside continuous shots |
| physics-heavy moments (shattering, billiards) | realistic fights: contact, limb stability, weight, timing |
| long reference-heavy briefs; 30 s without swapping face, outfit or set | in-frame text, small numbers, logos, charts (Seedance 2.5 rated better on text) |
| editing: top of a video-edit arena (Atlas, vendor) | hands, dense crowds |
| stylized and non-real worlds (10 of the handbook's 64, second only to multi-shot) | dialogue audio texture; lip-sync mixed; Japanese and non-English speech uncertain |
| | 30 s narratives: one benchmark lost the entire 23-30 s closing beat of a four-beat story |
| | secondary characters lose position when occluded for more than a few frames |

Planning consequences `[CRAFT]`: keep the story to what fits - **a 30 s clip carries 3-4 beats, not
6**; put the payoff earlier than the last second; do not make legible small text the point of a
shot; for a fight, anime-style action is more forgiving than realistic.

## Scope not covered here

Document-to-video and web-page-to-video (API-only, require thinking mode `[FIELD]`); anything the
Higgsfield catalog does not list for `wan3_0`. Other models: `models_explore(action:"recommend")`.
When the user asks for a thing outside this list, say so instead of improvising.

## Speech languages `[OPEN]`

Not documented by Alibaba. Third-party guides name English, Spanish, French, German, Japanese,
Korean and Mandarin; Russian is never named. Calibration C4 (4 credits) answers it for Russian;
until then Russian speech is a risk: the fallback is silent generation plus Higgsfield `dubbing` /
`sync_so` lip-sync tools (`wan3-sound`).
