"""Mechanical pre-send checks for a Wan 3.0 prompt.

    python prompt_lint.py prompt.txt --duration 15 --res 720p [--model wan3_0|wan3_0_prime]
                          [--images 2 --videos 1 --audios 1] [--mode T2V|I2V|FLF|REF|EDIT|EXT]
    python prompt_lint.py - < prompt.txt

Counts and structure a model tends to get wrong from memory. It prints the header counts
(`Words: N | Negatives: N`), the price line, and a list of warnings. A warning is a question to
answer, not an automatic failure: some negatives are requested, some timecodes are deliberate.

Checks
  words        word and character count (diagnostic; the hard limit is 20,000 characters)
  cost         credits for model x resolution x duration (Higgsfield rates measured 2026-10-14;
               the live `get_cost` call is the authority - this is the offline estimate)
  negatives    every negative word with its line, so each can be justified or removed (quoted speech and
               'No cut.' boundary statements are not counted; one prohibition can yield several words)
  timeline     ranges start at 0, are contiguous, end at --duration, never exceed 30 s;
               shot-label count vs range count; shots per second (over-cutting)
  camera       every shot names a camera treatment (fixed, push, pan, track, orbit ...)
  cuts         a continuous take repeats its no-cut clause; a multi-shot prompt declares what
               happens at the boundaries
  references   tags (Image N / @ImageN / Video N / Audio N) have a role line, indices exist,
               one style is used, supplied assets are all addressed, mode conflicts
  sound        spoken lines are attributed; words per second against the 2.5 w/s pace;
               a sound decision is present; <> used both for effects and for names
  header       the length stated in the opening sentence ('30 seconds', '15-second') equals --duration
  pacing       spoken words per shot against the shot length (about 2.5 words/second)
  ledger       lines starting 'Segment' / 'Dialogue ledger' are NOT read as shots or time ranges
  language     non-ASCII (mixed-language) text, fluff words, emotion words, pronouns in shots
Exit code: 0 always (it informs, the writer decides).
"""

import argparse
import re
import sys

RATES = {  # credits per second, Higgsfield, measured with get_cost on 2026-10-14
    "wan3_0": {"480p": 1.0, "720p": 1.75, "1080p": 3.5},
    "wan3_0_prime": {"480p": 1.5, "720p": 3.0, "1080p": 6.0},
}

NEG = re.compile(
    r"\b(no|not|never|none|nothing|nobody|without|avoid|prohibit(?:ed|s)?|forbid(?:den)?|"
    r"don't|doesn't|isn't|aren't|won't|cannot|can't|do not|does not|must not|should not|zero (?:voiceover|music|dialogue))\b",
    re.I)
# a time range needs a unit on its end: [0-3s], 0s-30s, 4-9 seconds, (1.48-3s)
RANGE = re.compile(
    r"(?<![\d.])(\d+(?:\.\d+)?)\s*(?:s|sec|seconds)?\s*[-–—~]\s*(\d+(?:\.\d+)?)\s*"
    r"(?:s\b|sec\b|seconds\b)", re.I)
SHOT_LABEL = re.compile(r"\bShot\s+(\d+)\b", re.I)
REF = re.compile(r"(@)?\b(Image|Video|Audio)\s?(\d+)\b", re.I)
ROLE = re.compile(
    r"\b(is|are|defines?|serves?|references?|sole|only|supplies|provides?|voice|timbre|tone of voice|"
    r"first frame|last frame|storyboard|style|locked|lock|maps? to|from|replace[sd]?|wears?|using|"
    r"based on|strictly|keyframe|plate|extract|remove|add|edit|extend|swap|reshape|transform|insert)\b", re.I)
EXCL = re.compile(r"\b(do not use|don't use|only the|only its|sole|not the|without the people|"
                  r"do not replace|not use)\b", re.I)
CAMERA = re.compile(
    r"\b(camera|fixed|static|locked[- ]off|tripod|push[- ]?in|pull[- ]?(?:back|out)|pans?|panning|"
    r"tilt(?:s|ing)?|track(?:s|ing)?|orbit(?:s|ing)?|dolly|zoom(?:s|ing)?|handheld|crane|aerial|"
    r"drone|follow(?:s|ing)?|whip|close-up|medium shot|wide shot|long shot|full shot|establishing|"
    r"over-the-shoulder|overhead|top-down|low[- ]angle|high[- ]angle|POV|fpv|freeze|slow motion)\b", re.I)
NOCUT = re.compile(r"\b(no (?:hard )?cuts?|do not cut|without (?:any )?cuts?|no editing transitions|"
                   r"no abrupt scene transitions|uncut|unbroken)\b", re.I)
