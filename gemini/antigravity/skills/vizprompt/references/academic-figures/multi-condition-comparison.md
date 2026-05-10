# 多工況 / 多條件結果對比圖模板

本檔案用於生成「同一研究物件在不同工況 / 條件 / 組別下的多面板結果對比圖」：

- 不同溫度 / 壓力 / 濃度 / 配比 / 時間下的實驗或模擬結果
- 不同處理組 / 對照組 / 工藝方案的並列結果
- 多面板 (a)(b)(c)(d) 形式的論文 result figure

特徵：

- 2×2 / 1×3 / 1×4 等統一網格佈局
- **所有 panel 嚴格統一**：相同尺寸、相同色彩邏輯、相同圖例、相同字型層級、相同邊距
- 白底、低飽和工程色，論文結果圖風格
- **無真實資料時只做定性表達，禁止虛構數值 / 等值線 / 色標範圍**

## 適用範圍

- 工程 / 物理 / 化學 / 能源 / 材料 / 環境方向的多工況結果對比
- 燃燒 / 流場 / 溫度場 / 應力場 / 濃度場 等場圖對比
- 不同處理組 / 不同劑量 / 不同時間點 的實驗對照
- 同一指標在多個 condition 下的多面板視覺化

## 何時使用

- 使用者提到「多工況 / 多條件 / 不同 X 下的對比 / panel (a)(b)(c)(d) / 結果對比圖」
- 使用者希望視覺「論文 result figure，不是營銷資訊圖」
- 比較的是**同一物件在不同條件下的同類結果**

不要使用：

- 使用者要的是「不同方法在同一樣本上的輸出對比」（行=樣本，列=方法） → 用 `academic-figures/qualitative-comparison-grid.md`
- 使用者要的是「單個 publication-ready 圖表」（bar / line / scatter） → 用 `academic-figures/publication-chart.md`
- 使用者要的是「營銷 / 資訊圖風格的二元對比」 → 用 `infographics/comparison-infographic.md`

## 缺失資訊優先提問順序

1. 比較物件是什麼（同一現象 / 同一指標）
2. 比較的是哪些工況 / 條件（建議 2-6 個；超過 6 個考慮分兩張圖）
3. 每個 panel 顯示的是什麼（場圖 / 折線 / 柱圖 / 等值線 / 顯微圖）—— 必須**所有 panel 同型別**
4. 是否有真實資料（**關鍵**：決定是定性圖還是定量圖）
5. 網格佈局（2×2 / 1×3 / 1×4 / 2×3）
6. 標籤語言（中文 / 英文 / 雙語）
7. 共享圖例 / 共享色標（強烈建議共享）

## 主模板：N panel 多工況對比（統一規格）

📖 描述

整張圖按統一網格分割成 N 個 panel，每個 panel 展示同一類結果在不同工況下的表現。所有 panel 共享色標 / 圖例 / 字型層級 / 邊距。子圖示記為 (a)(b)(c)(d)，標籤簡短剋制。**絕對不允許每個 panel 自成一套風格。**

📝 提示詞

