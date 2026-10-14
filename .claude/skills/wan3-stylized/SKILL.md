---
name: wan3-stylized
description: "WAN 3.0 STYLIZED - non-photographic looks for Wan 3.0: 2D anime and cel, oil-painting and ink-wash motion, claymation and miniature, plush and felt, paper craft, motion-graphics illustration, 3D CG animated short and Pixar-like feature look, game CG, live-action plus drawn hybrids, restyling a clip. Covers the film's style bible (a text block pasted into every prompt), character-design locks, physics register (soft-body, brushstroke, cartoon vs real weight), the 'not X' clause and style reference images. Use for \"мультфильм\", \"аниме\", \"3D-мульт\", \"Pixar\", \"пластилин\", \"глина\", \"плюшевый\", \"тушь\", \"масло\", \"MG-графика\", \"стилизуй\", \"рисованный\", \"style bible\", or any look that is not photographic. Load after wan3-core; photographic looks and director packs are in wan3-film. Not for stills (lira-image-prompts) or Seedance animation (seedance-25-3d-animation)."
---

# WAN 3.0 STYLIZED

Stylized and non-real worlds are Wan's home ground: 10 of the 64 official handbook prompts are
filed under "Stylized & Non-Real" (second only to multi-shot), and the strongest official demos
of physics-heavy fantasy sit there `[DOC]` `[FIELD]`. Anime action is also **more forgiving than
realistic action**, where contact, limb stability and weight break first `[FIELD]`. That makes it
the efficient place to spend credits. `wan3-core` §0 governs this file; marks as in
`wan3-core/references/provenance.md`. Ids are official handbook prompts.

## Reading map

| Situation | Open |
|---|---|
| Choosing a look; the words the handbook uses for each | `references/style-vocabulary.md` |
| A film that needs one look across many clips | §2 below, then `references/style-vocabulary.md` §3 (template) |
| Restyling an existing clip | `wan3-edit` (one line: `Edit the video, transforming the video style into a claymation style.`, 055) |

## §1 - Lead with the medium `[DOC]`

The handbook opens stylized prompts with the **medium**, then the rest: `Japanese sports anime
style 2D animation, 30 seconds.` (010) · `Hand-drawn animation style, oil painting brushstrokes, cold
color palette.` (012) · `A 3D animated fantasy short film with 4 shots` (008) · `3D animated short,
30 seconds, dark fantasy theme, single shot` (011) · `This is a refined Japanese 2D cartoon
animation short film` (009) · `Generate a 20-second, 16:9 ultra-widescreen plush universe adventure
clip` (025). Style and texture are 47% of what the official prompts say. A label alone is not a
look, though: add the traits that make it visible (proportions, surfaces, shading, palette).

**Name what the look is not, once** `[DOC]`: `The overall look is not realistic live-action film,
not childish cartoon, nor dirty, heavy industrial cyberpunk` (038); `All animations are rough 2D
frame-by-frame hand-drawn, not smooth vector animation, not 3D cartoon, not plastic stickers`
(028). One sentence of "not" at the top of the style block, because the model has a strong default
toward glossy 3D.

**No studio or director names in the model-facing text.** Describe traits (rounded proportions,
physically based materials, soft global illumination, volumetric light, cinematic depth of
field). A trait list cannot drag a studio's characters in with it, and Alibaba advises against
naming real people `[DOC-2]` `[CRAFT]`.

## §2 - The style bible `[CRAFT]` from the Seedance 3D-animation skill, applied to Wan

A film is dozens of separate generations and the model remembers none of them, so the look is
**a text block pasted verbatim into every prompt**, plus character sheets made in that look.
Template (details and a worked example in `references/style-vocabulary.md` §3):

```text
Look family / Proportions / Surfaces / Render and shading / Light / Palette (3-5 colours + 1 accent)
/ Depth and lens / Film texture (usually none) / Physics register / Style fence (one sentence)
```

Rules the handbook supports:

1. **Character design is a locked list, restated per shot.** 027 states the styling as bullets
   and ends `No changes to hairstyle, clothing color, or the number of yellow decorations`; 018
   lists features and costume for each character from a card.
2. **Props get shape and count locks**: `Maintains the same proportion and shape in all shots; Does
   not turn into a regular small dice` (027); `There is always only one orb, its size is stable - it
   does not duplicate, disappear, or deform` (038).
3. **A style reference image carries the whole-film look**: `Reference the aesthetic style of
   @Image1` (022); list what to take (tone, texture) and what not (its characters). Make character
   sheets **in the final look**: in a cartoon the render style is part of the character's identity
   (unlike live action).
4. **Decide the physics register once**: real-weight, or cartoon-exaggerated, or a special rule
   (soft-body for plush: `realistic soft-body physics`, 025; brushstroke motion for ink: `the
   movements must have a brushstroke feel, the speed must be fast, and the details must be
   sufficient (ink drops, sparks, ink trace cracks)`, 062; clay: `stream water flowing slowly under
   the bridge like transparent resin`, 022). Leaving it unstated makes the model drift from shot to
   shot.
5. **Film texture: usually none** in feature-style 3D - grain, halation and gate weave pull toward
   photoreal. If the film wants them (35 mm on an animation), state them deliberately and once
   (`wan3-film` light-and-look §6).
6. **Hybrids declare their layers**: a real plate and a drawn layer have separate rules (028: the
   real hand has pores and fine hair, the MG lines animate *around* it and never outline it like a
   sticker); a world change keeps camera and character continuous (035).
7. **Legibility of action**: whatever the style, it must be clear who attacks, who dodges, who
   counters; write fights as numbered beats (062: first strike / second strike / third strike).

## §3 - Cost note `[CRAFT]` with `wan3-budget`

Flat and graphic styles (2D anime, MG, cel, ink) keep their structure at **480p** where photoreal
faces do not, so drafts of stylized clips validate more at 1 credit per second than a photoreal
draft would; texture styles (clay, felt, oil, plush) lose their material read at 480p and need
the 720p tier to judge. Hands, small text and typography still need the final tier.

## §4 - Text on screen

The handbook asks for titles, subtitles, UI and data labels (027: `color of summer` in a retro serif;
045: a Chinese diary typeface `(#E8D5A3)`; 047: spreadsheet numbers). Text rendering is a reported
weak spot `[FIELD]`; ask for **short** strings in one typeface with a stated position and colour,
confirm them in the first draft, and plan to add critical text in post. A prompt that must not
show text says so once (`no text`, 037).

## §5 - Checks added by this skill

1. Pre-send: the prompt opens with the medium; the style fence (what it is not) is present once;
   the style block is byte-identical to the film's bible.
2. Full audit: character lists restated per shot; prop count/shape locks; physics register stated;
   film texture decided; no studio or real-person names; the style reference's role line says what
   not to take from it.
