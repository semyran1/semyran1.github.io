# Wan 3.0 creator handbook - the 64 official prompts, verbatim

Source: Alibaba's Wan 3.0 creator handbook (DingTalk doc archived 2026-08-11), as republished in
`AtlasCloudAI/awesome-wan-3.0-prompts` (`data/prompts.json`, licence CC BY 4.0, attribution:
Atlas Cloud / Wan (Alibaba)). English texts are translations of Chinese originals: a few keep
Chinese fragments, and several entries are **cut short in the archive** (e.g. 005, 007, 016, 017,
025, 027, 028, 038 end mid-text). Timecodes in 008, 013, 023, 048, 049 exceed 30 s and must not be
copied. Reference images were not published with the handbook: prompts that cite `@Image1` need
your own assets. The seventeen X posts of the archive are omitted (short teasers, no craft).

How to use: grep for a technique (`grep -n "No cut\|Do not cut" handbook-prompts.md`), read the
whole prompt around the hit (R1), and imitate the structure, not the content. Analysis:
`official-corpus.md`.

## Index

| Id | Category | Title | Words |
|---|---|---|---|
| 001 | Character Performance | Graduation Day Worry | 120 |
| 002 | Cinematic Lighting & Color | Desperate Hospital Chase In Cold Green Tint | 138 |
| 003 | Camera Movement & One-Take | One-Take Actor's Emotional Rollercoaster In A Studio | 919 |
| 004 | Camera Movement & One-Take | West Coast Street Fantasy One-Take Shopping Cart Ride | 543 |
| 005 | Stylized & Non-Real | Biomechanical Soldier In Post-Apocalyptic Battle | 127 |
| 006 | Cinematic Lighting & Color | Monster Emerges From Stormy Sea In Epic Disaster Scene | 493 |
| 007 | Stylized & Non-Real | Surreal Gas Station Refueling With A Horse | 172 |
| 008 | Multi-Shot Storytelling | Night Lake Encounter With Giant Transparent Plant | 339 |
| 009 | Character Performance | Lonely Girl's Dramatic Leap Over Cliff | 303 |
| 010 | Stylized & Non-Real | Struggling Boxer In Training Montage | 49 |
| 011 | Character Performance | Dark Fantasy Villain Monologue With Cosmic Power | 223 |
| 012 | Stylized & Non-Real | Alien Abduction In A Cold-Toned Farm Painting | 47 |
| 013 | Multi-Shot Storytelling | Rainy Station Farewell With Emotional Exchange | 196 |
| 014 | Reference-Driven Generation | Static Frame Chinese Hair Ornament Showcase | 163 |
| 015 | Audio-Synced Dialogue | Gym Conversation Between Two Friends | 127 |
| 016 | VFX & Transitions | High-Speed Miniature Fairy Chase With Dragonfly Motion | 137 |
| 017 | Multi-Shot Storytelling | Symmetrical Hotel Chase With Profile Cross | 193 |
| 018 | Reference-Driven Generation | Character-Consistent Scene Generation With Reference Images | 179 |
| 019 | Commercial & Product | Material Design Product Launch With Paper Craft | 186 |
| 020 | Commercial & Product | Lip Gloss Model Swatch Video | 21 |
| 021 | Character Performance | Tough Bartender Finds Stray Kitten In Rain | 176 |
| 022 | Reference-Driven Generation | Clay Fox's Autumn Journey Through Miniature Town | 163 |
| 023 | Commercial & Product | Fashion Showcase In A Vintage European Cafe Setting | 193 |
| 024 | Multi-Shot Storytelling | High-Contrast Black-White K-Pop Group Dance Sequence | 678 |
| 025 | Stylized & Non-Real | Fleeing Stuffed Animals In A Plush Cosmic Chase | 297 |
| 026 | Camera Movement & One-Take | Dunhuang Dancer In Golden Light With Dynamic Camera | 408 |
| 027 | Stylized & Non-Real | High-Saturation Summer Street Fashion Short | 362 |
| 028 | Stylized & Non-Real | Low-Light POV With Hand-Drawn Motion Graphics | 662 |
| 029 | VFX & Transitions | Removing Pool Floats and Art Supplies from Scene | 65 |
| 030 | VFX & Transitions | Seamless Object Insertion With Consistent Lighting | 62 |
| 031 | VFX & Transitions | Seamless Object Removal And Background Inpainting | 27 |
| 032 | Character Performance | Character Aging And Wardrobe Transformation In Static Scene | 63 |
| 033 | VFX & Transitions | Foreground Ship Scaling With Detail Enhancement | 46 |
| 034 | Reference-Driven Generation | Hat Removal With Natural Hairstyle Preservation | 26 |
| 035 | Multi-Shot Storytelling | Child Opens Door To Magical Gothic Alley | 580 |
| 036 | Multi-Shot Storytelling | Triple Character Game PV With Elemental Skills | 611 |
| 037 | Multi-Shot Storytelling | Dual Heroine Fashion Film With Jump Cuts | 393 |
| 038 | Stylized & Non-Real | Stylized Urban Chase With Motion Graphics And Dynamic Lighting | 346 |
| 039 | Commercial & Product | Premium Snack Packaging Showcase With Warm Lifestyle Tone | 188 |
| 040 | Reference-Driven Generation | Character Substitution In Skateboarding Scene | 39 |
| 041 | Reference-Driven Generation | Coffee Cup On Rooftop Table With Referenced Camera Moves | 20 |
| 042 | Reference-Driven Generation | Reference-Driven Energy Effect And Motion | 19 |
| 043 | Audio-Synced Dialogue | Idol Dance In Modern Kitchen With Audio Sync | 126 |
| 044 | Reference-Driven Generation | Character Replacement with Emotional Phone Call | 181 |
| 045 | Multi-Shot Storytelling | Warm Diary of a Golden Retriever's First Year | 374 |
| 046 | Commercial & Product | Morning Skincare Ritual Showcasing Natural Beauty | 95 |
| 047 | Commercial & Product | Animated Data Dashboard With Sound Design | 381 |
| 048 | Creative Fun | Quantum Mechanics Explained Through Fun Animation | 171 |
| 049 | Chinese Classical & Literary | Who Is Wang Wei? An Animated Introduction For Kids | 257 |
| 050 | VFX & Transitions | Adding A Semi-Buried Rock To A Beach Scene | 37 |
| 051 | Reference-Driven Generation | Gender-Swapped Skateboarder With Preserved Motion | 48 |
| 052 | VFX & Transitions | Seamless Eyewear Removal With Natural Eye Makeup | 28 |
| 053 | Cinematic Lighting & Color | Soft Three-Point Lighting For Natural Skin Tones | 82 |
| 054 | VFX & Transitions | Man And Ostrich Swap Positions While Walking | 57 |
| 055 | Stylized & Non-Real | Transforming Video Into Claymation Style | 11 |
| 056 | Audio-Synced Dialogue | Dialogue Replacement In A Video Scene | 16 |
| 057 | Reference-Driven Generation | Character Wardrobe And Accessory Replacement | 76 |
| 058 | Character Performance | Man Plays Guitar In A Spontaneous Performance | 21 |
| 059 | Multi-Shot Storytelling | Teahouse Negotiation With Extended Dialogue And Period Detail | 283 |
| 060 | Multi-Shot Storytelling | Waltz Opening At A Grand 19th Century Ball | 242 |
| 061 | Camera Movement & One-Take | Girl Approaches Camera In Snowy Forest | 112 |
| 062 | Stylized & Non-Real | Ink-Wash Duel In Misty Bamboo Forest | 443 |
| 063 | Multi-Shot Storytelling | Elegant Woman's Reflective Journey Through Time | 225 |
| 064 | Camera Movement & One-Take | One-Take Water Goddess Emerges From West Lake | 574 |

## 001 - Graduation Day Worry

*Character Performance.* A young Black woman in a graduation gown speaks seriously to the camera, her expression shifting from direct address to looking down with subtle handheld movement.

```text
This is a frontal medium close-up shot, the frame primarily showing the head and upper body of a young Black girl wearing a blue graduation gown. The shot is slightly off-center, with another person visible on the left, but the background is blurred and out of focus, appearing very hazy. The girl is speaking directly to the camera, her mouth moving, her brows slightly furrowed, her expression appearing somewhat serious and worried. Light shines from above, naturally highlighting the contours of her face and even revealing the realistic texture of her skin. Although the shot is static, it carries a slight handheld breathing sensation and subtle shake, and her gaze shifts from looking forward to looking down at her hands.
```

## 002 - Desperate Hospital Chase In Cold Green Tint

*Cinematic Lighting & Color.* A woman in a dark green jacket sprints down a stark, empty hospital corridor under fluorescent lights, culminating in a frantic plea for help at the nurse's station.

```text
A modern suspense-style cinematic long take, with the entire frame presenting a strong light green filter, creating a cold atmosphere based on a light green color scheme. Under the cold white glow of fluorescent lights, an empty hospital corridor exhibits desaturated colors and extremely high-contrast lighting, sharp and impersonal. The shot begins from behind the nurse's station. A woman in a dark green jacket bursts through a door at the end of the corridor and runs quickly along the symmetrical center line towards the camera, with the camera smoothly tracking backward. Her footsteps are hurried and loud, and she shouts anxiously. Finally, she rushes to the station, slams her hands on the countertop, desperately looks around, and lets out a nearly崩溃 cry for help, her voice echoing in the silence broken only by the faint hum of equipment.
```

## 003 - One-Take Actor's Emotional Rollercoaster In A Studio

*Camera Movement & One-Take.* A single continuous shot captures an actor rapidly switching between complex emotional states as a director feeds him dramatic scenarios in a professional film studio.

```text
Shot 1 [0s-30s]
Close-up, eye-level perspective, continuous fast panning, one-take (single-shot continuous seamless camera movement):
On the left side of the frame is a director wearing a black trendy director's vest and high-end professional work headphones, with a large professional film camera placed slightly below and to his left. On the right is a meticulously made-up, fashionable Korean-style comma-banged, high-custom suit-wearing 'guanxi' young idol. The background is a spacious professional studio shooting set, visible are a huge green screen, several towering film-grade C-stands, tangled cables, and busy crew members like lighting technicians and makeup artists moving in the background.
Professional studio artificial lighting. Soft LED softbox light source spills in from the right, evenly illuminating the faces of the three main subjects, with rich scene colors. The background photography equipment and green screen cast faint shadows under the ample studio lighting, presenting a realistic and bustling modern big-budget production set texture.
The shot is handheld one-take, close-up. At the start of the shot, filming the director. The director has an indifferent expression, glances at the 'guanxi' young idol off-screen to the right front of the frame, and gives him an instruction, saying: "The media is deliberately smearing you, show me an expression." After speaking, the camera quickly pans right to a close-up of the idol's face. Do not cut. The 'guanxi' young idol, his face oriented towards the off-screen director direction to the left front of the frame, looks composed, with a sincere and confident gaze. His lips move slightly, and he explains professionally to the other party: "For something like this, there can be several emotions." While speaking, his head has extremely slight natural movement. After speaking, the camera quickly pans left to a close-up of the director's face. Do not cut. The director thinks for a moment, then provocatively tilts his head and says to the 'guanxi' young idol: "Paparazzi leaked that you had a secret midnight rendezvous." After the director delivers his line, the camera swiftly pans right to a close-up of the young idol's face. Do not cut. The 'guanxi' young idol, his face oriented towards the off-screen director direction to the left front of the frame, quickly enters a performance state. He furrows his brows tightly, his eyes panicked and anxious, darting rapidly. Then he bites his lower lip hard, closes his eyes, and his entire face (despite the meticulous makeup) tenses with extreme anxiety, perfectly presenting the inner terror, tension, and intertwined struggle of facing the destruction of his idol career. After the performance, the camera again swiftly pans left to a close-up of the director. Do not cut. The director's facial expression changes slightly, his speech speeds up, and he says: "The media helped whitewash you again, saying that was your biological sister!" After the director finishes speaking, the camera again swiftly pans right to a close-up of the young idol. Do not cut. In the frame, the 'guanxi' young idol, his face oriented towards the off-screen director direction to the left front of the frame, his expression completes a god-tier transformation in a thousandth of a second. First, his face freezes, then his eyes suddenly narrow, his mouth stretches into an extremely wide grin, revealing a row of white teeth, displaying an extremely exaggerated, even somewhat distorted, ecstatic smile. This insane emotion intertwining "despair of a ruined career" and "completely breaking free from constraints" twists on his face. After the character performance, the camera again swiftly pans left to a close-up of the director. Do not cut. The director says: "Your biological sister revealed to the media that you were adopted." After the director finishes speaking, the camera again swiftly pans right to a close-up of the young idol. Do not cut. In the frame, the 'guanxi' young idol's face is oriented towards the off-screen director direction to the left front of the frame. His eyes bulge wide open, eyeballs protruding, his meticulously trimmed eyebrows raised high, his mouth agape in a shocked "O" shape. Immediately after, the corners of his mouth uncontrollably pull upwards again, revealing an expression of disbelief, shock, and complex emotion. After the character performance, the camera again quickly pans left to a close-up of the director. Do not cut. Then the director shows a slightly surprised expression and says: "Actually, you are the true young master of a trillion-dollar wealthy family." After the director finishes, the camera immediately swiftly pans right to a close-up of the young idol. Do not cut. In the frame, the 'guanxi' young idol's face is oriented towards the off-screen director direction to the left front of the frame. He instantly erupts into extremely demonic ecstasy. His whole body trembles slightly with excitement, his eyes squint into slits from laughter, his hands even rise to his chest, clapping rapidly and continuously in small motions, his body leans forward and sways, performing the delirious joy of overnight wealth beyond self-control to the fullest. After the character performance, the camera again quickly pans left to a close-up of the director. Do not cut. The director says: "Your sister ran off with the money." After the director finishes, the camera again swiftly pans right to a close-up of the young idol. The young idol's face is oriented towards the off-screen director direction to the left front of the frame. His eyes widen again, pupils trembling, the corners of his mouth drooping downwards, his expression plunging from heaven to hell within a second, filled with shock, pain, and bewilderment. The frame finally freezes on this expression.
```

