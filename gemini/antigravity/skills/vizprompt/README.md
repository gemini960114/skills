# VizPrompt Skill

> GPT Image 2 視覺提示詞生成 — Cowork Skill 獨立套件

---

## 這是什麼

`vizprompt` 是一個可直接安裝到 Claude Cowork 的 Skill，讓你在對話中輸入視覺需求，Claude 自動選取最合適的範本、輸出結構化繁體中文 JSON 提示詞，可直接用於 GPT Image 2、Gemini Imagen、Midjourney 等圖像生成工具。

與 `web-studio` Web App 的差別：

| | Web App（`backend/`） | VizPrompt Skill |
|---|---|---|
| 使用方式 | 瀏覽器介面 | Cowork 對話 |
| 推理引擎 | Gemini ReACT Agent | Claude 對話推理 |
| 串流顯示 | SSE 即時推理步驟 | 對話回覆 |
| 多人使用 | ✅（Express Server） | 單人 |
| 適合情境 | 正式產出、存檔、分享 | 快速單次生成、邊討論邊調整 |

---

## 目錄結構

```
vizprompt/
├── SKILL.md          ← Skill 主文件（Claude 讀取的工作指引）
├── README.md         ← 本說明文件（給人類看）
└── references/       ← 範本庫（與 backend/references/ 內容相同）
    ├── prompt-writing.md
    ├── academic-figures/
    ├── assets-and-props/
    ├── avatars-and-profile/
    ├── branding-and-packaging/
    ├── editing-workflows/
    ├── grids-and-collages/
    ├── infographics/
    ├── maps/
    ├── portraits-and-characters/
    ├── poster-and-campaigns/
    ├── product-visuals/
    ├── scenes-and-illustrations/
    ├── slides-and-visual-docs/
    ├── storyboards-and-sequences/
    ├── technical-diagrams/
    ├── typography-and-text-layout/
    └── ui-mockups/
```

---

## 範本庫

共 **18 分類、90+ 個結構化 JSON 範本**，涵蓋：

| 分類 | 適用場景 |
|---|---|
| `ui-mockups/` | 電商直播、社交介面、聊天介面、短影片封面、SaaS 落地頁 |
| `product-visuals/` | 白底主圖、影棚商品、爆炸視圖、禮盒包裝、生活場景 |
| `maps/` | 美食地圖、旅行路線、城市插畫、門市分佈、一日遊海報 |
| `slides-and-visual-docs/` | 講解 Slide、政策說明、商業報告、教學示意圖 |
| `poster-and-campaigns/` | 品牌海報、Campaign KV、Banner、雜誌封面、仿生概念海報 |
| `portraits-and-characters/` | 商務肖像、創始人大片、VTuber、角色設定稿、姿勢參考表 |
| `scenes-and-illustrations/` | 治癒插畫、電影感場景、繪本、極簡氛圍圖 |
| `editing-workflows/` | 背景替換、物件移除、產品精修、人像局部修改 |
| `avatars-and-profile/` | 風格轉換頭像、網格肖像、3D 圖示頭像、貼紙套裝 |
| `storyboards-and-sequences/` | 4 格漫畫、TVC 分鏡、電影分鏡、流程板、角色關係圖 |
| `grids-and-collages/` | 2×2 Banner、Lookbook、多風格拼貼、動漫立項板 |
| `branding-and-packaging/` | 品牌識別、吉祥物套裝、化妝品包裝、飲料標籤 |
| `typography-and-text-layout/` | 大字主張海報、中英雙語版式 |
| `assets-and-props/` | 擬物圖示集、遊戲截圖 mockup |
| `academic-figures/` | 論文 pipeline 圖、神經網路架構、學術海報、Graphical Abstract |
| `infographics/` | 高密度科普圖、手繪資訊圖、便當格、KPI 儀表盤 |
| `technical-diagrams/` | 系統架構圖、流程圖、時序圖、ER 圖、思維導圖 |

---

## 使用方式

### 在 Cowork 安裝

將整個 `vizprompt/` 資料夾安裝為 Cowork Skill。安裝後，直接在對話中描述視覺需求即可觸發。

### 觸發範例

以下範例涵蓋各主要分類，複製貼上即可啟動 skill：

#### 🛒 商品 / 電商

```
幫我生成一份高端護膚品三瓶白底電商主圖的提示詞，磨砂玻璃瓶身，金屬滴管，要能直接上架淘寶
```

```
我想要一份產品爆炸視圖海報的 JSON，商品是無線降噪耳機，黑色，需要 callout 標示三個核心賣點
```

```
生成一份電商超複合銷售看板提示詞，商品是有機燕麥奶，要包含主圖、詳情頁、使用步驟、場景圖
```

#### 🗺️ 地圖 / 旅遊

