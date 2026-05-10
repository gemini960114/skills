---
name: vizprompt
description: 當使用者要生成視覺圖像提示詞或 JSON prompt，包括：商品圖、白底主圖、電商主圖、海報、品牌識別、吉祥物、包裝設計、標籤設計、地圖、旅遊路線圖、UI mockup、直播樣機、介面設計、人物肖像、角色設定、貼紙表情包、頭像、插畫、場景圖、分鏡板、TVC、漫畫、資訊圖、學術論文圖、系統架構圖、流程圖、時序圖、技術示意圖等任何視覺生成需求時，讀取 vizprompt/references/ 範本庫，輸出結構化繁體中文 JSON 渲染提示詞。
---

# VizPrompt — GPT Image 2 視覺提示詞生成 Skill

此 skill 讓你在對話中直接生成可用於 GPT Image 2、Gemini Imagen 或 Midjourney 的 **結構化 JSON 提示詞**。

範本庫已內建於 skill 目錄中：`vizprompt/references/`（共 18 分類、90+ 範本），使用時直接從本目錄讀取，不依賴外部 Web App。

---

## 語言規定（最高優先）

**所有輸出一律使用繁體中文**，包括欄位值、說明文字、陣列項目。絕對禁止輸出簡體中文或英文說明文字。

---

## 工作流程（ReACT 推理）

依照「先觀察、再行動」循環：

### Step 1：對照範本索引，確認分類

閱讀本文件下方的「範本索引」，根據使用者需求判斷最貼近的**分類目錄**（例如 `product-visuals/`、`ui-mockups/`）。

### Step 2：讀取 1–2 個最相關範本

從 `vizprompt/references/<分類>/<範本>.md` 讀取完整範本骨架（含 JSON 結構、引數策略、提問順序）。

- 若讀完發現範本與需求不符 → **說明原因，改讀另一個**，不強迫使用不合適的範本

### Step 3：判斷是否需要提問

只在以下情境提問：
- 主體身份不明（主播是誰、商品是什麼）
- 核心文案 / 價格 / UI 文字是畫面中心組成
- 多個目標互相衝突

其他缺失欄位 → 使用範本預設值或合理推斷，直接繼續。

### Step 4：對應欄位，輸出 JSON

輸出前先說明：選了哪個範本、為什麼、使用者輸入如何對應到各欄位。
然後輸出符合範本骨架的完整 JSON 提示詞。

---

## 輸出格式規範

最終輸出**必須**是一個純 JSON 物件，包含：

```json
{
  "type": "範本類型（繁體中文）",
  "goal": "圖像目標描述（繁體中文）",
  "reference_0": "若有上傳圖片，描述圖片內容；無圖片則省略此欄位",
  "...": "範本核心欄位，依所選範本骨架填寫",
  "constraints": {
    "do_not": ["..."],
    "must": ["..."]
  },
  "_meta": {
    "templates_used": ["所選範本相對路徑"],
    "notes": "選用理由與欄位對應說明"
  }
}
```

- 所有欄位值一律使用**繁體中文**
- 不加 markdown code block 包裝，直接輸出純 JSON
- `_meta` 欄位供使用者理解選範本邏輯，不影響圖像生成

---

## 重要規則

- 只讀取最相關的 1–2 個範本，不一次讀整個 references/
- 優先自己做合理預設並繼續執行，不要反覆詢問無關緊要的細節
- 不負責出圖，使用者拿到 JSON 後自行送往圖像生成工具

---

## 範本索引（18 分類）

> 選擇策略：只讀最貼近需求的具體範本檔案，不要一次讀完整個分類目錄。

### 1. 方法論總文件

- `vizprompt/references/prompt-writing.md` — 模板設計規範、欄位設計原則、引數分類策略

適用於：尚未確定 JSON 結構時、需要判斷欄位應問 / 預設 / 隨機時。

---

### 2. UI Mockups（`vizprompt/references/ui-mockups/`）

介面 + 內容樣機視覺。

- `live-commerce-ui.md` — 電商直播帶貨截圖樣機（主播 + 聊天區 + 禮物區 + 商品卡）
- `social-interface-mockup.md` — 社交平臺動態詳情頁樣機（Twitter/X、小紅書、微博、Threads）
- `product-card-overlay.md` — 落地頁 hero / 詳情頁主圖（人物 + 商品 + 賣點 + 價格）
- `chat-interface-scene.md` — 聊天 / 對話介面樣機（iMessage、微信、群聊、AI 助手）
- `short-video-cover-ui.md` — 短影片封面 / 直播縮圖（YouTube、抖音、B 站、VTuber stream）
- `landing-page-case-study.md` — 深色 SaaS / 營銷 case study 長頁面 UI mockup