## 004 - West Coast Street Fantasy One-Take Shopping Cart Ride

*Camera Movement & One-Take.* A cool teen in a shopping cart rides through streets, crashes into a billboard to become flat art, while his real self watches below.

```text
This is a 30-second cinematic high-intensity single-shot (One-Take) visual spectacle short film. The overall style is positioned as "West Coast Street Fantasy," with a visual language that blends the gritty feel of 1990s street skateboarding videos with the refined quality of modern commercial blockbusters. The overall image uses an extreme "California Sunshine" cinematic color grade, with the highly saturated blue sky and the shadows of palm trees under direct sunlight forming a strong contrast. The air is filled with the scorching heat of asphalt, the metallic sound of shopping cart wheels grinding, and a fearless youthful rebellious energy. Spatial perspective continuously elongates with the protagonist's high-speed glide, and the camera creates a strong visual impact through extremely low-angle following and highly dynamic physical traversal.

The protagonist is a trendy, cool teenager wearing a color-blocked striped shirt and a black baseball cap. His expression instantly switches from initial lazy relaxation to the excitement of breaking through limits. The protagonist in the second scene is the same teenager, but he appears in the real dimension in a posture of an "observer."

Shot 1 [0s-6s]:
The opening shot is a close-up. The teenager lazily lies in a red metal shopping cart, with the background featuring California's iconic straight avenues and towering palm trees. As the music rhythm erupts, the camera executes an extremely rapid backward pull-out and sinks to ground level, following at an extremely low angle close to the wheels. The teenager begins to plunge down a steep road, the shopping cart jolts violently on the pavement, cars on both sides rapidly recede, and the camera captures a sense of acceleration that is almost insane.

Shot 2 [7s-15s]:
No cut. The camera follows closely along the ground like a skateboarder. The moment the teenager goes over a simple wooden ramp, the camera顺势 executes a graceful parabolic lift. The shopping cart takes off into the air, and the camera passes underneath it. At this moment, a giant commercial billboard ahead rapidly occupies the entire field of view. The camera pushes forward in an incredible "crosshair-style" manner, directly targeting the center of the billboard.

Shot 3 [16s-24s]:
No cut. The teenager, along with the shopping cart, directly embeds into the huge billboard in a way that "breaks the dimensional wall." His originally three-dimensional body undergoes a "flattening" transformation the instant it contacts the poster, with realistic paper tearing textures and colorful glitch ink stains appearing in the frame. The teenager maintains his gliding posture but transforms into a piece of flat artwork on the billboard. The camera at this point executes a 180-degree horizontal orbit and performs a diving descent from high altitude, returning to the ground.

Shot 4 [25s-30s]:
No cut. The camera smoothly lands on the street directly below the billboard. Another "real" teenager appears in the frame. He stops, slowly lowers the brim of his cap, and looks up at his "frozen" self on the billboard with a playful smile. The camera follows his line of sight to execute a rapid zoom push-in, finally freezing on the torn hole next to the "WAN" lettering on the billboard. The background music blends high-energy hip-hop rhythms with the physical sound of film reel rolling. The visual information is highly condensed and full of fashionable rebellious force.
```

## 005 - Biomechanical Soldier In Post-Apocalyptic Battle

*Stylized & Non-Real.* A hyper-realistic CGI animation shows a biomechanical soldier, built from human remains and black metal, fighting in a desolate future city under cold, oppressive lighting.

```text
Generate a 30-second, 16:9 landscape-ratio adult sci-fi war animated short.

The visuals employ:
Hyper-realistic CGI;
Biomechanical structures;
Fusion of gray-white bone and black metal;
Insect-like joints;
Extremely detailed bone textures;
Dry bloodstains, ceramic cracks, and industrial grease;
Abandoned future city;
Cold gray skylight;
Sparse toxic green lifeforms;
High-contrast cinematic lighting;
Low-saturation cold color palette;
Flames and alarms use minimal orange-red;
Realistic physical destruction;
Oppressive, heavy, non-heroic atmosphere.

The characters no longer have complete flesh, primarily composed of:
Human spine;
Ribs;
Skull;
Black hydraulic muscles;
Metal joints;
Neural fiber optics;
Weapon interfaces.

The skeletons are not zombies, but 'legacy hardware' continued for use by the military-industrial system.

30-Second Plot and Dynamic Timeline
0–4 seconds｜Still Fighting After Death

Shot starts from a soldier's dog tag falling into a puddle.
```

## 006 - Monster Emerges From Stormy Sea In Epic Disaster Scene

*Cinematic Lighting & Color.* A small fishing boat battles a storm before a massive, Pacific Rim-style sea monster erupts from the depths, showcasing realistic water effects and colossal creature design.

```text
This is a 30-second real movie-quality scene of a sea monster's debut, with the overall atmosphere referencing Hollywood disaster monster blockbusters. The story begins with a small fishing boat struggling to sail in a storm, with the clear marking "WAN" visible on its hull. The shot first establishes the恶劣 sea conditions and the boat's渺小脆弱 state, then gradually creates压迫感 through details like unusual sea surface movement, underwater shadows, hull vibrations, and abnormal海浪隆起,最终 a massive deep-sea monster, resembling the style of "Pacific Rim" monsters, breaks through the waves from the海底. Overall requirements are realistic,厚重,真实比例,强烈水体冲击,暴雨与闪电下的大光比氛围, emphasizing电影级特效质感,海水体积感,怪兽皮肤湿润细节 and巨物压迫感.

Shot 1 [0s-30s]: Nighttime stormy sea surface, real movie quality, wide-angle shot showing a small fishing boat艰难前行 in huge waves, the hull is old, wet, constantly battered by waves, the side of the hull clearly shows white letters "WAN". The sea is波涛汹涌,狂风卷起雨幕, the sky乌云翻滚, distant闪电 briefly illuminates the entire sea area. The image emphasizes real seawater,暴风雨 environment, hull details and渺小无助感.

Shot 2: Medium close-up shot near the boat's bow or deck side,海浪猛烈拍打 the hull, seawater冲过 the deck, ropes, fishing nets, metal railings剧烈摆动 in the wind and rain. The镜头随着船体起伏产生真实摇晃感, rain constantly hits the lens foreground and hull surface. The WAN marking on the hull briefly enters the frame again. Overall emphasizes real材质,恶劣天气,湿漉漉的 metal and wooden structures,强烈生存危机感.

Shot 3: The镜头从渔船视角 looks at the sea surface ahead, in the暴雨中 the originally chaotic海浪出现不自然的巨大隆起, as if something庞然大物 is rapidly approaching from海底. The sea surface forms a huge漩涡与异常翻涌,浪峰被从下方顶起,海水流向紊乱. When闪电 illuminates the sea surface, a模糊而庞大的黑影 is vaguely visible deep below. The shot highlights悬疑感,海面压迫感与巨物逼近的恐怖预兆.

Shot 4:真人写实镜头切入渔船甲板, crew members艰难站稳 in the暴雨, faces covered in rain and惊恐, turning to look at the abnormal sea surface. Wind blows raincoats and hair, boat lights sway,背景中海浪不断升高. The镜头快速靠近人物面部, then follows his gaze转向远处翻涌海面, forming an emotional and dangerous connection. Overall强化灾难片临场感和人物渺小感.

Shot 5: The镜头切到半水下或贴近海面的低机位, between暴雨与浪涛, an extremely巨大的黑影快速掠过 from below or near the fishing boat, stirring up huge bubbles,水流和海面抬升. The fishing boat is猛然顶起 or剧烈倾斜, the hull发出不堪重负的吱嘎声.闪电 and boat lights'微弱光线 can only outline part of the monster's轮廓,保持神秘但极具压迫感.

Shot 6: The镜头回到海面, the seawater ahead suddenly像被一股巨大力量向上顶开, forming a rapidly rising浪墙,暴雨与白色浪沫被巨力掀起. The fishing boat in the foreground is甩动 by the waves,远处海面中央鼓起成巨大的圆形隆起,仿佛海底火山喷发前兆. The atmosphere reaches极限紧张, the monster is about to appear.

Shot 7: Climax shot, the sea surface轰然炸裂, a massive deep-sea monster破浪而出 from the海底,掀起数十米高的海浪与漫天水雾. The monster's image references "Pacific Rim" monster style: huge,凶暴,异形生物结构,粗糙厚重的湿润皮肤,锋利骨刺,巨大头部轮廓,发光细节 or深海生物般的恐怖纹理.闪电划过夜空, briefly illuminating the monster's全身局部与张开的巨口. The shot emphasizes真实尺度感,海水冲击力和怪兽压迫感.

Shot 8: Medium close-up or仰视镜头对准巨兽头部和上半身, the monster抬起身躯 in暴雨和闪电, its skin surface covered in seawater,伤痕,角质结构和深海生物纹理, opening its mouth发出震撼咆哮. Rainwater flows down the monster's外骨骼和鳞甲,眼部或头部细节 appear异常恐怖 under the lightning. Emphasizes湿润生物质感,真实皮肤结构,重量感和电影级怪兽设计.

Shot 9: The镜头回到渔船, the fishing boat is猛然掀起 in the冲击波与海浪 brought by the monster's emergence, the deck倾斜,海水灌入,缆绳断裂,船灯爆闪. The WAN marking一闪而过 on the剧烈晃动的船身, the boat is almost被巨浪吞没. The shot emphasizes人类造物在巨兽面前的绝对脆弱感, seawater,木板, metal碎片 and雨幕共同构成混乱灾难场面.

Shot 10: Final shot pulls back, the monster高高矗立在狂暴海面上, surrounded by巨浪翻腾, the fishing boat in the foreground or侧下方显得极其渺小. Sky闪电再次劈下, briefly illuminating the monster's庞大的轮廓,背部骨刺与翻涌海水, forming an史诗级灾难怪兽电影海报般的终极画面. The shot停留在最震撼的一刻, ending with巨物压迫感和末日感.

配乐采用好莱坞灾难怪兽电影风格. Opening with低沉环境音,深海般的低频轰鸣,稀疏鼓点和压抑弦乐营造暴风雨中的不安感; as the sea surface异动逐渐加入更强的低音脉冲,金属撞击感和不断堆积的弦乐张力; before the monster surfaces, the music enters an almost屏息般的悬停和持续上升; when the monster破浪而出, it爆发出巨大的铜管,重型打击乐和低频冲击, forming a灾难级高潮; ending with厚重,压迫,末日感极强的长音和鼓点收束,强化巨兽矗立海面的史诗感.
```

## 007 - Surreal Gas Station Refueling With A Horse

*Stylized & Non-Real.* A cool cowgirl rides her horse to a retro gas station and uses the fuel pump to feed it fresh grass, stunning the attendant.

```text
Content Summary
This is a 'refueling' event filled with deadpan humor and absurdity, taking place on a brightly colored, futuristic wasteland. At a forgotten gas station reminiscent of Route 66, a bored attendant welcomes a peculiar guest—a cool cowgirl riding a real horse. Just as the attendant thinks this is just a passing lunatic, the cowgirl walks straight to the fuel pump, picks up the nozzle, and 'fills up' her horse with fresh grass. This surreal scene leaves the well-traveled attendant in a state of cognitive dissonance and stunned silence.
Scene Description & Lighting Aesthetics
Visual Style: Realistic style, with high-saturation, high-brightness cinematic color grading to create a 'sunny' feel, allowing the absurd story to unfold in an utterly normal, even somewhat pleasant environment.
Color Aesthetics: Strictly adheres to a bright 'teal and orange' color scheme.
Teal: The cloudless sky is a bright, clear azure blue (leaning towards teal). The main building of the gas station has a retro yellow-orange-blue color scheme, slightly faded. The fuel pump is a faded retro red.
```

