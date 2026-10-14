---
name: wan3-film
description: "WAN 3.0 FILM - cinematography layer for Wan 3.0 prompts, loaded after wan3-core: the camera named in every shot (Wan cuts or wanders otherwise), push/pan/track/orbit/handheld/fixed and what they mean, the continuous-take clause, lens and depth of field as visible results, light source and exposure, what stays visible in dark scenes, film stock and grain, hardware lines used by the official handbook, no 21:9 on Higgsfield, dramatic functions, and director packs (Fincher, Villeneuve, Wong Kar-wai, Wes Anderson). Use for \"кинематографично\", \"какую камеру\", \"оптика\", \"свет\", \"зерно\", \"плёнка\", \"как в кино\", \"стиль Финчера / Вильнёва / Вонг Кар-Вая / Уэса Андерсона\", \"одним кадром\", \"наезд\", \"low key\", or any Wan 3 prompt where the look matters. One style pack per prompt. Not for acting (acting-system), sound (wan3-sound) or stills (lira-image-prompts)."
---

# WAN 3.0 FILM - cinematography layer

`wan3-core` §0 governs this file. Marks (`[DOC]` `[DOC-2]` `[HF]` `[FIELD]` `[CRAFT]` `[OPEN]`
`[EMPIRICAL]`) are defined in `wan3-core/references/provenance.md`. Most of the craft here is
carried over from the Seedance 2.5 film skill and the film literature (`[CRAFT]`); what is
specific to Wan - naming the camera every shot, the hardware spec lines, the missing 21:9 - is
marked with its source.

## §0 - Scope and reading map

This skill answers **"how is it shot."** `wan3-core` owns limits, formulas, references, timeline
and checks; `wan3-sound` owns the sound half of a beat; `acting-system` the performance;
`wan3-stylized` non-photographic looks. FILM fills Alibaba's **aesthetic control** slot: *light
source, lighting environment, shot size, camera angle, lens, camera movement* `[DOC]`.

| Situation | Open |
|---|---|
| Camera vocabulary, movement chains, handheld, locked-off, orbit/whip/FPV, camera "reaction time" | `references/camera.md` |
| Light registers, exposure, dark scenes, atmosphere, stock, grain, hardware lines, aspect ratio | `references/light-and-look.md` |
| Story function of a shot (establish ... resolve) | `references/dramatic-functions.md` |
| The user asks for a named director look | exactly one file from `references/stylepacks/` (contract and index: `_contract.md`) |

References are short; read the one the situation needs whole (core R1).

## §1 - The translation law `[CRAFT]`