---

### 3. Product Visuals（`vizprompt/references/product-visuals/`）

以商品為視覺中心。

- `exploded-view-poster.md` — 產品爆炸視圖海報（主體垂直堆疊 + callout + logo）
- `white-background-product.md` — 電商純白底主圖（單品 / 多角度 / 極簡營銷疊層）
- `premium-studio-product.md` — 高階影棚商業產品圖（雜誌廣告級氛圍）
- `packaging-showcase.md` — 禮盒 / 包裝展示圖（外盒 + 內容物展示）
- `lifestyle-product-scene.md` — 生活方式產品場景圖（商品出現在真實場景中）
- `ecommerce-marketing-board.md` — 中式電商超複合銷售看板（主圖 + 詳情頁 + 賣點 + 場景組合）

---

### 4. Maps（`vizprompt/references/maps/`）

地圖類視覺。

- `food-map.md` — 城市美食手繪地圖（編號點位 + 圖例 + 中心吉祥物）
- `travel-route-map.md` — 旅行路線圖（多日行程 / 單日 city walk / 戶外路線）
- `illustrated-city-map.md` — 城市風貌插畫地圖（地標 + 文化元素）
- `store-distribution-map.md` — 品牌門店 / 服務覆蓋分佈圖
- `itinerary-day-trip-map.md` — 一日遊 split 海報（左行程卡 + 右奇幻寫實地圖，5–7 站點嚴格對齊）

---

### 5. Slides & Visual Docs（`vizprompt/references/slides-and-visual-docs/`）

一頁講清楚一件事的視覺文件。

- `dense-explainer-slides.md` — 高密度講解 Slide（Irasutoya × 霞關混合風格）
- `policy-style-slide.md` — 政策 / 政府公告 / 白皮書風格說明 Slide
- `visual-report-page.md` — 商業報告執行摘要 / 投資人簡報 / 年報概覽頁
- `educational-diagram-slide.md` — 教學示意圖（概念 / 機制 / 流程分解）

---

### 6. Poster & Campaigns（`vizprompt/references/poster-and-campaigns/`）

品牌主視覺 + campaign + banner + 雜誌封面。

- `brand-poster.md` — 品牌主海報（產品 / 人物 / 純文字主張）
- `campaign-kv.md` — Campaign Key Visual + 衍生 layout 系統
- `banner-hero.md` — Web hero / 落地頁 / app banner（橫向構圖 + CTA）
- `editorial-cover.md` — 雜誌 / 期刊 / 出版物封面
- `biomimetic-concept-poster.md` — 仿生工業設計概念海報（自然原型 → 演化條 → hero render）
- `vintage-editorial-infographic.md` — 復古檔案 / 1940s 編輯式資訊圖海報（Bell Labs 風）
- `character-catalog-poster.md` — 同一角色多版本資訊圖海報（星座 / 元素 / 朝代系列卡片）
- `lineup-comparison-poster.md` — 系列產品 lineup 對比資訊圖海報（30+ SKU 同圖 + 圖例 + 等級 key）

---

### 7. Portraits & Characters（`vizprompt/references/portraits-and-characters/`）

人物視覺。

- `professional-portrait.md` — 職業級商務肖像（LinkedIn / 團隊頁 / 媒體配圖）
- `founder-portrait.md` — 創始人媒體大片肖像（戲劇燈光 + 留標題位）
- `virtual-host.md` — VTuber / 虛擬主播個人卡 + 直播預覽
- `character-sheet.md` — 角色綜合設定稿（三視圖 + 表情 + 服裝 + 配色板）
- `pose-reference-sheet.md` — N×N 姿勢 / 動作字典參考表（舞蹈 / 戰鬥 / 健身）

---

### 8. Scenes & Illustrations（`vizprompt/references/scenes-and-illustrations/`）

氛圍 + 故事 + 情緒的插畫類視覺。

- `healing-scene.md` — 治癒系日常 / 季節場景插畫
- `concept-scene.md` — 電影感概念大場景 / IP key art
- `picture-book-scene.md` — 童書 / 繪本內頁 / 節日卡片
- `minimalist-mood-scene.md` — 極簡留白氛圍圖 / 文學性桌布

---

### 9. Editing Workflows（`vizprompt/references/editing-workflows/`）

基於現有圖片做編輯的圖改任務。

- `background-replacement.md` — 背景替換（商品 / 人像 / 戶外 / 棚景）
- `local-object-replacement.md` — 區域性物件替換（配合或不配合蒙版）
- `object-removal.md` — 雜物 / 路人 / 電線 / 瑕疵去除
- `product-retouching.md` — 產品精修（光澤 / 標籤 / 陰影 / 瑕疵）
- `portrait-local-edit.md` — 人像局部修改（髮型 / 服裝 / 妝容 / 配飾）