## 008 - Night Lake Encounter With Giant Transparent Plant

*Multi-Shot Storytelling.* A young explorer cautiously approaches a glowing lake at night, witnessing the slow rise of a massive, luminous plant that fills him with awe.

```text
A 3D animated fantasy short film with 4 shots, moving from cautious approach to the appearance of a giant creature and then to a stunned gaze. The emotional expression is quiet, mysterious, and amazed. The scene environment is a shallow lake in a night forest, an outdoor natural space. The lake surface is calm, surrounded by tall trees, with glowing petals floating on the water and thin mist in the air. The main color palette is cyan-blue, dark green, and moon-white, primarily cool tones. Local glowing plants provide cyan-white highlights, with medium saturation and medium-high contrast. The subjects are an explorer boy and a giant transparent plant at the lake's center. The explorer boy is young, with a slender build, short light-colored hair, freckles, wearing light exploration gear, holding a small oil lamp, with a soft face.
Shot 1 [0s-30s] is a medium-long establishing shot. The explorer boy moves from the right side of the frame towards the lake center, stepping on stones protruding from the water. The camera slowly pushes forward.
Shot 2 [30s-60s] hard cuts to a medium shot from behind. The camera continues to track his movement. Shallow water ripples spread outwards, gently pushing aside a few floating petals.
Shot 3 [60s-90s] cuts to a medium shot of the lake center. Increasingly dense concentric ripples appear on the water's surface. A giant transparent plant slowly rises, with liquid-like light flowing inside. As its branches and leaves unfold, they cast shimmering reflections.
Shot 4 [90s-120s] cuts to a medium-close shot from the side. The explorer boy stops, his feet planted on two stones front and back, lowers his hand lamp. His facial expression changes from alertness to wide-eyed surprise, his gaze fixed on the giant transparent plant at the lake center.
The audio type includes ambient sounds and music, no dialogue, only night insect chirps, faint water sounds, low-frequency resonance as the plant rises, and ethereal synthesizer and string music. Clearly define the lake surface ripples, glowing materials, camera push, character performance, and cool-toned night scene lighting.
```

## 009 - Lonely Girl's Dramatic Leap Over Cliff

*Character Performance.* A lonely girl with silver hair leaps from a cliff into a vast, colorful sky, showcasing dramatic lighting and emotional character performance.

```text
This is a refined Japanese 2D cartoon animation short film, requiring delicate handling of emotional climax scenes, especially the use of sky color gradients and cloud layer light and shadow. It needs dramatic backlighting effects, employing compositions with strong perspective depth in terms of spatial sense, emphasizing the protagonist's smallness and determination within the vast scene. A vast scene at the edge of a cliff, with churning sea of clouds and a distant, faintly visible city in the distance. The sky presents violently changing gradient colors, gradually transitioning from deep blue to orange-red, with the edges of the clouds rimmed in gold. A fierce wind whips up petals and broken leaves from the ground, scattering them through the air.

Protagonist design: A lonely girl, with silver-white hair violently billowing in the wind, wearing a tattered white formal dress with fine, crack-like glowing patterns along the hem. Her face is pale as porcelain, her eyes containing deep struggle and resolve.

The shot opens with an extreme long shot, the protagonist's figure appearing exceptionally small and lonely within the vast expanse of heaven and earth. The camera slowly pushes in to a medium shot of her, her dress hem and hair violently billowing and swirling in the fierce wind. She slowly raises her head to look at the churning sea of clouds. A close-up on her face captures the complex emotions flashing in her eyes—fear, struggle, ultimately transforming into resolve. She takes a step forward to stand at the very edge of the cliff. The shot switches to a high-speed环绕拍摄 (surrounding shot), the colors of the sky flowing and changing around her. Finally, at the moment she leaps down, the画面进入慢镜头处理 (scene enters slow-motion processing), her dress blooming and unfolding like a flower in the air, white light points shimmering around her body scattering like feathers.
```

## 010 - Struggling Boxer In Training Montage

*Stylized & Non-Real.* A black-haired boxer trains with visible fatigue, his punches causing the heavy bag to shake as he sweats in a Japanese sports anime style.

```text
Japanese sports anime style 2D animation, 30 seconds. In a boxing training gym, a black-haired athlete throws continuous punches. The gloves striking the heavy bag produce a noticeable vibration and rebound, but he seems somewhat exhausted, with a pained expression, sweating, as if trapped in some kind of predicament.
```

## 011 - Dark Fantasy Villain Monologue With Cosmic Power

*Character Performance.* A pale, horned man in a moonlit room scoffs, summons a shadowy vortex in his hand, and declares his intent to extinguish a soul before crushing the energy with a cruel smile.

```text
3D animated short, 30 seconds, dark fantasy theme, single shot, dim brick interior scene. A coldly handsome man with violet eyes, messy dark blue and silver-streaked hair, dark crystal horns, pale cold skin, dark purple astral runes covering his temples, wearing a midnight blue brocade stand-collar trench coat over a black silk shirt, left ear adorned with a dark silver amethyst ear cuff.
Scene: Nighttime, cold white moonlight as the dominant hard light, high-contrast low-key lighting, side-lighting effect, two blurred figures and flickering warm yellow firelight in the background, faint blue dust particles floating.
Shot: Medium close-up with a slight high angle, shallow depth of field locked on the left-side character, extremely slow tilt up to eye level during the monologue.
Action: The man stands at a slight angle, lowers his head with a scornful smile, glances at his palm then turns towards the camera, looks up and says in a cold, magnetic voice: "Ripe enough for the void." He opens his left hand, palm gathering a shadowy nebula vortex, saying: "Your soul, a mere spark for me to extinguish." Suddenly clenches his fist, the nebula shatters and dissipates into dark purple mist and faint blue stardust, finally revealing a cruel smile, dark purple gradient nails slightly extended.
Accompanied by void resonance sound effects and energy rupture sounds, English young villain voiceover throughout.
```

## 012 - Alien Abduction In A Cold-Toned Farm Painting

*Stylized & Non-Real.* A hand-drawn animation in cold-toned oil paint style shows a UFO abducting a cow with a green beam, witnessed by a boy from a farmhouse window.

```text
Hand-drawn animation style, oil painting brushstrokes, cold color palette. On an American suburban farm, a UFO flies in from the distance. A green beam shoots down from the UFO, sucking up a cow from the farm. A little boy in a second-floor room nearby witnesses this scene.
```

## 013 - Rainy Station Farewell With Emotional Exchange

*Multi-Shot Storytelling.* A girl bids farewell to a boy at a small rainy train station, culminating in a whispered message and a trembling handoff of a note.

```text
Referencing the storyboard from @Image1, Shot 1 [0s-30s]: Panorama of a small train station platform on a rainy night, a long-haired girl stands alone on the platform holding a blue umbrella, warm light shines from the small station building behind her, distant green mountains fade into the rainy mist; Shot 2 [30s-60s]: Medium shot, the girl holding the umbrella and a short-haired boy with a backpack stand facing each other on the platform, heavy rain pours down, train tracks extend between them; Shot 3 [60s-90s]: Close-up of the girl's face shot through raindrops sliding down a transparent umbrella surface, her eyes are slightly red, she whispers softly, "Remember to send a message when you get there"; Shot 4 [90s-120s]: Over-the-shoulder shot from behind the boy looking towards the girl, a train with bright headlights approaches slowly in the distance, light halos diffuse through the rain curtain; Shot 5 [120s-150s]: Close-up of hands, the girl hands a folded note into the boy's hand, her fingertips tremble slightly; Shot 6 [150s-180s]: The girl stands alone by the platform edge, watching the train tracks extend into the distance, the boy is no longer beside her, the rain gradually weakens.
```

## 014 - Static Frame Chinese Hair Ornament Showcase

*Reference-Driven Generation.* A clean, restrained 10-second video sequentially showcases five Chinese hair ornaments with subtle head movements and delicate accessory animation.

```text
Reference the 5 uploaded keyframe images to generate a 10-second, 16:9 landscape-format Chinese-style character hair ornament showcase short video. The overall style continues the rhythm and presentation logic of the reference video, with exquisite, clean, restrained visuals, featuring a fashionable Chinese style and Chinese visual design sense. The 5 characters appear in the order of upload, each character always fixed in the center of the frame, with stable composition—no character movement, no large camera movements, no exaggerated body movements. Each character stays for about 2 seconds, with primary dynamics being slight left-right head shaking, slow tilting of the head, slight raising of the chin, or returning to center, allowing the hair ornament to be fully displayed. Decorations on the hair ornaments such as tassels, flowers, magpies, kites, and butterflies can have slight swaying or trembling. The Chinese patterns in the background, such as auspicious clouds, pavilions, towers, and landscape patterns, remain relatively static, with only a very slight breathing sensation or parallax effect.
```

## 015 - Gym Conversation Between Two Friends

*Audio-Synced Dialogue.* A realistic clip shows two women conversing naturally by treadmills in a bright, airy gym, with their dialogue synced to distinct audio references.

```text
Define the woman in Image1 as Subject1, define the woman in Image2 as Subject2. Subject1's dialogue tone of voice references Audio1, Subject2's dialogue tone of voice references Audio2. Inside a gym, Subject1 and Subject2 stand side-by-side next to treadmills. Subject1 turns her head, smiles, and says to Subject2, "Which area are we training today?" Subject2 responds while wiping sweat with a towel, "Let's train back, my legs are still sore from yesterday." Subject1 nods with a smile and says, "Alright, I'll join you. Let's warm up for ten minutes first." Subject2 picks up a water bottle, takes a sip, and responds, "Let's go." The background is the equipment area and floor-to-ceiling mirrors. Realistic shooting, the scene is bright and airy, with a cool-white, naturally saturated color tone.
```

## 016 - High-Speed Miniature Fairy Chase With Dragonfly Motion

*VFX & Transitions.* A 10-second chase shows a tiny fairy moving with rapid, jerky dragonfly-like bursts and sharp stops, leaving pink afterimages.

```text
Generate a 10-second, 16:9 landscape, 1920×1080, 30fps, single-shot continuous miniature fantasy high-speed chase short.

Highest priority requirement: The fairy must adopt a dragonfly-style "fixed-point hover—instantaneous ejection—complete emergency stop—acute angle trajectory change" motion. It is forbidden to portray it as an ordinary fairy slowly floating, moving at a constant speed, or continuously gliding smoothly. Reference image style: @Image2

For the first 7.8 seconds of the entire film, at least six clearly distinguishable burst movements must appear. Each ejection must cross 60%–90% of the screen width within 3–5 frames, and come to a complete stop for 2–4 frames immediately upon reaching the new position. The sprint process leaves only 1–2 frames of pink body afterimages and transparent wing trails; the character must instantly become sharp again after the emergency stop.

Visual effects should be close to a real dragonfly:
```

## 017 - Symmetrical Hotel Chase With Profile Cross

*Multi-Shot Storytelling.* A symmetrical hotel corridor chase freezes two cats mid-run, then shifts to a profile view showing their paths crossing.

```text
0-4 seconds (Full shot / Symmetrical freeze-frame):
Image: An infinitely extending luxury hotel corridor. In the exact center of the frame, a fluffy Ragdoll cat @Image1 is suspended mid-air in a standard running pose, charging towards the camera. Its expression is serious and focused, as if executing a sacred mission. About two meters behind it and to the right, a smaller black cat @Image2 is running away from the camera towards the depths of the corridor, but its head is exaggeratedly twisted 180 degrees backwards, its eyes wide open as it looks back at the pursuer.
Details: The actions of both are frozen in a kind of 'dynamic stillness,' like exquisite clockwork toys. The arches, wall lamps, and carpet patterns in the background are all strictly symmetrical left and right.
4-9 seconds (Side tracking shot / Profile perspective):
Image: The shot switches to a profile perspective of the corridor (as if the wall has been cut open). The Ragdoll cat runs from left to right in the foreground at a steady pace, its steps mechanical and elegant; the black cat crosses from right to left in the midground, forming intersecting lines of motion.
```

## 018 - Character-Consistent Scene Generation With Reference Images

*Reference-Driven Generation.* A clip showing a male and female character in a lakeside reed field, with their appearances and the sunset scene strictly matching uploaded reference images.

