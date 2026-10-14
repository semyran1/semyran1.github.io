"""Offline Wan 3.0 price arithmetic for Higgsfield credits.

    python wan3_cost.py price  --res 720p --dur 10 [--model wan3_0|wan3_0_prime] [--count 1]
    python wan3_cost.py table
    python wan3_cost.py expected --res 720p --dur 10 --p 0.35
    python wan3_cost.py draft  --final-res 720p --final-dur 10 --p-direct 0.30 \
                               --draft-res 480p --draft-dur 4 --draft-n 1 --p-after-draft 0.55
    python wan3_cost.py plan   --budget 150 --res 720p --dur 10 --p 0.4

Rates are credits per second measured with Higgsfield `get_cost` on 2026-10-14 (plan Plus):
  wan3_0       480p 1.00   720p 1.75   1080p 3.50
  wan3_0_prime 480p 1.50   720p 3.00   1080p 6.00
Price is linear in duration; `duration = -1` (smart) is billed as 10 s; audio and thinking did not
change the preflight. Reference-video seconds MAY be billed on top (unmeasured on Higgsfield): always
confirm with `get_cost` with the real media attached. This script is the offline estimate; the live
`get_cost` call is the authority. Re-measure when Higgsfield changes prices.
"""

import argparse
import math

RATES = {
    "wan3_0": {"480p": 1.0, "720p": 1.75, "1080p": 3.5},
    "wan3_0_prime": {"480p": 1.5, "720p": 3.0, "1080p": 6.0},
}


def price(model, res, dur):
    secs = 10 if dur == -1 else dur
    return RATES[model][res] * secs


def cmd_price(a):
    one = price(a.model, a.res, a.dur)
    note = " (smart duration is billed as 10 s)" if a.dur == -1 else ""
    print(f"{a.model} {a.res} {a.dur}s{note}: {one:g} cr per clip")
    if a.count > 1:
        print(f"x {a.count} variants = {one * a.count:g} cr "
              "(get_cost with count>1 returned the single-clip price: multiply yourself)")


def cmd_table(a):
    durs = [2, 3, 5, 8, 10, 15, 20, 30]
    for model in RATES:
        print(f"\n{model} (credits)")
        print("  sec  " + "  ".join(f"{r:>7}" for r in ("480p", "720p", "1080p")))
        for d in durs:
            print(f"  {d:>3}  " + "  ".join(f"{price(model, r, d):7g}" for r in ("480p", "720p", "1080p")))
    print("\nRatios: 720p = 1.75x 480p; 1080p = 3.5x 480p = 2x 720p; Prime = 1.5x (480p) / 1.71x (720p, 1080p).")


def cmd_expected(a):
    one = price(a.model, a.res, a.dur)
    if not 0 < a.p <= 1:
        raise SystemExit("--p must be in (0, 1]")
    tries = 1 / a.p
    print(f"One attempt: {one:g} cr | acceptance p={a.p:g} -> {tries:.1f} attempts per accepted clip "
          f"-> expected {one * tries:g} cr per usable clip")
    n90 = math.ceil(math.log(0.1) / math.log(1 - a.p)) if a.p < 1 else 1
    print(f"Attempts to be 90% sure of at least one accepted clip: {n90} ({one * n90:g} cr)")


def cmd_draft(a):
    final = price(a.model, a.final_res, a.final_dur)
    draft = price(a.model, a.draft_res, a.draft_dur) * a.draft_n
    direct = final / a.p_direct
    staged = draft + final / a.p_after_draft
    print(f"Final attempt: {final:g} cr | draft pass: {draft:g} cr ({a.draft_n} x {a.draft_res} {a.draft_dur}s)")
    print(f"Direct (p={a.p_direct:g}): expected {direct:g} cr per usable final")
    print(f"Draft first (p={a.p_after_draft:g} after draft): expected {staged:g} cr per usable final")
    if staged < direct:
        print(f"-> draft first saves {direct - staged:g} cr ({(1 - staged / direct) * 100:.0f}%)")
    else:
        print(f"-> draft first costs {staged - direct:g} cr MORE: it must lift acceptance above the "
              "direct rate by more than its own price to pay off (try --p-after-draft higher, "
              "a cheaper/shorter draft, or skip the draft)")
    print("Remember: no seed on Higgsfield - the draft validates the prompt, not the take.")


def cmd_plan(a):
    one = price(a.model, a.res, a.dur)
    clips = int(a.budget // one)
    usable = clips * a.p
    print(f"Budget {a.budget:g} cr / {one:g} cr per attempt = {clips} attempts "
          f"-> about {usable:.1f} accepted clips at p={a.p:g}")
    print(f"Break-even for a 3-clip sequence: {3 / a.p:.1f} attempts = {3 / a.p * one:g} cr")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(p, final=False):
        p.add_argument("--model", default="wan3_0", choices=list(RATES))
        if not final:
            p.add_argument("--res", default="720p", choices=["480p", "720p", "1080p"])
            p.add_argument("--dur", type=int, default=5)

    p = sub.add_parser("price"); common(p); p.add_argument("--count", type=int, default=1); p.set_defaults(f=cmd_price)
    p = sub.add_parser("table"); p.set_defaults(f=cmd_table)
    p = sub.add_parser("expected"); common(p); p.add_argument("--p", type=float, required=True); p.set_defaults(f=cmd_expected)
    p = sub.add_parser("draft"); common(p, True)
    p.add_argument("--final-res", default="720p"); p.add_argument("--final-dur", type=int, default=10)
    p.add_argument("--p-direct", type=float, required=True)
    p.add_argument("--draft-res", default="480p"); p.add_argument("--draft-dur", type=int, default=4)
    p.add_argument("--draft-n", type=int, default=1); p.add_argument("--p-after-draft", type=float, required=True)
    p.set_defaults(f=cmd_draft)
    p = sub.add_parser("plan"); common(p); p.add_argument("--budget", type=float, required=True)
    p.add_argument("--p", type=float, default=0.4); p.set_defaults(f=cmd_plan)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
