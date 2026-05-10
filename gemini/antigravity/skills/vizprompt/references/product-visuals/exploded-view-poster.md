# 產品爆炸檢視海報模板

本檔案用於生成“將一個完整產品垂直堆疊展開成內部元件 + callout 標註 + 頂部宣傳文案 + 底部品牌區”的高階產品海報。

代表案例：

- VR 頭顯爆炸檢視
- 手機內部結構爆炸圖
- 智慧音箱拆解圖
- 無線耳機爆炸圖
- 高階家電拆解圖
- 相機 / 鏡頭元件展開圖
- 戶外裝備拆解圖

## 適用範圍

- 高階產品釋出主視覺
- 詳情頁“技術亮點”單圖
- 工程美學展示
- 內部結構教育圖
- 媒體級技術海報

## 何時使用

- 使用者提到“爆炸檢視 / 拆解圖 / 內部結構 / exploded view”
- 使用者要展示產品工程結構 / 模組化設計 / 技術細節
- 使用者希望視覺風格偏“硬核工程感 + 商業海報”

不要使用：

- 使用者只要白底產品圖（用 `white-background-product.md`）
- 使用者只要場景化產品圖（用 `lifestyle-product-scene.md`）
- 使用者要的是包裝展示（用 `packaging-showcase.md`）

## 缺失資訊優先提問順序

1. 產品是什麼（具體型號或類目）
2. 你希望突出幾個元件（典型 6-9 個）
3. 品牌名 / 主標語 / 副標語
4. 顏色基調（柔和漸變 / 純黑 / 極光 / 深空）
5. 是否需要雙語 callout（中文 + 英文）
6. 標註佈局：左右兩側分佈 / 頂部底部分佈 / 單側分佈

## 主模板：垂直爆炸檢視 + 雙側 callout

📖 描述

主體在畫面中央垂直堆疊展開為多個層級，左右兩側分佈 callout 標籤，頂部為產品名 + 主標語，底部為收束文案 + 品牌 logo。

📝 提示詞

```json
{
  "type": "產品爆炸檢視海報",
  "goal": "生成一張高科技、工程美學風格的產品海報，主體為產品的垂直爆炸檢視，左右輔以技術 callout，整體可作為釋出會主視覺或詳情頁技術亮點圖",
  "subject": "{argument name=\"product\" default=\"VR 頭顯\"}",
  "style": {
    "rendering": "{argument name=\"render style\" default=\"簡潔的高科技 3D 渲染，攝影棚燈光，發光裝飾\"}",
    "background_color": "{argument name=\"background color\" default=\"柔和的紫藍色漸變\"}",
    "lighting": "{argument name=\"lighting\" default=\"攝影棚頂光 + 微弱邊緣光，元件之間存在淡淡發光氣氛\"}"
  },
  "header": {
    "logo": "{argument name=\"product brand mark\" default=\"∞ Meta Quest 3\"}",
    "subtitle": "{argument name=\"main catchphrase\" default=\"以全新的結構，重塑全新的現實。\"}"
  },
  "layout": {
    "centerpiece": "{argument name=\"centerpiece description\" default=\"VR 頭顯的垂直堆疊爆炸檢視，從下到上展示 9 層不同內部元件：外殼、攝像頭感測器、帶晶片的主機板、Pancake 透鏡、內部框架、電池組、側帶、頂部頭帶和麵部介面襯墊\"}",
    "callout_layout": "{argument name=\"callout layout\" default=\"左右兩側均勻分佈\"}",
    "callout_labels": {
      "count": "{argument name=\"callout count\" default=\"8\"}",
      "left_side": [
        "{argument name=\"left callout 1\" default=\"Snapdragon® XR2 Gen 2\\n卓越的處理效能，帶來實時沉浸體驗。\"}",
        "{argument name=\"left callout 2\" default=\"可調節 IPD 機構\\n為廣大使用者提供舒適的佩戴感。\"}",
        "{argument name=\"left callout 3\" default=\"精密設計的頭帶\\n追求舒適與穩定的工程學設計。\"}"
      ],
      "right_side": [
        "{argument name=\"right callout 1\" default=\"前面板\\n精緻的設計與最佳化的重量平衡。\"}",
        "{argument name=\"right callout 2\" default=\"追蹤攝像頭\\n實現高精度的位置追蹤與環境感知。\"}",
        "{argument name=\"right callout 3\" default=\"Pancake 透鏡\\n輕薄設計，提供廣闊視野與清晰畫質。\"}",
        "{argument name=\"right callout 4\" default=\"高效能電池\\n最佳化電源設計，支援長時間續航。\"}",
        "{argument name=\"right callout 5\" default=\"柔軟的面部介面\\n確保長時間佩戴依然舒適。\"}"
      ]
    },
    "footer": {
      "left_text_block": {
        "headline": "{argument name=\"bottom headline\" default=\"體驗，源於結構的進化。\"}",
        "body": "{argument name=\"bottom body\" default=\"每一個零件都蘊含著支撐沉浸式體驗的前沿科技與匠心設計。Meta Quest 3 從內部構建未來，為您帶來超乎想象的體驗。\"}"
      },
      "right_logo": "{argument name=\"footer brand logo\" default=\"∞ Meta\"}"
    }
  },
  "constraints": {
    "must_keep": [
      "元件層級感清晰，層與層之間有適當距離",
      "callout 引線指向正確元件",
      "頂部 logo 和底部品牌區不能與元件重疊",
      "整體看起來像高階釋出會海報"
    ],
    "avoid": [
      "元件展開過密導致看不清",
      "callout 文字過長換行混亂",
      "光線方向不統一",
      "元件之間出現穿模或穿插"
    ]
  }
}
```