```text
Based on the uploaded character card, strictly maintain the male character's features: black hair in a high bun, sideburns with stray hairs blown by the wind, sharp dark eyes, a thin and sharply defined facial contour; strictly maintain his costume details: gray-white cross-collar inner robe, outer black-gray tattered fringe shoulder cape, multiple silver coin pendant chains on the chest, deep brown wide belt wrapped around layered fabric. Based on the uploaded character card, strictly maintain the female character's features: deep brown long straight hair slightly damp and falling over the shoulders, cool side-profile contour, dark pupils; strictly maintain her costume details: olive-brown leather stand-collar short martial attire, multiple cross-bound leather straps on the chest and abdomen, inner light-colored shirt collar. The scene is strictly based on the uploaded lakeside reed beach image (golden reed clusters swaying en masse in backlit sunset light, ground scattered with dark gravel and rocks, lake surface shimmering with fine ripples in the distance, sky transitioning from cyan to gold forming a band of warm-cool交界 color), do not replace or mix in other scene elements.
```

## 019 - Material Design Product Launch With Paper Craft

*Commercial & Product.* A clean, white studio video shows a UI interface elegantly revealed through animated colored paper and translucent materials in a micro-shot style.

```text
Generate a 9-second high-end product launch dynamic video, pure white studio shoot, soft natural light, cinematic macro. Style: Google Apple/Material Design, combining colored paper craft, translucent materials and UI interface, clean and refined.

Shoot according to 5 image storyboards:
- Image 1 (0–1.48s): White background center, compact colored paper stack (white pages + blue-green-purple translucent paper), ample white space, only breathing float, maintaining a restrained opening. @Image1
- Image 2 (1.48–3s): UI panel cut out via paper wipe/mask reveal from the paper. Main panel → card → button/tag appear in sequence (Material ease), surrounding paper decorations float. @Image2
- Image 3 (3–4.64s): Diagonal top-down view, spatial parallax. UI panel floats above green grid paper, blue transparent strip, purple folded paper, orange card, camera slowly pans + slight press. @Image3
- Image 4 (4.64–8.52s): Horizontal card wall, multiple cards (content/file/task) slide in and arrange via card cascade, layout reflow, soft slide, midway transitions to a task completion scene, right-side functional area and highlight prompts form. @Image4
- Image 5 (8.52–9s): Final UI stabilizes, highlighted slogan, right-side function card, colored decorative anchor points, smooth ease-out freeze frame. @Image5
```

## 020 - Lip Gloss Model Swatch Video

*Commercial & Product.* A 15-second vertical video featuring a model trying on lip gloss, highlighting the color payoff and finish.

```text
Only a lip gloss product image @Image1, generate a model swatch video, 15 seconds, vertical screen, highlighting the lip color effect.
```

## 021 - Tough Bartender Finds Stray Kitten In Rain

*Character Performance.* A weary bartender discovers a shivering stray kitten after closing, his hardened expression softening into a gentle, awkward smile.

```text
Shot 1: After closing late at night, Image1 carefully wipes the bar counter with a cloth <sound of cloth rubbing>, a pair of giant hands covered in old calluses and new wounds moves steadily, his face shows the exhaustion after closing.
Shot 2: A faint whimper is heard <kitten whimper>, his hand stops moving, he frowns slightly and pulls open the door, only to see a skinny stray kitten shivering in the rain at the entrance.
Shot 3: Slow push-in to the kitten's helpless eyes, Image1's tired expression gradually replaced by a kind of gentleness, after a silent standoff for several seconds, this giant man slowly and stiffly crouches down.
Shot 4: Facial close-up, the hard lines on his face relax, the corner of his mouth splits into a clumsy yet kind smile, the muscles around the scar at the corner of his eye also relax. Cel animation texture, bold black outline lines and hard-edged visuals, warm yellow lighting of the ramen shop contrasted with the cold blue of the rainy night in the back alley.
```

## 022 - Clay Fox's Autumn Journey Through Miniature Town

*Reference-Driven Generation.* A clay fox explores a miniature autumn forest and town, interacting with objects in a detailed, tactile world with shallow depth of field.

```text
Reference the aesthetic style of @Image1. A small fox with a clay texture stands at the edge of an autumn forest, pricking up its ears and looking towards a distant town with cooking smoke. It starts to trot down the hillside with its short legs, passes through a miniature stone arch bridge, with stream water flowing slowly under the bridge like transparent resin. The fox runs into the town market, stops in front of a fruit stall, and uses its paw to fiddle with a red apple, which rolls onto the ground and spins a few times. It picks up the apple with its mouth and continues running, passing by the entrance of a bakery where smoke from the chimney rises in puffs like cotton wool. Finally, the fox jumps onto a low wall outside the town, sits down facing the sunset, and nibbles on the apple, with orange sunset clouds spreading across the entire clay sky. Miniature scene, shallow depth of field.
```

## 023 - Fashion Showcase In A Vintage European Cafe Setting

*Commercial & Product.* A woman models a lace blouse and skirt outfit, demonstrating detailed garment movement and texture under soft natural light.

```text
The girl from @Image1 puts on the off-white lace shirt from @Image2, paired with a black high-waisted A-line skirt and pointed-toe ankle boots. The scene is in front of a vintage European street corner cafe—wrought iron tables and chairs, climbing roses, warm yellow shop windows, old brick walls.
Shot 1 [0s-30s]: Pushing open the cafe's glass door and stepping out, full body in frame to show the overall outfit silhouette, the three-tiered ruffled cuffs flutter and layer with arm movements.
Shot 2 [30s-50s]: Leaning slightly against the wrought iron chair back, standing with a slight side angle, one hand gently raised to the collarbone, the camera pushes in to show the lace cut-out pattern on the chest and the delicate details of the pearl buttons arranged along the placket.
Shot 3 [50s-70s]: She smooths her hair and turns to the side, the soft sheen of the satin fabric flows with the curve of her body.
Shot 4 [70s-90s]: Picks up a coffee cup from the table and takes a light sip, the ruffled cuffs spread out in layers near the cup's rim, freeze frame to end. Soft afternoon natural light, French慵懒 romantic tone.
```

## 024 - High-Contrast Black-White K-Pop Group Dance Sequence

*Multi-Shot Storytelling.* A five-member girl group performs a hard-hitting, fashion-photography-style dance with sharp lighting, synchronized industrial beats, and dynamic camera work.

```text
MV concept-style hardcore dance segment for a five-member Korean girl group. Pure black and pure white seamless studio backgrounds alternate. The color tone is high-contrast black and white with hard lighting for a fashion photography texture. The music rhythm is industrial electronic bass with sudden-stop heavy drum beats.

The five members are distributed in staggered, magazine-cover-like layered positions. The center member has a lazy aura with sharp eyes, short wet hair clinging to the skull, and long silver nail extensions. The member on the left wears a black wide-brimmed hat pulled low over the brow, with wavy long hair down to the waist. The member on the right has a golden buzz cut revealing a sharp jawline. The two front members have black shoulder-length straight hair and highlighted long curly hair respectively; both maintain a high-brow, cold, glamorous expression with mouths closed and eyes looking 45 degrees below the lens.

All five wear black velvet hats or off-shoulder satin dresses with leather hollow-cut blazers and silver belt buckles. The satin hems and hollow-cut tailoring will produce specific deformations during spins and arm swings. The ground is dark reflective floor tiles creating a delayed reflection sense but not mirror walls.

On the first drum hit, the five maintain a sculptural back-facing starting pose, simultaneously whip their heads 90 degrees to show their profiles, and use their fingertips to adjust their hats, completing a preparatory point freeze for one beat.

On the heavy accent of the first lyric line, the center member slowly drags her index finger down from her collarbone and stops abruptly for two beats at the end of the line, while the side members each perform a small hit by isolating and moving their shoulders inward in a staggered manner.

At the syncopation point of the second lyric line, the five members' fingertips simultaneously make symbolic point gestures, using the silver nail extensions to draw short arcs.

Entering the interlude, energy initiates from the center member's fingertips, transmits through the arm to the shoulder, then sinks into the waist and hips to complete a full body wave, and is successively passed to the side members forming a chain reaction, taking four beats in total. The formation thereby shifts from a loose, staggered stance to a diagonal line via sliding steps along an arc. When side members pass by the center member's side, they give way by turning sideways to cross without interrupting the central line of sight.

At the densest drum beats of the chorus, the five members suddenly fan out from the diagonal line into a maximized扇形 (fan-shaped) spread. The satin hems fan out in arcs with the turns, and the hollow-cut blazers reveal waistlines when raising arms. At the moment of hair whipping, the镜头 (shot) abruptly cuts from a fixed wide-angle high/low angle composition to slow-motion close-up, capturing the suspended tension of hair strands and fabric billowing. Then it stops abruptly and maintains visible chest breathing tremors for two beats.

Entering the bridge, the center member steps back two paces to give way; the right-side long-haired member crosses steps behind her to complete a center position rotation within five beats. The new center performs an independent showcase move by leaning back and using the momentum to rise.

In the closing segment, the five members quickly return along the opposite path and gather into a V-shaped formation. The镜头 (shot) slowly pushes in with a circling follow to the new center's face, freezing on the moment of her killer eye contact with the lens while the lighting switches from top light to backlight rim light for two beats to conclude.

Full video shot allocation: opening fixed medium shot imitating cover composition, segmented parts cutting to close-ups of point hands, interlude circling follow for wave transmission, chorus wide-angle fan-out then abrupt cut to slow-motion close-up, bridge circling follow the new center, ending slow push-in freeze.

The entire video maintains high-contrast black and white with hard-edged lighting and a cool-toned studio texture, no soft light, no filters. The reflective edges of fabric and nail extensions remain clearly discernible throughout.
```

## 025 - Fleeing Stuffed Animals In A Plush Cosmic Chase

*Stylized & Non-Real.* A plush spaceship crewed by small animals flees a giant stuffed whale through a yarn and fabric cosmos, showcasing detailed soft-body physics and dynamic FPV camera work.

```text
Generate a 20-second, 16:9 ultra-widescreen plush universe adventure clip.

A spaceship made of plush fabric, buttons, zippers, and stuffing flees at high speed through a universe of giant yarn planets, fluffy nebulae, and plush behemoths. Piloting the ship are three small plush animals: a rabbit, a fox, and a crow.

A giant interstellar whale covered in deep blue long fur, with eyes like two glass buttons, chases the ship from within a nebula.

Overall style: ultra-fine plush textures, cinematic space scale, cute appearance with intense action contrast, exaggerated FPV camera movement, and realistic soft-body physics.

20-second dynamic timeline
0–3 seconds｜Zipper ship catapults launch

Shot inside the plush ship, cockpit made of stitching, buttons, and fabric instruments.

Red warning button flashes rapidly. The rabbit pulls down a giant zipper control lever, the front hatch splits open like a cloth bag.

The camera rapidly pulls back from the cockpit, passes through the zipper hatch to the ship's exterior. The ship catapults into the sky from the knitted crater of a yarn planet.

3–6 seconds｜High-speed flight skimming the yarn planet

The camera is tight on the ship's tail, flying low-altitude along the planet's surface.

The ground is made of giant knitted yarn:

Knitted mountains rush past below;
Loose thread ends sway like forests;
The ship dodges sharply left and right;
The camera continuously banks and rolls;
The thrusters emit white cotton puff trails.

6–8.5 seconds｜Giant plush whale appears

The fluffy nebula suddenly parts to both sides, the giant deep blue plush whale bursts out from behind.

The long fur on the whale's surface is blown backward by the high-speed airflow, its glass button eyes reflect the planet's light.

The camera quickly circles halfway around the ship, switching to a reverse flight perspective, making the whale continuously enlarge behind the ship.
```

## 026 - Dunhuang Dancer In Golden Light With Dynamic Camera

*Camera Movement & One-Take.* A one-take shot dynamically follows a Dunhuang-style dancer performing in a dark cavern, with warm golden light, rich colors, and stylized CG animation.

```text
One continuous shot, dynamic follow-shot mixed with orbiting perspective, 16:9 aspect ratio, CG animated film quality, character's face is delicate, smooth, without pores or skin texture, facial features have simple and elegant lines, colors are rich and saturated, lighting is soft and warm with dramatic contrast, 8K ultra-high definition, shallow depth of field, motion blur, warm gold and stone green gemstone color tones, warm golden light beam in a dark stone cavern. Low drumbeats and pipa string sounds intertwine in Dunhuang-style music, rhythm accelerates as the confrontation escalates.
Deep inside a dark stone cavern, almost pitch black, a huge golden Buddha statue in the center glows with amber warm light in the darkness, its compassionate face and outline faintly visible. A crack in the dome lets in a beam of warm golden light, golden dust slowly rotates within the beam. Murals on the four walls are submerged in darkness, only the outlines of stone green and cinnabar colors are faintly discernible. The cavern is vast, with deep, lingering echoes.
In the light beam, a flying Apsara dancer: oval face, willow-leaf curved eyebrows, phoenix eyes with upturned outer corners, skin tone like warm jade, smooth and delicate, vermilion lips slightly parted, a cinnabar floral forehead ornament at the center of the brow. Jet-black high coiled bun, two strands of loose hair fall at the temples, a three-tiered golden lotus crown inlaid with turquoise beads on the head, golden chain tassels from the crown top fall to the ears. Three layers of necklaces hang over the chest: the top layer is a delicate pearl chain, the middle layer has alternating turquoise and agate beads, the bottom layer has golden lotus pendants. Wears a stone green cross-collar narrow-sleeved short top with golden scrolling vine pattern trim on the collar and cuffs, amber gold high-waisted wide-leg trousers with golden rings gathering the cuffs, a cinnabar red wide satin ribbon tied in a bow at the waist, the ends falling to the knees. A three-meter-long ribbon is tied over each shoulder: left cinnabar red, right stone green, ribbons about twenty centimeters wide with fine golden thread piping along the edges, colors are rich and lines are fluid when unfurled. Golden armlets carved with lotus patterns on both arms, three golden bracelets on each wrist. Holds a vermilion lacquer pipa behind the back, the body painted with a golden phoenix, the head carved with cloud scroll patterns. Barefoot, golden bells tied around the ankles.
```

