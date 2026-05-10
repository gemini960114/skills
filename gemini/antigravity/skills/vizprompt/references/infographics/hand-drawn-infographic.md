# 手繪風資訊圖模板

本檔案用於生成"手繪 / 筆記本 / 塗鴉 / 暖色 macaron / morandi 霧感"質感的資訊圖：

- 學習筆記 / 知識卡 / 概念圖解
- 公眾號 / 小紅書"手繪種草"圖文
- 教學講義 / 課堂塗鴉
- 旅行手賬 / 美食手賬 / 閱讀筆記
- 活動通知 / 暖系活動海報

特徵：

- 所有線條都有輕微抖動 / 不規則（hand-drawn wobble）
- 配色低飽和、溫暖、像水彩或彩鉛
- 元素之間有大量"留白 + 塗鴉裝飾"
- 字型是手寫感（非電腦字型）
- 顏色填充會"留邊"，像手工上色

> 設計判斷：手繪風是「風格語言」，自由度極高，不同主題（學習 / 美食 / 旅行 / 心情）的具體元素差異極大。**強行 JSON 反而會限制畫面自由度**，因此本模板採用「**結構化自然語言提示詞 + 參數列 + 元素清單**」的混合形式，比純 JSON 更自然。

## 適用範圍

- 學習筆記 / 概念解析 / 知識卡片
- 步驟教程 / how-to / 操作流程的"手繪版"
- 列表 / 清單 / 排行榜的"手繪版"
- 暖系內容（情緒 / 治癒 / 美食 / 旅行）
- 公眾號 / 小紅書 / 社交平臺"手賬風"配圖

## 何時使用

- 使用者提到 "手繪 / 手賬 / sketch notes / 塗鴉 / 筆記 / 課堂筆記 / macaron / morandi / 暖色 / 治癒"
- 使用者希望視覺「親切、好讀、不像 PPT」
- 使用者希望「讀者感覺是真人手畫的」

不要使用：

- 使用者要的是高密度科普因果鏈 / 解剖圖（用 `infographics/legend-heavy-infographic.md`）
- 使用者要的是模組化便當格（用 `infographics/bento-grid-infographic.md`）
- 使用者要的是工程精度的流程圖 / 架構圖（用 `technical-diagrams/`）
- 使用者要的是出版級圖表（用 `academic-figures/publication-chart.md`）
- 使用者要的是真正的治癒系場景插畫（用 `scenes-and-illustrations/healing-scene.md`）

## 缺失資訊優先提問順序

1. 主題（要講什麼？比如"5 種泡咖啡的方法"、"番茄工作法"、"上海 City Walk Top 10"）
2. 資訊條數（建議 3-7 條）
3. 配色基調（macaron 暖奶油 / morandi 霧感 / kraft 牛皮紙 / 黑板色）
4. 是否有人物 / 吉祥物（一隻貓 / 簡筆小人 / 無人物）
5. 比例（小紅書 3:4 豎版 / 公眾號 16:9 橫版 / 1:1 方版）
6. 是否要配色塊「條目分割槽」還是"自由排布"

## 主模板：手繪風資訊圖

📖 描述

整張圖是一張「像被人在筆記本上手畫出來」的資訊圖：暖色背景 + 手寫體大標題 + 3-7 條手繪卡片 / 圓圈 / 氣泡 + 簡筆圖示 + 塗鴉裝飾 + 手繪箭頭連線。

📝 提示詞（結構化自然語言模板）

