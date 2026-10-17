# Seedance 2.5 vs Wan 3.0 - what differs for the prompt writer

Marks as in `provenance.md`. Written 2026-10-17 after the applied tests. The Seedance side is quoted
from its official Prompt Guide / User Guide / `sd25-pe` optimizer as the Seedance skill set holds
them (`[DOC]`). The Wan side is the 64-prompt creator handbook (`[DOC]`) plus third-party summaries
(`[FIELD]`): Alibaba's own prompt guide could not be opened from the session (DNS and egress block).
Use this file to decide what to port from a Seedance prompt; port nothing marked "differs" as is.

## The documentation itself

| | Seedance 2.5 | Wan 3.0 |
|---|---|---|
| Form | rules: mapping ladder, required-entity audit, `Unused Assets`, internal dialogue ledger, a generation template | formulas and a library: basic / advanced / sound / reference / multi-shot / edit formulas, 64 official prompts |
| Prompt length | long structured blocks are normal | official median about 268 Chinese characters; style and "stay unchanged" locks dominate, prohibitions about 6% |
| Negatives | documented scope: subtitles and audio; a prohibition tends to print the thing it names | no negative-prompt field; exclusions are ordinary sentences |
| Assets seen by the writer | 30 images / 10 videos / 10 audio, audio total 30 s | 10 images / 5 videos / 5 audio, audio total 15 s `[FIELD]` |
| Reference syntax | `@Image1`, saved elements as `<<<id>>>` placeholders | `Image 1` per type in upload order; `@Image1` also binds `[EMPIRICAL]`; saved elements are not supported, pass their images |
| First frame + references | combinable | rejected at submit on Higgsfield (422) `[HF]` |
| Aspect | 21:9 available | no 21:9 on Higgsfield `[HF]` |
| Duration | 4-30 s | 2-30 s |
| Cuts | timestamps plus the boilerplate "natural shot switching" at every cut | name the camera in every shot, say `Hard cut to`; `No cut.` for a take; declared cut counts held at 3 shots / 6 s `[EMPIRICAL]`, unproven at 8 shots |
| Sound syntax | `()` music, `<>` effects, `{}` dialogue, `[]` subtitles | quotes for dialogue, `<>` effects, `()` music |
| Speech languages | more than ten documented | not documented; Russian never named `[OPEN]` |
| Recorded takes | "reuse the dialogue in the audio" is a documented sentence; the audio supplies timbre, accent, pace, emotion by default | handbook shows the line written in the prompt with a voice reference (015, 044); whether a Wan take is spoken as recorded is untested |
| Edit / extend | out of scope for the Seedance set | native modes; 22 of the 64 handbook prompts |
| Draft and seed | Draft mode, seed reuse | no seed on Higgsfield; a 480p draft checks the prompt, not the take |

## Acting

Seedance documents the shape: `direction + trigger + observable performance + camera/light/sound
change`, two to four cues per transition, moderate emotion words allowed when exact control is not
needed, intense emotion words can make eyes glow `[DOC]`. Wan has no equivalent official text. What
the Wan sources say is smaller: describe visible actions, not emotion labels (third-party `[FIELD]`),
and the handbook's own expression blocks are two lines long (044: `natural blinking, slight head nods,
and a sense of breathing`; 036: a separate `Expression & Lip Sync` block). So the Seedance acting
layer (objective, obstacle, tactic, a 150-220 word master profile per character) is a hypothesis on
Wan: the part that should carry over is behaviour and trigger-before-reaction, the part to test is
the length. Test plan in `field-tests/2026-10-17-blindspot-office.md`.

## What does not port

- `<<<element id>>>` placeholders and `<<<image_1>>> as the first frame`: use the element images as
  `Image N` references and describe the opening composition in text.
- The "natural shot switching ... prohibit rigid cutting" paragraph repeated at each cut: replaced by
  one `Hard cut to` per shot (not tested at 8 shots).
- Dialogue words in a `{}` ledger with a recorded take that is "spoken as recorded": on Wan the words
  stand once in the shot sentence; the take is a voice reference.
- Audio takes totalling more than 15 s in one generation: split by shot.