## 027 - High-Saturation Summer Street Fashion Short

*Stylized & Non-Real.* A young man in a distinctive white coat interacts with a large black dice in a vibrant, historic Latin American city, featuring selective colorization.

```text
Generate a 25-second, 9:16 vertical, high-saturation summer street fashion short.
The entire video takes place in a city block with the character of the Caribbean, Havana, Cuba, or a historic Latin American old town. The streets are narrow, paved with old stone slabs, flanked by colorful, slightly weathered historic buildings:
Coral red walls;
Orange-yellow facades;
Turquoise green doors and windows;
Cobalt blue wooden doors;
Pink and magenta exterior walls;
Old-fashioned balconies, wrought-iron railings, and peeling paint;
An occasional vintage yellow car parked in the distance;
Bright, strong summer sunlight;
A slight sense of humidity and heat in the air with film grain.
The protagonist is a young adult male, slender, with short black hair, a calm, confident, and slightly aloof fashion model-like demeanor.
The character's styling remains consistent throughout the film:
A white or cream-colored long, slim-fit coat;
The coat length reaches near the knees;
Four to five sets of yellow curved, circular, or strip-like decorations arranged vertically from the chest to the abdomen on the front;
The yellow decorations resemble soft cords sewn onto the garment;
The inner layer of the coat remains simple;
High-saturation cobalt blue or royal blue trousers;
White shoes;
No hat;
No changes to hairstyle, clothing color, or the number of yellow decorations.
An important prop throughout the film is a large black soft dice:
Approximately cube-shaped;
Surface made of black soft rubber, fabric, or matte plastic;
Six faces with large white dots;
Size close to the height of the character's calf;
Can be held, kicked, tossed, dragged, or placed on the ground by the character;
Maintains the same proportion and shape in all shots;
Does not turn into a regular small dice.
A small red subtitle appears continuously or intermittently at the bottom of the screen:
color of summer
The title uses a retro bold serif or typewriter-style font, with slightly wide letter spacing, in dark red or bright red. The text is positioned centrally at the bottom, small but eye-catching. Apart from this subtitle, no other large blocks of text appear.
I. Overall Visual Style
Color System
The first half of the video uses a black-and-white background with a localized colorization effect on the character:
```

## 028 - Low-Light POV With Hand-Drawn Motion Graphics

*Stylized & Non-Real.* A first-person POV clip shows a low-light, lived-in apartment at night, with rough hand-drawn motion graphics animating around the real hands, simulating a personal creative video. (source video: 1.)

```text
Generate a 15-second, 16:9 horizontal short film of "low-light real indoor photography × rough hand-drawn MG animation × first-person interactive VFX". The entire film is from a first-person POV, simulating the use of a small action camera or handheld ultra-wide-angle camera for continuous shooting in a residential space at night. The overall feel is not a polished commercial, but a personal creative video with a sense of contingency, immediacy, and slight loss of control.

Real Space and Color Palette

The scene is a small residential space at night, with a living room, dining table, computer work area, narrow hallway, and kitchen connected to each other. The space is slightly crowded, furniture is not perfectly symmetrical, retaining traces of real life.

Walls are matte beige-brown and light coffee-colored, with subtle paint texture, uneven shadows, and slight signs of use. Furniture is mainly dark old wood, black leather, and dark fabrics, with wooden tabletops retaining fine scratches, uneven reflections, and everyday items. Do not be overly tidy, do not look like a showroom, do not look like a high-end homestay.

No bright overhead lights are on indoors. The main light sources come from warm yellow wall lamps, small table lamps, laptop screens, and a string of irregularly hung red, yellow, green, and blue small bulbs along the ceiling. Outside the window is completely dark. Most areas of the room are in low-light shadows, with only local areas illuminated by wall lamps.

The overall color palette is dominated by dark brown, caramel, amber orange, and deep black. Dark areas cannot be fully brightened; corners, under furniture, and hallways must retain large areas of deep shadows. The computer screen provides a small amount of cool blue light. When the refrigerator opens, a sudden burst of cool white light appears, requiring brief automatic exposure adjustment.

The image retains the low-light characteristics of consumer-grade cameras: slight high-ISO noise, color grain in shadows, limited dynamic range, slight color shift, lens vignetting, compressed texture, and not entirely clean motion blur. Prohibit cinematic noise-free image quality, prohibit transparent and sharp commercial photography, prohibit 3D rendered feel and plastic materials.

POV Shot and Realistic Handheld Shake

Use an approximately 14–16mm ultra-wide-angle lens, with slight fisheye distortion and barrel distortion, causing furniture and door frames at the edges of the frame to curve slightly. The camera is at adult eye or chest height; the viewer is the person in action.

The lens cannot be as smooth as a gimbal. Retain irregular realistic handheld motion throughout:

When observing statically, there are also small breathing fluctuations and left-right weight shifts;
When raising an arm, the camera slightly offsets in the opposite direction;
When the person walks, each step brings small up-and-down fluctuations and slight left-right roll;
When turning the lens, it accelerates first, then decelerates, with a very small overshoot and rebound at the stopping position;
Hand movements occur first, and the camera follows with about a 0.1-second delay, creating a realistic reaction time;
During quick looking down, up, and turning around, noticeable directional motion blur and slight rolling shutter distortion appear;
When the lens gets close to the computer, wall, or refrigerator, the composition allows for skewing, cropping, and brief loss of focus;
After movement stops, autofocus needs about 0.2 seconds to re-lock.

The shake must come from breathing, footsteps, turning inertia, and startled reactions, not regular vibration, nor constant high-frequency random shaking. The shot must have a realistic sense of instability while allowing the viewer to see the core actions clearly.

Only the real right hand or both forearms of the same person appear in the frame. The arms maintain unretouched real skin texture, including pores, fine hair, joint texture, and warm light shadows. The arms must not have white outlines, cartoon outlines, or matte edges. MG lines can only animate around the arm movements, not outline the entire hand like a sticker.

Hand-Drawn MG Texture

All animations are rough 2D frame-by-frame hand-drawn, not smooth vector animation, not 3D cartoon, not plastic stickers.
```

## 029 - Removing Pool Floats and Art Supplies from Scene

*VFX & Transitions.* The clip shows a woman floating in a pool, with all pool floats and art supplies removed and naturally replaced by the surrounding water and stone ground. (source video: 1.)

```text
Remove all the blue and yellow swimming rings on the pool water surface from Video 1, and also remove the drawing paper, paint cans, brushes, and black storage box on the stone ground by the pool, naturally filling in with the surrounding pool water and stone ground. Only retain the woman floating in the pool, keeping the woman's posture, movements, and the pool background unchanged.
```

## 030 - Seamless Object Insertion With Consistent Lighting

*VFX & Transitions.* A vase is added to a wooden table, its shadows matching the natural window light, while the woman's actions remain unchanged. (source video: 1.)

```text
Edit the video. In Video 1, add the vase from Image 1 to the empty space on the right side of the woman's desk. The lighting and shadows on the vase should be consistent with the direction of the natural light from the window, integrating naturally into the wooden table scene. The woman's actions and the rest of the picture remain unchanged.
```

## 031 - Seamless Object Removal And Background Inpainting

*VFX & Transitions.* The clip shows a man being digitally removed from the left side of the frame, with the background naturally filled in, while all other people and actions remain unchanged. (source video: 1.)

```text
Remove the man on the left in video 1, and naturally fill that position with the surrounding background, keeping all other characters, actions, and the picture unchanged.
```

## 032 - Character Aging And Wardrobe Transformation In Static Scene

*Character Performance.* A young girl ages into a woman in her twenties, wearing a fitted dress, while maintaining her pose and expression against the unchanged Times Square backdrop. (source video: 1.)

```text
The little girl in Video 1 transforms into a young woman around twenty years old, with a mature face. The dress is replaced with a fitted long skirt of the same color scheme. The action of looking up at the city neon lights and the expression and demeanor remain consistent. The Times Square street scene and the rest of the picture remain unchanged.
```

## 033 - Foreground Ship Scaling With Detail Enhancement

*VFX & Transitions.* The left sailboat scales up proportionally for greater visual impact, with enhanced mast and sail details and matching water reflections. (source video: 1.)

```text
In Video 1, proportionally enlarge the sailboat on the left to give it a greater sense of visual oppression, with more prominent mast and sail details, and synchronously match the water reflection. Keep the character on the right, the distant fleet, and the sea fog unchanged.
```

## 034 - Hat Removal With Natural Hairstyle Preservation

*Reference-Driven Generation.* The clip shows a woman's hat being digitally removed to reveal her natural hairstyle while keeping her actions and the rest of the scene unchanged.

```text
Remove the hat from the woman's head in Video 1, revealing her natural hairstyle, while keeping the woman's movements and the rest of the picture unchanged.
```

## 035 - Child Opens Door To Magical Gothic Alley

*Multi-Shot Storytelling.* A child opens his apartment door to reveal a seamless transition into a wet, lantern-lit gothic alley, showcasing a realistic to dark fantasy world shift.

```text
Shot 1 [0s-5s]: A continuous, photorealistic cinematic shot. Inside @Image2's modern apartment foyer, @Image1's child stands at a diagonal angle in the center of the frame, smiling at the camera and making a natural waving gesture to signal the viewer to follow, a shallow dimple appearing on his right cheek. He then lowers his arm, smoothly turns his body to the left rear <two soft sounds of footsteps on the wooden floor>, walks with his back to the camera towards the wood-grain front door ahead, extends his left hand to grip the black electronic lock handle and turns it <click of a mechanical unlocking sound>, slowly opening the door inward. In the first half of this segment, the camera remains completely still, the character's appearance and clothing are consistent, the movements are natural and fluid, and the door's structure and material present a realistic texture. Soft overhead indoor lighting evenly illuminates the beige walls and light brown wooden floor, with no hard cuts or abrupt scene transitions.

Shot 2 [5s-10s]: Seamlessly continuing from the last frame of the previous shot, the character, clothing, apartment foyer, and camera position remain completely consistent. The character fully opens the door, and a warm yellow light carrying a damp atmosphere floods in from outside. Outside is @Image3's magical alley world—a wet, narrow cobblestone alley extends into the depth, flanked by towering Gothic spired buildings, wrought-iron signs protrude from the walls, warm orange gas lanterns illuminate every shop window, a distant spire is faintly visible within gray-blue twilight clouds, and roof chimneys emit white smoke <faint distant bell tolling>. The composition design, camera angle, spatial distance, and the relationship between the two spatial layers of the foyer and the alley remain consistent; all environments outside the door belong to the magical alley world. He pauses briefly at the doorway, looks back over his left shoulder towards the camera again, his smile shifting from relaxed to curious excitement. As the camera crosses the threshold, the lighting and atmosphere transition from the indoor bright warm wood tones to the alley's damp, cool interweaving of warm orange lantern light and gray-blue twilight, but the space and lighting remain physically natural and continuous (a low cello melody slowly rises, interspersed with harp plucks). No hard cuts or abrupt scene transitions.

Shot 3 [10s-15s]: Seamlessly continuing from the last frame of the previous shot, the camera has now passed through the doorframe into the magical alley world. He turns and steps onto the wet cobblestone pavement <crisp echo of leather shoes on wet stone>, the camera smoothly follows from behind with a stable tracking trajectory, continuing through the doorway arch into the depths of the narrow alley. His figure walks slowly between the towering buildings on either side, his gray sweater and dark trousers alternately illuminated by the warm light from the shop windows on both sides, puddles on the road reflect the overhead lanterns and building outlines, and the distant spire becomes increasingly clear. The shot finally settles on a deep panoramic composition, placing his back walking in the lantern-lit magical narrow alley at the center of the wet stone road and the Gothic spire (the cello and harp intertwine here, reaching a steady and mysterious climax). No hard cuts or abrupt scene transitions throughout. Seamless transition texture from realism to dark fantasy, high-definition sharp imagery, the foyer's warm wood low-saturation tones gradually shift to the alley's high-contrast dark palette of interwoven warm orange lantern light and gray-blue twilight.
```

