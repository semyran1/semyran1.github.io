# Modes and references

Marks as in `provenance.md`. Ids (`013`, `038`) are official handbook prompts, quoted from the
archive in `official-corpus.md`. Read this whole file before any prompt that uploads media.

Contents: 1 Choosing the mode - 2 The reference protocol - 3 Forms the handbook uses - 4 Image
references - 5 Video references - 6 Audio references - 7 First/last frame and start-image chaining - 8 Upload
hygiene - 9 Count and ownership

## 1. Choosing the mode

Ask in this order; stop at the first yes.

1. Is there an existing clip to repair, restyle or extend? -> **EDIT / EXT** (`wan3-edit`).
2. Must a *specific* face, product or room appear exactly? -> **I2V** if one picture is enough
   (one subject, opening composition known); **REF** if several identities, a voice, or a motion
   or camera plate are involved.
3. Must the start and the finish both be controlled (transformation, match cut, handing over to
   the next clip)? -> **FLF**.
4. Otherwise **T2V**, and keep identity as a locked text description pasted into every shot.

Two checks: a 30 s one-take that needs identity -> REF, because FLF gives no per-shot identity
anchor beyond its two frames; a chain of clips that must join -> I2V with a still from the previous clip as the next
`start_image` (FLF only if you also fix the end frame) (section 7).

## 2. The reference protocol `[DOC-2]` `[DOC]`

The principle in Alibaba's guide and in the handbook is the same one the Seedance set enforces:
the goal is not to attach everything, but to **define the relationship** - which asset applies to
which subject, and what to take from it.

**Step 1 - number per type, in upload order.** `Image 1..n`, `Video 1..n`, `Audio 1..n`; the
three types count independently `[FIELD]`. Freeze the numbers after upload: change the order and
every role line is wrong without anything failing.

**Step 2 - one line per asset, with a job and a limit.**

```text
Image 1 is the sole appearance reference for the man: face, hairstyle, build, clothing.
Image 2 is the sole appearance reference for the woman: face, hairstyle, build, clothing.
Image 3 defines the location only: city space, neon atmosphere, road structure.
```

Never "reference these images". An unaddressed asset is a guess the model makes for you
(Atlas: "bind each reference to a role and say what may be taken from it").

**Step 3 - group**: characters (with `Do not interchange their faces, clothing, actions or lines`
`[CRAFT]`), props with owner, location, motion/camera plate, voices. **Step 4 - state counts once**
in the global lock ("exactly two people appear") rather than inside each shot `[CRAFT]`, since a
count the model failed to build constrains nothing.

**Step 5 - lock sentence.** The handbook's most frequent addition after the mapping is a
consistency lock (44% of prompts): `Strictly maintain the stability and uniformity of both
characters' faces, hairstyles, body types, clothing structure, color schemes, and recognizability`
(038).

**Step 6 - identity anchors `[CRAFT]` ported from Seedance's costliest case.** Say who someone is by
what the model cannot reassign: the **face** (bound to its reference), the **position in frame**,
the **build**. Clothing alone is not an identifier - if the model dresses a face differently
than you assumed, an attribute-only line matches nobody and the model invents a match.

## 3. Forms the handbook uses

| Form | Id | Use |
|---|---|---|
| `Only a lip gloss product image @Image1, generate a model swatch video, 15 seconds, vertical screen, highlighting the lip color effect.` | 020 | minimal product -> model; the model supplies the rest |
| `Define the woman in Image1 as Subject1, define the woman in Image2 as Subject2. Subject1's dialogue tone of voice references Audio1...` | 015 | named subjects reused through the prompt, voice bound by number |
| `Based on the uploaded character card, strictly maintain the male character's features: ...; strictly maintain his costume details: ...` | 018 | character card; features listed *and* locked |
| `The scene is strictly based on the uploaded lakeside reed beach image (...), do not replace or mix in other scene elements.` | 018 | location lock with an exclusion |
| `Inside @Image2's modern apartment foyer, @Image1's child stands...` / `@Image3's magical alley world` | 035 | possessive tag attaches an asset to a noun |
| `a fluffy Ragdoll cat @Image1 ... a smaller black cat @Image2` | 017 | tag after the noun, two look-alike subjects kept apart |
| `Referencing the storyboard from @Image1, Shot 1 [0s-30s]: ...` | 013 | one image holds the storyboard |
| `Shoot according to 5 image storyboards: Image 1 (0-1.48s) ... @Image1` | 019 | **one image per time range**, fractional seconds |
| `Reference the 5 uploaded keyframe images ... The 5 characters appear in the order of upload` | 014 | upload order *is* the sequence |
| `Reference the aesthetic style of @Image1.` | 022 | style plate (clay world) |
| `Image @Image1 serves as a reference for the city space ...; Image @Image2 serves as the sole appearance reference for the male character` | 038 | three plates, three jobs |
| `The girl from @Image1 puts on the off-white lace shirt from @Image2` | 023 | garment transfer |
| `【Reference Material】Three character illustrations (Red Fox Dual Pistol Gunner: Feishou @Image1, ...)` | 036 | roster with names; the names then carry the dialogue |
| `the @Image1 ... packaging is centrally displayed` ... `flips it to show the @Image2 back` | 039 | front and back of one package as two assets, text kept legible |

