# 擬物 / 復古圖示集模板

本檔案用於"成套圖示 / 擬物 / Y2K / 復古"圖示視覺：

- 擬物風應用圖示集（Skeuomorphic）
- Y2K 風格水晶圖示
- 畫素 / 復古遊戲圖示
- 主題圖示包（生活 / 工作 / 旅行）
- UI 圖示系統

特徵：

- 多個圖示，統一風格
- 通常 6 / 8 / 12 / 16 個
- 每個圖示圓角方形 / 圓形
- 強調材質質感（玻璃 / 金屬 / 擬物）
- 適合作為 app 圖示包 / icon set

## 適用範圍

- 應用圖示集
- 主題圖示包
- UI 圖示系統
- 周邊貼紙 / 卡片

## 何時使用

- 使用者提到"圖示 / icon set / 擬物 / skeuomorphic / Y2K / 畫素圖示"
- 使用者希望成套圖示

不要使用：

- 單個 3D 圖示頭像（用 `avatars-and-profile/themed-3d-icon.md`）
- 貼紙套裝（用 `avatars-and-profile/sticker-set.md`）
- 通用品牌識別（用 `branding-and-packaging/brand-identity-board.md`）

## 缺失資訊優先提問順序

1. 風格（擬物 / Y2K / 畫素 / Flat / Glass / Clay）
2. 圖示主題（應用 / 工作 / 生活 / 旅行）
3. 圖示數量（6 / 8 / 12 / 16）
4. 主色 1-2 個
5. 形狀基底（圓角方形 / 圓形 / 自由形）
6. 是否帶文字標籤

## 主模板：擬物風應用圖示集

📖 描述

整體一張圖，包含 N 個統一風格的擬物圖示，以網格排布。

📝 提示詞

```json
{
  "type": "擬物風應用圖示集",
  "goal": "生成一組成套統一風格的圖示，可作為 icon pack / 主題包",
  "theme": "{argument name=\"theme\" default=\"經典辦公應用\"}",
  "style": {
    "rendering": "{argument name=\"rendering\" default=\"擬物 3D + 軟光 + 柔和陰影\"}",
    "material": "{argument name=\"material\" default=\"玻璃質感 + 微微反光\"}",
    "color_palette": "{argument name=\"color palette\" default=\"米白 + 暖橙 + 淺藍 + 灰\"}",
    "shape_base": "{argument name=\"shape base\" default=\"圓角方形（24% 圓角）\"}"
  },
  "layout": {
    "grid": "{argument name=\"grid\" default=\"4x3\"}",
    "icon_count": "{argument name=\"icon count\" default=\"12\"}",
    "spacing": "16px",
    "background": "{argument name=\"background\" default=\"米色紙紋\"}",
    "label_below": "{argument name=\"label below\" default=\"true\"}",
    "label_style": "細灰色無襯線小字"
  },
  "icons": [
    {"id": 1, "concept": "{argument name=\"icon 1\" default=\"郵件 - 信封 + 發光指示\"}", "label": "Mail"},
    {"id": 2, "concept": "{argument name=\"icon 2\" default=\"日曆 - 翻開頁面 + 紅色今日標記\"}", "label": "Calendar"},
    {"id": 3, "concept": "{argument name=\"icon 3\" default=\"備忘錄 - 黃色便籤 + 紅色書籤\"}", "label": "Notes"},
    {"id": 4, "concept": "{argument name=\"icon 4\" default=\"相機 - 復古膠片機\"}", "label": "Camera"},
    {"id": 5, "concept": "{argument name=\"icon 5\" default=\"音樂 - 黑膠唱片\"}", "label": "Music"},
    {"id": 6, "concept": "{argument name=\"icon 6\" default=\"地圖 - 摺疊地圖 + 紅針\"}", "label": "Maps"},
    {"id": 7, "concept": "{argument name=\"icon 7\" default=\"天氣 - 太陽 + 雲\"}", "label": "Weather"},
    {"id": 8, "concept": "{argument name=\"icon 8\" default=\"計算器 - 數字按鍵\"}", "label": "Calc"},
    {"id": 9, "concept": "{argument name=\"icon 9\" default=\"時鐘 - 圓形錶盤\"}", "label": "Clock"},
    {"id": 10, "concept": "{argument name=\"icon 10\" default=\"設定 - 齒輪\"}", "label": "Settings"},
    {"id": 11, "concept": "{argument name=\"icon 11\" default=\"健康 - 心形脈搏線\"}", "label": "Health"},
    {"id": 12, "concept": "{argument name=\"icon 12\" default=\"錢包 - 棕色皮夾\"}", "label": "Wallet"}
  ],
  "constraints": {
    "must_keep": [
      "12 個圖示風格嚴格統一（同樣光源、同樣圓角、同樣厚度）",
      "色板 ≤ 6 色",
      "label 字型一致",
      "每個圖示可單獨識別"
    ],
    "avoid": [
      "圖示風格漂移（有些擬物有些扁平）",
      "顏色超過 6 種",
      "圖示內部細節過密",
      "label 錯字"
    ]
  }
}
```

### 引數策略

- 必問：主題、數量、風格
- 可預設：layout、配色、形狀基底
- 可隨機：每個圖示具體設計

### 自動補全策略

- 使用者給主題 + 數量時：自動展開每個圖示具體形象
- 預設 4×3 = 12 個
- 預設擬物 3D + 玻璃質感

## 變體 1：Y2K 水晶圖示包

📝 提示詞

```json
{
  "type": "Y2K 水晶圖示包",
  "style": {
    "material": "透明水晶 + 折射光",
    "color_palette": "高飽和粉 + 藍紫 + 銀"
  },
  "constraints": {
    "must_feel": "Y2K Aero 風"
  }
}
```

## 變體 2：畫素復古遊戲圖示

📝 提示詞

```json
{
  "type": "畫素復古遊戲圖示",
  "style": {
    "rendering": "16-bit 畫素 + 銳利邊緣",
    "color_palette": "16 色復古遊戲調色盤"
  },
  "constraints": {
    "must_feel": "FC / SNES 時代"
  }
}
```

## 變體 3：自動補全模式

📝 提示詞

```json
{
  "type": "圖示包自動補全",
  "mode": "auto-fill",
  "rule": "使用者給主題，自動決定圖示數量、風格、配色、layout",
  "constraints": {
    "must_feel": "可作為 icon pack 上架"
  }
}
```

## 避免事項

- 不要讓圖示風格漂移
- 不要讓色板 > 6
- 不要讓 label 字型超過 1 種
- 不要讓單個圖示內部塞 > 3 元素
- 不要讓網格大小不一致
- 不要讓 icon 與 background 對比度不夠