## 036 - Triple Character Game PV With Elemental Skills

*Multi-Shot Storytelling.* A 15-second game PV shows three characters emerging, performing dynamic elemental skill attacks, and uniting in a final group shot with synchronized dialogue and effects.

```text
【Video Type】Game marketing character PV showcase video
【Video Duration】15 seconds
【Reference Material】Three character illustrations (Red Fox Dual Pistol Gunner: Feishou @Image1, Human Alchemy Scholar: Ziluo @Image3, Tiger Beastman Mage: Tingyue @Image2)
【Shot Structure】
Shot 1 [0s-3s]: The three characters appear in sequence with close-up shots, emerging from shadows, surrounded by their unique elemental particles (Feishou - Foxfire Illusion @Image1, Ziluo - Alchemy Essence @Image3, Tingyue - Thunder Eagle Magic @Image2). The camera slowly pushes in to focus on their faces, with expressions showcasing character traits (Feishou @Image1 alertly glances back, Ziluo @Image3 smiles intelligently, Tingyue @Image2 gazes steadily).
Shot 2 [3s-10s]: Dynamic skill showcase shots with fast scene transitions.
● Feishou: Crouches low in profile, fires twin flintlock pistols in rapid succession, mint-gold foxfire bursts from the barrels and coalesces into three fox-shadow clones that dart forward, with gunshot sound effects + foxfire particle effects.
● Ziluo: Raises a brass scale with one hand, violet essence streams from fingertips, forming liquid duplicates that orbit around, with essence surge sound effects + violet transparent particle effects.
● Tingyue: Holds a magic staff diagonally, summoning a golden eagle to soar, dark bronze-green lightning erupts from the staff tip and sweeps across to intimidate enemies, with thunder sound effects + lightning particle effects.
The camera pans following the elemental trajectories, dynamically showing character action poses, with expressions focused on combat.
Shot 3 [10s-15s]: Group shot of the three standing side by side, slowly pulling in from a wide shot to a medium shot. Their unique elements converge and fuse behind them (mixed particle cloud of foxfire + essence + thunder eagle), with color gradient (mint gold + violet + dark bronze-green). Each character displays their characteristic expression. Their names flash on screen sequentially.
【Shot Control】
● Close-up shot: Character facial close-up, expression details and lip sync.
● Medium shot: Character upper body, action and effect release.
● Wide shot: Group shot of three, showcasing team presence.
● Dynamic shot: Fast movement during skill release, following elemental trajectories.
● Transitions: Shadow fade-in, elemental transitions (foxfire → essence → thunder eagle), fast cuts, slow-motion pull-in.
【Action & Effects】
● Feishou: Dual pistol rapid fire summons foxfire phantoms, mint-gold foxfire particles orbit, agile hunter aura.
● Ziluo: Scale and essence manipulation, violet liquid-light particles, alchemy scholar aura.
● Tingyue: Golden eagle soaring, lightning sweeping, dark bronze-green lightning particles, magic master aura.
● Convergence effect: Mixed particle cloud of the three characters' elements, color gradient fusion.
【Expression & Lip Sync】
● Feishou: Alert glance back, slightly sharp, eyes playful yet resolute, lip sync to dialogue "Under the trigger, none can escape."
● Ziluo: Intelligent smile, slightly mysterious, eyes kind and calm, lip sync to dialogue "Everything has an equivalent price, including fate."
● Tingyue: Steady gaze, slightly authoritative, eyes sharp as an eagle's, lip sync to dialogue "Where the eagle goes, there is thunder."
【Voice & Sound Effects】
● Feishou dialogue: Male voice clear and cool, slightly free-spirited and roguish, moderately fast pace, moderate pitch.
● Ziluo dialogue: Female voice gentle and intelligent, slightly mysterious, slow pace, moderate pitch.
● Tingyue dialogue: Male voice authoritative and solemn, slightly stern, moderate pace, lower pitch.
● Sound effects: Gunshots + foxfire burst + essence surge + lightning sweep + golden eagle wing flap + mixed particle explosion.
● BGM: Epic symphony + electronic sound effects mix, rhythm synchronized with shot transitions / skill releases / dialogue delivery.
【Visual Style】
● Color tone: Dark tones + high contrast, Feishou mint gold, Ziluo violet, Tingyue dark bronze-green.
● Particle effects: Foxfire particles, essence particles, thunder eagle particles, convergence fusion.
● UI elements: Game logo appears, character names flash, skill names are labeled.
```

## 037 - Dual Heroine Fashion Film With Jump Cuts

*Multi-Shot Storytelling.* A fast-paced fashion film shows two models in contrasting styles, featuring sharp jump cuts, high-speed photography, and cinematic lighting.

```text
Cinematic dual-heroine fashion blockbuster, extremely fast-paced, pure jump cut editing logic, shot with Arri Alexa 65 and Panavision anamorphic lenses, Kodak Vision3 500T film texture, 8K resolution, photorealistic, no text. Facial features are completely locked to Girl A @Image1 and Girl B @Image2.

Shot 1 [0s-3s: Rapid Entrance and Contrast] (Jump Cut) Pure white minimalist space, cut by strong side light creating sharp shadows. Left screen/left side: Girl A wears a black deconstructed leather suit, her gaze cool and glamorous under cold light, quickly turns her head to look directly at the camera. Right screen/right side: Girl B wears a champagne gold flowing silk gown, her gaze languid under warm light, quickly turns her head to look directly at the camera. Authentic film grain.

Shot 2 [3s-6s: Extreme Material Close-ups] (Jump Cut) Extreme macro close-ups. Girl A reference outfit @Image3: Cold light hits the sharp folds of the black leather and metal accessories, presenting a cold, high-end sheen. Girl B reference outfit @Image4: Warm light outlines the lines of her collarbone, the silk fabric flows like water waves, skin presents a hyper-realistic, translucent, dewy texture with fine hairs visible.

Shot 3 [6s-9s: Tense Interweaving (High-Speed Photography)] (Jump Cut) The two walk towards each other in the pure white space, passing by each other. High-speed photography (1000fps slow motion). The toughness of black leather and the softness of champagne silk collide intensely at the moment of passing, skirts and hair fly in the air. At the zero-point-one second of passing, their gazes meet sharply.

Shot 4 [9s-12s: Back-to-Back Intensity] (Jump Cut) The two stand back-to-back. Strong side backlight (Rim light) simultaneously outlines their facial contours and hair halos. They both quickly turn their heads, looking directly at the camera. Their expressions are intensely powerful, professional, and full of top supermodel confidence.

Shot 5 [12s-15s: Relaxation and Freeze] (Jump Cut) The two stand side by side, slightly tilting their heads to look at each other, revealing highly infectious, relaxed, and confident smiles. The camera slowly zooms out (Slow zoom out), showing their perfect proportions in the grand light and shadow space, the scene gradually darkens in a high-end glow.

Camera Movement: Fast handheld, rapid push-ins, high-speed photography slow motion, pure jump cuts, no flashy visual effects.
Color: High-contrast black, white, and gray base, accented with cold metallic sheen and warm champagne gold, cinematic color grading.
```

## 038 - Stylized Urban Chase With Motion Graphics And Dynamic Lighting

*Stylized & Non-Real.* A high-stakes, stylized chase unfolds between two martial artists in a neon city as they fight for control of a glowing orb.

```text
Generate a roughly 30-second, 16:9 landscape, high-aesthetic urban MG chase short film. Image @Image1 serves as a reference for the city space, neon atmosphere, road structure, and overall visual texture; Image @Image2 serves as the sole appearance reference for the male character; Image @Image3 serves as the sole appearance reference for the female character. Strictly maintain the stability and uniformity of both characters' faces, hairstyles, body types, clothing structure, color schemes, and recognizability.

【Overall Style】
High-end motion graphics dynamic illustration style, integrating flat MG graphic language, exquisite 2.5D spatial layering, and restrained three-dimensional volume. The overall look is not realistic live-action film, not childish cartoon, nor dirty, heavy industrial cyberpunk. The vibe should be showy, cool, beautiful, tense, and eye-catching, like an action movie-level urban chase promotional short. The shots heavily use handheld follow shots, fast whip pans, snap zooms, low camera angles close to the ground, front-facing backward tracking shots, whip pans, and occasional drone wide shots to create a strong sense of chase pressure.

【Character Action Logic】
The woman's advantages are lightness, speed, agile reactions, and skill in using the environment and changing direction; the man's advantages are strength, anticipation, pressure, and skill in interception and close-quarters control. Both are martial arts masters, so the struggle is not random grappling but a series of "grab, block, redirect force, change hands, use force, turn, dodge, counter" actions centered around the light orb. The woman often uses turning to redirect force, changes direction to escape, and uses obstacles to create distance; the man often uses preemptive positioning, grabbing the wrist to intercept the orb, using his body to block routes, and pressing forward to suppress.

【Light Orb】
The light orb is small enough to hold in one hand, with a white core and soft purple-pink-blue halos. It is the sole object of contention throughout the film. The orb must realistically illuminate the edges of hands, faces, clothing, and the surrounding environment. There is always only one orb, its size is stable—it does not duplicate, disappear, or deform. When moving, it only leaves short, clean light trails.
```

## 039 - Premium Snack Packaging Showcase With Warm Lifestyle Tone

*Commercial & Product.* The clip shows a detailed, multi-shot presentation of a premium snack package, highlighting its elegant design and clear nutritional information in a warm, commercial style. (source video: 1.)

```text
Shot 1: Wide shot, in a kitchen wooden table scene, the @Image1 Cuiyanshe Black Truffle Sea Salt Mixed Nut Brittle packaging is centrally displayed, with a few scattered almonds, cashews, walnut kernels, and black truffle slices as atmosphere props; the shot slowly pushes in.
Shot 2: Close-up, the packaging front fills the frame, clearly displaying the top gold-stamped wheat ear nut circular badge logo, the gold-stamped calligraphy characters "Cui Yan She", the product name "Black Truffle Sea Salt Mixed Nut Brittle", three capsule labels "Selected 6 Kinds of Imported Nuts", "0 Trans Fatty Acids", "Non-Fried·Low-Temperature Light Baking", and the deep forest green background with gold-stamped color scheme, with sharp, legible text.
Shot 3: A hand picks up the packaging from above and flips it to show the @Image2 back, displaying the densely arranged ingredient list, nutrition facts table, manufacturer information, and bottom barcode; the small cream-white text is clearly readable on the dark green background, then flips back to the front.
Throughout, the product packaging's gold-stamped logo, text, deep forest green color scheme, and printed patterns remain highly consistent without distortion. E-commerce product display style, warm-toned lifestyle feel.
```

## 040 - Character Substitution In Skateboarding Scene

*Reference-Driven Generation.* A skateboarder is replaced with a different person while preserving the original motion, trajectory, and background environment. (source video: 1.)

```text
Reference the video, replace the skateboard man in video 1 @Video with the woman and clothes from image @Image1. Note: only replace the character, keep the skateboard action, motion trajectory, and skatepark background from the original video completely unchanged.
```

## 041 - Coffee Cup On Rooftop Table With Referenced Camera Moves

*Reference-Driven Generation.* The clip shows a cup of coffee on a rooftop table, filmed using the camera movements from a reference video. (source video: 1.)

```text
Reference the camera movements from the video, change the scene to a cup of coffee on a rooftop coffee table.
```

## 042 - Reference-Driven Energy Effect And Motion

*Reference-Driven Generation.* The clip shows a character performing an action with an energy effect, matching the style and motion from a reference video.

```text
The character from Image 1 references the energy effect from Video 1 to generate the same effect and action.
```

## 043 - Idol Dance In Modern Kitchen With Audio Sync

*Audio-Synced Dialogue.* A young woman performs an idol-style dance perfectly synchronized to a fixed audio track's rhythm and emotional shifts within a minimalist kitchen. (source video: 1.)

```text
Vertical screen 9:16, full-body shot, fixed stable camera position. A young woman with long black hair, wearing a white long-sleeved top with floral embroidery, a white pleated short skirt with a black belt, and white platform sneakers, dances an idol-style dance to the beat of a fixed audio track in a modern minimalist kitchen. The background features light gray cabinets, a white island, and dark night-view windows. A square fill light behind the character creates a rim light, with cool white indoor lighting.
Choreograph the dance according to the fixed audio's rhythm, speed, and emotional fluctuations: heavy drum beats correspond to sharp, large-scale movements and定格姿势,舒缓段落对应柔和的身体波浪与手部姿态,副歌高潮段落动作更密集更有爆发力. The overall style is idol dance, with smooth,连贯流畅的动作,富有节奏感和表现力, perfectly synchronized with the audio beat.
Motion is fluid, body proportions are natural.
```