---

### 10. Avatars & Profile（`vizprompt/references/avatars-and-profile/`）

風格化頭像 / 人設 / 網格 / 貼紙 / 系列肖像。

- `style-transfer-selfie.md` — 把參考圖人物轉成 cosplay / 哥特 / 復古膠片 / 偶像寫真等任意風格
- `character-grid-portrait.md` — 同一角色 n×n 網格肖像（多職業 / 多表情 / 多朝代 / 多風格）
- `themed-3d-icon.md` — Kawaii 3D / Minecraft / 擬物 3D 應用圖示式頭像
- `sticker-set.md` — 貼紙套裝 / 表情包合集（獨立元素 + 描邊 + 標籤）
- `cultural-portrait-series.md` — 朝代 / 神話 / 文學 / 民族系列肖像

---

### 11. Storyboards & Sequences（`vizprompt/references/storyboards-and-sequences/`）

多分鏡 / 漫畫 / 流程步驟等敘事性序列視覺。

- `four-panel-comic.md` — 4 格漫畫 / 諷刺漫畫（起承轉合 + 對話氣泡）
- `manga-spread-page.md` — 單頁 / 跨頁漫畫分鏡（不規則格子 + 對話 + 心聲）
- `anime-key-visual.md` — 單圖動漫 KV / 輕小說封面 / IP 海報
- `character-relationship-diagram.md` — 角色關係圖海報（卡片 + 關係連線 + 圖例）
- `recipe-process-flowchart.md` — 食譜 / 教程 / 流程步驟圖（編號 + 插圖 + 說明）
- `product-tvc-storyboard.md` — 產品 TVC 商業廣告分鏡板（9-panel 實拍質感 + 鏡頭描述 + 時長）
- `cinematic-storyboard-grid.md` — 電影感敘事分鏡 contact sheet（3×4 / 4×4，連續敘事 + cinematic still）
- `process-photo-board.md` — 真人 cinematic 流程板（裝備穿戴 / 化妝 / 訓練 / 操作分解）

---

### 12. Grids & Collages（`vizprompt/references/grids-and-collages/`）

多面板網格 / 拼貼 / 立項 board 類視覺。

- `banner-grid-2x2.md` — 2×2 營銷 banner 套裝（一次出 4 張統一系列設計）
- `lookbook-grid.md` — 7 日 lookbook / 9 宮 self-care / TOP N 清單圖
- `mixed-style-multi-panel.md` — 多風格混合拼貼（同一主體不同畫風演繹）
- `anime-pitch-board.md` — 動漫 / 遊戲 / 影視立項 pitch board（KV + 角色 + 世界觀 + 文案）
- `ad-banner-multi-grid.md` — 多行業 / 多主題混合廣告 banner 網格（每格獨立行業 + 風格 + 文案）

---

### 13. Branding & Packaging（`vizprompt/references/branding-and-packaging/`）

品牌識別系統 / 吉祥物 / 包裝設計類視覺。

- `brand-identity-board.md` — 品牌識別系統板（logo + 配色 + 字型 + 應用 mockup）
- `mascot-brand-kit.md` — 吉祥物多面板品牌識別套裝（主形象 + 三視圖 + 表情 + 應用）
- `cosmetic-packaging.md` — 化妝品 / 護膚品 單瓶 / 系列 / 禮盒包裝
- `beverage-label-design.md` — 飲料 / 食品 / 調味品標籤設計（國潮 / 日式 / 西式）
- `full-mascot-brand-doc.md` — 18+ 模組大型品牌識別 + 吉祥物全流程文件
- `character-merch-board.md` — IP 角色 + 周邊 / 包裝 / 海報 / 社交 profile 多元素綜合品牌板

---

### 14. Typography & Text Layout（`vizprompt/references/typography-and-text-layout/`）

以文字為主視覺的字面優先 / 雙語版式。

- `title-safe-poster.md` — 大字主張型海報（日式高能量 / 瑞士極簡 / 復古印刷）
- `bilingual-layout-visual.md` — 中英 / 中日雙語版式視覺（文化 / 學術 / 跨文化品牌）

---

### 15. Assets & Props（`vizprompt/references/assets-and-props/`）

圖示集 / 遊戲截圖等成套素材 / 遊戲資產類視覺。

- `retro-skeuomorphic-icons.md` — 擬物 / Y2K / 畫素圖示集（成套統一風格）
- `game-screenshot-mockup.md` — 遊戲內截圖 mockup（HUD + 字幕 + 任務面板）

---

### 16. Academic Figures（`vizprompt/references/academic-figures/`）

