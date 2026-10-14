# What the official handbook actually does

The best evidence this set has: 64 prompts written by the model's makers for their own showcase
(`handbook-prompts.md`, verbatim, ids below refer to it). Read as a practitioner, not as a
specification - it shows what Alibaba's team writes, not what is guaranteed. Marks as in
`provenance.md`; everything here is `[DOC]` unless marked.

Contents: 1 Shape of the corpus - 2 Techniques (T1-T16) - 3 Eight short exemplars to imitate -
4 What the corpus does not show - 5 Reading cautions

## 1. Shape of the corpus

Categories of the 64 (the archive's 17 X posts are not counted): Multi-shot storytelling 11 ·
Stylized and non-real 10 · Reference-driven 10 · VFX and transitions 8 · Character performance 6 ·
Commercial and product 6 · Camera movement and one-take 5 · Cinematic lighting and colour 3 ·
Audio-synced dialogue 3 · Creative fun 1 · Chinese classical 1. Of the 64, **22 carry a source
video** (edit, replace, extend, motion/camera transfer, dialogue replacement) - the handbook
treats Wan 3 as an editor as much as a generator. Atlas counts over the 64 `[FIELD]`: style and texture 47% · consistency locks 44% ·
camera 31% · sound 23% · reference assignment 20% · ratio 19% · one-take 14% · shot + timecode
12% · prohibitions 6% · frame-level rhythm 3%. Median 268 Chinese characters; half are under 300.

## 2. Techniques

**T1 - The lock line opens the prompt.** `3D animated short, 30 seconds, dark fantasy theme,
single shot, dim brick interior scene.` (011) · `Generate a 25-second, 9:16 vertical,
high-saturation summer street fashion short.` (027) · `This is a 30-second cinematic high-intensity
single-shot (One-Take) visual spectacle short film.` (004) · `A 3D animated fantasy short film with
4 shots, moving from cautious approach to the appearance of a giant creature and then to a
stunned gaze.` (008: the arc in one sentence).

**T2 - A style bible before the action.** Visual language + colour system + texture + camera
habits in one paragraph (004: "blends the gritty feel of 1990s street skateboarding videos with
the refined quality of modern commercial blockbusters ... extreme 'California Sunshine' cinematic
color grade"). Lists are used for long bibles: `The visuals employ: Hyper-realistic CGI; ...`
(005), a colour dictionary with jobs (007).

**T3 - Spec lines as camera hardware.** `shot with Arri Alexa 65 and Panavision anamorphic
lenses, Kodak Vision3 500T film texture, 8K resolution, photorealistic, no text` (037); `35mm
film ... natural light flares ... 4k high quality` (063); `approximately 14-16mm ultra-wide-angle
lens, with slight fisheye distortion and barrel distortion` (028). Hardware names are paired
with a visible consequence in the strongest cases (028).

**T4 - Camera named per shot, one treatment each.** `Camera: Medium shot.` · `Camera: Fast
orbiting.` · `Camera: Handheld feel, high-speed capture.` · `Camera: Slow motion to freeze frame.`
(062) · `Close-up, eye-level perspective, continuous fast panning, one-take` (003).

**T5 - No-cut clauses repeated.** `Do not cut.` after each pan (003) · `No cut.` opening each
later shot (004) · `No hard cuts or abrupt scene transitions` closing each shot (035) · `no
cuts` in the global line (064).

**T6 - Continuation sentence.** `Seamlessly continuing from the last frame of the previous shot,
the character, clothing, apartment foyer, and camera position remain completely consistent` (035,
shots 2 and 3).

**T7 - Reference mapping lines.** See `modes-and-references.md` section 3.

**T8 - Storyboard per time range.** `Image 1 (0-1.48s) ... @Image1` (019); `Referencing the
storyboard from @Image1, Shot 1 ...` (013).

**T9 - Sound written into the picture.** Inline effect cues in angle brackets (`<sound of cloth
rubbing>`, `<kitten whimper>`, `<click of a mechanical unlocking sound>`, 021, 035); music as an
arc over the timeline (006: low ambient opening, rising bass and strings, a held breath, brass when the
monster surfaces - paraphrased from the half-translated text; 045: a per-segment piano/strings/guitar plan); voice
descriptors (`Male voice clear and cool, slightly free-spirited, moderately fast pace, moderate
pitch`, 036); a sound-effect layer with triggers (`a 'whoosh' sound when color blocks slide in, a
light keyboard 'click' sound when numbers tick`, 047); explicit silence (`The audio type
includes ambient sounds and music, no dialogue`, 008; `zero voiceover`, 046).

**T10 - Sectioned briefs when the cast is large.** `[Video Type] [Video Duration] [Reference
Material] [Shot Structure] [Shot Control] [Action & Effects] [Expression & Lip Sync] [Voice &
Sound Effects] [Visual Style]` (036); `【Overall Style】`, `【Character Action Logic】`, `【Light Orb】` (038).

**T11 - Action logic, not just action.** 038 gives the *why* of both fighters' movement
(`the woman's advantages are lightness, speed ...; the man's are strength, anticipation ...`) and
turns it into verbs (`grab, block, redirect force, change hands, ... counter`): behaviour rules
that make choreography consistent.

**T12 - Quantified motion.** 016 (see `constraints.md` section 4).

**T13 - Camera like a person.** `Hand movements occur first, and the camera follows with about a
0.1-second delay`; `autofocus needs about 0.2 seconds to re-lock`; `The shake must come from
breathing, footsteps, turning inertia, and startled reactions, not regular vibration` (028).

**T14 - Edit prompts are tiny.** `Remove the man on the left in video 1, and naturally fill that
position with the surrounding background, keeping all other characters, actions, and the picture
unchanged.` (031, 27 words). Operation + target + fill rule + keep list. Library: `wan3-edit`.

**T15 - Beats tied to music and breath.** `On the first drum hit, the five maintain a sculptural
back-facing starting pose, simultaneously whip their heads 90 degrees ...` (024): the timeline is
musical, not clock-based, and the final shot allocation is summarised in one line at the end
(`Full video shot allocation: opening fixed medium shot ..., chorus wide-angle fan-out then
abrupt cut to slow-motion close-up ...`).

**T16 - Closing frame stated.** `The frame finally freezes on this expression` (003) · `freezing
into a perfect movie poster composition` (064) · `freeze frame to end` (023): the last frame is
designed, so a dropped final beat costs nothing.

## 3. Eight short exemplars to imitate (read the full prompt in `handbook-prompts.md`)

| Id | Teaches | Shape |
|---|---|---|
| 001 | single-shot grammar | shot size -> subject -> face behaviour -> light -> camera character -> one gaze change |
| 010 / 012 | how little a stylized clip needs | style + setting + one event, 47-49 words |
| 031 | edit | 27 words |
| 020 | product -> model | 1 sentence + 1 image |
| 015 | two-person dialogue with two voice references | Subject1/Subject2 definitions + alternating action-and-quote lines |
| 021 | inline sound + camera per shot | `Shot 1 ... <sound of cloth rubbing> ... Shot 3: Slow push-in ...` |
| 035 | seamless world change | continuation sentence, inline sound and music cues, no-hard-cut closing |
| 016 | quantified motion | priority, forbid, count |

## 4. What the corpus does not show

- A negative-prompt list. The handbook has no such field; exclusions are inline.
- Resolution, `enable_thinking` or seed guidance: the prompts are API-agnostic.
- Failure rates. These are showcase clips picked by the maker; Atlas's cut count over the same
  clips found the declared shot count missed in two of five multi-shot cases `[FIELD]`.
- Russian or any non-English/Chinese speech: dialogue appears in English and (transliterated)
  Chinese (064: pinyin `Yu ba Xi Hu bi Xi Zi`).
- Price. Nothing in the handbook speaks to cost - which is what `wan3-budget` is for.

## 5. Reading cautions

Several entries are cut short in the archive (005, 007, 016, 017, 025, 027, 028, 038); five carry
timecodes beyond 30 s (008, 013, 023, 048, 049); a few translations keep Chinese fragments
(`nearly崩溃`, 002; whole runs in 006); the English is machine translation, so phrases such as
"guanxi young idol" (003) are artefacts. Copy the structure and the clause, rewrite the words.
