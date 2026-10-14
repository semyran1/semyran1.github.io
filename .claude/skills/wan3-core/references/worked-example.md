# Worked example - two speakers, three hard-cut shots, REF, 15 s

One complete, lint-clean delivery, so the rules of core, film and sound can be seen working
together. The scene, names and lines are invented for the demonstration; the structure is what to
copy. Marks: the structure follows the handbook's shapes (035, 037 for the timeline, 015 for
two named speakers) `[DOC]`; the ledger, the Fincher interior variant and every budget number are
`[CRAFT]` / `[HF]` as in their files - **nothing here has been generated yet**.

**Brief (Russian-speaking user, translated):** an interrogation room, a detective (man in a grey
suit, Image 1) and a witness (young woman in a green coat, Image 2), Fincher look, four short
English lines, three shots, 15 s, final at 720p, budget 40 credits.

## 1. Plan

- Mode REF, two `image_references`; the cut state is **hard cuts** (coverage), so each shot could be
  its own REF clip; one 15 s clip is chosen here because the budget allows one final only.
- Price: 15 s at 720p = 26.25 cr (`wan3_cost.py price`). `wan3_cost.py expected --p 0.3 --budget 40`:
  expected 87.5 cr per usable clip, over budget, so `wan3-budget` §4b applies: one L1 structure test
  (480p, 3 s, same role lines, one line of dialogue = 3 cr), then one final; total 29.25 cr, no
  retry. The user is told this before anything is spent.
- Packs: `wan3-film` Fincher, enclosed-interior variant; `wan3-sound` dialogue (2 speakers).
- The test answers one question: do Image 1 and Image 2 bind to the right people, and does the right
  mouth move? (calibration C1 is the same question for the tag syntax.)

## 2. Header

```text
Loaded: wan3-core - SKILL, limits, prompt-grammar, modes-and-references, long-form, constraints; wan3-budget - SKILL, price-table; wan3-film - SKILL, camera, light-and-look, stylepacks/_contract + fincher; wan3-sound - SKILL, dialogue | Not loaded: wan3-edit (no source clip), wan3-stylized (photoreal) | Mode: REF | Model: wan3_0 720p 15s | Cost: 26.25 cr (offline estimate; media-attached price unmeasured) | Words: 630 | Negatives: 2
```

## 3. Prompt

```text
Live-action photoreal procedural thriller, 15 seconds, 16:9, three shots joined by hard cuts, one interrogation room, two characters, dialogue in English.

Image 1 is the sole appearance reference for Harlan, the detective: face, hairstyle, build, grey suit; its background is unused.
Image 2 is the sole appearance reference for Ivy, the witness: face, hairstyle, build, green coat; its background is unused.
Exactly two people appear. Harlan and Ivy keep their own faces, clothing and lines in every shot.

Look: desaturated teal-cyan shadows, dirty tobacco-amber highlights, deep blacks lifted just off pure black. The darkest surfaces are the oxidized steel door and the scuffed cinderblock wall, faint texture still visible in them. One cold clean white is reserved for the single lamp. Ivy's coat stays recognisably green, only muted. Exposed for the lamp; the faces fall where the lamp leaves them; haze visible inside the light cone. Fine-grained 35mm film grain, most visible in the shadows. Short-telephoto look: faces sharp, the back wall a soft dissolved wash.

Setting: a bare windowless interrogation room. A steel table with a closed manila folder on it, two chairs facing each other across it, the steel door at the back left. The only light is one lamp above the table, out of frame, throwing a hard-edged cone onto the table and both people, with hard falloff into dark that still holds the shape of the room. The steel door stays discernible as a flat dark shape.

Shot 1 [0-6s]: Fixed shot with a slight handheld breathing pulse, eye-level two-shot from slightly off the profile line, camera 15 degrees off perpendicular. Harlan sits frame-left, forward, forearms on the table, nearer the camera; Ivy sits frame-right, upright, hands flat on the table. The table edge, the door and the lamp cone stay at the same place in frame. Harlan says in English, "Where were you at nine?" After a pause Ivy says, "At home. Alone." The shot ends as Harlan's right hand settles flat on the folder <soft paper rustle>.

Shot 2 [6-11s]: Hard cut to a fixed medium close-up of Harlan at eye level with a slight handheld breathing pulse, facing frame-right toward Ivy off-screen; a dark out-of-focus table edge fills the lower 30 percent of the frame. Harlan holds his gaze on Ivy and says in English, "Your coat was on the pier." Then Harlan stays still until the shot ends.

Shot 3 [11-15s]: Hard cut to a medium close-up of Ivy at eye level, facing frame-left toward Harlan off-screen; a dark out-of-focus table edge fills the lower 30 percent of the frame. The camera holds locked-off while Ivy says in English, "Then someone borrowed it." When Ivy finishes, the camera begins a very slow push-in toward her eyes and continues to the last frame. Ivy's gaze holds steady on Harlan.

Dialogue ledger
Segment 1 (first shot) - Harlan, the man in the grey suit (Image 1), frame-left, on-screen, speaks first; Ivy's lips closed. Then Ivy, the young woman in the green coat (Image 2), frame-right, on-screen, speaks; Harlan's lips closed.
Segment 2 (second shot) - Harlan alone in frame, on-screen, speaks; Ivy is off-screen and silent.
Segment 3 (third shot) - Ivy alone in frame, on-screen, speaks; Harlan is off-screen and silent.
In every segment the speaker's lips move with the words and the other mouth stays closed.

Sound. Voice: Harlan's voice is a man's, low, dry and quiet, even pace, close to the microphone; Ivy's voice is a young woman's, soft and steady, slightly slower pace, close to the microphone. Effects: the paper rustle marked in the first shot and a faint chair creak as Harlan sits forward. Music: no music. Ambience: room tone, a low electrical hum from the lamp and a faint ventilation hum, silence between the lines. No subtitles.
```

## 4. Lint

```text
python3 -I scripts/prompt_lint.py prompt.txt --duration 15 --res 720p --mode REF --images 2
Words: 630 | Negatives: 2 | Cost: 26.25 cr
Warnings: none
```

(Re-run it on your own copy: the ledger lines are skipped by the shot/range readers on purpose.) The
two negatives are the user-style lines `no music` and `No subtitles`, each traced to a request.

## 5. What to notice

- **One pack, one lens, one palette** - the interior variant of the Fincher pack, with the reference
  colour (green coat) winning over the palette in a single sentence.
- **Every shot names its camera**; shot 3's `locked-off, then a slow push-in after the line` is one
  treatment with a trigger.
- **Each speaker is named in every speaking sentence**, the other mouth is stated closed, and the
  speaker is always visible (off-screen voices are avoided on purpose, `wan3-sound` rules 6-8).
- **Words once**: in the shot sentences; the ledger repeats none.
- **Pacing**: the longest line is 6 words (about 3.4 s with air) inside a 5 s shot; shot 1 carries 7
  words in 6 s.
- **Word count 630** is above the 350-620 range of `prompt-grammar.md` section 4: this is a
  two-reference scene with dialogue and a style block; if the L1 test passes, trim the setting and
  look paragraphs first, never the role lines, the lines or the end states.
- **Budget**: the first spend is the 3 s, 480p structure test (3 cr), not the 26.25 final.