```
A hand-drawn educational infographic in the style of a high-quality bullet journal page.

Topic: {argument name="topic" default="番茄工作法的 5 個核心步驟"}.

Aspect ratio: {argument name="aspect_ratio" default="3:4 portrait"}.

Background:
- Warm {argument name="background_color" default="cream / off-white"} paper texture with subtle grain.
- Optional washi-tape strips in the corners (diagonal stripes, muted tones).
- DO NOT use pure white or pure black background.

Color palette:
- {argument name="palette" default="macaron"} — describe colors:
  - macaron: warm cream #F5F0E8 background, muted blue #A8D8EA, lavender #D5C6E0, mint #B5E5CF, peach #F8D5C4, coral red #E8655A accent
  - morandi: dusty sage, terracotta, mustard, taupe, soft brick
  - kraft: kraft paper background, dark brown ink, tomato red accent, muted navy
  - chalkboard: dark slate background, white chalk, yellow / coral / mint chalk highlights
- Limit to 4-5 colors total. Use the accent color sparingly for emphasis.

Title:
- "{argument name="title" default="番茄工作法 5 步"}" in large hand-lettered calligraphy at the top.
- Title sits inside a hand-drawn frame: irregular oval, scalloped rectangle, or wavy banner.
- Optional subtitle below in smaller handwritten print.

Body:
- {argument name="item_count" default="5"} information items.
- Each item is presented as a hand-drawn card / rounded rectangle / cloud bubble / circle, with:
  - A number badge (1, 2, 3 ... in a circle, drawn by hand)
  - Item title in bold handwritten text
  - 1-2 lines of body text in neat handwritten print
  - A simple doodle icon (1-2 strokes, NOT realistic) representing the item
- Items can be arranged: vertical list / 2-column grid / circular wheel / winding path.

Doodle decorations (sprinkle naturally, not symmetrically):
- Tiny stars, sparkles, hearts, arrows-curvy, dotted lines, exclamation marks
- Hand-drawn underlines and circle-marks for emphasis on key words
- Smiley / frowny faces (😊 ☹) as quality indicators where relevant
- Optional: a single mascot character (a cat / a stick-figure person / a coffee cup with face) as the "narrator"

Style enforcement:
- ALL lines have visible hand-drawn wobble — never perfectly straight
- ALL color fills leave a tiny gap before the outline (hand-painted feel)
- All text is hand-lettered — NO computer fonts, NO Helvetica, NO Arial
- Slight imperfection is intentional — it should NOT look digitally precise
- The whole image feels like a single page from someone's notebook

Composition:
- Generous whitespace (~30-40% of the canvas)
- Information hierarchy: title > item titles > body > doodle decorations
- Items are large enough to be readable; do not cram

Language: {argument name="language" default="中文（手寫體感）"}; technical / proper nouns can stay in English.
```

### 引數策略

- **必問**：`topic`、`item_count`、`aspect_ratio`
- **可預設**：`palette`（預設 macaron）、`background_color`（跟隨 palette）、`language`（預設中文）
- **可隨機**：mascot 是否出現 / 用什麼吉祥物、doodle 裝飾的具體造型、卡片形狀（圓角矩形 / 雲朵 / 圓圈）

### 自動補全策略

- 使用者只給 `topic` 時：
  - 自動決定 5 條要點（除非主題明顯是 list 類的，比如"7 個習慣"那就用 7 條）
  - 自動用 macaron 配色
  - 自動用 3:4 portrait（小紅書友好）
  - 不放 mascot（除非主題適合，如"貓咪護理 5 步"自然出現貓）
- 使用者說"我要小紅書風" → palette 自動選 macaron 或 morandi，aspect 3:4
- 使用者說"教學 / 課堂" → palette 自動選 chalkboard 或 macaron
- 使用者說"暖系 / 美食 / 治癒" → palette 自動選 morandi 或 kraft

## 變體 1：黑板粉筆風手繪資訊圖

把上面提示詞裡的 palette 換成 `chalkboard`：

```
Background: dark slate / chalkboard green (#2F4F4F) with faint chalk dust texture.
Lines and text: white chalk with visible pressure variation.
Highlights: yellow chalk for important keywords, coral / mint chalk for accents.
Decorations: hand-erased smudges in the background, chalk arrows, chalk underlines.
```

適用：教學講義、班級文化牆、知識科普"上課"感。

## 變體 2：牛皮紙 / Kraft 暖系手繪資訊圖

把背景換成 `kraft paper`：

```
Background: warm kraft paper #C9A876 with visible paper fibers.
Lines and text: dark espresso brown #3E2723 with hand-drawn wobble.
Accents: tomato red #E63946, muted teal #457B9D.
Decorations: stamp marks, dotted borders, thread / yarn doodles, postal style elements.
```

適用：復古手賬、咖啡 / 烘焙 / 慢生活、文創周邊。

## 變體 3：單色鉛筆 / 極簡手繪資訊圖

```
Background: pure cream #FAF7F2.
Lines: single dark color (charcoal #2B2B2B or sepia #6B4423) only.
NO multi-color fills. Use varying line weight and cross-hatching for shading.
Decorations: minimal — just dotted lines and small symbols.
```

適用：剋制 / 文藝 / 嚴肅但仍要手繪感的內容（哲學、讀書筆記）。

## 避免事項

- 任何元素出現完美的幾何形狀 / 直線 → 失去手繪靈魂
- 使用 Helvetica / Arial / 思源黑等電腦字型 → 立刻塑感
- 顏色填滿到邊緣沒有留白 → 像電子貼紙，不像手畫
- 漸變 / 陰影 / 玻璃質感 / 金屬質感 → 完全跑偏
- 一張圖 ≥ 6 種主色 → 失去手賬的剋制感
- 文字行距過緊 / 字號一致 → 失去層次感
- 裝飾物太多到喧賓奪主 → 資訊讀不出來
- 所有資訊卡造型完全一致（一模一樣的圓角矩形 ×5）→ 失去手繪的有機感
