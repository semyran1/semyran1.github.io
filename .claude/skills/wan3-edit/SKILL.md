---
name: wan3-edit
description: "WAN 3.0 EDIT - using Wan 3.0 on an EXISTING clip: remove or add an object, replace a character or outfit, swap positions, restyle, relight, change a line of dialogue, reshape the action, transfer camera movement or an effect, extend a clip forward or backward, chain clips past 30 s. 22 of the 64 official handbook prompts carry a source video, most are edits. Use for \"убери объект\", \"замени персонажа\", \"поменяй одежду\", \"исправь деталь без перегенерации\", \"продли ролик\", \"+15 секунд\", \"перенеси камеру из референса\", \"стилизуй видео\", \"поменяй реплику\", \"edit the video\", \"Video 1\", \"extend video\", or whenever a nearly-good clip should be repaired instead of re-rolled. Requires wan3-core; run get_cost with the clip attached first (first measurement: an `Edit the video ... Video 1` prompt routes as an edit and bills the output seconds only; small logos can vanish). Not for generating from scratch (wan3-core)."
---

# WAN 3.0 EDIT

The handbook treats Wan 3 as an **editor** as much as a generator: 22 of its 64 prompts carry a
source video (most of them edits), and the edit prompts are the shortest in the corpus (11-82 words). One short
sentence replaces a 17.5-credit re-roll when the clip is mostly right. `wan3-core` §0 governs this
file; marks as in `wan3-core/references/provenance.md`.

**Read first:** whether Higgsfield routes `Edit the video ...` on `wan3_0` with a
`video_references` clip as an edit (rather than as a loose reference) is `[OPEN]`, and so is the
price (`wan3-core/references/calibration.md` C9, C13). Before the first edit: `get_cost` with the
clip attached, then a 480p 3 s test. Alternatives that Higgsfield lists for the same jobs `[HF]`:
`kling_video_edit` (Kling 3.0 Omni Edit), Genjutsu `hf_mult_replace_object` (replace an object in one
source video from reference images) and `hf_mult_motion_control` (move a motion onto reference
subjects). Compare `get_cost` before choosing.

## §1 - The edit formula `[DOC-2]` `[DOC]`

```text
Edit the video. <Operation> <target> in Video 1 [using Image 1]. <How it integrates>. <Keep list> unchanged.
```

Alibaba's editing formula is *editing target + editing action + state that everything else stays
the same* `[DOC-2]`. The handbook's edit prompts all follow it:

> `Remove the man on the left in video 1, and naturally fill that position with the surrounding background, keeping all other characters, actions, and the picture unchanged.` (031)

Seven habits visible in the 22 source-video prompts:

1. **Open with the verb**: `Edit the video`, `Remove`, `Reference the video`, `Extend`, `Reshape`.
2. **The source is `Video 1`** (also `@Video1`, `video 1`); an inserted or replacing asset is
   `Image 1`. Numbers per type, in upload order (`wan3-core` §4).
3. **One operation per prompt** `[CRAFT]` - the corpus does one thing each time (the only
   multi-part edit, 057, is three garment swaps of the same kind).
4. **Name the fill.** For removal: what replaces the object (`naturally filling in with the
   surrounding pool water and stone ground`, 029).
5. **Integration clause** for anything added or changed: light direction, shadow, reflection,
   scale (`The lighting and shadows on the vase should be consistent with the direction of the
   natural light from the window`, 030; `synchronously match the water reflection`, 033).
6. **A keep list**, specific: `the woman's posture, movements, and the pool background unchanged`
   (029); `Retain the original video's baseball cap, knee pads, elbow pads, and other protective
   gear. The skateboarding actions, motion trajectory, and skate park background remain completely
   unchanged` (051). A keep list that names *actions, trajectory and background* protects the
   motion the model would otherwise redraw.
7. **Do not re-describe what stays.** The source supplies it; extra description invites change.

## §2 - Operations library (ids refer to `wan3-core/references/handbook-prompts.md`)