Observation `[DOC]`: the handbook writes `@Image1`, `Image1` and `Image 1` for the same thing
(18 prompts use `@Image`, 6 use a bare `Image N`). Calibration C1 decides which one Higgsfield binds; until then use
`Image 1` (Alibaba's guide wording) and let the lint warn on mixed styles.

## 4. Image references

- **Character**: the face reference first; add a full-body or costume plate as a second image of
  the *same* subject only if wardrobe is part of the job. Multiple views of one subject: declare
  "Images 1 and 2 are the same man; the output contains one man" `[CRAFT]`.
- **Location**: architecture and light only, no people in the plate; say "do not use the people in
  it" when it has any.
- **Product**: front and back as separate assets (039); the handbook asks for `sharp, legible
  text` and logos `remain highly consistent without distortion`. Small text is a reported weak
  spot `[FIELD]`: confirm in the first draft or fix it in post.
- **Style plate**: one image, one job: `Reference the aesthetic style of @Image1` (022); tone and
  light only: "borrow the colour tone and lighting, not the characters" `[DOC-2]`.
- **Resolution** `[CRAFT]`: Seedance showed AI-made references above the output resolution print
  fingerprint patterns into foliage. Downscale references to the output class (<= 1920 px long
  side for 1080p). Unverified on Wan; costs nothing.
- **Reference sheets** from `lira-image-prompts` work as plates; keep grain, lens artefacts and
  grade **out of** them (they belong in the video prompt), exactly as in the Seedance style packs.

## 5. Video references `[DOC]`

Four jobs, each stated alone:

| Job | Handbook line | Id |
|---|---|---|
| Camera movement only | `Reference the camera movements from the video, change the scene to a cup of coffee on a rooftop coffee table.` | 041 |
| Effect + action transfer | `The character from Image 1 references the energy effect from Video 1 to generate the same effect and action.` | 042 |
| Motion kept, subject swapped | `replace the skateboard man in video 1 @Video with the woman and clothes from image @Image1. Note: only replace the character, keep the skateboard action, motion trajectory, and skatepark background ... completely unchanged.` | 040 |
| A plate to edit | everything in `wan3-edit` | 029-034, 050-057 |

State which attributes to inherit and do not re-describe the action; subject, scene and style are
defined separately. A reference video of 1-15 s each, 15 s in total `[FIELD]`; **trim to the
shortest clip that carries the motion** - on some hosts every reference second is billed
(`wan3-budget`).

## 6. Audio references `[DOC]`

`Subject1's dialogue tone of voice references Audio1` (015) and `Extract the vocal characteristics
from audio @Audio1 and have the character speak the following lines: "..."` (044) bind a timbre to
a character; for a dance, `Choreograph the dance according to the fixed audio's rhythm, speed, and
emotional fluctuations: heavy drum beats correspond to sharp, large-scale movements...` (043).
Details, the silence and padding notes, and the ledger for 2+ speakers: `wan3-sound`.

## 7. First/last frame and start-image chaining

FLF: write timed beats for the road between the frames; keep subject, lens, ratio and light the
same in both frames. **Chaining clips** `[FIELD]` `[CRAFT]`: take a still from near the end of clip N
(not the last frame - the last frame often carries motion blur or a half-closed eye), use it as
`start_image` of clip N+1, restate identity, location, camera, motion and sound in the continuation
prompt ("lock identity, location, camera, motion and sound in every continuation" - Atlas), and
expect more than one run per join. Because reference mode and frame mode do not combine `[HF]` (the validator rejects `start_image` +
`image_references`), the identity of a long chain rides on the quality of the chosen frames: choose them from the cleanest moment, front-lit, eyes
open.

## 8. Upload hygiene (Higgsfield)

Generation takes `media_id`s, never URLs: `media_import_url` for a web file, `media_upload` +
`media_confirm` for a local one. Upload in the order the prompt numbers them, one asset per role.
Re-check that the media list shown by the tool equals the numbering in the prompt before paying.

## 9. Count and ownership

Per asset write down: type, number, subject it defines, what is taken, what is excluded. Per
character and key prop: count and owner in the global lock. A reference that is not used in the
prompt does not stay attached "just in case" - it can be billed (video) and it can pull the
picture. If a fix needs removing a reference, say so; do not delete assets silently.
