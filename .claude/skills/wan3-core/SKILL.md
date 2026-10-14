---
name: wan3-core
description: "WAN 3.0 CORE - prompt grammar, mode routing and pre-send checks for Alibaba Wan 3.0 / Wan 3.0 Prime video (Higgsfield wan3_0, wan3_0_prime: 2-30 s, 480p-1080p, native audio, image/video/audio references, first+last frame, edit and extend). Use whenever the user writes, fixes, checks or asks about a Wan 3 prompt: \"промпт для Wan\", \"Ван 3\", \"Wan 3.0\", \"wan3\", \"сцена на 30 секунд\", \"референсы Image 1 / Video 1 / Audio 1\", \"первый и последний кадр\", \"мультишот\", \"одним кадром без склеек\", \"модель сама режет\", \"поплыло лицо\", \"does Wan support...\", even if they only describe a shot. Load first for every Wan 3 task; wan3-budget (credits), wan3-film (camera, light, director packs), wan3-sound (voice, lip-sync, music), wan3-edit (edit/extend a clip) and wan3-stylized (anime, clay, ink, MG, 3D toon) build on it. Not for Seedance (seedance-25-core), Kling, Veo or stills (lira-image-prompts)."
---

# WAN 3.0 CORE

The prompt grammar for **Alibaba Wan 3.0 / Wan 3.0 Prime**, built from the official creator
handbook (64 prompts read in full), the Alibaba prompt guide as quoted by secondary sources, a
Higgsfield catalog and cost audit, and craft rules ported from the Seedance 2.5 set. The same
discipline applies here as there: **evidence first, craft second, and every claim carries a mark**.

Marks: `[HF]` measured on Higgsfield · `[DOC]` Alibaba text seen verbatim · `[DOC-2]` Alibaba, via
a secondary source · `[FIELD]` third-party report · `[CRAFT]` ported rule, untested on Wan ·
`[OPEN]` sources disagree · `[EMPIRICAL]` confirmed by generations here. The register, with every
source and what could not be opened, is `references/provenance.md`. **Read it once**: the official
pages were unreachable when this set was built, and the first three calibration results (C1, C10,
C13) are logged in `references/calibration.md`, which lists the cheap tests that create the rest.