CONT = re.compile(r"\b(one[- ]take|one continuous|single[- ]shot|continuous shot|long take|"
                  r"single continuous|seamless)\b", re.I)
BOUNDARY = re.compile(r"\b(cut|cuts|jump cut|hard cut|transition|dissolve|fade|match cut|seamless)\b", re.I)
SPEECH = re.compile(r"\b(says?|said|speaks?|spoke|asks?|replies|responds?|whispers?|shouts?|"
                    r"recites?|narrates?|voiceover|voice-over|V\.O\.|monologue|lip sync|dialogue)\b|:\s*$",
                    re.I)
SOUND_WORDS = re.compile(r"\b(silence|silent|no dialogue|no music|no voiceover|ambient|ambience|music|"
                         r"bgm|score|voice|voiceover|dialogue|sound|sfx|soundtrack|audio)\b", re.I)
PRON = re.compile(r"\b(he|she|they|him|her|his|hers|them|their)\b", re.I)
FLUFF = re.compile(r"\b(cinematic|epic|beautiful|stunning|masterpiece|breathtaking|amazing|8k|4k|"
                   r"ultra[- ]?hd|award[- ]winning|premium)\b", re.I)
EMOTION = re.compile(r"\b(anxious|nervous|sad|angry|happy|worried|scared|afraid|excited|lonely|"
                     r"melancholic|joyful|furious|tense)\b", re.I)
HEAD_LEN = re.compile(r"\b(\d{1,2})[- ]?(?:seconds?|secs?|s)\b", re.I)
LEDGER = re.compile(r"^\s*(?:Segment\b|Dialogue ledger)", re.I)
EDIT_VERB = re.compile(r"\b(edit|remove|add|extend|replace|swap|reshape|transform|change|insert|wears?)\b", re.I)


