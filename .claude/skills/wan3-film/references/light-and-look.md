# Light and look - optics, light, stock, palette

Marks as in `wan3-core/references/provenance.md`. **`[CRAFT]` here includes rules that were bought
with failed generations on Seedance 2.5** (written "Seedance-observed"): they are model-independent
film physics as far as one can tell, but none has been confirmed on Wan - calibrate before treating
one as law. Ids are official handbook prompts. Read this whole file before any deliberate light.

Contents: 1 Optics as meaning - 2 Light registers and exposure - 3 Light level: what stays
visible - 4 Atmosphere - 5 Palette and grade - 6 Stock, grain, defects - 7 Hardware lines -
8 Resolution and ratio

## 1. Optics as meaning `[CRAFT]`

Choose the register by what the frame must say; **write the visible result, never the
millimetres** - focal length and aperture only supplement the result (`[CRAFT]`: the Seedance
optimizer's rule; Alibaba's list also separates *lens* from the rest of aesthetic control).

| Register | Approx. | Earned when | Write |
|---|---|---|---|
| Ultra-wide | 14-18 mm | disorientation, vastness, a POV rig | `causing furniture and door frames at the edges of the frame to curve slightly` (028) |
| Wide | 21-28 mm | a space with a person still readable | `both the figure and the full room stay in view` |
| Moderate wide | 35 mm | observational, walk-and-talk | `natural perspective, background readable but not sharp` |
| Normal | 50 mm | neutral, procedural | `natural human-eye perspective, no obvious distortion` |
| Short tele | 85 mm | an intimate face | `eyes and face sharp, background soft circular bokeh` |
| Tele | 135 mm | isolation | `subject razor-sharp, background dissolves into soft bokeh` |
| Long tele | 200 mm+ | surveillance, distance as danger | `camera far from the subject, close framing through lens reach; background flattened` |

Enclosed interiors (cabin, corridor, lift): there is nowhere to stand back to, so drop to
85-135 mm and omit the distance clause (Seedance-observed: the model otherwise invents a space).
Depth of field = which plane is sharp and what falls outside it (`shallow depth of field locked on
the left-side character`, 011). **Rack focus names both planes and each plane's change**
(`shift focus from the leaves in the foreground to the person in the background; the leaves
blur while the face goes from soft to sharp`). One optical register per shot; switch across a cut.

## 2. Light registers and exposure `[DOC]` `[CRAFT]`

Alibaba's two slots: *light source* and *lighting environment* `[DOC]`.

| Register | Direction and quality | Priority |
|---|---|---|
| Single motivated source | one window, lamp, sky | exposed for the source; faces may fall into shadow |
| Practical-sourced | the light comes from an object in frame | the practical sets exposure - and outshines what it lights |
| Backlit | source behind the subject | camera on the shadow side; rim and bounce reveal detail |
| Low key | small ratio of light to dark | black point just above zero; the darkest surface is a named material |
| High key | broad, even | exposure priority + one burned-out zone |
| Golden hour | low warm sun, long shadows | `golden hour backlighting, lens flare` (061) |
| Night practicals | cool ambient, warm practicals as the only warm accent | one ambient temperature |

Official lines to copy in shape: `Under the cold white glow of fluorescent lights ... extremely
high-contrast lighting, sharp and impersonal` (002); `A square fill light behind the character
creates a rim light, with cool white indoor lighting` (043); `Soft three-point lighting
characteristic of American TV dramas, eliminate the hard shadow on the right side of the man's
face` (053 - a relight edit); `Tyndall light beams` over a lake (064); `the main light sources come
from warm yellow wall lamps, small table lamps, laptop screens` (028).
**State the exposure priority**: "exposed for the window, the room falls dark" beats "well-lit
room with a window".

## 3. Light level: what stays visible `[CRAFT]` (Seedance-observed)

Darkness adjectives fail: "near-total darkness" makes the model darken everything, including the
doorway the scene needs. Write **what darkens, what stays visible, where the effect stops**
(`darken the four corners gradually while keeping the skin tone in the centre natural, without a
black border`). In a low-key shot:

- name **exactly one**, small, bounded object that stays discernible (a doorway, a face, a card);
  five such lines read as "preserve everything" and the exposure returns to the faces; a wall that
  fills the frame as "the discernible object" lit everything grey;
