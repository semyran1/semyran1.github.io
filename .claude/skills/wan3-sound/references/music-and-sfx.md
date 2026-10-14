# Music, effects, ambience, silence

Marks as in `wan3-core/references/provenance.md`; ids are official handbook prompts. Read this whole
file when sound is a design element, not an afterthought.

Contents: 1 Music as an arc - 2 Effects - 3 Ambience beds - 4 Mixing instructions - 5 Silence -
6 Sound for dance and rhythm - 7 Sound by dramatic function

## 1. Music as an arc `[DOC]`

The handbook never writes "epic music". It writes a **structure over time**:

- 006 (monster film), paraphrased from its half-translated text: a Hollywood disaster-monster score
  that opens with low ambient sound, a deep-sea low-frequency rumble, sparse drums and tense strings;
  adds stronger bass pulses, metallic impacts and mounting strings as the sea moves; hangs almost
  breathless before the monster surfaces; erupts into brass, heavy percussion and low-frequency
  impact when it breaks the surface; closes on thick, oppressive long notes and drumbeats.
- 045 (diary film): a segment-by-segment plan - felt piano and chamber strings as the base, a single
  sustained piano note to open, nylon-string guitar outdoors, cello entering for the sickness
  segment, a callback to the opening notes at the end; the emotional rule is `the emotion never
  spills out, always a kind of restrained tenderness`.
- 064: guzheng and bamboo flute, water ripples and morning birdsong, then a voice from the 8th
  second.

Recipe: **instruments + register + density + the point where it changes**. Anchor changes to
picture events or seconds (`from the 8th second`, `before the monster surfaces`, `on the first
drum hit`).

## 2. Effects `[DOC]`

Alibaba's effect formula: **source material + action + ambient sound** `[DOC-2]` (what makes the
sound, what it does, what surrounds it). Inline cues at the moment they happen:

```text
He wipes the bar counter with a cloth <sound of cloth rubbing> ... a faint whimper is heard <kitten whimper> ...
turns the black electronic lock handle <click of a mechanical unlocking sound> ... steps onto wet cobblestone <crisp echo of leather shoes on wet stone>
```
(021, 035). A trigger table for graphic or UI work: `a 'whoosh' sound when color blocks slide in,
a light keyboard 'click' sound when numbers tick, a crisp 'ding' bell sound when key data pops
up` (047). For game or action: `with gunshot sound effects + foxfire particle effects` per skill
(036). Be specific about material (cloth, leather on wet stone, mechanical lock), not "sound
effects".

## 3. Ambience beds

A bed is the sound of the place when nobody acts: `night insect chirps, faint water sounds, a
low-frequency resonance as the plant rises` (008); `the faint hum of equipment` (002); `low
teahouse ambient sounds` (059); `Soft guzheng and bamboo flute, subtle water ripples and morning
birdsong` (064). Write the bed in the global lines, one sentence, with a distance word (`distant`,
`close`). Water, waves or echo words can print ripple artefacts (Seedance FAQ `[CRAFT]`): remove
them where the picture does not need them.

## 4. Mixing instructions `[DOC]`

The handbook states relative levels: `BGM (must be present, runs through the entire video, volume
clearly audible) ... when the voiceover appears the music does not disappear, volume slightly lower
than the voice` (047); `overall quiet and restrained, with emotions turned inward` (045). Say it in
words: which layer leads, which sits under it, when the music rests.

## 5. Silence `[DOC]` `[CRAFT]`

Silence is a design choice and has to be written, or the model fills it. Forms:

- the whole film: `zero voiceover` (046), `no dialogue, only ...` (008), Alibaba's `No BGM,
  generate only ambient and action sounds`;
- a beat: the sound **drops** at the break (see `wan3-film` dramatic functions) - write the
  drop as an event (`all sound cuts out the instant the blade stops`);
- a character: their lips stay closed while listening.

If music leaks into a "no music" prompt, restate the constraint at the end of the prompt as well as
at the head, and name what the soundtrack does contain `[CRAFT]`.

## 6. Sound for dance and rhythm `[DOC]`

043: `Choreograph the dance according to the fixed audio's rhythm, speed, and emotional
fluctuations: heavy drum beats correspond to sharp, large-scale movements ...` (the rest is
Chinese in the archive: calm passages -> soft body waves and hand poses, the chorus -> denser,
more explosive movement).
024 lets the **music clock the timeline**: `On the first drum hit ...`, `On the heavy accent of
the first lyric line ...`, `At the syncopation point of the second lyric line ...`, then a single
closing line allocating the shots. Use a reference audio for fixed music, or write the beats
yourself; do not expect cuts to land on beats unless the beats are named.

## 7. Sound by dramatic function `[CRAFT]`

Establish: ambience before the subject (sound before picture). Reveal: a cue just before the
visual. Escalate: add a layer at intervals. Break: remove sound. Climax: peak then cut to
silence, or hold the peak into the freeze. Resolve: a held note, a reprise of the opening motif,
a bed returning (045 ends on the opening notes). The function table is in
`wan3-film/references/dramatic-functions.md`.
