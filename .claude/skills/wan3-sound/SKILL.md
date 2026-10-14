---
name: wan3-sound
description: "WAN 3.0 SOUND - the audio half of a Wan 3.0 prompt, loaded after wan3-core: native dialogue and lip-sync, voice descriptors, voice references (Audio 1 bound to a character), inline sound effects, music design, ambience, explicit silence, speaker attribution with 2+ characters, words-per-second pacing, accidental subtitles, speech-language risk (English/Mandarin vs Russian) and the dubbing fallback. Use for \"диалог\", \"лип-синк\", \"голос\", \"озвучка\", \"музыка\", \"без музыки\", \"звуки\", \"говорит не тот\", \"субтитры появились\", \"реплика\", \"озвучить на русском\", \"voiceover\", \"BGM\", \"ambient\", or any Wan 3 prompt where something is heard. Wan generates sound in the same pass as the picture and fills the track if you say nothing, so sound is always a decision. Not for picture (wan3-film) or reference mapping (wan3-core)."
---

# WAN 3.0 SOUND

Wan 3 generates **picture and sound together** `[DOC-2]`: dialogue, effects and music come from the
same pass, a reference audio can be attached, and an unmentioned track is filled with whatever the
model finds plausible `[FIELD]`. On Higgsfield `generate_audio` is on by default and **does not change
the price** `[HF]` - so sound costs nothing and must be decided anyway. `wan3-core` §0 governs this file; marks as in
`wan3-core/references/provenance.md`. Rules ported from the Seedance dialogue/audio references are
`[CRAFT]` (their mechanism - speaker resolved by prominence, silent segments filled with speech,
per-word delivery notes turning into subtitles - looks model-independent, but each was paid for on
Seedance and none is confirmed on Wan).

## Reading map

| Situation | Open |
|---|---|
| Two or more characters, any line spoken, a voice without a mouth, a recorded take | `references/dialogue.md` |
| Music arc, sound effects, ambience, silence, a dance to a track, sound design by shot | `references/music-and-sfx.md` |
| Everything else | this file |

## §1 - Decide the four layers `[DOC-2]`

Alibaba's guide splits sound into a **voice** (lines + emotion + tone + speed + timbre + accent), a
**sound effect** (source material + action + ambient sound) and **music** (score + style) `[DOC-2]`.
Add the fourth the handbook uses: **ambience / silence**. For every clip write one sentence per
layer or declare it absent:

```text
Voice: <speaker> says, "<line>" - <voice descriptors: age/gender, timbre, pace, pitch, emotion>.   | no dialogue
Effects: <inline cues at the moment they happen, in angle brackets>                              | none
Music: <score + style + arc over time, in parentheses>                                           | no music
Ambience: <what the room/street sounds like>                                                     | silence
```

An omitted layer is an open invitation: the model supplies music under a quiet scene and a voice
under a mouth that moves.

## §2 - Syntax the handbook uses `[DOC]`

| Layer | Form | Example (id) |
|---|---|---|
| Dialogue | speaker + speech verb + quoted line | `Subject1 turns her head, smiles, and says to Subject2, "Which area are we training today?"` (015) |
| Dialogue edit | `Edit the video, changing the male character's line to: "..."` | 056 |
| Dialogue + lip-sync label | `lip sync to dialogue "Under the trigger, none can escape."` | 036 |
| Voice descriptors | `Male voice clear and cool, slightly free-spirited and roguish, moderately fast pace, moderate pitch` | 036 |
| Voiceover | `Host (V.O.): "..."`, `Narrator: "..."` | 048, 049 |
| Inline effect | `<sound of cloth rubbing>`, `<kitten whimper>`, `<click of a mechanical unlocking sound>` | 021, 035 |
| Music cue in prose | `(a low cello melody slowly rises, interspersed with harp plucks)` | 035 |
| Music arc | opens low and ambient, adds bass pulses and strings, holds its breath, erupts into brass when the monster surfaces (paraphrase) | 006 |
| Sound-effect layer with triggers | `a 'whoosh' sound when color blocks slide in, a light keyboard 'click' sound when numbers tick` | 047 |
| Voice reference | `Subject1's dialogue tone of voice references Audio1` / `Extract the vocal characteristics from audio @Audio1 and have the character speak the following lines: "..."` | 015, 044 |
| Silence | `zero voiceover` (046); `The audio type includes ambient sounds and music, no dialogue, only night insect chirps, faint water sounds` (008) | |

Conventions for this set: dialogue in straight double quotes with the speaker named in the same
sentence; effects in `<angle brackets>` placed where they occur; music in `(parentheses)`;
section labels in square brackets (`[Voice & Sound Effects]`, as 036 does with its own brackets) if the prompt is
sectioned. A third-party suggestion to use curly braces for dialogue `[FIELD]` is unverified on
Wan: quotes are what the handbook shows. Use angle brackets for effects **or** for names, never both
(the lint warns).

## §3 - Dialogue basics `[CRAFT]` unless marked

- **The speaker slot takes a name.** "He says" resolves to the most prominent face; name the
  speaker in every speaking sentence.
