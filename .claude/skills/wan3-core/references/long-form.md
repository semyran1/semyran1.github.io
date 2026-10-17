# Long form - timelines, one-takes, cuts, 30 seconds and beyond

Marks as in `provenance.md`; ids are official handbook prompts (`official-corpus.md`). Read this
whole file for any clip with more than one beat.

Contents: 1 What Wan does with a timeline - 2 Time rules - 3 The three cut states - 4 Per-shot
camera clause - 5 Restating continuity - 6 Templates - 7 Sound on the timeline - 8 Budget the
beats - 9 Verify the result - 10 Past 30 seconds

## 1. What Wan does with a timeline

Wan generates up to 30 s in one pass `[HF]`, and the official long clips are written as timelines.
The model **decides for itself whether to cut** `[FIELD]`; a timeline is an instruction it follows
imperfectly: Atlas ran ffmpeg over the official multi-shot clips and found the declared shot
count hit exactly in 3 cases, missed in 2, and a 4-shot prompt rendering 2 `[FIELD]` (vendor
count, directional). Reviews also report unprompted jump cuts in a partner-dance clip and
multi-shot sequences that "feel stitched". The practical rule: **say what happens at every
boundary** - cut, no cut, or a transition - and verify in the result.

## 2. Time rules `[DOC]` `[CRAFT]`

- Ranges are contiguous, start at 0, and the last one ends at the generation length. A gap is
  improvised by the model; an overlap is resolved arbitrarily.
- Whole seconds by default. Fractions occur in official prompts (019: `Image 2 (1.48-3s)`,
  `Image 4 (4.64-8.52s)`) - acceptable for storyboard-frame timing, noise elsewhere.
- **Do not copy official timecodes.** Five of the 64 run past 30 s - 008 (`Shot 4 [90s-120s]`), 013
  (`[150s-180s]`), 023, 048, 049. They look like relative slots; whatever they are, they violate
  the rule above and would be improvised.
- One shot = one primary state change and an observable end state (`The frame finally freezes on
  this expression`, 003). A range is a time budget: too much in too short a range makes the model
  drop beats or cut excessively `[FIELD]`.
- Official ranges are uneven and follow the story: 0-3, 3-10, 10-15 (036); 0-6, 7-15, 16-24, 25-30
  (004, note the 1 s gaps, which that prompt tolerates). Choose by beat, then check the sum.

## 3. The three cut states

Write one of them at every boundary - never leave it to the model.

| State | Wording that appears in the handbook | Use |
|---|---|---|
| **No cut** (continuous take) | `Do not cut.` after each camera move (003); `No cut.` as the first words of each later shot (004); `One continuous shot` / `one-take (single-shot continuous seamless camera movement)` in the shot header (003, 026); `no cuts, 15-second long take` in the global line (064) | a camera that travels through one space; a transformation shown unbroken |
| **Hard cut** | `Shot 2 [30s-60s] hard cuts to a medium shot from behind` (008); `(Jump Cut)` after the shot label, `pure jump cut editing logic` globally (037); `cuts` / `cuts to` | coverage, montage, time jumps |
| **Seamless transition** | `Seamlessly continuing from the last frame of the previous shot, the character, clothing, apartment foyer, and camera position remain completely consistent ... No hard cuts or abrupt scene transitions` (035) | the world changes while the camera and the character persist |

Rules `[CRAFT]` that the corpus supports: a continuous take needs its clause **every time** (the
Seedance set learned that adding one camera move to a finished one-take without the clause
turned it into cuts); a one-take chains moves *in written order*, each with subject and end state
(003: pans alternate between the director and the idol through the whole scene, `Do not cut.` after each);
montage is requested by saying montage, not by counting moves.

## 4. Per-shot camera clause `[FIELD]` `[DOC]`

