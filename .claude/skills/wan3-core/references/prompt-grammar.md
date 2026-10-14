# Prompt grammar - formulas, slot order, skeletons

Marks as in `provenance.md`. Read this whole file before writing a prompt. Examples are quoted
from the official handbook by id (`wan3_0NN`, see `official-corpus.md`) unless marked `[CRAFT]`.

Contents: 1 Slot order - 2 Skeletons - 3 Writing the slots - 4 Word budgets - 5 Weak words -
6 Header line vs parameters

## 1. Slot order

The Chinese note over the 64 official prompts describes the dominant order `[FIELD]`: **style and
tone first, then the space, then the subject and its action, and the camera movement last** (p02).
Alibaba's own order for the structured form is `[DOC-2]` (as the samples are described by secondary sources):

```text
1  Length, ratio, medium, genre          (the lock line; optional for a bare single shot)
2  Subject + assets                      (who/what; reference mapping lines)
3  Scene + style
4  Shot + motion                         (size, angle, lens, camera, then the action)
5  Dialogue + sound effects
6  Exclusions
7  Timeline                              (only when more than one beat)
```

These two orders agree on the part that matters: what the picture *is* comes before what it
*does*, and the camera clause sits next to the action it follows. Pick one and keep it inside a
project, so a changed line is visible as a diff.

## 2. Skeletons

### 2a. Single shot, 4-10 s `[DOC]` pattern

Handbook exemplar (001, one paragraph, 120 words): shot size and framing -> subject -> what the
face does -> light -> camera character -> the one change over time. Template:

```text
<Medium/genre>, <length>, <shot type>. <Style and texture in 1 sentence>.
<Space and light: where, time, what is lit by what>.
<Subject: who, wardrobe, build - or "Image 1 is ..." when referenced>.
<Action: the primary change, in order, with speed words>.
<Camera: one named treatment, with start and end>.
<Sound: the decision, one sentence>.
```

Rule of one: **one primary action per shot.** `[DOC-2]` guides repeat "avoid stacking incompatible
events in one short generation"; the handbook's short clips (010, 012, 061) carry one event.

### 2b. Multi-shot script, 10-30 s `[DOC]`

Two official shapes; take the first by default.

```text
<Overall: length, ratio, medium, genre, the film in one sentence, style bible, continuity locks,
 sound bed>

Shot 1 [0-6s]: <size/angle>, <camera treatment>. <Subject, action, end state>. <Sound cue>.
Shot 2 [6-13s]: <No cut. | Hard cut to> <size/angle>, <camera>. <...>
Shot 3 [13-20s]: ...

<Closing: the final frame, the sound arc, constraints (<= 2)>
```

Exemplars: 004 (30 s, four shots, `No cut.` after the first), 035 (three 5 s shots with a
continuity sentence each), 037 (five 3 s jump cuts, each shot labelled `(Jump Cut)`), 062
(`Shot 3 [8s-13s] Camera: Fast orbiting. / Scene / Plot / Details`). The second shape is
the sectioned brief - `[Video Type] [Duration] [Reference Material] [Shot Structure] [Shot Control]
[Action & Effects] [Expression & Lip Sync] [Voice & Sound Effects] [Visual Style]` (036, 15 s, three
characters) - handy when many references and many sound layers must each have a labelled place;
it costs words, so use it above ~3 references or ~3 speakers.

Alternative bracket form for a continuous take (064): `[0-3s: A drop of water]` followed by a
paragraph, with a *Global setting* block and a *Voiceover and sound effects* block before the
timeline. Use it when the film is **one** camera with beats, not a cut sequence.

### 2c. Reference-driven `[DOC-2]`

`Reference identifier + Action + Scene + Lines + BGM`. Mapping lines first (the role lines of
SKILL.md §4), then the action, then scene and sound. Full protocol:
`modes-and-references.md`.

### 2d. From a start image (I2V) `[DOC-2]` `[FIELD]`

The image already carries subject, scene and style: write **motion and camera only**. State what
moves, which way, how fast and with what force; keep subject motion and camera motion as separate
instructions; describe start, acceleration, stop; name what must **not** change, because a start
image anchors the opening, not the clip. One user test saw the subject leave his post and the camera
walk behind him when the prompt did not forbid it `[FIELD]`.

```text
The man holds the pose for one second, then turns his head slowly to the left
and lowers his eyes to the letter in his hand. The camera is fixed.
The room, the lamp and the man's position stay as in the first frame.
```

