# Style pack contract - how a pack is written, and the index

A style pack compresses a director's or cinematographer's identity into reusable, observable
parameters, not a bare name. Independent research is direct: name-drops "compress dozens of
parameters into one phrase, but should be used sparingly and with concrete terms, or the model
defaults to surface mimicry" `[FIELD]`. Every pack here exists to prevent that failure. Read this
file before writing or editing a pack; read only the one pack the shot needs.

Adapted from the Seedance 2.5 style-pack contract, with two Wan-specific changes: **a SOUND
section** (Wan generates audio in the same pass, so a look without its sound is half a look) and a
**CUT STATE** line in the camera section (Wan decides for itself whether to cut).

## Index - one line per pack, routing only

| Style | File | When to reach for it |
|---|---|---|
| Fincher / *Se7en* - *Mindhunter* | `fincher.md` | dark procedural suspense, one motivated source, a camera that watches from concealment, desaturated teal-and-amber |
| Villeneuve / *Arrival* - *Dune* - *Blade Runner 2049* | `villeneuve.md` | scale and silence: monumental space, a small figure, haze and diffused light, slow inevitable camera, low-frequency sound |
| Wong Kar-wai / *In the Mood for Love* - *Chungking Express* | `wong-kar-wai.md` | longing in saturated colour: step-printed slow motion, reflections, narrow frames, handheld closeness, music as narrator |
| Wes Anderson / *The Grand Budapest Hotel* | `wes-anderson.md` | symmetrical tableau, pastel palette, lateral tracking, whip pans, dollhouse staging, deadpan |

New styles get a pack file and one row here, never their full parameters in this index.

## Fixed sections, in this order `[CRAFT]`

```
IDENTITY
  One line: the name and a one-sentence thesis of what makes the style recognizable - the thing
  that has to survive translation into prose.

VOCABULARY
  The shared word-list the other sections quote verbatim: palette, light register, lens register,
  grain register, composition habits, materials. The single source - it keeps the asset brief and the
  video block from drifting apart.

ASSET BRIEF (-> lira-image-prompts)
  What a location / character / prop sheet built for this style should and should not contain.
  States what NOT to bake into the asset: grain, lens artefacts, compression, occlusion and grade
  belong in the video prompt; baking them into a sheet locks a wrong "photograph" into every shot.

VIDEO STYLE BLOCK (-> wan3-core)
  A ready block for the style / aesthetic-control part of a Wan prompt, built from VOCABULARY and
  the translation law. The part pasted verbatim; it must agree word for word with VOCABULARY.

CAMERA DISCIPLINE
  Movements the style favours and declines; the CUT STATE it uses (no cut / motivated cut / jump
  cut). A style is as much restraint as technique: the exclusion is honoured by NOT choosing, not
  by negatives.

BLOCKING / MONTAGE (optional)
  Where bodies and camera sit in space; what motivates a cut and what carries information between
  cuts. Quotes VOCABULARY.

SOUND
  The sound bed, the music register, the voice register (if the style has dialogue), and silence.
  Written as the sentence(s) to paste into wan3-sound's slots.

SELF-CHECK
  Two or three yes/no questions unique to the style, answerable against a finished prompt.
```

## Rules

- **One style per file**, roughly 900 tokens. Past that the pack starts repeating FILM's own
  references.
- **One pack per prompt.** Blending happens only by explicit request and by hand-editing one
  pack's output.
- **Style never overrides the story contract**: it shapes light, lens, cutting and sound; it
  does not add, remove or re-identify subjects, or change an end state.
- **No real names in the model-facing block.** A pack's VIDEO STYLE BLOCK describes the look; the
  director's name stays in the title and the index (Alibaba's guidance is to avoid naming real
  people, and the name adds mimicry, not information). Titles of films may appear in the ASSET BRIEF
  for the human reader only.
- A pack carries no platform artefacts (reference caps, tag syntax, prices): those belong to core
  and budget, and a pack that carries them goes stale.
- **Provenance**: every pack is `[CRAFT]` until a 480p test on Wan 3 is logged
  (`wan3-core/references/calibration.md`); the SELF-CHECK is the acceptance test of that run.