**Scope.** Generating and editing video with Wan 3 on Higgsfield. Platform facts below are what the
Higgsfield catalog exposes, not what the raw Alibaba API offers.
Hand-offs: credits and drafts -> `wan3-budget` (always, before a paid call); camera, light,
look, director packs -> `wan3-film`; voice, lip-sync, music -> `wan3-sound`; edit, replace,
extend, restyle a clip -> `wan3-edit`; anime, clay, ink, MG, plush, 3D toon -> `wan3-stylized`;
performing characters -> `acting-system` (the craft applies, its Seedance numbers do not);
stills and reference sheets -> `lira-image-prompts`; Russian-language director workflow ->
`cinema-director-ru` (its Seedance 2.0 limits do not apply, use this file's); Seedance prompts ->
`seedance-25-core`.

## Reading map

| Situation | Open |
|---|---|
| Counts, durations, resolutions, ratios, what Higgsfield exposes, "does Wan do..." | `references/limits.md` |
| Writing any prompt: formulas, slot order, skeletons, word budgets | `references/prompt-grammar.md` |
| Choosing a mode; any image/video/audio reference; first/last frame; mapping lines | `references/modes-and-references.md` |
| More than one shot, a one-take, 15-30 s, timecodes, cuts, chaining past 30 s | `references/long-form.md` |
| Exclusions, quantified motion rules, "the model keeps doing X" | `references/constraints.md` |
| What the official handbook actually does; real exemplars to imitate | `references/official-corpus.md`; the 64 prompts themselves are in `references/handbook-prompts.md` (114 KB: search it, read only the hit's prompt) |
| Which claims are tested, how to test them for pennies | `references/calibration.md` |
| Where a claim comes from | `references/provenance.md` |

Reference files are short and read whole (R1), except `handbook-prompts.md`, which is a corpus: grep
it, then read the whole prompt around the hit. A worked, lint-clean example of a two-speaker, three-shot
REF prompt is `references/worked-example.md`.

## §0 - Operating rules

**R1 - A matched line is not a technique `[CRAFT]`.** A grep for "no cut" returns the phrase, not
the fact that the official long takes repeat it at every camera move. Read the section a
technique lives in, whole.

**R2 - An edit is a diff `[CRAFT]`, from the Seedance set's costliest lesson.** The accepted (or
last generated) prompt is the base. A revision names the line it changes, shows old -> new,
leaves everything else byte-identical, one fix per generation. Wan has no seed control on
Higgsfield `[HF]`: every generation is a new roll, so a rewritten prompt makes the next result
untraceable and the money unrecoverable.

**R3 - Verification produces text, not a yes.** Each check below yields a quote from the prompt,
a number from the cost tool, or an observation of a frame. A check answerable from memory
verified nothing.

**R4 - Price before you press.** No paid generation without a `get_cost` line (`wan3-budget`).
It is free and takes one call; the header carries its result. In a session without the Higgsfield
tools write the offline figure and say so: `Cost: 26.25 cr (offline estimate; media-attached price
unmeasured)`.

**R5 - Some failures are silent** (registry in §9): the output looks acceptable and the cause
hides. Only the checks catch them.

**R7 - Language.** Talk to a Russian-speaking user in Russian; the model-facing prompt, the header line
and the ledger are English (speech lines in the language to be spoken).

**R6 - Every delivered prompt carries a header line**, above the prompt block, outside the
model-facing text:

```text
Loaded: <skill - what was read>; ... | Not loaded: <skill - reason> | Mode: T2V|I2V|FLF|REF|EDIT|EXT | Model: wan3_0 720p 10s | Cost: 17.5 cr | Words: N | Negatives: N
```

A skill read before the latest compaction counts as not loaded; if you cannot tell whether a
compaction happened, re-read the files you are about to rely on. Words and Negatives come from
`python scripts/prompt_lint.py <file> --duration N`. A prompt without the header is a draft.

## §1 - Mode router `[HF]` `[DOC-2]`

Wan 3 is one model with several input shapes. The shape decides who owns the picture, so choose it
before writing a word. Higgsfield media roles: `start_image`, `end_image`, `image_references`,
`video_references`, `audio_references` `[HF]`.

| Mode | Media | Who owns the picture | Reach for it when |
|---|---|---|---|
| **T2V** | none | the text | look development, environments, anything with no fixed identity |
| **I2V** | `start_image` | the image owns frame 1; the text owns motion and camera | one specific face, product or location must match |
| **FLF** | `start_image` + `end_image` | both frames; the text owns the road between | a controlled transformation, a match cut |
| **REF** | `image_references` / `video_references` / `audio_references` | references own identity, style, motion or voice by role line; the text owns action | several identities, a product, a voice, camera or motion transfer |
| **EDIT / EXT** | `video_references` + an edit verb | the source video; the text names what changes | repair or alter an existing clip (`wan3-edit`) |

Rules `[FIELD]` unless noted, test with `calibration.md` C10 before relying on them on Higgsfield:

- **REF and start/end frames do not combine** `[HF]`: Higgsfield's validator rejects
  `start_image` / `end_image` together with reference media (422 "start_image/end_image cannot be
  combined with reference media", nothing charged; tested with `start_image` + `image_references`).
  Identity across a chain of clips therefore rides on the chosen frames, not on references: pick
  frames that carry it.
- **One primary task per prompt** `[CRAFT]`: generate, edit and extend never share a prompt.
- **When one face matters, use I2V or REF, not words.** Describing a face in prose is the weakest
  identity anchor (Atlas: "use image-to-video when one specific face matters").
- `aspect_ratio: auto` is listed by the catalog `[HF]`; that it follows the start image or reference
  framing is `[FIELD]` (C14). Set a ratio explicitly when references are mixed. Higgsfield lists 16:9, 9:16, 1:1, 4:3, 3:4 - **no 21:9** `[HF]`
  (see `wan3-film` for the workaround).

## §2 - The prompt in one screen `[DOC]` `[DOC-2]`

Alibaba's formulas, in the order the official examples write them:

```text
Basic     = Entity + Scene + Motion
Advanced  = Basic + Aesthetic control (light source, lighting environment, shot size,
            camera angle, lens, camera movement) + Stylization
From image= Motion + Camera movement           (the image already carries subject, scene, style)
Reference = Reference identifier (Image n / Video n / Audio n) + Action + Scene
            + Lines (optional) + Background music (optional)
Multi-shot= overall description + numbered shots with time ranges + shot content
Edit      = target + operation + "everything else unchanged"
Full      = overall description, references, timed shots, dialogue, sound, style,
            negative list (every section optional)
```

What 64 official prompts actually spend their words on (Atlas's count of the prompts, `[FIELD]`): style and texture 47% ·
consistency locks ("keep", "lock", "remains unchanged") 44% · camera language 31% · sound 23% ·
reference assignment 20% · aspect 19% · one-take 14% · shot + timecode 12% · prohibitions **6%** ·
frame-level motion rules 3%. Median 268 Chinese characters: **the handbook does not reward long
prompts**; the long ones are 20-30 s multi-shot scripts. Full skeletons, slot order and word
budgets: `references/prompt-grammar.md`.

Three habits visible in the handbook, worth adopting at once:

1. **Open with the lock line.** Medium + length + shot type + genre in the first sentence
   (`3D animated short, 30 seconds, dark fantasy theme, single shot, dim brick interior` - 011;
   `Generate a 25-second, 9:16 vertical, high-saturation summer street fashion short` - 027).
   Third-party guides say the opening is what Wan locks first `[FIELD]`.
2. **Write consistency as a sentence, per shot.** `Seamlessly continuing from the last frame of
   the previous shot, the character, clothing, apartment foyer, and camera position remain
   completely consistent` (035). Locks are 44% of the corpus because drift is the default.
3. **One primary camera treatment per shot, always named** - even "fixed shot" `[DOC-2]` `[FIELD]`. Unnamed camera
   direction lets the model cut or wander (`wan3-film`, `long-form.md`).

## §3 - Story contract first `[CRAFT]`

Before the assets: list from the user's **text** the subjects and counts, actions and their order,
scene and time, prop ownership, end state. One internal slot per named person, group, key prop and
place. Assets add only what is directly visible in them. A reference that shows a more prominent
person, outfit or room does not replace a plot element. Why first: every check below tests the
prompt against this contract, and a contract written after looking at the assets inherits their
prominence bias (the Seedance set paid for this with a duplicated character).

## §4 - References in one screen `[DOC]` `[DOC-2]`

Caps `[FIELD]`: 10 images, 5 videos (1-15 s each, 15 s total), 5 audio clips (15 s total), 20
assets overall. Naming `[DOC-2]`: **per-type numbering in upload order** - `Image 1`, `Image 2`,
`Video 1`, `Audio 1`. The handbook writes the same thing as `@Image1`, `Image1` and `Image 1`
interchangeably (18 prompts use `@Image`, 6 use `Image N`); mixing styles inside one prompt is
unnecessary risk, pick one. **Both bound correctly on Higgsfield** in a 3 s test (`Image 1 / Image 2`
in two clips, `@Image1 / @Image2` in one; calibration C1): `Image 1` is the default (two runs),
`@Image1` is acceptable (one run). A camera-only `Video 1` reference leaked no content in the one run.

Every reference gets one job and a role line that also says what **not** to take:

```text
Image 1 is the sole appearance reference for the man: face, hairstyle, build, clothing. Do not use its background.
Image 2 is the sole appearance reference for the woman: face, hairstyle, build, clothing.
Image 3 defines the location: city space, neon atmosphere, road structure. Do not use the people in it.
Video 1 supplies only the camera movement. Do not use its subject, scene or colour.
Audio 1 is the voice of the man; it covers all of his lines.
```

The handbook's own forms: `Image @Image2 serves as the sole appearance reference for the male
character` (038), `Facial features are completely locked to Girl A @Image1 and Girl B @Image2`
(037), `Define the woman in Image1 as Subject1 ... Subject1's dialogue tone of voice references
Audio1` (015), `Reference the aesthetic style of @Image1` (022), `Referencing the storyboard from
@Image1` (013). Counts, owners and the storyboard-per-time-range form (019):
`references/modes-and-references.md`.

## §5 - Time, shots, cuts `[DOC]` `[FIELD]`

Wan decides for itself whether to cut. Official long takes therefore say so, again and again:
`Do not cut.` after every camera move (003), `No cut.` opening each later shot of a 30 s take
(004), `No hard cuts or abrupt scene transitions` closing each shot (035), `no cuts, 15-second
long take` in the header (064). A shot list is not a guarantee either: Atlas counted the cuts
in the official multi-shot clips and found the declared count hit exactly in 3 cases, missed in
2, with a 4-shot prompt rendering 2 `[FIELD]`.

Write time as contiguous ranges from 0 to the generation length, each shot with its camera
clause and its end state; fractional seconds appear in official prompts (019: `1.48-3s`).
**Never copy an official timecode blindly**: five of the 64 run past 30 s (`Shot 4 [90s-120s]`).
Full rules, the one-take template, restating at each shot, and chaining past 30 s:
`references/long-form.md`.

## §6 - Sound in one screen

Audio is generated in the same pass `[DOC-2]`; unrequested, the model fills the track
`[FIELD]`; on Higgsfield `generate_audio` defaults on and **did not change the price** in the
preflight `[HF]`. So sound is always a decision: dialogue (speaker, quoted line, voice
descriptors), effects (`<sound of cloth rubbing>` inline, `[DOC]` 021/035), music (style and arc),
or explicit silence (`zero voiceover`, `no dialogue, only ambient`, 046/008). All of it in
`wan3-sound`.

## §7 - Exclusions `[DOC-2]` `[DOC]`

There is no negative-prompt field `[DOC-2]`. Write exclusions as plain sentences, only what must not
appear, never padded. The handbook uses prohibitions in **6%** of prompts, only where the model
has a strong default (a fairy that floats instead of darting; extra characters; subtitles). A
prohibition names the thing and risks printing it, so the first move is always the positive
rewrite. Rules, the "forbid the default, then count the replacement" form (016), and the checklist
for each negative: `references/constraints.md`.

## §8 - Parameters, not prompt text `[HF]`

Duration (2-30, or -1), resolution (480p/720p/1080p), `generate_audio`, `enable_thinking` and
aspect ratio are Higgsfield parameters. The handbook also states length and ratio inside the
prompt (`Generate a 25-second, 9:16 vertical...` - 19% mention a ratio), which sets pacing; keep
the two identical (the lint compares them). Two traps: **`-1` (smart duration) is billed as 10 s**
`[HF]` - never use it by accident; **`get_cost` with `count: 2` returned the single-clip price**
`[HF]`, so multiply variants yourself. `enable_thinking` (slower, better adherence `[FIELD]`) did
not change the preflight price `[HF]`; it is free in credits, so a draft should carry the same flags as the final (a draft with
thinking off does not predict the final's adherence); the only price is latency `[CRAFT]`.

## §9 - `[SILENT]` registry

Failures that still look like an acceptable clip:

| Failure | Why silent | Counter |
|---|---|---|
| An uncommanded cut inside a "continuous" shot | the clip is good, just not one shot | per-shot camera clause + `No cut.`; count cuts in the result |
| Timecodes that do not sum to the length (copied from a handbook example) | the model improvises the gap | lint; ranges 0 -> duration |
| Unrequested music or voice | sounds plausible | decide sound explicitly (`wan3-sound`) |
| Reference numbers shifted after changing upload order | wrong person looks "close enough" | numbers frozen after upload; re-read role lines against the media list |
| A 480p draft judged as the final look | no seed: the draft is not the take | `wan3-budget`: drafts test the prompt, not the take |
| Emotion adjectives instead of visible behaviour | flat acting reads as a model limit | `acting-system`; Atlas: "'anxious' is a hope, a description of chewing and gaze is an instruction" `[FIELD]` |
| `-1` duration | billed 10 s whatever comes out | fixed durations only |

## §10 - Checks `[CRAFT]`

**Pre-send - every prompt.** Print only failures with their fix, or `pre-send: pass`.

1. Header line present (R6); no skill in it was read before the latest compaction.
2. Mode declared; media roles consistent with it (no reference media together with `start_image` or
   `end_image`: the platform rejects it; no edit verb on a T2V).
3. Every reference numbered per type in upload order, with a role line that says what to take
   **and** what not to take; counts stated once.
4. Cost line present and inside the session budget; resolution is the lowest that answers the
   question this generation asks (`wan3-budget`).
5. Timeline: ranges contiguous, start 0, end = duration; every shot names its camera treatment;
   a one-take carries the no-cut clause.
6. Sound decided: each line attributed to a speaker, or silence/ambient stated; music decided.
7. Negatives counted, each justified by a strong default; a positive rewrite was tried first.
8. `python scripts/prompt_lint.py <file> --duration N --res 720p --images N --videos N --audios N --mode REF` ran (edit prompts: `--mode EDIT`); each warning
   answered.
9. A revision changed only the named lines (R2).
10. The loaded skills' own pre-send items passed.

**Full audit** - first prompt of a setup, after a failed generation (as the diagnosis), on
request. Each item quotes evidence:

1. Story contract slots filled and each one performs exactly one role in the prompt.
2. Reference jobs: one per asset, no asset used twice for different jobs, nothing uploaded and
   left unaddressed.
3. Opening sentence = lock line (medium, length, shot type, genre).
4. Per shot: camera clause, subject, one primary action, end state; physically possible per body.
5. Continuity: restate sentence at each shot that follows another; counts and owners of props.
6. Trigger before reaction (`seedance-25-film` §3 applies, `[CRAFT]`): the cause is visible
   before the face reacts.
7. Dialogue ledger (`wan3-sound`) for 2+ speakers.
8. Constraints: each negative traced to a default; quantified motion rules are countable.
9. Cost: the number matches `get_cost`; draft/final logic in `wan3-budget` followed.
10. After a failed generation: classify (cut, drift, audio, motion, identity, physics) and change
    **one** thing.