論文 / 頂會投稿 / 學術海報 / 答辯 PPT / 期刊投稿 Graphical Abstract 配圖。

整體偏白底 + 出版物字型 + 幾何精確 + 低飽和工程色（深藍 / 灰藍 / 黑灰，≤3 主色）。**嚴格禁止虛構定量資料**。

CS / CV / ML 方向：
- `method-pipeline-overview.md` — 方法總覽圖 / pipeline figure（多 stage 塊 + 資料流）
- `neural-network-architecture.md` — 神經網路架構圖（layer 塊 + tensor shape + 跳連）
- `qualitative-comparison-grid.md` — 多方法 qualitative 對比網格（行 = 樣本，列 = 方法）

工程 / 自然科學 / 答辯通用：
- `scientific-schematic.md` — 概念 / 原理 / 實驗裝置示意圖（自由度高）
- `mechanism-diagram.md` — 機理示意圖 / 因果鏈路 / 轉化路徑
- `multi-condition-comparison.md` — 多工況 / 多條件結果對比圖（2×2 / 1×N / M×N）
- `publication-chart.md` — publication-ready 資料圖表（bar / line / scatter / heatmap / box）

總覽 / 摘要 / 答辯首頁：
- `graphical-abstract.md` — 期刊投稿 Graphical Abstract（橫向 4 段式 / 中心展開 / 方形 / 豎版）
- `research-overview-poster.md` — 開題 / 答辯 / 彙報首頁研究總覽圖

> 選擇策略：CS/CV/ML 論文首選 `method-pipeline-overview` + `qualitative-comparison-grid`；工程 / 能源方向首選 `mechanism-diagram` + `multi-condition-comparison`；投稿期刊摘要圖用 `graphical-abstract`；答辯 PPT 首頁用 `research-overview-poster`。

---

### 17. Infographics（`vizprompt/references/infographics/`）

資訊圖 / 高密度科普 / 手繪資訊圖 / KPI 儀表盤等資訊視覺化大圖。

- `legend-heavy-infographic.md` — 高圖例密度科普 / 因果鏈 / 演化 / 解剖圖（雙語）
- `hand-drawn-infographic.md` — 手繪風資訊圖（macaron / morandi / 黑板 / 牛皮紙）
- `bento-grid-infographic.md` — 便當格模組化資訊圖（高密度多模組 widget 排布）
- `comparison-infographic.md` — 二元 / 多元對比資訊圖（A vs B / 套餐檔位 / 誤區 vs 正解）
- `step-by-step-infographic.md` — 步驟教程資訊圖（插畫感、溫暖；非工程流程圖）
- `kpi-dashboard-infographic.md` — KPI 儀表盤式資訊圖（年度回顧 / Wrapped / 業務 dashboard）

---

### 18. Technical Diagrams（`vizprompt/references/technical-diagrams/`）

系統架構 / 流程 / 時序 / 狀態機 / ER / 思維導圖 / 網路拓撲等工程示意圖。

統一暗色 grid 背景 + 等寬字型 + 角色編碼配色，每個模板附 light 變體。

⚠️ 生成的是 **PNG 點陣圖**，不是可編輯 SVG。

- `system-architecture.md` — 系統架構圖（前端 + 後端 + DB + 快取 + 佇列 + 外部）
- `flowchart-decision.md` — 流程圖 / 決策圖（BPMN 形狀語義 + Yes/No 分支）
- `sequence-diagram.md` — 時序圖（actor + lifeline + 訊息箭頭 + 啟用條）
- `state-machine.md` — 狀態機 / 生命週期圖（state + transition + guard / action）
- `er-diagram.md` — ER 圖 / 資料模型圖（實體 + 欄位 + PK/FK + crow's foot 關係）
- `mind-map-tech.md` — 技術主題思維導圖（中央 + 放射式分支）
- `network-topology.md` — 網路拓撲圖（裝置 glyph + zone / VPC + 頻寬 / 協議標）

---

## 何時提問

只在這些資訊缺失且**會顯著影響結果**時提問：

- 沒有明確的 Prompt 目標
- 主體身份或視覺類型決定結果走向（主播是誰、商品是什麼）
- 商品 / 價格 / 文案 / UI 文字是畫面核心組成部分
- 使用者同時表達了多個互相衝突的目標

除此之外，優先自己做合理預設並繼續執行。

---

## 重要約束

- 所有欄位值一律使用**繁體中文**，不輸出簡體或英文說明文字
- 只讀取最相關的 1–2 個範本，不一次讀取整個 references/
- 最終只輸出純 JSON，不加任何說明文字或 markdown code block
- 不負責出圖；使用者拿到 JSON 後自行送往圖像生成工具