(The picture goes in as `start_image`; it is not an `Image 1` and needs no tag. The Seedance set's
standalone "use X as the first frame" sentence is `[CRAFT]` there and not needed here.)

### 2e. First + last frame (FLF) `[FIELD]`

Prompt **the road, not the destination**: write timed motion beats between the two frames. Keep
subject, lens, aspect ratio and lighting consistent across both frames or the clip reads as a hard
cut. Frames of different ratios fail `[CRAFT]`. Atlas's first pass: 5 s, 720p, audio off.

## 3. Writing the slots

**Subject.** Concrete and observable: build, wardrobe, props with a size ("a large black soft dice,
close to the height of the character's calf", 027). Identity that must survive lives in
references; prose descriptions of a recurring face "burn words and drift" `[FIELD]`. Where prose
is the only anchor (T2V, no references), write a **locked description** and paste it unchanged into
every shot: 027 does this as a bullet list ending `No changes to hairstyle, clothing color, or the
number of yellow decorations`.

**Scene and style.** Medium and texture first: `Japanese sports anime style 2D animation`,
`Hand-drawn animation style, oil painting brushstrokes, cold color palette` (010, 012). Palette as
named colours and their jobs (`Teal: the cloudless sky ... retro red fuel pump`, 007). When a look
must not become another, say what it is not: `The overall look is not realistic live-action film,
not childish cartoon, nor dirty, heavy industrial cyberpunk` (038).

**Action.** Ordered verbs on one body; speed words from Alibaba's guide - slowly, sharply, rapidly
`[FIELD]`; timing in beats when it matters (`first drum hit`, `at the 8th second`). Visible
behaviour, not mood: `her gaze shifts from looking forward to looking down at her hands` (001);
the Atlas rule is the same `[FIELD]`.

**Camera.** The vocabulary lives in `wan3-film`; here the rule is one main treatment per shot,
named, with subject and both ends; `fixed shot` is a treatment, and without it Wan moves the
camera on its own `[FIELD]`. Alibaba ties each move to its meaning - push-in intimacy or tension,
tracking beside the subject, orbit emphasis, fixed stillness `[DOC]` (quoted in a search excerpt of the guide).

**Light.** Source plus environment, in Alibaba's words `light source` and `lighting environment`
(`Soft LED softbox light spills in from the right`, 003; `cold white moonlight as the dominant hard
light, high-contrast low-key lighting, side-lighting`, 011).

## 4. Word budgets `[CRAFT]` informed by `[DOC]`

| Clip | Words (diagnostic, not a cap) | Official orientation |
|---|---|---|
| Edit / swap / remove | 10-85 | 029-034, 050-057 run 11-82 English words |
| Bare single shot | 45-130 | 010: 49, 012: 47, 061: 112, 001: 120 |
| Single shot with sound / dialogue | 120-230 | 015: 127, 011: 223 |
| 15 s multi-shot | 350-620 | 037: 393, 035: 580, 036 (sectioned): 611 |
| 20-30 s multi-shot / one-take | 400-920 | 026: 408, 004: 543, 064: 574, 003: 919 |

(Word counts are of the English translations in the archive; the Chinese originals are shorter -
median 268 characters, ten prompts over 800 - so these numbers describe the upper side.)

Growth between versions is the signal to compress, not the absolute count: cut repeated style
terms and repeated constraints first, never mappings, roles, events or end states (the Seedance
set's rule, same cause). A very short prompt is not empty - the platform may rewrite it
(`prompt_extend` `[OPEN]`) - but the rewrite is not under your control either.

## 5. Weak words `[FIELD]`

"Cinematic", "premium", "epic", "beautiful" crowd out concrete content; name the shot type and one
move instead. Emotion adjectives ("anxious") are hopes, a described behaviour is an instruction.
Stacked incompatible terms ("close-up" with "wide shot", "drone shot, handheld close-up, locked-off
dolly, fast orbit") are resolved arbitrarily; pick one.

## 6. Header line vs parameters

The platform parameters (duration, resolution, ratio, audio, thinking) are set outside the
prompt. The handbook also writes length and ratio into its opening sentence (19% of the 64 name a
ratio) and the model's pacing seems to follow it `[CRAFT]`. Keep the two identical: a prompt that
says 30 seconds on a 15 s generation gets the first half of the story. `prompt_lint.py` compares
the sentence with `--duration`.
