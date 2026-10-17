# Angles and room geometry - the view contract

Marks as in `wan3-core/references/provenance.md`. Written 2026-10-17 from one applied test: the same
dialogue scene (Arthur's office, 8 shots) shot once on Seedance 2.5 and rebuilt on Wan 3.0 in two clips
(`wan3-core/references/field-tests/2026-10-17-blindspot-office-frames.md`). Everything marked
`[EMPIRICAL]` here is one scene, two clips: provisional until a second scene confirms it. Read this
whole file before any prompt with more than one camera angle on the same space.

## 1. What was seen `[EMPIRICAL]`

Seedance, with the office plate, the first frame and the element images attached, kept the room across
8 shots: the window wall stayed behind Angelika and the shelving unit behind Arthur in every angle,
and the light bands fell on the same walls. Wan, with the same plate and a one-line description of the
room, kept the declared number of cuts (3 of 3 in each clip) but not the room:

| Wan shot | What the prompt said | What the model built |
|---|---|---|
| A, shot 2, Angelika medium | "from the side, Arthur out of frame" | a glass partition with horizontal blinds behind her, no tall window blinds; Arthur's shoulder in frame |
| B, shot 1, Angelika close | front three-quarter, no background named | a flat dark teal wall, no window, no desk |
| B, shot 2, Arthur close | - | window with blinds on the left of him |
| B, shot 3, Arthur from the side | "left edge open" | the window now **behind and to the right** of him: the same window cannot be on both sides |
| A, shots 3-4 | folder "open on the desk" | the folder in Arthur's hands in both shots |
| B, shot 3 | "reaches out of frame to the left, toward the wall" | picks the sheet off the desk pile inside the frame |

The rule behind the table: **Wan keeps what a reference shows in the frame and invents a plausible
room for every angle that has no reference.** The invention is locally believable and globally
inconsistent, which is what a viewer reads as "the room changed".

## 2. The view contract `[CRAFT]` from the Seedance blocking rules, `[EMPIRICAL]` for the failure

For every shot of a multi-angle scene, one sentence states what the frame contains, from the
camera's position:

```text
View: behind Angelika, the window wall with three tall vertical blinds fills the right third of frame; the concrete wall with the light bands is at her left.
View: behind Arthur, the low shelving unit with the white model; the desk phone at the frame's left edge.
```

A close-up gets one too (`behind her, out of focus, the bright blinds of the window wall`): a close-up
with no background named gets a blank wall.

## 3. Anchors, not descriptions

Pick two fixed anchors for the room (the window wall, the shelving wall) and stage the scene so each
character is always in front of **their own** anchor: Angelika against the window wall, Arthur against
the shelving. Every angle then shows one anchor behind the speaker and the audience never has to trust
the model with a wall it has not seen. This is the 180-degree rule used as a geometry rule; the
Seedance footage kept to it without being told.

## 4. Give every new angle its own plate

An angle with no reference is an angle the model will invent. Cheapest cure: build one still per angle
first (an image model from the office plate and the character references; one to two credits each),
attach it as an `Image N` with a role line that limits it to its shots (`Image 8 is the background of
shots 2 and 5 only: the window wall seen from the desk; camera angle and people unused`). Several
plates fit the 10-image cap; a two-character scene with a room, a prop and four plates is eight.

When the geometry matters more than a native voice: one shot per clip, each started from its keyframe
still as `start_image` (I2V). That cannot carry references, audio references included `[HF]`, so the
voice comes in afterwards.

## 5. How many angles per generation `[CRAFT]`

Wan counted its cuts correctly and lost the room with each new angle. Plan two to three new angles per
generation; the fourth and later come from a separate clip with its own plate, cut together in an
editor. Hard-cut coverage needs no chaining (`wan3-core` long-form §10).

## 6. Actions across the frame edge

Anything that happens outside the frame is resolved by the model inside it (the sheet taken off the
desk, a pen and a folder in hands that were meant to stay on the table). Write the action where the
camera sees it; put an object's place in each shot's view contract (`the project folder lies open on
the desk and stays there`); attach only the assets a clip uses.

## 7. Checks

1. Each shot quotes its **View** sentence; each close-up names its background.
2. Each character has one anchor wall, named; no wall appears on both sides of the same character.
3. Each angle has a plate, or the shot is the clip's first or second angle.
4. No action starts or ends outside the frame; no unused asset is attached.
5. After the render: for each shot, is the window where the contract says? Count it in a frame, not
   from memory.
