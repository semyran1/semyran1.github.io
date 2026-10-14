# Constraints - exclusions, locks, quantified motion

Marks as in `provenance.md`; ids are official handbook prompts. Read this whole file before adding
a prohibition or when "the model keeps doing X".

Contents: 1 What exists - 2 The ladder - 3 Locks - 4 Quantified motion - 5 The prohibitions the
handbook allows itself - 6 Accounting - 7 Safety and names

## 1. What exists

- **No negative-prompt field** `[DOC-2]`: Wan 2.6 had a 500-character one, Wan 3.0 does not
  `[FIELD]`. Exclusions are sentences in the prompt, "only what you do not want, no padding, no
  repetition of the positive prompt" `[DOC-2]`; an empty list is fine.
- Alibaba's common negatives: no subtitles, no watermark; for sound, `No BGM, generate only
  ambient and action sounds` `[DOC-2]` `[DOC]`.
- The handbook uses prohibitions in **6%** of its prompts (Atlas count) `[FIELD]`, always where the
  model has a **strong default**: how a fairy flies (016), extra people or objects (018, 027), a
  clean-commercial look when a rough one is wanted (028), subtitles/text (027, 037), music
  (046: `zero voiceover`).
- A prohibition names the thing, and a named thing is half-drawn `[CRAFT]`: it is the last rung of
  the ladder, never the first.

## 2. The ladder

Before writing "no X", climb in order and stop at the first rung that works.

1. **State what exists.** "The corridor is empty" instead of "no people".
2. **Lock the thing you want.** "There is always exactly one orb; its size is stable" (038).
3. **Quantify** the behaviour (section 4).
4. **Forbid the default and name the replacement**: `It is forbidden to portray it as an ordinary
   fairy slowly floating ... must adopt a dragonfly-style "fixed-point hover - instantaneous
   ejection - complete emergency stop - acute angle trajectory change" motion` (016).
5. Plain prohibition, one line, the object named once.

## 3. Locks `[DOC]`

Consistency is the largest single block of the handbook after style (44%). Forms that appear:

| Lock | Wording | Id |
|---|---|---|
| Identity | `Strictly maintain the stability and uniformity of both characters' faces, hairstyles, body types, clothing structure, color schemes, and recognizability` | 038 |
| Wardrobe | `No changes to hairstyle, clothing color, or the number of yellow decorations` | 027 |
| Prop shape | `Maintains the same proportion and shape in all shots; Does not turn into a regular small dice` | 027 |
| Prop count | `There is always only one orb, its size is stable - it does not duplicate, disappear, or deform` | 038 |
| Composition | `each character always fixed in the center of the frame, with stable composition - no character movement, no large camera movements` | 014 |
| Product | `the product packaging's gold-stamped logo, text, deep forest green color scheme, and printed patterns remain highly consistent without distortion` | 039 |
| Continuation | `the character, clothing, apartment foyer, and camera position remain completely consistent` | 035 |
| Look | `The entire video maintains high-contrast black and white with hard-edged lighting ... no soft light, no filters` | 024 |

Write the lock once in a named block, point to it per shot. Locks are positive in form ("stays the
same") even when they contain a "no".

## 4. Quantified motion `[DOC]`

When the default motion is wrong, adjectives lose. The handbook's best technique (016, the only
official example the Chinese note calls "physical-level") replaces the default with a countable
rule:

```text
Highest priority requirement: <motion archetype in quotation marks>. It is forbidden to portray it as <the default>.
For the first 7.8 seconds, at least six clearly distinguishable burst movements must appear.
Each ejection must cross 60%-90% of the screen width within 3-5 frames, and come to a complete
stop for 2-4 frames immediately upon reaching the new position.
The sprint process leaves only 1-2 frames of body afterimages; the character must instantly become sharp after the stop.
```

Ingredients to copy: a priority marker, a metaphor from the real world (a dragonfly), the
default named and forbidden, **how many times, how fast in frames, how far in screen fractions,
how long it holds**, and what the trace looks like. Use it for jerky/robotic/stop-motion movement,
speed ramps, rhythm that must land on beats; do not use it for ordinary acting.

Related official numbers: camera reaction lag `the camera follows with about a 0.1-second delay`,
refocus `about 0.2 seconds to re-lock` (028); speech pace `about 2.5 words/second` (047);
shot rhythm: `at least six clearly distinguishable burst movements` in the first 7.8 s (016).

## 5. Physical possibility `[CRAFT]`

Per shot, every verb sits on one body and one limb at a time; a hand cannot hold the cup and open
the door at once. Contact moments (fight blows, catches, handoffs) are where realism breaks first
`[FIELD]`: write contact as a sequence of readable beats (first strike / second strike / third
strike, 062), give each its camera (`the camera captures the subtle details of ink traces cracking
as the blades grind`), or choose a stylized treatment, which is more forgiving.

## 6. Accounting `[CRAFT]`

`prompt_lint.py` prints every negative with its line. For each, write the default it fights
(one phrase). A negative with no default behind it is deleted. Standing user lines (no music, no
subtitles) are requests and stay, once each. Count goes in the header (`Negatives: N`); growth
between versions is the signal that fixes are being stacked instead of replaced.

## 7. Safety and names `[DOC-2]`

Alibaba's family-wide "avoid" list: real named people, rapid scene changes inside a single clip,
and relying on rendered text. In practice: describe a look instead of naming a real person; one
event per shot; if on-screen text is the point, plan to confirm it in the draft or add it in post.
