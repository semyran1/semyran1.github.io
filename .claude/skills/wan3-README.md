# Wan 3.0 skill set

Six skills for Alibaba **Wan 3.0 / Wan 3.0 Prime** video on Higgsfield, built 2026-10-14 the way the
Seedance 2.5 set was built: documentation first, craft second, every claim marked with where it
came from, and a lint script that checks what a model gets wrong from memory.

| Skill | Job | Load when |
|---|---|---|
| `wan3-core` | prompt grammar, mode router (T2V / I2V / FLF / REF / EDIT), references, timeline and cuts, constraints, checks, lint, cut counter, the official handbook (64 prompts, verbatim) | every Wan 3 task |
| `wan3-budget` | measured Higgsfield prices, draft ladder, re-roll economics, `get_cost` rule, spending protocol, cost calculator | before any paid generation |
| `wan3-film` | camera named per shot, light, optics, stock, aspect limits, dramatic functions, director packs (Fincher, Villeneuve, Wong Kar-wai, Wes Anderson) | the look matters |
| `wan3-sound` | dialogue and lip-sync, voice references, effects, music, silence, the 2+ speaker ledger, Russian-speech fallback | anything is heard |
| `wan3-edit` | edit, replace, remove, restyle, relight, change a line, extend, chain past 30 s | a clip already exists |
| `wan3-stylized` | anime, clay, plush, ink, MG, 3D toon, hybrids, the style bible | the look is not photographic |

Order of reading in a session: `wan3-core` -> `wan3-budget` -> the rest as the brief demands. Each
`SKILL.md` has a reading map to its references; references are short and read whole.

## What is known and what is not

The official Alibaba pages could not be opened while this set was built (the session's network
policy blocked them). What stands on solid ground: the 64 prompts of the official creator handbook
(read in full), Higgsfield's catalog and 20+ `get_cost` readings, and the Seedance set's craft.
What stands on third-party reports is marked `[FIELD]`; contradictions are `[OPEN]`; ported craft is
`[CRAFT]`. **No generation has been run yet**, so there is no `[EMPIRICAL]` mark anywhere.
`wan3-core/references/calibration.md` lists the experiments that create them: the first six cost
about 30 credits. `wan3-core/references/provenance.md` is the full source register.

## Install

- **Claude Code in this repository**: the skills live in `.claude/skills/` and load automatically.
- **claude.ai (the same account that holds the Seedance skills)**: zip each skill folder (folder at
  the top level of the zip) and upload it under Settings -> Capabilities -> Skills.
  `python skill-creator/scripts/package_skill.py .claude/skills/wan3-core <outdir>` produces the
  package.

## Scripts

```bash
python .claude/skills/wan3-core/scripts/prompt_lint.py prompt.txt --duration 15 --res 720p --images 2
python .claude/skills/wan3-core/scripts/count_cuts.py clip.mp4 --expect 2      # needs ffmpeg
python .claude/skills/wan3-budget/scripts/wan3_cost.py table
python .claude/skills/wan3-budget/scripts/wan3_cost.py draft --final-res 720p --final-dur 10 --p-direct 0.3 --p-after-draft 0.55
```

## Updating

When a generation teaches something: log it in `calibration.md`, change the mark of the rule it
touches, and, as in the Seedance set, change one rule per pass and say which. When Higgsfield
changes a price, re-run `get_cost` and update `RATES` in `prompt_lint.py` and `wan3_cost.py`
together (two copies on purpose: the skills install separately).