### 引數策略

- 必問：產品、元件數量、主標語
- 可預設：背景色、燈光、callout 模板文案
- 可隨機：次級技術描述措辭、底部段落話術

### 自動補全策略

當使用者只給出“產品名”時：

- 自動推測 6-9 個常見元件
- callout 文案使用“技術名稱 + 一句價值描述”句式
- 主標語使用“以…重塑…”或“源於結構的進化”等收束感語句
- 底部品牌區預設與頂部 logo 一致

## 變體 1：手機 / 平板類爆炸圖

📝 提示詞

```json
{
  "type": "智慧終端爆炸檢視海報",
  "subject": "{argument name=\"product\" default=\"旗艦智慧手機\"}",
  "style": {
    "rendering": "深空黑底 + 極簡金屬反光",
    "background_color": "{argument name=\"background color\" default=\"近黑色深空灰\"}"
  },
  "header": {
    "logo": "{argument name=\"product mark\" default=\"NEX Pro\"}",
    "subtitle": "{argument name=\"catchphrase\" default=\"看見每一層，理解每一處\"}"
  },
  "layout": {
    "centerpiece": "手機內部從底到頂垂直爆炸展開 8 層：金屬中框、主機板（含 SoC）、螢幕元件、攝像頭模組、震動單元、電池、揚聲器、玻璃後蓋",
    "callout_labels": {
      "count": 8,
      "items_template": "元件名 + 技術亮點一句話"
    }
  },
  "constraints": {
    "must_feel": "工程美學 + 旗艦釋出感"
  }
}
```

## 變體 2：可穿戴 / 音訊類爆炸圖

📝 提示詞

```json
{
  "type": "可穿戴產品爆炸檢視海報",
  "subject": "{argument name=\"product\" default=\"無線降噪耳機\"}",
  "style": {
    "rendering": "極簡白色背景 + 柔和陰影 + 區域性金屬反光",
    "background_color": "{argument name=\"background color\" default=\"米白漸變\"}"
  },
  "header": {
    "logo": "{argument name=\"product mark\" default=\"AURA Pro\"}",
    "subtitle": "{argument name=\"catchphrase\" default=\"從內到外的安靜\"}"
  },
  "layout": {
    "centerpiece": "耳罩側面爆炸展開 6 層：外殼、麥克風陣列、降噪晶片板、驅動單元、聲學海綿、記憶棉耳墊",
    "callout_labels": {
      "count": 6
    }
  }
}
```

## 變體 3：自動補全模式

📝 提示詞

```json
{
  "type": "爆炸檢視海報自動補全模板",
  "mode": "auto-fill",
  "rule": "使用者給出產品名後，自動決定層數（6-9 層）、callout 數量、主標語、底部段落與品牌 logo，但必須保持四要素：元件清晰、callout 與元件對位、頂部主語、底部品牌",
  "constraints": {
    "must_feel": "高階釋出會主視覺"
  }
}
```

## 避免事項

- 不要讓元件層數過多（超過 10 層就會顯得擁擠）
- 不要讓 callout 引線越過其他元件穿插
- 不要把 callout 文字寫成營銷口號，應該是“元件 + 技術 + 價值”三段式
- 不要讓頂部 logo 和底部品牌 logo 不一致
- 不要在背景里加無關裝飾元素（圓環、花紋、筆刷）
- 不要讓燈光方向出現反向（頂光 + 反向陰影會立刻穿幫）
