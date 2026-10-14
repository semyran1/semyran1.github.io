# STYLEPACK - Fincher / *Se7en* - *Mindhunter*

Built to `_contract.md`. Load with `wan3-film` and `wan3-core`, and with no other pack. All
`[CRAFT]`; rules marked (S) were Seedance-observed (failed generations on Seedance 2.5) and are not yet
confirmed on Wan. Read the whole pack: the VOCABULARY changes the style block in an enclosed
interior, and a pack applied from its style block alone reproduces the surface mimicry it exists to
prevent.

## IDENTITY

Dark procedural suspense: one motivated light source, a camera that watches from concealment
rather than films, and a world stripped of every colour except cold shadow and dirty warmth. The
thesis is restraint - almost nothing is shown, and what little is shown is exact.

## VOCABULARY

- **Palette:** desaturated teal-cyan shadow, dirty tobacco-amber highlight, deep blacks with the
  black point just above zero - the darkest surface in frame is a named material (wet concrete,
  oxidized metal) with faint texture still in it - and one cold clean white reserved for the single
  practical light source.
- **Light:** exactly one motivated source per shot (streetlamp, flashlight, window), hard falloff
  into deep dark that still holds the room's shape, no camera-side fill, volumetric haze inside
  every beam. Wide frames (S): "solid black, no shadow detail" left a dead frame - the darkness
  comes from the grade; describe a real place under little light.
- **Lens:** long-telephoto compression (200 mm+ register), foreground occlusion as dark
  out-of-focus shapes **only in the lower 30-45% of frame** (S: a vertical black mass across half
  the width eats the frame). **In an enclosed interior** drop to 85-135 mm and omit the
  physical-distance clause.
- **Grain:** fine-grained 35 mm, most visible in shadow; judge it at the final tier, heavy grain at
  480p-720p in the dark turns blocky (S).
- **Composition:** claustrophobic, the subject boxed by real foreground objects, negative space
  read as dread rather than air.
- **Materials:** wet concrete, mud, oxidized metal, matte non-reflective canvas coat fabric.

## ASSET BRIEF (-> lira-image-prompts)

Not baked into a reference image: grain, telephoto compression, occlusion and the teal/amber grade
are video-prompt-only; a pre-graded sheet locks a wrong photograph into every shot.
**Locations:** architecture and light only, no people, 3/4 view, one light-source logic per
location. **Characters:** neutral sheet, flat even light, plain background, real skin with pores.
**Props:** neutral studio light; grime only where the prop is wet or corroded in the story.

## VIDEO STYLE BLOCK (-> wan3-core)

Fill `[named material]` with the scene's darkest real surface; in an enclosed interior replace the
lens sentence per VOCABULARY.

```text
Photoreal desaturated procedural-thriller look. Palette locked to desaturated teal-cyan shadows,
dirty tobacco-amber highlights, deep blacks with the black point just above zero - the darkest
surface is [named material] with faint texture still in it - and one cold clean white reserved for
the scene's single practical light source. Exposed for that source, not for the faces; no fill from
the camera side; haze visible inside the beam. Fine-grained 35mm film grain, most visible in the
shadows. Long-telephoto compression: the camera sits far from the subject, close framing comes
from lens reach, the background flattens into a soft dissolved wash; dark out-of-focus foreground
shapes occupy only the lower 30 to 45 percent of the frame, as if shooting from behind concealment.
```

## CAMERA DISCIPLINE

**Favours:** a locked-off frame with a slow handheld breathing pulse; slow pans or tracks that
follow one named subject from concealment; rack focus used sparingly, onto the one detail that
matters. Small, motivated, reluctant movement - a camera trying not to be seen.

- **The camera moves only when a character moves**, and matches them: a lateral track holds the
  walking figure at a constant frame position.
- **The late pan:** when a character crosses the frame the camera turns a beat *after* they commit.
- **The slow push-in is reserved for a decision**: it starts when a character stops talking and
  commits; one per scene at most.
- Reframes are small and mechanical, like machinery, not a float.

**Declines:** aerial/drone, whip pans (except as an explicit hard-cut transition), fast orbit,
any confident or celebratory move, a smooth gimbal glide, a perfectly static tripod. The observer is
never in frame. Honoured by not choosing, not by negatives.

**CUT STATE:** hard cuts that land on a completed action (the glass set down, the head turn
finished), or one continuous slow take written with `No cut.` at each move. Never a jump cut,
never a transition effect.

## BLOCKING / MONTAGE

- Characters move through static frames; doorways, corridors and windows are internal frames.
- Perpendicular, eye-level geometry, frontal or profile, seldom diagonal.
- Distance is status: the interrogator owns the closer, larger frame position.
- One body moves at a time; a second mover is an escalation.
- Dialogue cuts on the listener; inserts (hands, documents, locks) carry the procedure and are
  earned by a character's gaze; enter late, leave early; the cut rate is almost metronomic.

## SOUND

Room tone and a low electrical or ventilation hum; distant city or rain at a believable distance;
footsteps and paper at foley precision; no score, or one sustained low note arriving late;
dialogue close, dry, quiet, never performed. Silence is allowed to be the loudest element.
Paste: `Sound: only room tone, a low ventilation hum, distant rain and footsteps; no music; the
dialogue is close, dry and quiet.`

## ENCLOSED INTERIOR VARIANT (interrogation room, cabin, corridor, lift)

For a room with nowhere to stand back to. Replace the lens sentence of the style block and the sound
line; keep everything else.

```text
Short-telephoto look (85 to 135 mm): faces sharp, the back wall a soft dissolved wash; a dark
out-of-focus table edge or doorframe fills the lower 30 percent of the frame.
Sound: only room tone, a low electrical hum from the lamp and a faint ventilation hum; silence between
the lines; no music.
```

- **A reference colour beats the palette.** The grade desaturates around the references: the green
  coat stays recognisably green, only muted. Say so in one sentence rather than letting the palette
  repaint the asset.
- **Dialogue cuts on the listener** needs a visible listener. With an off-screen voice, the largest
  face tends to take the line (`wan3-sound` dialogue rules 6-8): cut to the speaker, or hold a
  two-shot where both mouths are visible.
- **Distance is status** in a symmetric profile two-shot: the interrogator sits at the larger,
  nearer half of the frame; the pressured side sits deeper and smaller. In a pure profile, move the
  camera 15-20 degrees off perpendicular rather than writing a status the geometry cannot show.
- The slow push-in after a line is one treatment with a trigger (`wan3-film` §2).
- Self-check 1 applies with the interior wording: no physical-distance clause, short telephoto, a stated
  foreground edge.

## SELF-CHECK

1. Is the lens telephoto-compressed with the foreground occlusion stated, and, in an enclosed
   interior, is the distance clause gone?
2. Does the camera move only when a character moves, and read as reluctant?
3. In a cut sequence, does each cut land on a completed action, with an insert (not a face)
   carrying the information? Is there no score?
