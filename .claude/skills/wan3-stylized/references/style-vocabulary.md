# Style vocabulary - the words the official handbook uses, by look

Marks as in `wan3-core/references/provenance.md`. Every entry quotes the handbook (`[DOC]`, id in
brackets, `wan3-core/references/handbook-prompts.md`); additions of ours are marked `[CRAFT]`.
Read this whole file when choosing or building a look.

Contents: 1 Look catalogue - 2 Physics and motion registers - 3 Style bible template and worked
example - 4 Hybrids and transitions - 5 Drift

## 1. Look catalogue

| Look | Words that appear in official prompts | Id |
|---|---|---|
| Japanese 2D anime / sports anime | `Japanese sports anime style 2D animation`; `refined Japanese 2D cartoon animation short film ... sky color gradients and cloud layer light and shadow ... dramatic backlighting` | 010, 009 |
| Cel animation | `Cel animation texture, bold black outline lines and hard-edged visuals, warm yellow lighting ... contrasted with the cold blue of the rainy night` | 021 |
| Oil-painting hand-drawn | `Hand-drawn animation style, oil painting brushstrokes, cold color palette` | 012 |
| 3D animated short | `3D animated short, 30 seconds, dark fantasy theme`; `A 3D animated fantasy short film with 4 shots`; a locked character description (hair, eyes, horns, wardrobe) | 011, 008 |
| CG animated film quality | `CG animated film quality, character's face is delicate, smooth, without pores or skin texture, facial features have simple and elegant lines, colors are rich and saturated ... shallow depth of field, motion blur` | 026 |
| Hyper-real CGI (adult sci-fi) | `The visuals employ: Hyper-realistic CGI; Biomechanical structures; ... Low-saturation cold color palette; ... Realistic physical destruction; Oppressive, heavy, non-heroic atmosphere` | 005 |
| Plush / soft toy | `ultra-fine plush textures, cinematic space scale, cute appearance with intense action contrast, exaggerated FPV camera movement, and realistic soft-body physics`; `A spaceship made of plush fabric, buttons, zippers, and stuffing` | 025 |
| Clay / miniature | `A small fox with a clay texture ... stream water flowing slowly under the bridge like transparent resin ... Miniature scene, shallow depth of field`; plus a style reference image | 022 |
| Claymation restyle | `Edit the video, transforming the video style into a claymation style.` | 055 |
| Ink-wash | `ink-wash style`; `The assassins' movements are also composed of ink brushstrokes, flowing like ink traces`; `Style Note: The entire process maintains the high-contrast black-and-white, ink-wash painting style ... The movements must have a brushstroke feel` | 062 |
| Rock-colour (guofeng) painting x 3D | `Guofeng rock-color painting texture, mineral pigment granular texture, gold foil texture, strong color clash of cyan blue and flowing gold`; `mineral pigment texture of rock-color painting collides with 3D rendering` | 064 |
| Dunhuang CG | `CG animated film quality ... warm gold and stone green gemstone color tones, warm golden light beam in a dark stone cavern` | 026 |
| Motion-graphics illustration | `High-end motion graphics dynamic illustration style, integrating flat MG graphic language, exquisite 2.5D spatial layering, and restrained three-dimensional volume` | 038 |
| Hand-drawn MG over live footage | `low-light real indoor photography × rough hand-drawn MG animation × first-person interactive VFX`; `All animations are rough 2D frame-by-frame hand-drawn` | 028 |
| Paper craft / Material Design | `Google Apple/Material Design, combining colored paper craft, translucent materials and UI interface, clean and refined` | 019 |
| Explainer / whiteboard | `pure white background, soft color blocks and simple line charts, Apple Keynote-style minimalist business aesthetic`; cartoon host with `@Image1` | 047, 048 |
| Kids' educational animation | `A friendly cartoon narrator ... bright, painterly landscape in animation` | 049 |
| Fashion editorial (stylized live) | `high-contrast black and white with hard lighting for a fashion photography texture`; `high-saturation summer street fashion`, selective colourisation | 024, 027 |
| Deadpan surreal | `deadpan humor and absurdity ... bright 'teal and orange'` | 007 |

## 2. Physics and motion registers

| Register | How the handbook states it | Id |
|---|---|---|
| Real-weight inside a stylized world | `Realistic physical destruction`; `Black hydraulic muscles; Metal joints`; `Dry bloodstains, ceramic cracks, and industrial grease` | 005 |
| Soft-body | `realistic soft-body physics`; fur blown backward by airflow; hatch `splits open like a cloth bag` | 025 |
| Brushstroke | `The movements must have a brushstroke feel, the speed must be fast ...` | 062 |
| Insect-like burst | `fixed-point hover - instantaneous ejection - complete emergency stop - acute angle trajectory change`, with counted frames | 016 |
| Tactile miniature | `like transparent resin`, `puffs like cotton wool` | 022 |
| Cartoon-exaggerated | `an extremely exaggerated, even somewhat distorted, ecstatic smile`; `a god-tier transformation in a thousandth of a second` | 003 |
| Dance on a fixed track | movement phrased by the beat structure | 043, 024 |

Pick the register once and write it into the bible. Whichever is chosen, legibility stays.

## 3. Style bible template and worked example `[CRAFT]`

```text
STYLE BIBLE - <film title>
IDENTITY    one sentence: what must survive every generation
Look family     <one row of the catalogue>
Proportions     <rounded / elongated / realistic with stylized surfaces>
Surfaces        <skin/fur, cloth, props, set - one line each>
Render/shading  <flat two-tone with outline | soft global illumination | painted brush ...>
Light           <default, plus a night variant>
Palette         <3-5 colours + one accent>
Depth and lens  <cinematic depth of field | deep focus | ...>
Film texture    <none | deliberate choice>
Physics         <real-weight | cartoon-exaggerated | soft-body | brushstroke>
Style fence     <the look is not X, not Y>
VIDEO STYLE BLOCK (2-4 sentences, built only from the lines above; pasted verbatim)
```

Worked example (original, assembled from the handbook's phrasings above, nothing borrowed from an
existing film):

```text
STYLE BLOCK
A warm feature-film 3D animated look: rounded chibi proportions, physically based soft materials
(felt-like wool coats, matte painted wood), soft global illumination with gentle volumetric
light, cinematic shallow depth of field. Palette of honey yellow, moss green and dusty blue
with one tomato-red accent. Characters move with real-animal weight and small exaggerated
reactions. The look is not photoreal, not glossy plastic, not flat cartoon.
```

Each character profile repeats the look in its first line (`a rounded chibi orange tabby kitten,
warm 3D animated feature look, big dark eyes, ...`), and every shot repeats the character lock.

## 4. Hybrids and transitions

- **Real world -> fantasy world, one camera** (035): continuation sentence, light and atmosphere
  transition named, `the space and lighting remain physically natural and continuous`.
- **Real plate + drawn layer** (028): separate rules for the plate (low-light, noise, handheld) and
  the layer (rough frame-by-frame lines, never outlines on skin).
- **Photoreal -> stylized by edit** (055): one line.
- **Painting -> 3D** (064): `mineral pigment texture of rock-color painting collides with 3D rendering`, with a
  colour clash as the unifier.

## 5. Drift

Drift between shots shows first in proportions, eye style and surface finish. Counter: the
bible in every prompt, the per-character tag in every character description, a style reference
image where available, and the restate sentence per shot (`wan3-core` long-form §5). If one clip
renders a character in a different finish, check whether that clip lacked the per-character tag
before blaming the model.
