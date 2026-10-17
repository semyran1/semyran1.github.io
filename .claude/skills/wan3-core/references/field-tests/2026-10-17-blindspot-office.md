# Field test plan 2026-10-17 - "Blind spot", scene 4, Arthur's office (planned, nothing generated)

Source clip: Higgsfield project Blinding Spot, folder Scene 4, job `bdd79bb6-dcdf-4c77-b6c9-a2061911b3ee`
(Seedance 2.5, 25 s, 21:9, 720p, 8 shots, favourite). Beat: Angelika says Maestro wanted Arthur on
the project but he is always busy, whispers it back, Arthur closes it ("Да нормально.") and holds up
the drawing ("Слушай, а это где-нибудь видела?"). Goal: remake it on Wan 3.0 and learn what of the
Seedance acting layer (`acting-system`) transfers. Prompts get written, linted and priced with
`get_cost` before anything is generated; the user approves the spend.

## Inputs (all reusable by media id)

| Role | Name | Media |
|---|---|---|
| Arthur | artur-talking | `c95dcebc-d736-41ee-a6b7-15afe936a323` (media_input) |
| Angelika | Angi | `4bb22ad3-0087-4258-88f1-aaec244036ed` (image_job) |
| The sheet | List | `53e3e53a-1535-478f-9747-54320c890cd0` (image_job) |
| Project folder | kaskad-papka | `f9274822-ecd9-4a95-a828-30f4bdf98958` (media_input) |
| Client folder | Dogovor-papka | `19877c85-02d7-4f6b-aa93-bc86b3b89530` (image_job) |
| Office plate | cabinet_2 | `40c84da2-c8a9-4718-b57a-4f3ce020b14e` (image_job) |
| First frame (not usable with references) | image_1 | `0a6c979a-8c7b-4a16-9b3e-7353fa5b4fba` |
| Takes (Russian) | Angelika line 1 9.7 s, Angelika whisper 2.5 s, Arthur 2.5 s, Arthur 2.8 s | `f26ec13c-...`, `fe8f4520-...`, `f63b6b95-...`, `e14bcfff-...` (audio_input, order as in the Seedance job) |

## Shots to carry over (Seedance timings)

1 hold 0-1 s (drop) - 2 Angelika medium 1-5.5 s, line 1 - 3 over-the-shoulder on Arthur 5.5-11 s, line 1 continues
off-screen, hand wave, Arthur's face does not change, pen stops - 4 two-shot 11-13.5 s, silent, Angelika's face
changes - 5 Angelika close 13.5-16 s, whisper, half step back - 6 Arthur close 16-18.5 s, "Да нормально.",
eyes drop - 7 Arthur medium 18.5-22 s, silent, hesitation, reaches left, returns with the sheet - 8 over-the-shoulder
22-25 s, question, eyes come up on the first word.

## Known conflicts with Wan on Higgsfield

- 21:9 does not exist: use 16:9.
- `start_image` cannot be combined with `image_references`: the opening composition is described in text and held by the office plate.
- Takes total 17.5 s and Wan's audio-reference total is 15 s `[FIELD]`: generate by shot, not as one 25 s clip.
- Speech language Russian is unconfirmed `[OPEN]` (calibration C4); a Wan voice reference supplies timbre, the words come from the prompt.
- 8 declared cuts in one clip is untested (3 shots / 6 s held).

## Proposed order

1. Probe P1 (3 s, 480p): shot 6 with Arthur's take as voice reference, Russian line in the prompt. Answers C4 and whether a take binds.
2. Probes P2/P3 (about 5.5 s each, 480p): shot 3 twice, same refs, same dialogue-free action: once with plain action, once with the acting layer (behaviour, trigger before reaction, interrupted action). Answers whether the acting layer changes anything on Wan.
3. If P1-P3 pass: shots 2-8 separately at 480p, then re-roll the weak shots; final tier only for the accepted ones.

Results: pending the user's approval.