```json
{
  "type": "學術多工況結果對比圖（multi-condition comparison figure）",
  "goal": "生成一張可直接放進論文 results 章節的多面板對比圖，要求所有 panel 嚴格統一、白底、低飽和工程色、可單色印刷可讀",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"4:3\"}",
    "background": "pure white #FFFFFF",
    "outer_padding": "50px around the grid",
    "inter_panel_gap": "16-20px, identical horizontal and vertical",
    "render_quality": "vector-clean look, anti-aliased, sharp text"
  },
  "title_caption": {
    "figure_label": "{argument name=\"figure_label\" default=\"Figure X.\"}",
    "caption": "{argument name=\"caption\" default=\"Comparison of results under varying conditions.\"}",
    "position": "bottom-center, italic serif or compact sans-serif, smaller font size"
  },
  "grid_layout": {
    "rows": "{argument name=\"rows\" default=\"2\"}",
    "cols": "{argument name=\"cols\" default=\"2\"}",
    "panel_count": "{argument name=\"panel_count\" default=\"4\"}",
    "rule": "rows × cols == panel_count; all panels identical size; consistent vertical and horizontal alignment"
  },
  "panels": {
    "panel_type": "{argument name=\"panel_type\" default=\"contour-field\"}",
    "panel_type_options": "contour-field | line-chart | bar-chart | heatmap | micrograph | flow-field | bubble-chart",
    "rule": "ALL panels MUST share the same panel_type; never mix bar with line within the same comparison figure",
    "items": [
      {
        "id": "(a)",
        "condition_label": "{argument name=\"panel_a_label\" default=\"Condition A\"}",
        "condition_detail": "{argument name=\"panel_a_detail\" default=\"e.g. excess-air ratio λ = 1.0\"}"
      },
      {
        "id": "(b)",
        "condition_label": "{argument name=\"panel_b_label\" default=\"Condition B\"}",
        "condition_detail": "{argument name=\"panel_b_detail\" default=\"e.g. excess-air ratio λ = 1.2\"}"
      },
      {
        "id": "(c)",
        "condition_label": "{argument name=\"panel_c_label\" default=\"Condition C\"}",
        "condition_detail": "{argument name=\"panel_c_detail\" default=\"e.g. excess-air ratio λ = 1.4\"}"
      },
      {
        "id": "(d)",
        "condition_label": "{argument name=\"panel_d_label\" default=\"Condition D\"}",
        "condition_detail": "{argument name=\"panel_d_detail\" default=\"e.g. excess-air ratio λ = 1.6\"}"
      }
    ]
  },
  "panel_style": {
    "frame": "thin border 1px #1F2937 OR clean axis lines without outer frame, applied identically to all panels",
    "label_position": "(a) (b) (c) (d) at top-left of each panel, bold sans-serif, 11pt",
    "condition_label_position": "centered above each panel OR inside each panel top-right, identical position across all panels",
    "axis_labels": "shared if possible; if shown, identical font size, identical tick density across panels",
    "internal_titles": "AVOID per-panel decorative titles; rely on (a)(b)(c)(d) + condition label only"
  },
  "shared_legend": {
    "enabled": "{argument name=\"shared_legend_enabled\" default=\"true\"}",
    "position": "{argument name=\"shared_legend_position\" default=\"right-of-grid\"}",
    "rule": "single legend / colorbar shared across ALL panels; never give each panel its own legend with different range",
    "colorbar_range": "{argument name=\"colorbar_range\" default=\"qualitative-low-to-high\"}",
    "colorbar_range_rule": "if user provided a numerical range, use it; otherwise render as a qualitative gradient labeled 'low → high' with NO fabricated numerical ticks"
  },
  "color_logic": {
    "rule": "≤ 3 main colors total; if a sequential colormap is used, choose a perceptually uniform low-saturation engineering colormap (e.g. viridis-like, blue-to-orange, gray-to-deep-blue); apply the SAME colormap and SAME range to every panel",
    "must_print_grayscale_readable": true
  },
  "data_authenticity": {
    "user_provided_real_data": "{argument name=\"has_real_data\" default=\"false\"}",
    "rule_when_false": "render the panels as QUALITATIVE schematics: smooth gradient fields, generic shapes, no numerical tick labels on the colorbar, no specific values in axes; explicitly avoid the visual impression of a real dataset",
    "rule_when_true": "use the user-provided values; never extrapolate, interpolate, or invent additional values"
  },
  "constraints": {
    "must_keep": [
      "all panels identical size, identical aspect, identical position scheme",
      "shared color logic and shared legend across all panels",
      "white background, no gradient backdrop, no decorative pattern",
      "(a)(b)(c)(d) labels in identical position and identical style across all panels",
      "only sans-serif typography, identical font family across all panels",
      "the figure should look like it came from a results section of an engineering or science journal"
    ],
    "avoid": [
      "different colormap or different color range per panel",
      "different chart type per panel (e.g. mixing bar and line)",
      "decorative panel titles, hero panel that visually dominates the rest",
      "saturated brand colors, neon, vivid gradients",
      "3D effects, drop shadows, glossy fills, lens flare",
      "fabricated numerical tick values, fabricated colorbar ranges, fabricated isolines",
      "marketing-poster aesthetics, infographic-collage aesthetics",
      "watermarks, copyright stamps"
    ]
  }
}
```

