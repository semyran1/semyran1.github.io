# Blind spot, scene 4 - frame-by-frame, Seedance 2.5 against Wan 3.0 (2026-10-17)

Material: Seedance job `bdd79bb6` (1470x630, 24 fps, 25 s) and the user's two Wan recreations at 720p:
clip A `feeb2b8d-db77-4c83-b33f-f95c81f1dfb9` (14 s, shots 1-4) and clip B
`1cc409e4-4c96-4562-99b7-3a7927e27508` (12 s, shots 5-8). Frames were pulled in a Higgsfield cloud
sandbox (ffmpeg; the local session cannot reach the CDN) and read by Claude; speech was transcribed with
faster-whisper (`ru`, small model, so words are approximate). One scene, one run per clip: provisional.

## Cuts (scene-change detection, threshold 0.25)

| Clip | Declared cuts (s) | Detected cuts (s) |
|---|---|---|
| Seedance, 8 shots | 1.0, 5.5, 11, 13.5, 16, 18.5, 22 | 1.1, 6.1, 10.7, 13.7, 16.3, 18.7, 22.2 (7 of 7, within 0.6 s) |
| Wan A, 4 shots | 1, 5.5, 11 | 2.4, 4.8, 11.6 (3 of 3, off by up to 1.4 s) |
| Wan B, 4 shots | 2.5, 5, 8.5 | 3.6, 5.8, 8.9 (3 of 3, late by 0.4-1.1 s) |

## Seedance, shot by shot

1. 0-1.1 s wide master: Angelika left against three tall bright blinds, Arthur at the desk right, shelving behind him.
2. 1.1-6.1 s Angelika medium from the side, the blinds bright behind her right, concrete wall with light bands at her left.
3. 6.1-10.7 s over-the-shoulder on Arthur: olive shelving unit behind him, her dark arm at the left; his face still, pen in hand.
4. 10.7-13.7 s the scripted two-shot came out as an Arthur close-up, eyes down (a deviation from the script that served the beat).
5. 13.7-16.3 s Angelika close, a bright window on the right of her, face and whisper.
6. 16.3-18.7 s Arthur close, eyes closed or down; the same blurred background as shot 4.
7. 18.7-22.2 s Arthur from the side, reaching for papers, the same shelving behind.
8. 22.2-25 s two-shot with the bright window wall behind both, Arthur holding the sheet.
Room: window wall behind Angelika and shelving behind Arthur in every angle; light bands on the same walls.

## Wan A (shots 1-4)

1. 0-2.4 s wide master: close to the supplied first frame (windows left, Angelika left, Arthur at the desk with the open folder in his hands). Held 2.4 s, not 1.
2. 2.4-4.8 s Angelika medium: the tall blinds are gone; a glass partition with horizontal blinds stands behind her; Arthur's shoulder and pen are in frame although the prompt said he is out of frame.
3. 4.8-11.6 s over-the-shoulder on Arthur: shelving and the light-band wall are right; the project folder is in his hands, not on the desk; Angelika's "careless wave" became a hand on the desk papers; his face stays almost still (the beat holds).
4. 11.6-14 s side two-shot: Angelika left looking down, Arthur right with the folder; the wall carries diagonal light bands, no window in frame.

## Wan B (shots 5-8)

1. 0-3.6 s Angelika close: a flat dark teal wall behind her; she speaks, then looks into the lens with a slight smile (the beat asked for a blurted whisper and a step back).
2. 3.6-5.8 s Arthur close: window with blinds at the left, a desk phone; eyes down; clean, younger-looking face than the Seedance Arthur.
3. 5.8-8.9 s Arthur in profile at the desk, the window now behind him at the right, a black leather chair; he takes the sheet off the pile in front of him.
4. 8.9-12 s over-the-shoulder, Angelika's hair soft at the left; Arthur holds up the sheet, the twisting-tower drawing is faithful, he looks at the camera while he speaks; shelving and phone behind him.

## Speech (ASR)

Seedance: all four lines. Wan A: "Он и хотел, чтобы ты к нам присоединился, но тут из-за одного всем этим занят" (the two sentences recognisable). Wan B: "Я не в том смысле." and "Слушай, а это где-нибудь видела?" clean; "Да нормально." heard as "Где он нормально?". So Russian recorded takes bind and speak on Wan; word accuracy is close, not exact.

## Conclusions (provisional)

- Declared cut counts held; cut times drifted (late, and in A early).
- Room geometry did not hold across angles: see `wan3-film` `references/angles-and-geometry.md`.
- Props leave their place (folder in the hands, sheet taken from the desk).
- Close-ups with no background named get a blank wall; the gaze drifts to the lens.
- Faces are more photographic than Seedance's but drift between shots and read younger and cleaner; this is a model trait, not a prompt trait (the user's observation; one scene).
- The acting layer: the stillness beat (Arthur's face does not change) held in A shot 3; the whisper-and-step-back beat did not appear in B shot 1; the hand wave became a touch of the papers. Beats with a concrete frame-internal action transferred, beats that depend on a gesture across the frame edge or a posture change did not.