## 044 - Character Replacement with Emotional Phone Call

*Reference-Driven Generation.* A male character seamlessly replaces a woman in a video, having an emotional phone call by a rainy window with perfect lip-sync and mixed lighting.

```text
Seamlessly replace the female character in video @Video1 with the male character from image @Image1. The character sits by the window, holding a phone to their ear while speaking.

【Voice & Dialogue】Extract the vocal characteristics from audio @Audio1 and have the character speak the following lines: "Really? That sounds great! When are you coming back? I miss you so much."

【Lip-sync & Expression】The generated speech must precisely drive the character's mouth for natural opening and closing. Speaking should be accompanied by natural blinking, slight head nods, and a sense of breathing. Facial micro-expressions must perfectly match the caring and reminiscent emotions in the dialogue.

【Lighting & Scene】The character's face must naturally receive mixed lighting from warm indoor light and cool neon light from outside the window. In the background, raindrops continuously and slowly slide down the window. Slight steam rises from the coffee on the table. The character and scene edges should blend naturally, with no signs of cut-out.

【Shot & Quality】15-second long take, the lens pushes forward extremely slowly, the shot is extremely stable, cinematic-grade lighting, 8K resolution, photo-realistic quality.
```

## 045 - Warm Diary of a Golden Retriever's First Year

*Multi-Shot Storytelling.* A warm-toned film shows a man reading his old diary about his dog 'Summer', with each page's narration triggering a nostalgic memory clip from the puppy's first year.

```text
This video contains 6 shots, with a total duration of 30.0 seconds.

The entire film uses a warm yellow tone and film grain texture as its base. The narrative thread is the owner opening an old diary written for a Golden Retriever late at night—each voiceover is a page read from the diary, and the visuals are the memory images evoked by the diary's text. Through five life fragments of the Golden Retriever 'Summer' from puppy arrival to its first birthday, accompanied by piano and strings with a page-turning feel, it tells a warm growth story.

Global font setting: All Chinese text in the entire film (including opening title, per-shot subtitles, and ending title) uniformly uses the 'KaiTi' font type, presenting the warm, literary texture of a handwritten diary. The text color is warm yellow (#E8D5A3), with a relatively small font size, slender strokes, and the edges of the strokes have a very slight warm-colored soft glow diffusion, naturally blending with the film grain texture of the visuals, as if written with a fountain pen on yellowed diary paper.

Global sound setting: The BGM is a combination of soft felt piano and chamber strings, overall quiet and restrained, with emotions turned inward. The piano touch is soft and dense, like fingers gently pressing the keys rather than striking; the strings are warm and thick, with the granularity of bow friction audible, not pursuing grandeur but an intimate closeness to the ear. The emotion flows with the plot—the opening has only a single sustained piano note, the puppy segment has a lightly started simple piano melody that is warm and restrained, the outdoor segment adds nylon-string guitar plucking becoming light and bouncy, the fetch-the-ball segment has strings gently lifting the mood upward, the sickness segment has the piano sinking into the low register with cello slowly entering becoming the quietest and most heart-wrenching part of the film, the birthday segment has strings filling out with a bright and open melody, and the finale returns to the opening notes for a callback, with the last note drawn out, the lingering charm slowly returning to silence. The entire BGM is like a letter written to oneself, the emotion never spills out, always a kind of restrained tenderness.
```

## 046 - Morning Skincare Ritual Showcasing Natural Beauty

*Commercial & Product.* A woman's morning routine, from waking to leaving, filmed in natural light to convey confidence in bare skin, ending with a product shot.

```text
Generate a brand advertisement film for Suyan SĒRA Light Essence based on my proposal document—a story about 'Three Minutes in the Morning'. The female lead, from waking up to skincare to going out, is bare-faced throughout, using the texture of natural light to prove: good skin doesn't need to be covered, it just needs to be treated well. The entire film has zero voiceover, zero product efficacy claims, relying solely on the emotional visuals to convey the brand attitude of 'bare-faced confidence'. Ensure consistency of the protagonist. The final shot ends with a product image.
```

## 047 - Animated Data Dashboard With Sound Design

*Commercial & Product.* A whiteboard business presentation shows animated charts and numbers with synchronized sound effects and a confident voiceover explaining growth metrics.

```text
Total duration 22 seconds, 4 shots sequentially spliced. Entire video has a pure white background, soft color blocks and simple line charts, Apple Keynote-style minimalist business aesthetic, sans-serif dark gray font. BGM (must be present, runs through the entire video, volume clearly audible): a light and upbeat business background music, steady rhythm, simple melody, music starts from the first second, uninterrupted throughout, when the voiceover appears the music does not disappear, volume slightly lower than the voice. Sound effects layer: a 'whoosh' sound when color blocks slide in, a light keyboard 'click' sound when numbers tick, a crisp 'ding' bell sound when key data pops up. Voiceover: English male or female voice, bright and confident, speaking speed about 2.5 words/second, tone like giving a presentation at a quarterly meeting—professional but not cold, rhythmic, slightly emphasizing key numbers.
H1-2026 Cross-border E-commerce Monthly GMV.xlsx
Shot 1: Wide shot, centered composition, pure white background, soft light, minimalist business style, visual reference @Image1's clean white background + soft color blocks. Pure white screen expands from the center, countless golden light particles converge from the edges of the screen towards the center, particles collide and sparkle then condense into the title text 'H1 2026 · Wan', the text surface has flowing data light effects, edges have faint light particles continuously floating and dispersing, overall cool and premium. After a brief pause, the title dissolves into particles and disappears, simultaneously two sets of large dark gray numbers slide in below—left is the value from cell B7 row 7 $1,580 (January GMV), right is the value from cell G7 row 7 $3,460 (June GMV), connected by a light gray arrow in the middle, below the arrow floats light gray small text 'Monthly GMV Growth'. A coral-colored rounded tag pops up at the bottom, showing the value from cell H8 row 8 +45.7% (H1 overall growth rate), accompanied by a crisp 'ding' sound when popping up. The voiceover says brightly and confidently: 'In the first half of 2026, monthly GMV grew from 15.8 to 34.6 million dollars.' BGM is clearly audible from the first second of the shot, light rhythm runs through, color blocks sliding in have a slight 'whoosh' sound. At the end of the shot, the color blocks slide smoothly to both sides, revealing the next scene.
```

## 048 - Quantum Mechanics Explained Through Fun Animation

*Creative Fun.* An animated explainer uses simple metaphors and visuals to make complex quantum physics concepts accessible and engaging for a general audience.

```text
Shot 1 [0s-30s]: A friendly animated host appears in a colorful, abstract space. They hold a glowing "quantum" orb.
Host (to camera): "Ever feel like quantum mechanics is just... weird? Let's change that!"
@Image1: A stylized, friendly cartoon character in a lab coat, smiling.

Shot 2 [30s-60s]: The host tosses the orb. It splits into multiple copies that bounce around, demonstrating "superposition."
Text overlay: "Superposition = Being in multiple places at once!"
@Image2: Animated diagram of a particle as a blur in several positions.

Shot 3 [60s-90s]: Two orbs are shown. When one spins, the other instantly spins the opposite way, no matter the distance.
Host (V.O.): "This is 'entanglement'—spooky action at a distance, as Einstein called it."
@Image3: Simple graphic connecting two particles with a glowing line.

Shot 4 [90s-120s]: Fast-paced montage of real-world tech (lasers, MRI machines, computer chips) with quantum icons overlaid.
Host (V.O.): "And this isn't just theory! It powers lasers, MRIs, and the computers of tomorrow."
Upbeat, curious music throughout. Bright, dynamic colors. Playful sound effects.
```

## 049 - Who Is Wang Wei? An Animated Introduction For Kids

*Chinese Classical & Literary.* An animated video introduces the Tang Dynasty poet Wang Wei to first-grade children through simple narration and vibrant visuals. (source video: 1.)

```text
Shot 1 [0s-30s]: Animated scene. A friendly cartoon narrator appears on screen. @Image1: A simple, friendly cartoon character.
Narrator: "Hello, kids! Today, let's meet a great poet from ancient China. His name is Wang Wei!"

Shot 2 [30s-60s]: Animated scene. Show a simple map of China during the Tang Dynasty, highlighting Chang'an. A cartoon figure of Wang Wei appears. @Image2: A stylized, child-friendly map with a cartoon Wang Wei figure.
Narrator: "Wang Wei lived over 1,200 years ago in the Tang Dynasty. He was a poet, painter, and musician!"

Shot 3 [60s-90s]: Animated scene. Show Wang Wei in a beautiful, simplified landscape (mountains, river, a small boat). Cherry blossoms or willow trees are present. The scene is peaceful and colorful. @Image3: A bright, painterly landscape in animation.
Narrator: "He loved nature. He wrote poems about quiet mountains, flowing rivers, and beautiful flowers."

Shot 4 [90s-120s]: Animated scene. Show Wang Wei writing a poem with a brush. The characters of a very short, famous line (e.g., a simple phrase) appear in the air with a sparkling effect. @Image4: Close-up of animated brush writing, with magical text appearing.
Narrator: "He used words to paint pictures in people's minds. That's what makes his poems so special!"

Shot 5 [120s-150s]: Animated scene. The friendly narrator waves goodbye. Icons representing poetry, painting, and music float around Wang Wei's cartoon figure. @Image5: The narrator and Wang Wei figure on screen with icons.
Narrator: "So, Wang Wei was a talented artist who showed us the beauty of nature through his poems and paintings. Goodbye!"
```

## 050 - Adding A Semi-Buried Rock To A Beach Scene

*VFX & Transitions.* The clip shows a beach where a rock is added, half-buried in wet sand, with seawater gently covering its base as the tide recedes. (source video: 1.)

```text
Edit the content of video 1. Add a rock on the beach, so that the rock is half-buried in the wet sand, and let the seawater gently cover the bottom of the rock as the tide recedes.
```

## 051 - Gender-Swapped Skateboarder With Preserved Motion

*Reference-Driven Generation.* A short-haired woman in a sports bra and cargo pants performs the same skateboard tricks as the original male skater, keeping all protective gear and background. (source video: 1.)

```text
Edit the video, replacing the skateboard man in Video 1 with a short-haired woman wearing a sports bra and loose cargo pants. Retain the original video's baseball cap, knee pads, elbow pads, and other protective gear. The skateboarding actions, motion trajectory, and skate park background remain completely unchanged.
```

## 052 - Seamless Eyewear Removal With Natural Eye Makeup

*VFX & Transitions.* The clip shows a woman's sunglasses digitally removed to reveal natural eye makeup and expression while her movements and the rest of the scene remain perfectly unchanged. (source video: 1.)

```text
Edit the video, remove the woman's sunglasses in video 1, revealing natural eye makeup and gaze, while the woman's movements and the rest of the frame remain unchanged.
```

## 053 - Soft Three-Point Lighting For Natural Skin Tones

*Cinematic Lighting & Color.* The clip shows a man's face evenly lit with soft, natural light, eliminating harsh shadows for a unified, TV-quality look. (source video: 1.)

```text
Edit the video. For Video 1, brighten the overall lighting, adopt the soft three-point lighting characteristic of American TV dramas, eliminate the hard shadow on the right side of the man's face, ensure the facial features are evenly illuminated, and make the skin tone appear natural and translucent. Synchronously enhance the light perception of the white tiled wall and window in the background, maintaining a unified overall tonal range of the image, while keeping the man's actions and the video content unchanged.
```

## 054 - Man And Ostrich Swap Positions While Walking

*VFX & Transitions.* A man in a suit and an ostrich exchange positions on the street while maintaining synchronized walking movements and pace. (source video: 1.)

```text
Edit the video. In Video 1, swap the positions of the man in the suit and the ostrich. Move the ostrich to the front-left side of the frame, and move the man to the right side, closely following the ostrich. Ensure the walking actions and pace rhythm of both remain consistent, while keeping the street background unchanged.
```

## 055 - Transforming Video Into Claymation Style

*Stylized & Non-Real.* The clip shows a video transformed into a stop-motion clay animation style, demonstrating the ability to apply a specific stylized aesthetic. (source video: 1.)

```text
Edit the video, transforming the video style into a claymation style.
```

## 056 - Dialogue Replacement In A Video Scene

*Audio-Synced Dialogue.* A video clip is edited to replace a male character's original dialogue with a new, suspenseful line. (source video: 1.)

```text
Edit the video, changing the male character's line to: "The deal is done. Now... we disappear."
```

## 057 - Character Wardrobe And Accessory Replacement

