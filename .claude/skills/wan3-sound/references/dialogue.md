# The dialogue block - two or more characters, any speech

Marks as in `wan3-core/references/provenance.md`. The mechanisms below were bought with failed
generations on Seedance 2.5 (speaker attribution lost five times in a row, each time for a
different reason); here they are `[CRAFT]`, untested on Wan. The handbook's own dialogue examples
(015, 021, 036, 044, 048, 056, 059) show the intent. Read this whole file before a multi-speaker
prompt.

Contents: 1 The ledger - 2 Rules - 3 Official dialogue exemplars - 4 Pacing arithmetic - 5 Recorded
voices - 6 What breaks

## 1. The ledger `[CRAFT]`

An in-prompt block, one entry per time segment, silent segments included. A rule that is only an
internal note goes unapplied; a rule that is a block in the prompt gets checked (and the lint can
see it).

```text
Dialogue ledger
Segment 1 (0-5s) - speaker: ANNA, the woman on the left of frame (Image 1). On-screen.
  ANNA says in English: "Which area are we training today?" Her lips move as she speaks.
  MAYA's lips stay naturally closed while she listens.
Segment 2 (5-9s) - speaker: MAYA, the woman on the right (Image 2). On-screen.
  MAYA says: "Let's train back, my legs are still sore from yesterday." Her lips move.
  ANNA nods; her lips stay closed.
Segment 3 (9-10s) - no speech. Both mouths visible, lips closed; they begin to walk.
```

Each entry carries: the speaker's **name** and an identifier that survives (face/position/build,
not clothing alone), whether the voice is on- or off-screen, the exact line, the language if not
English, and the state of every other visible mouth.

## 2. Rules `[CRAFT]`

1. **Words in one place.** The quoted line appears once. A voice reference line binds the voice
   and its timing, and repeats no words, or the line is spoken twice.
2. **Name the speaker in every clause inside a timed segment.** A single "he" or "she" resolves
   to the largest or nearest face and takes the line with it. After fixing a pronoun, search the
   whole prompt for the next one.
3. **Identifier checked against the frame.** Describe the speaker by what the reference image or
   keyframe actually shows (nearest, left, taller), not by the intended blocking. With references:
   `define the woman in Image1 as Subject1, define the woman in Image2 as Subject2` (015) and use
   Subject1 / Subject2 in the lines.
4. **Distinct names.** No shared prefix, different lengths (ANNA / MAYA held; "Client One / Client
   Two" swapped).
5. **The speaker has a positive mouth task.** Do not stack "does not move" prohibitions on a
   speaking body.
6. **Gestures only where legible.** A gaze action the camera cannot show migrates to the nearest
   readable face, and takes the dialogue with it. Write the face business in the shots that show
   it.
7. **Over-the-shoulder:** the nearest body is the listener's shoulder; say whose shoulder it is
   and that their lips stay together. Speech otherwise migrates to the largest face.
8. **A voice with no mouth** (phone, radio, another room) is marked off-screen, and the listener
   turns or lowers the face for that segment.
9. **Delivery in the descriptors of the line**, one emotion per line; per-word tone notes can be
   rendered as subtitles. If you need two deliveries, write two lines.
10. **Do not invent lines.** Intention without words is played by pauses, breath, posture and the
    listener's reaction.

## 3. Official exemplars

| Id | Shape | Take |
|---|---|---|
| 015 | two women, two voice references | `Define ... Subject1 ... Subject2. Subject1's dialogue tone of voice references Audio1 ...` then alternating action + quote; the scene's body business (towel, bottle, nod) separates the lines |
| 021 | solo, inline foley | action sentences carry `<sound of cloth rubbing>` and `<kitten whimper>`; no spoken line - the silence is the scene |
| 036 | three speakers, sectioned | `Expression & Lip Sync` and `Voice & Sound Effects` blocks name each speaker's line and voice (`Male voice clear and cool ... moderately fast pace`) |
| 044 | replacement + voice | `Extract the vocal characteristics from audio @Audio1 and have the character speak the following lines: "..."` then a Lip-sync & Expression block (`natural blinking, slight head nods, and a sense of breathing`) |
| 056 | edit of a line | `Edit the video, changing the male character's line to: "..."` |
| 059 | extension, two men, long lines | `Extend video 1 by 15 seconds.` then every line attached to a named character with business between them |
| 048 / 049 | voiceover over animation | `Host (V.O.): "..."` per shot |

## 4. Pacing arithmetic

Spoken pace in the handbook: **about 2.5 words per second** (047, "speaking speed about 2.5
words/second"). Shot length >= words / 2.5 + a beat (0.5-1 s) before and after. Examples: 8 words ->
3.2 s -> a 5 s shot; 25 words -> 10 s; a 30 s clip holds about 60 words of dialogue if nothing else
happens. Overlong lines get speeded up and mushy, or truncated. The lint warns above 3 words per
second.

## 5. Recorded voices `[CRAFT]`

One reference audio per character (<= 15 s in total for all 5 clips `[FIELD]`); clean, no
music or room echo; the line recorded is the line in the prompt, and the prompt says so. If a take
is shorter than the shot, pad the **tail** with its room tone. Keep a list of lines not yet
recorded so that a missing line is a known gap. Cutting recorded speech: only on a played pause,
each cut closed by a physical event in frame, one master take per character per shot (the
Seedance set's `acting-system/references/craft.md` section on cutting recorded speech applies).

## 6. What breaks `[FIELD]`

Dialogue audio can sound processed; Japanese and other non-English speech is reported weak;
lip-sync is reported strong on controlled characters and delayed on long clips; on a 30 s
generation the last seconds drift. Plan short speaking shots (3-8 s) and cut between them
rather than one 30 s conversation; verify lip-sync at the final tier, not at 480p.