- **The words live in one place.** A line stated in the dialogue sentence and again in a
  description is spoken twice.
- **The speaker gets a positive mouth line** (`her lips move as she reads the words`); a list of
  prohibitions on a body with no active task reads as "inert" and freezes the mouth.
- **Silent characters** keep their mouths naturally closed while listening (Seedance's documented
  line; worth copying); a segment with no speech is written as fully as a speaking one - free time
  is filled with speech.
- **Pace**: the only pace the handbook states (047, a voiceover prompt) is **about 2.5 words per second**.  Shot length >= words / 2.5 + 1 s (half a second each side). A 15-word line needs 7 s.
- **Delivery**: put emotion and manner in the voice descriptors of the line, not in separate
  instructions attached to individual words - those tend to come back as on-screen subtitles
  (Seedance FAQ). Splitting a line into two with one emotion each is the safe form:
  `Anna's line (flat, tired): "By Friday." Anna's line (sharper, not louder): "Artur."`
- **Lip-sync**: ask for it where the face is legible (`lip sync to dialogue`, 036). A turned head or
  a mouth outside the frame has nothing to sync, so a voice without a visible mouth is marked
  off-screen and the listener's face turns away. A 480p draft proves only that the mouth moves;
  judge sync at the final tier.
- **Do not invent dialogue** the user did not supply: a character without text plays by pauses,
  posture, breath and reaction.

Two or more speakers: the dialogue ledger of `references/dialogue.md`. **Where the words live:** in the
shot sentence, as the handbook writes them (015, 021); the ledger then carries names, positions and
mouth states only and repeats no words. Style-pack sound lines (`wan3-film` packs) are menus: add a
voice-over or a spoken line only when the brief supplies it.

## §4 - Voice references `[DOC]` `[DOC-2]` `[FIELD]`

Attach the voice as `audio_references` and bind it by number to one character: `Subject1's dialogue
tone of voice references Audio1` (015) - **one reference per speaker**; the binding covers all of that
character's lines `[DOC-2]`. By default a reference gives timbre, accent, pace and emotion; if the
recorded take must be spoken as recorded, say so (`Audio 1 defines the man's voice and the line he
speaks`) `[CRAFT]`. Limits `[FIELD]`: 5 clips, 15 s in total, WAV or MP3 <= 15 MB. Clean takes: no music
under the voice, no reverb, no second speaker. Pad a very short line at the **tail** with the take's own
room tone, never digital silence (a zero-padded take was rejected as if moderated on Seedance;
Wan untested). A voice reference can also drive rhythm: `Choreograph the dance according to the
fixed audio's rhythm, speed, and emotional fluctuations` (043).

## §5 - Silence and "no music"

Say what the soundtrack **contains** and what it may not: `The soundtrack is only the room tone and
the footsteps; no music, no voiceover`. The handbook's forms: `zero voiceover` (046), `no dialogue,
only ...` (008); Alibaba's own: `No BGM, generate only ambient and action sounds` `[DOC-2]`. Music
that leaks through "no music" is a known problem class on Seedance; the cure there was an
audio policy at the head of the prompt and the same constraint repeated at the end `[CRAFT]`.
Subtitles: Alibaba's common negative is `no subtitles`; state it when text on screen would be a
defect, once.

## §6 - Language `[OPEN]` and the fallback

Alibaba does not document speech languages. Third-party lists name English, Spanish, French,
German, Japanese, Korean and Mandarin; **Russian is never named**, and reviewers report weak
Japanese dialogue and processed-sounding dialogue in general `[FIELD]`. The model-facing prompt
stays in English; the quoted line is in the spoken language. **Run calibration C4 (4 credits)
before planning Russian dialogue**; until it is logged:

1. For scenes that need Russian speech, generate the picture silent or with ambience
   (`no dialogue`) and add the voice in post - Higgsfield lists `dubbing`, `voice_change`,
   `create_voice` and a lip-sync model (`sync_so`) in its tools `[HF]`; their quality and price on
   Wan output are untested (`get_cost` first).
2. For English or Mandarin lines, Wan's native lip-sync is the first choice.
3. If a Russian line is spoken in an accent or garbled, retry once with the line transliterated in
   Latin and `in Russian` before the quote (`says in Russian: "..."`), then fall back to 1.

## §7 - Pre-send items added by this skill

1. Every spoken line: quote the sentence that names the speaker, and the words-per-second figure
   against the shot length.
2. Each of the four layers is written or declared absent (quote it); "no music" appears at the head
   and, if music leaked before, at the end too.

## §8 - Full audit

3. Words appear once. 4. Silent characters' mouths are stated closed. 5. No pronoun stands in for a
   speaker. 6. Distinct names (no shared prefix: "Client One / Client Two" swapped on Seedance).
7. Each voice reference is bound to exactly one speaker and its limits (5 clips, 15 s) respected.
8. Delivery notes sit in the line's descriptors, not attached to single words.
9. Sound effects are placed at the moment they occur; music has an arc, not an adjective.
10. The cut/timeline of the shot leaves time for the line (2.5 w/s).
