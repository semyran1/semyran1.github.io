# Provenance — where every Wan 3.0 claim in this set comes from

Register for the whole `wan3-*` set (core, budget, film, sound, edit, stylized). Compiled
2026-10-14. Read this once before trusting any number: **the official Alibaba pages could not be
opened in the build session** (egress policy blocked `help.aliyun.com`, `alibabacloud.com`, YouTube,
Reddit, Hugging Face and most vendor sites; only a search tool and the Higgsfield MCP worked). So
"official" below means "seen verbatim in the creator handbook archive" or "quoted by a source that
quotes the page", never "read on the page". Re-check `[DOC-2]` and `[OPEN]` items against
`https://www.alibabacloud.com/help/en/model-studio/wan3-video-generation-prompt-guide` and
`.../wan3-video-generation-guide` the first time a session has network access.

## Marks

| Mark | Meaning | Weight |
|---|---|---|
| `[HF]` | Measured on Higgsfield 2026-10-14: `models_explore` catalog and `get_cost` preflights (plan Plus). Free to repeat. | Wins for platform parameters and prices |
| `[DOC]` | Alibaba text seen verbatim: the 64 prompts of the official Wan 3.0 creator handbook (read in full from the AtlasCloudAI archive, archived 2026-08-11 from Alibaba's handbook), and doc excerpts quoted verbatim in search results | Highest for prompt behaviour |
| `[DOC-2]` | Attributed to Alibaba's Model Studio docs by a secondary source; page not seen | High, re-check |
| `[FIELD]` | Third-party guides, reviews, API aggregators. Most of them sell Wan access: directional, never proof | Medium-low |
| `[CRAFT]` | Rule carried from the Seedance 2.5 set or from film craft; untested on Wan | Hypothesis |
| `[OPEN]` | Sources contradict each other, or one source only. Test before relying | Do not build on it |
| `[EMPIRICAL]` | Bought with a generation in this project. Three logged so far (C1 `Image N` binding, C10, C13) - `calibration.md` lists the experiments that create more | Outranks everything once logged; never bans a documented capability |

Evidence order: `[HF]` for parameters and prices > `[DOC]` > `[DOC-2]` > `[FIELD]` > `[CRAFT]`.
A logged `[EMPIRICAL]` result outranks all of them for this project.

## Sources actually read

1. **Official creator handbook, 64 prompts** ("verbatim" = verbatim as archived: English machine translations of the Chinese originals, eight entries cut short) ("verbatim" = verbatim as archived: English machine translations of the Chinese originals, eight entries cut short) (plus 17 X posts) - `github.com/AtlasCloudAI/awesome-wan-3.0-prompts`,
   `data/prompts.json`, license CC BY 4.0; handbook original is a DingTalk doc
   (`alidocs.dingtalk.com/i/nodes/qnYMoO1rWxrkmoj2IjExdZLBJ47Z3je9`). English texts are translations
   with residual Chinese in a few (the original is Chinese). Several dataset entries are cut short.
   `references/official-corpus.md` is built from them.
2. **Chinese statistics note** `docs/prompting-guide.zh-CN.md` in the same repo: counts over the 64
   (style 47%, consistency locks 44%, camera 31%, sound 23%, reference assignment 20%, aspect 19%,
   one-take 14%, shot+timecode 12%, negatives 6%, frame-level pacing 3%; median 268 Chinese
   characters, max 1758, 10 prompts over 800). Atlas's count, not Alibaba's.
3. **Higgsfield MCP** `models_explore` (`wan3_0`, `wan3_0_prime`, `wan2_7`) and 20+ `get_cost`
   preflights. Nothing was generated; no credits were spent.
4. **genmedia-labs/skills** `wan-3-0-prime-reference-to-video` (RunComfy-hosted Prime reference
   endpoint): reference caps, schema, "counted seconds" billing on RunComfy. `[FIELD]`.
5. The Seedance 2.5 set (core, film, coverage, acting-system, cinema-director-ru, skill-creator):
   the methodology - marks, reading maps, diff-edits, header line, style-pack contract, lint.

## Search-mediated (not opened): the claims they carry

| Claim | Source (as returned by search) | Mark |
|---|---|---|
| Public beta 2026-08-06; model id `wan3.0-video` on Model Studio; API-only, no open weights | Alibaba Model Studio guide, Morphic, Atlas ("No 4K, No Weights"); one blog (youart) claims open weights/4K - rejected | `[DOC-2]` / `[FIELD]` |
| 2-30 s, 30 fps, 480p/720p/1080p; no 4K | Model Studio guide, several vendors; Atlas counted 110 official clips: none above 1080p | `[DOC-2]` |
| Prompt formulas: Basic = entity+scene+motion; Advanced = +aesthetic control+stylization; Sound; Reference = reference identifier + action + scene + lines (opt) + BGM (opt); Multi-shot; Editing = target + action + "rest unchanged" | Model Studio prompt guide via Segmind, Magnific, Pixo, Oxen | `[DOC-2]` |
| Aesthetic control = light source, lighting environment, shot size, camera angle, lens, camera movement | quoted from the Model Studio guide | `[DOC]` |
| Each camera move is chosen for its meaning (push-in intimacy/tension, tracking beside the subject, orbit emphasis, fixed stillness); plain wording works (push in, pull out, orbit, handheld follow) | excerpt of the Model Studio guide quoted in search results | `[DOC]` |
| The guide asks for the camera treatment in every shot; an unnamed camera lets Wan cut or wander; say `fixed shot` for a still camera | LUVI, OpenArt, Wavespeed on the guide; not seen on the page | `[DOC-2]` / `[FIELD]` |
| Avoid naming real people, rapid scene changes within a clip, relying on rendered text | the family-wide English docs per a Japanese translator; the Wan 3.0 page has no such list | `[OPEN]` |
| Each camera move is chosen for its meaning (push-in intimacy/tension, tracking beside the subject, orbit emphasis, fixed stillness); plain wording works (push in, pull out, orbit, handheld follow) | excerpt of the Model Studio guide quoted in search results | `[DOC]` |
| The guide asks for the camera treatment in every shot; an unnamed camera lets Wan cut or wander; say `fixed shot` for a still camera | LUVI, OpenArt, Wavespeed on the guide; not seen on the page | `[DOC-2]` / `[FIELD]` |
| Avoid naming real people, rapid scene changes within a clip, relying on rendered text | the family-wide English docs per a Japanese translator; the Wan 3.0 page has no such list | `[OPEN]` |
| Sound: voice = line+emotion+tone+speed+timbre+accent; effect = source+action+ambient; music = score+style; negatives for sound ("No BGM, generate only ambient and action sounds") | Segmind quoting Alibaba; Model Studio excerpt | `[DOC-2]` / `[DOC]` |
| Dialogue pattern speaker + verb + colon + quote; voice reference attached by numbered audio; "lip sync" tag | Model Studio guide via search | `[DOC-2]` |
| References: 10 images, 5 videos (1-15 s each, 15 s total), 5 audio (15 s total); total 20 | RunComfy, Scenario, Oxen, Venice (third-party) | `[FIELD]` |
| Handbook "omni-reference" mode takes up to 20 assets incl. documents and web pages; references are numbered per type (Image n / Video n / Audio n) | the Atlas zh note on the handbook; Alibaba guide via secondary sources | `[DOC-2]` |
| Reference mode and first/last-frame mode cannot be combined | RunComfy, Pixeldojo, Scenario; **confirmed on Higgsfield 2026-10-14**: 422 "start_image/end_image cannot be combined with reference media" at submission | `[HF]` |
| Extension: input video + new output must total <= 30 s | Model Studio docs via search | `[DOC-2]` |
| No negative-prompt field; exclusions go into the prompt | Model Studio guide; several guides | `[DOC-2]` |
| `prompt_extend` default true in the API; "does not exist" per a Japanese translation of the English docs | contradictory | `[OPEN]`; Higgsfield exposes `enable_thinking` only |
| `enable_thinking`: slower, better adherence; required for document/link inputs | Picsart, Scenario | `[FIELD]` |
| Uncommanded cuts inside "continuous" shots; shot lists do not guarantee cuts (Atlas: 3 multi-shot prompts hit their declared shot count, 2 under-delivered, worst case asked 4 and got 2) | Atlas 110-clip count (vendor), Aristotto | `[FIELD]` |
| Weak spots: dialogue audio texture, in-frame text and small numbers, hands, dense crowds, lip-sync (mixed), long-scene drift, closing beat of 4-beat 30 s narratives dropped | reviews (buildfastwithai, pixmax, curiousrefuge, Atlas) | `[FIELD]` |
| Strong spots: camera commands behave "like a parameter", physics, long reference-heavy briefs, 30 s continuity | reviews, Atlas same-seed test (49 runs) | `[FIELD]` |
| Speech languages: not documented by the vendor; English and Mandarin most credible; Russian never named | Sentioscope, Aristotto | `[OPEN]` |
| Prompt length up to 20,000 characters; Chinese, English, Japanese accepted | RunComfy skill, a note.com guide | `[FIELD]` |
| Third-party prices (USD per second 480/720/1080: $0.035-0.07/0.07-0.14/0.14-0.28) | many | irrelevant here: `[HF]` credits replace them |

## Known contradictions kept visible

- Official handbook timecodes: five of the 64 prompts (008, 013, 023, 048, 049) use ranges that
  run far past any 30 s clip (`Shot 4 [90s-120s]`, six shots to `[150s-180s]`). Read as relative
  slots or translation residue; never copied (`official-corpus.md`).
- Atlas Cloud's Chinese note says Wan 3.0 is not yet on its platform; its English blog sells it.
  Vendor material is weighted accordingly.
- Prime vs Standard: speed "up to 7x" (Picsart), quality 8.8 vs 8.2 (MaxVideoAI) or "no published
  table" (llm-stats). No two sources agree; only `[HF]` prices are used.