```
我要一份台南一日遊 split 海報，包含赤崁樓、安平古堡、花園夜市、林百貨五個站點，復古插畫風格
```

```
幫我做一份台灣連鎖咖啡品牌全台門市分佈圖提示詞，扁平化風格，綠色主色系，適合投影片使用
```

#### 🎨 海報 / 品牌

```
為健康科技新創生成 Campaign Key Visual 提示詞，主題是「讓身體說話」，人物 + 數據視覺化，深色背景
```

```
幫我設計一個抹茶飲料品牌的標籤設計提示詞，日式和風，竹葉插圖，玻璃瓶裝，高質感
```

```
生成一份品牌吉祥物套裝提示詞，角色是一隻戴眼鏡的小熊貓，科技感，要包含三視圖、表情包、應用場景
```

#### 🖥️ UI / 介面

```
生成一份電商直播 UI 樣機提示詞，主播是年輕女性，商品是口紅，需要聊天區、禮物飄屏、商品卡
```

```
我要一份 SaaS 產品落地頁 case study 的深色 UI mockup，主題是 AI 寫作工具，要有資料卡和 CTA
```

#### 👤 人物 / 角色

```
幫我生成一份創始人媒體大片肖像提示詞，男性，40 歲，深色西裝，戲劇側光，右側留白放標題
```

```
生成十二星座女子圖鑑海報的 JSON，同一角色 12 個版本，各有不同主題色和服裝，anime 風格
```

```
我要一套角色貼紙表情包，主角是一隻懶懶的橘貓，8 個表情，白底描邊，可用於 LINE 貼圖
```

#### 📊 資訊圖 / 學術

```
生成一份手繪風資訊圖提示詞，主題是咖啡的品種與產地，macaron 配色，溫暖插畫感
```

```
我要一份論文 pipeline 圖，方法名稱是 DualStreamNet，三個 stage：特徵提取、跨模態融合、輸出解碼
```

```
生成年度業務 KPI 儀表盤資訊圖提示詞，包含營收、用戶成長、轉換率三個核心指標，深色商務風
```

#### 🎬 分鏡 / 敘事

```
幫我做一份產品 TVC 分鏡板提示詞，商品是運動飲料，9 個鏡頭，30 秒廣告，戶外運動場景
```

```
生成一份 3×4 電影感敘事分鏡 contact sheet，主題是太空人在火星發現古文明，cinematic 寫實風格
```

#### ⚙️ 技術圖 / 系統圖

```
幫我畫一張微服務系統架構圖提示詞，包含前端、API Gateway、三個後端服務、Redis、PostgreSQL
```

```
生成一份使用者登入流程的時序圖提示詞，actors 包含 Browser、Auth Service、Database，暗色 grid 背景
```

### 輸出格式

Claude 輸出純 JSON，例如：

```json
{
  "type": "白底電商主圖",
  "goal": "高端護膚品三瓶組合白底主圖",
  "subject": {
    "product_name": "玻尿酸精華三件組",
    "visual_description": "磨砂玻璃瓶身，金屬滴管，由左至右排列"
  },
  "background": { "type": "純白", "shadow": "輕微底部柔光陰影" },
  "constraints": {
    "must": ["三瓶等距排列", "標籤文字清晰可讀"],
    "do_not": ["加入裝飾道具", "背景出現顏色斑塊"]
  },
  "_meta": {
    "templates_used": ["vizprompt/references/product-visuals/white-background-product.md"],
    "notes": "使用白底電商主圖範本，三瓶組合對應變體 1 多角度組合白底"
  }
}
```

拿到 JSON 後，自行貼入 GPT Image 2 或其他圖像生成工具執行。

---

## 範本同步

`vizprompt/references/` 是從 `backend/references/` 複製而來。若 Web App 的範本有更新，執行以下指令同步：

**Windows（PowerShell）：**
```powershell
Copy-Item -Recurse -Force ".\backend\references\*" ".\vizprompt\references\"
```

**macOS / Linux：**
```bash
cp -r backend/references/. vizprompt/references/
```

---

## 與 Web App 共用的核心邏輯

| 元件 | Web App | VizPrompt Skill |
|---|---|---|
| 範本庫 | `backend/references/` | `vizprompt/references/`（複本） |
| 推理規則 | `backend/SKILL.md` 的 System Prompt | `vizprompt/SKILL.md` |
| 輸出格式 | 完全相同的 JSON 結構 | 完全相同的 JSON 結構 |
| 工具呼叫 | Gemini function calling | Claude 直接讀取 references/ |

---

## 授權與維護

此 Skill 為 `web-studio` 專案的一部分，由同一份範本庫驅動。
範本索引與欄位規範詳見 `vizprompt/references/prompt-writing.md`。