- never give a dark material the word "brightest" - brightness outranks material;
- **describe a lit place and let the grade darken it**: "the corridor is all black except a strip"
  is skipped, not built; a solid-black field with no shadow detail ate a wide frame;
- a bare lamp or a screen in frame outshines what it lights: keep the source out of frame and show
  its light, or write its glow pale, cold and dimmer than the key; turn screens away so their
  content is never rendered;
- with one source, anchor each character inside its pool of light, or they drift out of it.

Example: `Only the flashlight beam and the stone it strikes are lit; the rest of the chamber falls to
near-black, its stone faintly textured. The arched doorway on the left stays discernible as a
silhouette.`

## 4. Atmosphere `[DOC]` `[CRAFT]`

Weather and haze are **interactions**, not nouns: `rain crosses the streetlamp's cone as bright
streaks, beads on the car's hood and kicks up spray where the tyres cut through standing water`.
Rain visible across a night street needs light sources at those depths (lamp near, window mid,
headlights far). Dense fog or overcast around a small space is a giant softbox: keep a practical
inside the space and expose for it. Volumetric light is a named effect: `Tyndall light beams`,
`golden dust slowly rotates within the beam` (026, 064), `glowing spores floating in the air`.

## 5. Palette and grade `[DOC]`

The handbook states palette as named colours **with jobs**: `Strictly adheres to a bright 'teal and
orange' color scheme. Teal: the cloudless sky ... Orange: ...` (007); `Pure black and pure white
seamless studio backgrounds ... high-contrast black and white with hard lighting` (024); `the entire
frame presenting a strong light green filter, creating a cold atmosphere` (002); `cyan blue x
flowing gold color clash` (064). Two or three colours with roles; one filter sentence if the whole
frame carries a cast. A grade stated as a *consequence* (`desaturated, high-contrast, sharp and
impersonal`) outperforms a bare "teal and orange" `[CRAFT]`.

## 6. Stock, grain, defects `[FIELD]` `[CRAFT]`

Name the stock technically and pair it with its visible trace (a generic "vintage" maps to a
hundred looks, a stock name to one `[FIELD]`):

| Register | Grain | Halation | Colour | Shadows |
|---|---|---|---|---|
| 35 mm daylight (250D-like) | fine, even | subtle | warm-neutral, soft highlight roll-off | soft, detail survives |
| 35 mm high-speed (500T-like) | coarser, present in shadow | pronounced around practicals and neon | warm midtones, rich skin | detail deep into low light |
| 16 mm | heavier, softer overall | stronger, diffuse | slightly desaturated | grain even in mid-tones |
| Clean digital (ARRI-like) | minimal | none unless added | neutral, high dynamic range | clean |

Defects are a realism tool when **localized, motivated by a real light source or lens, and
inconsistent frame to frame**: halation bloom around a streetlamp, a brief horizontal flare as the
source passes behind the subject, faint chromatic fringe at the frame border, a natural vignette
without a hard border, directional motion blur, deep blacks that keep a faint texture. Uniform,
centred or frame-static versions read as a filter. 028 is the official model: `slight high-ISO
noise, color grain in shadows, limited dynamic range, slight color shift, lens vignetting,
compressed texture`. A fast move smears a heavy grain register: slow it, lighten the grain, or
choose the smear.

## 7. Hardware lines `[DOC]`

The handbook's spec lines: `shot with Arri Alexa 65 and Panavision anamorphic lenses, Kodak
Vision3 500T film texture, 8K resolution, photorealistic, no text` (037); `35mm film ... natural
light flares, soft warm tones, shallow depth of field` (063); `Wong Kar-wai style cinematic feel`
(063); `Apple/Material Design ... cinematic macro` (019). Use them as **register signals**, one
line, once per prompt, followed by the trace the register must show (`anamorphic: a horizontal blue
streak flare crosses the frame; oval bokeh`). `8K` and `4k high quality` are uninformative; the
model's output tops out at 1080p anyway `[HF]`.

## 8. Resolution and ratio `[HF]`

Heavy grain in a dark scene at 480p/720p turns to blocks `[CRAFT]` (Seedance-observed): write
`fine-grained 35 mm grain`, judge it at the final tier (`wan3-budget`: 480p drafts cannot judge
grain). Delivered pixel size is a fact to check on every clip, not an assumption. No 21:9 on
Higgsfield for Wan: 16:9 plus crop, composition kept in the central 2.39 band.