Alibaba's guide asks for the camera treatment in every shot, and the unnamed case is where Wan
cuts or wanders (LUVI: "name the camera in every shot, or it cuts for you"; OpenArt: say `fixed
shot` if you want it still, because Wan will move it). Pattern: `Shot N [t-t]: <size/angle>,
<one camera treatment>.` The handbook's own slots: `Camera: Medium shot.` / `Camera: Fast
orbiting.` / `Camera: Slow motion to freeze frame.` (062). One main camera action per shot;
two moves in one shot fight (Wavespeed). Vocabulary: `wan3-film`.

## 5. Restating continuity

The handbook's multi-shot prompts spend words on **what must remain**, shot by shot (035: the
sentence is repeated, adapted, in shots 2 and 3). Restate, per shot that follows another:
subject (face/build/clothing), location, camera position or lens, light, and the sound bed. Use the
same words each time, so a change is a diff. Prefer a single named **lock block** at the head
(027: `The character's styling remains consistent throughout the film: ... No changes to hairstyle,
clothing color, or the number of yellow decorations`) and one pointer sentence per shot.

## 6. Templates

**Continuous 30 s take** (004 / 064 shape):

```text
<Length>, <ratio>, <medium>, one continuous take, no cuts. <Style bible: palette, texture, lens look>.
Global setting: <space, light, time>. Subject lock: <locked description or Image 1 mapping>.
Sound: <bed + cues>.

Shot 1 [0-8s]: <size/angle>, <camera treatment with subject and end>. <Action, end state>.
Shot 2 [8-16s]: No cut. <camera continues: move 2, subject, end>. <Action, end state>.
Shot 3 [16-24s]: No cut. ...
Shot 4 [24-30s]: No cut. <landing: where the camera stops, what is in frame, freeze or fade>.
```

**Hard-cut montage, 15 s** (037 shape):

```text
<Length>, <ratio>, <medium>, pure jump cut editing logic, <look>. Faces locked to Girl A (Image 1) and Girl B (Image 2).
Shot 1 [0-3s] (Jump Cut): <frame, subjects, light, one action>.
Shot 2 [3-6s] (Jump Cut): ...
Camera movement: <short list>. Colour: <2-3 named colours>.
```

**Seamless world change** (035 shape): one shot per world beat, each opening with the
`Seamlessly continuing from the last frame ...` sentence and closing with `No hard cuts or abrupt
scene transitions`.

## 7. Sound on the timeline

Anchor cues to seconds or beats as the handbook does (`From the 8th second, an ethereal, gentle
female voice slowly recites ...`, 064; `On the first drum hit ...`, 024) and put inline effects
where they happen (`<click of a mechanical unlocking sound>`, 035). A voice needs room: the
handbook's own pace is **about 2.5 words per second** (047) - a 15-word line needs ~6 s of shot,
not 3. Details: `wan3-sound`.

## 8. Budget the beats `[FIELD]` `[CRAFT]`

A 30 s clip carries three or four beats, not six. One benchmark lost the entire 23-30 s closing
beat of a four-beat story; Atlas: "a 30-second generation gives the model more opportunities to
fail". Put the payoff in the middle third and let the last seconds be a landing (a freeze, a pull
back, a fade), which costs nothing if dropped. For any story longer than 30 s, plan clips of
8-15 s joined by start-image chaining (or cut together in an editor), not a longer prompt (section 10).

## 9. Verify the result

Counting cuts is a measurement, not an impression: `python scripts/count_cuts.py clip.mp4
--expect N` prints the cut times it detects, so "the take stayed one shot" is a number (R3). Record
the verdict next to the prompt version; `calibration.md` C2/C3 use it to learn how reliably the
clauses of section 3 work on Higgsfield.

## 10. Past 30 seconds `[FIELD]`

Two routes; Alibaba's own continuation rule (input + new output <= 30 s `[DOC-2]`) shapes both.

1. **Extend** an existing clip with `video_references` and an extend instruction
   (`Extend video 1 by 15 seconds. Character A is ...`, 059; `Extend the video forward by two
   seconds from the middle segment ...` / `backward by three seconds`, 061): see `wan3-edit`.
   Whether Higgsfield routes an extend instruction (the vendor Sogni says the raw API has no
   extend task) is `[OPEN]` - calibration C9.
2. **Chain** (start-image chaining, I2V; `modes-and-references.md` section 7): generate scene by
   scene, pull a clean still near the end of each, use it as the next `start_image`, restate the
   locks, join in an editor. Expect more than one run per join; budget accordingly (`wan3-budget`).
3. **Hard-cut coverage needs no chaining at all**, but every new angle needs its own background anchor: Wan kept the declared cut counts and lost the room (`wan3-film` `references/angles-and-geometry.md`). If the scene is shot/reverse-shot or a montage,
   generate each shot as its own REF clip (same references, same locks) and cut them together in an
   editor; identity rides on the references, and a failed shot is re-bought alone.
