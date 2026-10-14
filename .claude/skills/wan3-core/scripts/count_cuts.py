"""Count hard cuts in a generated clip, so "the take stayed one shot" is a number.

    python count_cuts.py clip.mp4 [--expect 2] [--threshold 0.35] [--min-gap 0.4]

Uses ffmpeg's scene-change score (0..1) per frame. A cut is a frame whose score exceeds
--threshold; detections closer than --min-gap seconds are merged (a whip pan or a flash is one
event, not three). Prints each cut time and, with --expect N, a verdict against the number of cuts
the prompt asked for (shots - 1 for a hard-cut montage, 0 for a one-take).

Limits worth knowing: a fast whip pan, a lightning flash or a very hard match-cut can be reported as
a cut (or missed). Look at the frame just after each reported time before blaming the model;
lower --threshold to catch soft dissolves (they score low), raise it to ignore camera whips.
Needs ffmpeg and ffprobe on PATH. Exit code 0 always.
"""

import argparse
import re
import subprocess
import sys


def probe_duration(path):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", path],
        capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--expect", type=int, default=None, help="cuts the prompt asked for")
    ap.add_argument("--threshold", type=float, default=0.35)
    ap.add_argument("--min-gap", type=float, default=0.4)
    a = ap.parse_args()

    cmd = ["ffmpeg", "-hide_banner", "-nostats", "-i", a.path,
           "-vf", f"select='gt(scene,{a.threshold})',showinfo", "-an", "-f", "null", "-"]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0 and "showinfo" not in r.stderr:
        print("ffmpeg failed:\n" + r.stderr[-600:])
        return
    times = [float(m.group(1)) for m in re.finditer(r"pts_time:([0-9.]+)", r.stderr)]
    merged = []
    for t in times:
        if not merged or t - merged[-1] >= a.min_gap:
            merged.append(t)
    dur = probe_duration(a.path)
    print(f"File: {a.path} | duration: {dur:.2f}s" if dur else f"File: {a.path}")
    print(f"Cuts detected (threshold {a.threshold}, min gap {a.min_gap}s): {len(merged)}")
    for t in merged:
        print(f"  {t:7.2f}s")
    if a.expect is not None:
        if len(merged) == a.expect:
            print(f"Verdict: matches the {a.expect} requested cut(s).")
        elif len(merged) < a.expect:
            print(f"Verdict: UNDER-CUT - {a.expect} requested, {len(merged)} found "
                  "(beats may have merged; check the dropped shot).")
        else:
            print(f"Verdict: OVER-CUT - {a.expect} requested, {len(merged)} found "
                  "(uncommanded cuts, or whip pans / flashes scored as cuts - inspect the frames).")


if __name__ == "__main__":
    main()