### 引數策略

- **必問**：`panel_count`、`panel_type`（所有 panel 同一型別）、`has_real_data`
- **可預設**：`aspect_ratio`、`grid_layout`（2×2 是最常見）、`shared_legend_enabled`（true）
- **可隨機**：每個 condition 的 `*_detail` 措辭（使用者給了控制變數名時可學術化）

### 自動補全策略

- 使用者沒說有沒有真實資料 → **必須先確認**：`has_real_data` = false 時全圖走定性渲染
- 使用者給了不同 condition 但沒說每 panel 的具體取值 → 在 condition_detail 裡用佔位短語（如 `λ = X1`），**不要編造數字**
- 使用者給了 panel 數但 row × col 不匹配 → 自動選最接近正方的網格（2×2 / 2×3 / 3×3）
- 使用者說"中文論文 / 答辯" → 切換標籤為中文 + 字型 PingFang / 思源黑

## 變體 1：橫向 1×N（適合窄 panel 比較）

```json
{
  "type": "橫向 1×N 多工況對比",
  "modify": {
    "layout": "rows = 1, cols = N（建議 N ≤ 4）",
    "use_case": "panel 內部是窄柱圖 / 窄折線，更適合橫向鋪開；或論文雙欄排版需要橫向單行"
  }
}
```

適用：單欄 / 雙欄論文格式中的橫向比較。

## 變體 2：行列雙因子矩陣（M×N）

```json
{
  "type": "雙因子矩陣對比",
  "modify": {
    "layout": "rows = M（一種因子的不同水平），cols = N（另一種因子的不同水平）",
    "rule": "頂部一行寫列因子標籤，最左一列寫行因子標籤；panel 內部樣式嚴格統一",
    "use_case": "需要同時變化兩個獨立變數（如溫度 × 含水率，或時間 × 濃度）"
  }
}
```

適用：雙因子實驗設計的結果展示，正交試驗結果視覺化。

## 變體 3：定性場圖渲染（無真實資料）

```json
{
  "type": "定性場圖多工況對比",
  "modify": {
    "panel_type": "contour-field",
    "data_authenticity": {
      "user_provided_real_data": false,
      "rule": "render smooth qualitative gradient fields with NO numerical tick labels and NO specific isoline values; the colorbar shows 'low → high' as a qualitative scale only",
      "intent": "visually communicate 'higher temperature in panel (b)' without claiming any specific value"
    },
    "use_case": "答辯 / 開題階段尚未拿到資料，需要先講清研究思路時使用"
  }
}
```

適用：示意性結果對比、方法論說明階段。

## 避免事項

- 給每個 panel 用不同 colormap / 不同 range → 直接破壞可比性
- 在沒有真實資料時畫出帶具體數值的等值線 / 色標刻度（**嚴格禁止虛構資料**）
- 讓某一 panel 視覺權重明顯大於其他 panel（不允許"主圖 + 輔圖"的結構）
- 在每個 panel 加獨立的裝飾性標題
- 把不同型別的圖（bar / line / contour）混排在同一對比圖裡
- 使用飽和 brand 色或霓虹漸變
- 把"對比方法"的邏輯（行=樣本×列=方法）誤用到本模板（請改用 `qualitative-comparison-grid.md`）
- 加水印 / 期刊 logo / 裝置品牌標