| Operation | Official form | Id |
|---|---|---|
| Remove objects | `Remove all the blue and yellow swimming rings ... naturally filling in with ... Only retain the woman floating in the pool` | 029 |
| Remove a person | `Remove the man on the left in video 1 ... keeping all other characters, actions, and the picture unchanged.` | 031 |
| Remove clothing item | `Remove the hat from the woman's head in Video 1, revealing her natural hairstyle` | 034 |
| Remove eyewear | `Edit the video, remove the woman's sunglasses in video 1, revealing natural eye makeup and gaze` | 052 |
| Insert an object (asset) | `Edit the video. In Video 1, add the vase from Image 1 to the empty space on the right side of the woman's desk. The lighting and shadows ...` | 030 |
| Insert an object (described) | `Add a rock on the beach, so that the rock is half-buried in the wet sand, and let the seawater gently cover the bottom of the rock as the tide recedes.` | 050 |
| Replace a person | `Reference the video, replace the skateboard man in video 1 @Video with the woman and clothes from image @Image1. Note: only replace the character, keep the skateboard action ...` | 040 |
| Replace + describe | `replacing the skateboard man in Video 1 with a short-haired woman wearing a sports bra and loose cargo pants` | 051 |
| Replace + voice | `Seamlessly replace the female character in video @Video1 with the male character from image @Image1 ... Extract the vocal characteristics from audio @Audio1` | 044 |
| Wardrobe / accessories | `The woman in Video 1 wears the hat from Image 1, naturally fitting the head shape. The man ... hat from Image 2 ... shirt is replaced with the blue washed loose denim shirt from Image 3` | 057 |
| Change appearance | `The little girl in Video 1 transforms into a young woman around twenty years old ... The action of looking up at the city neon lights and the expression and demeanor remain consistent.` | 032 |
| Scale an object | `proportionally enlarge the sailboat on the left to give it a greater sense of visual oppression ... Keep the character on the right, the distant fleet, and the sea fog unchanged.` | 033 |
| Swap positions | `swap the positions of the man in the suit and the ostrich ... Ensure the walking actions and pace rhythm of both remain consistent` | 054 |
| Restyle the whole clip | `Edit the video, transforming the video style into a claymation style.` | 055 |
| Relight / grade | `brighten the overall lighting, adopt the soft three-point lighting characteristic of American TV dramas, eliminate the hard shadow on the right side ... keeping the man's actions and the video content unchanged` | 053 |
| Change a spoken line | `Edit the video, changing the male character's line to: "The deal is done. Now... we disappear."` | 056 |
| Reshape the action | `Reshape the plot of @Video1 so that the man directly picks up the guitar and starts playing a piece of music.` | 058 |
| Transfer camera movement | `Reference the camera movements from the video, change the scene to a cup of coffee on a rooftop coffee table.` | 041 |
| Transfer an effect | `The character from Image 1 references the energy effect from Video 1 to generate the same effect and action.` | 042 |
| Extend forward | `Extend video 1 by 15 seconds. Character A is ... Character B ... says ...` | 059 |
| Extend with both ends | `Extend the video forward by two seconds from the middle segment: ... Extend the video backward by three seconds from the middle segment: ...` | 061 |

## §3 - Extending `[DOC]` `[DOC-2]`

- Input video + new output **<= 30 s** `[DOC-2]` (so a 15 s source can grow by up to 15 s).
- Name what the continuation does: **actors, their look, the setting, then the beat**, in the
  handbook's order (059, 060: two named characters with clothing, the room, the sound bed, then a
  paragraph of action ending on a closing image). The continuity words come from the source; do
  not retell the first half.
- Forward and backward in one prompt are allowed (`061`); give each side its own sentence.
- Past 30 s, or if extend is not routed on Higgsfield: start-image chaining
  (`wan3-core/references/long-form.md` §10).

## §4 - Repair or re-roll? `[CRAFT]`

Compare, in credits, **before** deciding: one more attempt = the price of the clip / p(accept); a
repair = the price of the edit with the clip attached (get it with `get_cost`) / p(edit works).
Repair wins when: one object, one line of dialogue, one lighting problem, one outfit item is
wrong and the rest is good. Re-roll wins when: identity, motion or structure is wrong throughout,
or the clip is short (an edit of a 7 s source cost 7 cr at 480p = the price of a new 7 s clip, so no saving on short clips - one measurement `[HF]`). Trim the source to the problem span plus
a second either side if only a part needs work, and splice back in an editor `[CRAFT]` - but the
edit may then lose continuity at the seams, so prefer whole-clip edits for short clips.

**Small marks do not survive on trust** `[EMPIRICAL]` (field test D, one run): an embroidered fox
on a black longsleeve disappeared in an add-sunglasses edit although the keep list named it
(`the black longsleeve with the orange fox ... unchanged`). Before paying, ask whether a logo,
badge, print or small text on the subject must survive. If yes: after the first edit look at that
mark first; if it is gone, do not re-roll the same edit - rebuild the shot in REF mode with the mark
as its own `Image N` (the same fox held in the REF test A), or accept the loss and add the mark in post.

Check after an edit: the keep list really stayed (faces, hands, background text, logos, motion path);
audio may be re-generated rather than preserved `[OPEN]` - listen to it.

## §5 - Pre-send items added by this skill

0. Run the lint with `--mode EDIT` (or `EXT` for an extension), or its camera, sound and exclusion
   warnings do not apply to your prompt.
1. The prompt opens with the operation, names `Video 1` (and `Image N` for an inserted or
   replacing asset), carries one operation, and ends with a specific keep list.
2. A `get_cost` reading with the real clip attached exists, and the repair-vs-reroll comparison is
   written in credits.