def words_of(text):
    return len(re.findall(r"[A-Za-z0-9@'’\-]+", text))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--duration", type=int, default=None, help="generation length in seconds (-1 = smart)")
    ap.add_argument("--res", default=None, choices=["480p", "720p", "1080p"])
    ap.add_argument("--model", default="wan3_0", choices=list(RATES))
    ap.add_argument("--images", type=int, default=0)
    ap.add_argument("--videos", type=int, default=0)
    ap.add_argument("--audios", type=int, default=0)
    ap.add_argument("--mode", default=None, choices=["T2V", "I2V", "FLF", "REF", "EDIT", "EXT"])
    ap.add_argument("--no-audio", action="store_true", help="generate_audio is off")
    a = ap.parse_args()

    text = sys.stdin.read() if a.path == "-" else open(a.path, encoding="utf-8").read()
    lines = text.splitlines()
    warns = []

    nwords = words_of(text)
    first = text.strip()[:120]
    is_edit = a.mode in ("EDIT", "EXT") or bool(
        re.search(r"\b[Vv]ideo ?\d|@Video", text) and EDIT_VERB.search(first)
        or re.match(r"\s*(edit|remove|add|extend|replace|swap|reshape|transform|reference the video)\b", text, re.I))
    if len(text) > 20000:
        warns.append(f"length: {len(text)} characters exceeds the 20,000-character prompt limit")

    # ---- negatives
    negs = []
    for i, ln in enumerate(lines, 1):
        scan = re.sub(r"[\"\u201c][^\"\u201d]*[\"\u201d]", " ", ln)   # quoted speech is not a prohibition
        scan = NOCUT.sub(" ", scan)                                      # 'No cut.' is a boundary statement
        for m in NEG.finditer(scan):
            negs.append((i, m.group(0), ln.strip()[:90]))

    # ---- cost
    cost_line = None
    if a.duration is not None and a.res:
        secs = 10 if a.duration == -1 else a.duration
        if a.duration == -1:
            warns.append("duration: -1 (smart duration) is billed as 10 s whatever length comes back")
        if secs and not (2 <= secs <= 30):
            warns.append(f"duration: {secs}s is outside 2-30")
        rate = RATES[a.model][a.res]
        cost_line = f"Cost: {rate * secs:g} cr ({a.model} {a.res} {secs}s x {rate:g}/s; confirm with get_cost)"

    # ---- timeline
    spans = []
    for i, ln in enumerate(lines, 1):
        if LEDGER.match(ln):
            continue
        for m in RANGE.finditer(ln):
            s, e = float(m.group(1)), float(m.group(2))
            if e > s:
                spans.append((i, s, e))
    spans.sort(key=lambda x: (x[1], x[0]))
    # drop spans nested inside an earlier line's span family (e.g. "6s-10s" inside prose is rare)
    if spans:
        if spans[0][1] != 0:
            warns.append(f"timeline: first range starts at {spans[0][1]:g}s, not 0")
        for (l1, s1, e1), (l2, s2, e2) in zip(spans, spans[1:]):
            if s2 > e1:
                warns.append(f"timeline: gap {e1:g}-{s2:g}s (lines {l1}->{l2}) - the model improvises it")
            elif s2 < e1:
                warns.append(f"timeline: overlap at {s2:g}s (lines {l1}->{l2})")
        last = spans[-1][2]
        if last > 30:
            warns.append(f"timeline: a range ends at {last:g}s - Wan's maximum is 30 s "
                         "(official handbook examples with this are relative slots; do not copy)")
        if a.duration and a.duration > 0 and last != a.duration:
            warns.append(f"timeline: last range ends at {last:g}s, generation length is {a.duration}s")
        if any(("." in str(x)) for x in []):
            pass
    shot_labels = sorted({int(m.group(1)) for i, ln in enumerate(lines, 1) if not LEDGER.match(ln)
                          for m in SHOT_LABEL.finditer(ln)})
    nshots = max(len(shot_labels), len(spans))
    if shot_labels and spans and len(shot_labels) != len(spans):
        warns.append(f"timeline: {len(shot_labels)} 'Shot N' labels but {len(spans)} time ranges")
    if a.duration and a.duration > 0 and nshots and a.duration / nshots < 2:
        warns.append(f"timeline: {nshots} shots in {a.duration}s ({a.duration / nshots:.1f}s each) - "
                     "short ranges drop beats or cut excessively; the 30 s ceiling carries 3-4 beats")

    # ---- shot segments (for camera / pronoun / speech checks)
    seg_starts = sorted({i for i, *_ in spans} | {i for i, ln in enumerate(lines, 1)
                                                   if SHOT_LABEL.search(ln) and not LEDGER.match(ln)})
    segments = []
    for k, st in enumerate(seg_starts):
        en = (seg_starts[k + 1] - 1) if k + 1 < len(seg_starts) else len(lines)
        for j in range(st, en):          # a shot ends at the first blank line after its start
            if not lines[j].strip():
                en = j
                break
        segments.append((st, en, " ".join(lines[st - 1:en])))

    # ---- camera per shot
    if is_edit:
        pass
    elif segments:
        for st, en, seg in segments:
            if not CAMERA.search(seg):
                warns.append(f"camera: shot at line {st} names no camera treatment "
                             "(even 'fixed shot' - unnamed camera lets Wan cut or wander)")
    elif not is_edit and not CAMERA.search(text) and nwords > 25:
        warns.append("camera: no camera treatment named")

    # ---- cut state
    nocut_hits = len(NOCUT.findall(text))
    if is_edit:
        pass
    elif nshots > 1:
        if CONT.search(text) and nocut_hits < nshots - 1:
            warns.append(f"cuts: continuous take declared but the no-cut clause appears {nocut_hits}x "
                         f"for {nshots} shots - repeat it at each camera move / shot")
        if not BOUNDARY.search(text):
            warns.append("cuts: several shots but no boundary state declared (cut / hard cut / "
                         "seamless / no cut) - Wan decides for itself")
    elif nshots <= 1 and a.duration and a.duration >= 10 and not NOCUT.search(text) and not CONT.search(text):
        warns.append("cuts: a >=10 s single-timeline prompt without a one-take or no-cut statement may be "
                     "cut by the model")

    # ---- references
    used = {}
    for i, ln in enumerate(lines, 1):
        for m in REF.finditer(ln):
            key = (m.group(2).capitalize(), int(m.group(3)))
            used.setdefault(key, []).append((i, bool(m.group(1))))
    if used:
        styles = {at for v in used.values() for _, at in v}
        if len(styles) > 1:
            warns.append("references: mixes '@Image1' and 'Image 1' styles - pick one")
        for (typ, n), where in sorted(used.items()):
            role = any(ROLE.search(lines[i - 1]) for i, _ in where)
            if not role:
                warns.append(f"references: {typ} {n} (lines {[i for i, _ in where][:5]}) has no role line")
            cap = {"Image": a.images, "Video": a.videos, "Audio": a.audios}[typ]
            if (a.images or a.videos or a.audios) and n > cap:
                warns.append(f"references: {typ} {n} is cited but only {cap} {typ.lower()}(s) supplied")
        for typ, cap in (("Image", a.images), ("Video", a.videos), ("Audio", a.audios)):
            for n in range(1, cap + 1):
                if (typ, n) not in used:
                    warns.append(f"references: {typ} {n} supplied but never addressed in the prompt "
                                 "(unaddressed assets are guesses; videos may also be billed)")
        if not is_edit and not EXCL.search(text):
            warns.append("references: no exclusion language ('only the face', 'do not use the people') - "
                         "say what NOT to take from each asset")
        if a.mode == "FLF":
            warns.append("references: FLF mode with reference tags - Higgsfield rejects start_image/end_image "
                         "together with reference media (422, nothing charged; measured 2026-10-14)")
    elif a.images or a.videos or a.audios:
        warns.append("references: assets supplied but the prompt cites none of them")
    if a.mode == "EDIT" and not a.videos:
        warns.append("mode: EDIT without a source video")

    # ---- sound
    if not is_edit and not a.no_audio and not SOUND_WORDS.search(text):
        warns.append("sound: audio is on but the prompt makes no sound decision - the model fills the track "
                     "(say dialogue / effects / music, or 'no music, ambient only')")
    quotes = [q for q in re.findall(r"[\"“]([^\"”]{3,})[\"”]", text)]
    spoken_words = sum(words_of(q) for q in quotes if len(q.split()) >= 2)
    if quotes:
        for m in re.finditer(r"[\"“]([^\"”]{3,})[\"”]", text):
            if len(m.group(1).split()) < 2:
                continue
            before = text[max(0, m.start() - 90):m.start()]
            if not SPEECH.search(before):
                warns.append(f"sound: quoted text \"{m.group(1)[:40]}\" has no speaker/speech verb nearby "
                             "(is it dialogue, on-screen text, or a title?)")
        if a.duration and a.duration > 0 and spoken_words / a.duration > 3.0:
            warns.append(f"sound: {spoken_words} spoken words in {a.duration}s = "
                         f"{spoken_words / a.duration:.1f} w/s; the handbook's pace is about 2.5 w/s")
    span_by_line = {i: (s0, e0) for i, s0, e0 in spans}
    for st, en, seg in segments:
        if st in span_by_line:
            s0, e0 = span_by_line[st]
            q = sum(words_of(x) for x in re.findall(r"[\"\u201c]([^\"\u201d]{3,})[\"\u201d]", seg) if len(x.split()) >= 2)
            if q and e0 > s0 and q / (e0 - s0) > 3.0:
                warns.append(f"sound: shot at line {st} has {q} spoken words in {e0 - s0:g}s "
                             f"({q / (e0 - s0):.1f} w/s) - need about {q / 2.5 + 1:.0f}s (words / 2.5 + 1)")
    sfx = re.findall(r"<([^<>]*\s[^<>]*)>", text)
    names = re.findall(r"<([A-Z][\w\-]*)>", text)
    if sfx and names:
        warns.append(f"brackets: <> marks sound effects and also names ({', '.join(sorted(set(names))[:4])})")

    # ---- header length vs --duration
    head = " ".join(lines[:3])[:400]
    hm = HEAD_LEN.search(head)
    if hm and a.duration and a.duration > 0 and int(hm.group(1)) != a.duration:
        warns.append(f"header: opening sentence says {hm.group(1)} s but --duration is {a.duration}")

    # ---- language / style hygiene
    nonascii = len(re.findall(r"[一-鿿]", text))
    if nonascii:
        warns.append(f"language: {nonascii} CJK characters in the prompt - mixed-language prompt "
                     "(translation residue in handbook copies?)")
    if re.search(r"[Ѐ-ӿ]", text):
        warns.append("language: Cyrillic in the model-facing prompt - write the prompt in English "
                     "(spoken Russian lines are a deliberate exception: calibration C4)")
    fl = FLUFF.findall(text)
    if len(fl) > 3:
        warns.append(f"style: {len(fl)} fluff words ({', '.join(sorted(set(w.lower() for w in fl))[:5])}) - "
                     "replace with a shot type, a light source and one camera move")
    em = EMOTION.findall(text)
    if em:
        warns.append(f"acting: emotion words ({', '.join(sorted(set(w.lower() for w in em))[:5])}) - "
                     "write the visible behaviour instead (gaze, hands, breath)")
    for st, en, seg in segments:
        p = PRON.findall(seg)
        if len(p) >= 5:
            warns.append(f"pronouns: shot at line {st} uses {len(p)} pronouns - name who acts")

    # ---- output
    print(f"Words: {nwords} | Negatives: {len(negs)}" + (f" | {cost_line}" if cost_line else ""))
    if negs:
        print("\nNegative forms (name the default each fights, or remove):")
        for i, w, ln in negs[:25]:
            print(f"  L{i:<4} {w!r:12} {ln}")
        if len(negs) > 25:
            print(f"  ... {len(negs) - 25} more")
    warns = list(dict.fromkeys(warns))
    print("\nWarnings:" if warns else "\nWarnings: none")
    for w in warns:
        print("  - " + w)


if __name__ == "__main__":
    main()