*Reference-Driven Generation.* A man and a woman in a video have their hats and the man's shirt digitally replaced while preserving their original movements and the rest of the scene. (source video: 1.)

```text
Edit the video. The woman in Video 1 wears the hat from Image 1, naturally fitting the head shape. The man in Video 1 wears the hat from Image 2, naturally fitting the head shape. The man's reddish-brown shirt is replaced with the blue washed loose denim shirt from Image 3, with the collar open and sleeves rolled up to the forearms. The actions, clothing, and the rest of the picture of the two remain unchanged.
```

## 058 - Man Plays Guitar In A Spontaneous Performance

*Character Performance.* The clip shows a man picking up a guitar and beginning to play a piece of music, demonstrating the ability to reimagine a scene's action. (source video: 1.)

```text
Reshape the plot of @Video1 so that the man directly picks up the guitar and starts playing a piece of music.
```

## 059 - Teahouse Negotiation With Extended Dialogue And Period Detail

*Multi-Shot Storytelling.* A clip shows two men in a 1920s teahouse negotiating a shipment, featuring deliberate dialogue, subtle gestures, and authentic period atmosphere. (source video: 1.)

```text
Extend video 1 by 15 seconds. Character A is a man with slicked-back hair, wearing a dark gray Chinese-style long gown, with a brown Buddhist bead bracelet on his left wrist. Character B is a man wearing a dark-colored Chinese-style long gown. Character B slowly puts down his tea bowl, his gaze slightly lowering. He lightly taps the table twice with his fingertip and says unhurriedly, "The price is negotiable, but when will the goods arrive at the port? You need to give me a definite date." Character A's smile remains unchanged as he picks up the lidded bowl and gently scrapes the tea foam. Character A takes a sip of tea, places the bowl back on the saucer, leans forward, lowers his voice, the Buddhist beads swaying slightly with his gesture, and says with a firm tone, "By the end of the month at the latest. I've already taken care of everything at the docks. A whole ship of goods will be delivered right to your warehouse door." After speaking, he presses his right palm down on the table, looking directly at Character B. Character B ponders for a moment, his gaze sweeping toward the "Wan An Pawnshop" plaque outside the window, the bamboo curtain gently lifted by the breeze from the street. He turns back, a smile appearing at the corner of his mouth, picks up his lidded bowl, and raises it slightly toward Character A, "Good, delivery by the end of the month. I await your good news." The two men look at each other and smile. Maintain the沉稳调性 (steady tone) of a Republican-era商业战片 (business rivalry film), with a从容 (leisurely) dialogue pace and low茶馆环境音 (teahouse ambient sounds) in the background.
```

## 060 - Waltz Opening At A Grand 19th Century Ball

*Multi-Shot Storytelling.* A man in formal wear invites a woman in a vintage gown to dance, beginning a waltz in a warm-lit ballroom as guests watch. (source video: 1.)

```text
Extend video 1 forward by 15s. Character A is a dark brown short-haired male wearing a black tailcoat, white shirt, black bow tie, and beige vest. Character B is a brown-haired woman with an updo, wearing a beige vintage long dress with puffed sleeves, black lace trim on the skirt, and dark teardrop earrings. In the ballroom, the light from a crystal chandelier reflects on the marble floor. Guests chat in small groups, holding glasses and whispering. A melodious waltz string prelude slowly begins, and the crowd's conversation gradually quiets down. Character B walks slowly from one side of the ballroom, her skirt lightly brushing the marble floor as she glances around. Character A steps out from the crowd, walks straight through the guests to stand before Character B, gives a slight bow, extends his right hand, and gazes at her gently. Character B looks down with a faint smile, places her right hand lightly on Character A's palm, they exchange a smile, and Character A leads Character B to the center of the dance floor. The surrounding guests naturally step back to make space, their eyes focused on the pair. Character A raises Character B's right hand with his left, places his right hand lightly on the small of her back, they assume a waltz posture, and step out on the first beat of the main melody, beginning to rotate. The elegant atmosphere of a 19th-century court ball, warm golden tones.
```

## 061 - Girl Approaches Camera In Snowy Forest

*Camera Movement & One-Take.* A girl walks towards the camera in a snowy forest, stops, takes a breath, smiles warmly, and reaches for a snowflake as the camera pulls back.

```text
Extend the video forward by two seconds from the middle segment: The shot smoothly follows as a girl walks slowly towards the camera, stops, gently lifts her head slightly, takes a deep breath in the cold air, and parts her lips slightly.
Extend the video backward by three seconds from the middle segment: The girl finishes rubbing her hands, looks directly at the camera, and blooms into a warm, brilliant smile. She slowly raises one gloved hand to catch a gently falling snowflake. The camera slowly pulls back to a medium-long shot, revealing a sunlit snowy forest path, golden hour backlighting, lens flare, shallow depth of field, and a warm, healing atmosphere.
```

## 062 - Ink-Wash Duel In Misty Bamboo Forest

*Stylized & Non-Real.* A lone swordsman in ink-wash style confronts assassins in a misty bamboo grove, featuring fast-paced, brush-stroke combat and a dramatic final freeze-frame.

```text
Shot 1 [0s-3s] Camera: Medium shot.
Scene: Continue the ink-wash bamboo forest scene from @Image1. The silhouette of a swordsman wearing a bamboo hat and a black robe stands in the center, surrounded by thick fog and swaying bamboo shadows.
Action: The swordsman lightly rests his left hand on his sword hilt, bamboo leaves fall with the wind.
Atmosphere: Silent, oppressive, the grainy texture of ink-wash diffusion is clearly visible.

Shot 2 [3s-8s] Plot introduction, Camera: Close-up.
Plot: The swordsman senses killing intent.
Scene: The camera quickly pushes in for a close-up under the swordsman's bamboo hat.
Details: Sharp, resolute eyes like blades are revealed under the hat's brim. Ink-wash 'sweat beads' slide down his forehead.
Action: The swordsman slowly tightens his right hand on the sword hilt, knuckles turning white. The falling speed of bamboo leaves increases.

Shot 3 [8s-13s] Camera: Fast orbiting.
Scene: The camera orbits the swordsman rapidly.
Plot: Two assassins, also in ink-wash silhouette, charge out from the depths of the bamboo forest, wielding double hooks and a short blade.
Details: The assassins' movements are also composed of ink brushstrokes, flowing like ink traces. The camera quickly sweeps past the assassins' figures, emphasizing speed.

Shot 4 [13s-18s] Camera: Handheld feel, high-speed capture.
Fight: The swordsman suddenly draws his sword, the blade light is a pure white ink-wash crack. The assassins attack with double hooks.
Details:
First strike: The swordsman turns and slashes, the blade collides with the assassin's hooks, bursting forth with countless black-and-white sparks and ink dots with a calligraphic feel.
Second strike: The swordsman feints, uses a bamboo pole to propel himself, and slashes down from above. The assassin rolls to dodge. The bamboo pole is broken, transforming into scattered ink traces.
Third strike: The swordsman's blade tip points directly at the other assassin's throat, the assassin blocks with the short blade, the camera captures the subtle details of ink traces cracking as the blades grind.

Shot 5 [18s-20s] Camera: Slow motion to freeze frame.
Scene: The swordsman's blade stops beside the assassin's neck, the assassin freezes.
Details: The swordsman's bamboo hat is slightly tilted from the fight. The bamboo forest returns to calm, more bamboo leaves flutter.
Atmosphere: The camera slowly pulls back to a medium shot, freezing on the scene of the swordsman sheathing his sword and the assassin falling.
Text (optional): Ink-wash style text appears below the scene: "The Jianghu, merely a stroke of the brush."

Style Note: The entire process maintains the high-contrast black-and-white, ink-wash painting style of `image_0.png`. The movements must have a brushstroke feel, the speed must be fast, and the details must be sufficient (ink drops, sparks, ink trace cracks).
```

## 063 - Elegant Woman's Reflective Journey Through Time

*Multi-Shot Storytelling.* A woman transitions from a sunlit garden to a rainy car, expressing contemplation and melancholy through subtle performance and cinematic visuals.

```text
Shot 1 [0s-8s]
35mm film, retro sunny garden, an elegant woman in a straw hat, black necklace, and white dress stands before a blooming rose wall. The wind ruffles her hair, she gently touches her hat brim, her gaze tender and pensive. The camera slowly pushes in, natural light flares, soft warm tones, shallow depth of field, extremely delicate motion, 4k high quality.

Shot 2 [8s-15s]
Cinematic close-up, the woman slowly removes her straw hat, lowers her head, her expression tinged with faint melancholy and nostalgia. A soft breeze passes, the light and shadow in the frame shift subtly, creating a narrative atmosphere, 35mm film texture, deep and elegant, cinematic lighting.

Shot 3 [15s-23s]
Rear-seat perspective inside a moving car, the same woman in profile, her hand resting on the car door, gazing out the rain-streaked window. Blurred greenery and light outside recede rapidly, the interior light is dim yet warm, her side profile exquisite, highly cinematic emotional feel, real film grain, slow-motion photography, elegant melancholy.

Shot 4 [23s-30s]
Extreme close-up on the face, the woman slowly closes her eyes by the car window, revealing a serene and resolved expression. Raindrops slowly slide down the window glass, the focus gradually shifts to the raindrops on the glass, the background figure blurs, the image gradually fades to black, Wong Kar-wai style cinematic feel, deep and fluid.
```

## 064 - One-Take Water Goddess Emerges From West Lake

*Camera Movement & One-Take.* A water droplet falls into West Lake, coalescing into the goddess 'Xizi' who walks on water, blooming lotuses with each step, culminating in a serene, poster-worthy close-up.

```text
【One-take, slow and beautiful camera movement, no cuts, 15-second long take, mineral pigment texture of rock-color painting collides with 3D rendering, cyan blue × flowing gold color clash】
Global setting: Guofeng rock-color painting texture, mineral pigment granular texture, gold foil texture, strong color clash of cyan blue and flowing gold. The scene is West Lake in the morning mist: the lake surface shows a matte cyan blue wash, golden morning light penetrates the clouds forming Tyndall light beams, the stone pagodas of Three Pools Mirroring the Moon and Leifeng Pagoda are faintly visible in the mist, with lotus leaves and flowers nearby. The main subject is the West Lake water goddess "Xizi": rock-color painting texture, oval face, willow-leaf eyebrows, phoenix eyes, a cinnabar flower diadem dot on her forehead, skin like mutton-fat jade glowing softly, a pale golden halo floating behind her head; high coiled hair bun with a flowing gold lotus hairpin, her skirt and flowing ribbons are made of flowing lake water, cyan blue gradient, with shimmering water light on the surface.
Voiceover and sound effects: Background is soft guzheng and bamboo flute, ambient sounds include subtle water ripples and morning birdsong. From the 8th second, an ethereal, gentle female voice slowly recites: "Yu ba Xi Hu bi Xi Zi——"; the glance-back segment connects with the second half of the line: "Dan zhuang nong mo, zong xiang yi." Slow speech speed, with slight reverberation, lingering charm.
[0-3s: A drop of water]
Extreme close-up, on the edge of a morning lotus leaf, a water droplet gathers plumply, reflecting golden morning light, slowly falling. The camera follows the water droplet tilting down, the droplet drips into the lake, stirring a circle of golden-blue ripples, ripples spreading layer by layer.
[3-7s: Water coalesces into form]
At the center of the ripples, lake water slowly rises, coalescing into the form of the goddess "Xizi": the lake water becomes her cyan blue skirt and semi-transparent flowing ribbons, tiny water currents flow around her body. She slowly rises from the center of the lake, her eyes lightly closed then slowly opening, the flowing gold lotus hairpin glows faintly. The camera slowly orbits her half-lowered eyes and the skirt woven from flowing water.
[7-11s: One step, one lotus]
She walks barefoot slowly on the lake surface, each step causing a circle of golden ripples to spread, lotuses blooming in succession within the ripples. The camera pulls back to a medium full shot: the mist disperses, the three stone pagodas of Three Pools Mirroring the Moon light up with warm lights, Leifeng Pagoda appears in the morning light, weeping willows on the shore brush the water. At the 8th second, the female voiceover begins: "Yu ba Xi Hu bi Xi Zi——" Her flowing ribbons trail long golden-blue water light behind her.
[11-15s: Glance back·Zong Xiang Yi]
She stops walking, glances back towards the camera, the camera slowly pushes in to a medium close-up: morning light falls on her face, the lake water ribbons gently flutter beside her, a few glowing water droplets fall from her hair, turning into fine light points in the air. The voiceover connects with the second half of the line: "Dan zhuang nong mo, zong xiang yi." She smiles faintly, behind her are Leifeng Pagoda in the morning light and the hazy Three Pools Mirroring the Moon. In the final second, the frame completely freezes on her glance-back close-up, freezing into a perfect movie poster composition.
```