**Write what the instrument does to the image, not the instrument** (the Seedance optimizer's rule; the Alibaba handbook shows the same pairing at its best, 028). Alibaba's guide ties each
move to an effect - push-in for intimacy or tension, tracking beside the subject, orbit for
emphasis, a fixed camera for stillness `[DOC]` - and the handbook pairs hardware with its visible
consequence at its best: `approximately 14-16mm ultra-wide-angle lens, with slight fisheye
distortion and barrel distortion, causing furniture and door frames at the edges of the frame to
curve slightly` (028). The official spec lines also appear bare (`shot with Arri Alexa 65 and
Panavision anamorphic lenses, Kodak Vision3 500T film texture`, 037): usable as a *register*
signal, but the bare name is the weakest form. Pair every hardware word with what it does.

Directions are in-frame displacements `[CRAFT]` (Seedance's Scene 3 lesson, model-independent):
"orbits to the right" can resolve to anything; "the camera arcs so the man's profile turns to
face the lens, the lamp slides from the left edge toward centre" cannot.

## §2 - Name the camera in every shot `[DOC-2]` `[FIELD]`

The one Wan-specific camera rule. Alibaba's guide asks for the camera treatment in each shot;
secondary sources report that an unnamed camera is where Wan cuts inside a "continuous" clip or
moves on its own, and that a still camera must be requested (`fixed shot`) `[FIELD]`. So:

- **Every shot carries exactly one main camera treatment**, named, with its subject and both ends
  (`the camera slowly pushes in from a medium shot to the girl's eyes`).
- **A still camera is a treatment**: `fixed shot, the door frame, the table edge and the window
  stay at the same place in frame` - write what does not move, not "the last frame matches the
  first" (the model reads that as "return everything, the subject too, to the start" `[CRAFT]`).
- **One treatment may have a trigger.** `Fixed, then a slow push-in that begins when she finishes
  speaking` is one treatment (a start state, an end state, a trigger); a push-in *and* a pan in one
  shot is two.
- **One treatment may have a trigger.** `Fixed, then a slow push-in that begins when she finishes
  speaking` is one treatment (a start state, an end state, a trigger); a push-in *and* a pan in one
  shot is two.
- **No stacks.** `drone shot, handheld close-up, locked-off dolly, fast orbit` asks for incompatible
  grammars; keep one per shot, spend the others in later shots or across cuts.
- **A continuous take** repeats its no-cut clause at every camera move (`wan3-core` long-form §3)
  and chains moves in written order, each with its subject and end state: the official 003 pans
  between two faces many times and writes `Do not cut.` after each.

## §3 - Light and look in four lines `[CRAFT]`

1. **Source + environment**, in Alibaba's two words: where the light comes from, what it does in
   the space (`Soft LED softbox light spills in from the right`, 003; `cold white moonlight as the
   dominant hard light, high-contrast low-key lighting, side-lighting`, 011).
2. **Exposure priority**: say what the shot is exposed for.
3. **In a dark shot, name what stays visible** and where the darkening stops - exactly one small,
   bounded object. The black comes from the grade, not from "pure black".
4. **Texture last**: grain, halation, lens trace, as visible traces, localized and motivated.

Details, the visibility ladder and the stock table: `references/light-and-look.md`.

## §4 - Aspect ratio on Higgsfield `[HF]`

Wan on Higgsfield offers `16:9, 9:16, 1:1, 4:3, 3:4` and `auto`. **There is no 21:9 or 2.39:1.**
The handbook writes `ultra-widescreen` into prompts (025), but that is a prompt word, not a
parameter, and its effect is unmeasured. For a scope look: generate 16:9 and crop in the edit, or
keep the composition inside the central 2.39 band (leave top and bottom bands free of important
detail) `[CRAFT]`. Do not write "21:9" as if it were a setting.

## §5 - Dramatic functions

Each shot has one job - establish, reveal, escalate, break, climax, resolve - and the job picks
the technique. Wan-specific notes on how each is built (with sound, because audio is native)
are in `references/dramatic-functions.md`. The Russian-language director workflow (brief ->
function -> plan -> English prompt) lives in `cinema-director-ru`; use it for the planning, and
this file and `wan3-core` for limits and syntax.

## §6 - Style packs

A style is a compressed vocabulary, not a name - a bare director name gets surface mimicry
`[FIELD]` and, on Wan, risks the real-name issue (`wan3-core` constraints §7). Packs live in
`references/stylepacks/`; `_contract.md` holds the section contract and the index.
**Load exactly one pack per prompt** (a multi-shot prompt keeps one pack throughout). Two packs give two contradictory vocabularies and the model
averages them into neither look. A pack never overrides the story contract: it shapes light, lens,
cutting and sound, it does not add or remove subjects.

Current packs: Fincher, Villeneuve, Wong Kar-wai, Wes Anderson. **All four are `[CRAFT]` - none has
been run on Wan 3 yet**; calibrate each with one 480p 5 s test before relying on it (5 credits).
Official evidence that the registers work: Wong Kar-wai named in 063, a symmetrical hotel corridor
in 017, a hard-light black-and-white fashion film in 024, an Alexa 65 + anamorphic jump-cut film in 037.

## §7 - Register interview `[CRAFT]`

Before a prompt that uses this skill, ask (multiple choice), do not assume:

1. **Photographic or non-photographic?** (non-photographic -> `wan3-stylized`)
2. **Film register or clean digital?** (`references/light-and-look.md`, stock table)
3. **A style pack, or none?** If none, work from §1-§3 rather than defaulting to a name.

Do not re-ask what the user already answered.

## §8 - Anti-"clip" guardrails

This skill makes film, not short-form social video. It declines, unless asked: unmotivated speed
ramps and snap-zooms; flat frontal beauty light with no stated source; a centred talking head
with no reason for the shot size; vertical 9:16 (a platform parameter - the cinematic default is
landscape); quality packs ("masterpiece, 8K, ultra-detailed") - they are fluff the lint counts.
The handbook does write `8K` and `4k high quality` (026, 044, 063); they are harmless and
uninformative, never a substitute for a light source and a lens.

## §9 - Film checks

**Pre-send (two items added to core's list):**

1. Every shot: quote its one camera treatment; a continuous take: quote the no-cut clause at each
   move.
2. A dark shot: quote the one line naming the **one** small object that stays visible.

**Full audit:**

3. The register interview was asked or answered.
4. Every optical, lighting or stock choice reads as a visible consequence, not a bare value.
5. A fixed camera is written as things that stay put; every direction of travel names a frame
   edge and what fills the vacated space.
6. **Trigger before reaction** `[CRAFT]`, a rule from the Seedance guide that is model-independent:
   the cause is visible before the face reacts; do not push into a face-only close-up before the
   audience has seen the trigger.
7. A detail that is the point of a shot exists at a shot size where it fits (a card-sized detail
   vanishes at 15 m).
8. Light level: the exposure priority is stated; no dead black field; with one source, the
   characters are anchored in its pool; a bare lamp or screen in frame does not outshine the lit
   object.
9. Weather is an interaction (rain across a lamp cone), not a noun.
10. Grain weight is checked against motion speed and delivered resolution (heavy grain at 480p-720p
    in the dark turns to blocks).
11. One style pack at most; its VOCABULARY terms appear unchanged where the pack uses them, the
    asset brief carries none of the video-only traits (grain, grade, lens artefacts), and its
    SELF-CHECK ran.
12. No item from §8 appears unless requested.
