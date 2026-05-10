# 商業視覺報告頁模板

本檔案用於生成“商業報告 / 投資分析 / 增長覆盤 / OKR 概覽” 風格的視覺單頁：

- 商業諮詢公司風格
- 投行 / 研究報告
- 公司年報概覽
- 投資人簡報
- OKR 季度總結

特徵：

- 資料驅動
- 表格 + 圖表 + 插圖混合
- 排版嚴謹
- 一頁能講清楚一個商業判斷

## 適用範圍

- 單頁 KPI 概覽
- 投資人簡報封面
- 報告執行摘要頁
- 季度業務覆盤頁

## 何時使用

- 使用者提到“報告 / 覆盤 / 投資人簡報 / KPI / OKR / executive summary”
- 使用者需要資料視覺化 + 商業判斷風格

不要使用：

- 使用者要的是政府公告（用 `policy-style-slide.md`）
- 使用者要的是講解課件（用 `dense-explainer-slides.md`）
- 使用者要的是科普圖（用 `educational-diagram-slide.md`）

## 缺失資訊優先提問順序

1. 報告主題（業務 / 季度 / 專案 / 公司）
2. 關鍵資料（3-5 個）
3. 關鍵判斷（1 句話結論）
4. 是否需要時間線 / 趨勢圖
5. 配色：商業藍 / 黑金 / 暖灰
6. 是否英文 / 中英雙語

## 主模板：商業報告執行摘要頁

📖 描述

頂部為標題 + 報告期 + logo；中間為關鍵資料卡 + 趨勢小圖 + 一句判斷；底部為來源 / 備註。

📝 提示詞

```json
{
  "type": "商業報告執行摘要頁",
  "goal": "生成一張可作為投資人簡報、季度報告封面、內部 OKR 覆盤的執行摘要視覺單頁",
  "style": {
    "color_palette": "{argument name=\"color palette\" default=\"商業藍 + 灰 + 白\"}",
    "tone": "{argument name=\"visual tone\" default=\"理性、剋制、可信賴\"}",
    "typography": "{argument name=\"typography\" default=\"無襯線現代字型 + 數字粗體\"}"
  },
  "header": {
    "company_or_team": "{argument name=\"team name\" default=\"NEX Inc.\"}",
    "report_period": "{argument name=\"period\" default=\"2026 Q1\"}",
    "main_title": "{argument name=\"main title\" default=\"季度業務覆盤 · 執行摘要\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"3 項關鍵資料 + 1 句核心判斷\"}"
  },
  "kpi_cards": {
    "count": "{argument name=\"kpi count\" default=\"4\"}",
    "items": [
      {
        "label": "{argument name=\"kpi 1 label\" default=\"營收\"}",
        "value": "{argument name=\"kpi 1 value\" default=\"¥ 12.4 億\"}",
        "change": "{argument name=\"kpi 1 change\" default=\"+18% YoY\"}"
      },
      {
        "label": "{argument name=\"kpi 2 label\" default=\"活躍使用者\"}",
        "value": "{argument name=\"kpi 2 value\" default=\"3,820 萬\"}",
        "change": "{argument name=\"kpi 2 change\" default=\"+22% YoY\"}"
      },
      {
        "label": "{argument name=\"kpi 3 label\" default=\"毛利率\"}",
        "value": "{argument name=\"kpi 3 value\" default=\"62.1%\"}",
        "change": "{argument name=\"kpi 3 change\" default=\"+3.4 pp\"}"
      },
      {
        "label": "{argument name=\"kpi 4 label\" default=\"NPS\"}",
        "value": "{argument name=\"kpi 4 value\" default=\"62\"}",
        "change": "{argument name=\"kpi 4 change\" default=\"+8\"}"
      }
    ]
  },
  "trend_chart": {
    "enabled": "{argument name=\"trend chart enabled\" default=\"true\"}",
    "type": "{argument name=\"chart type\" default=\"折線 + 面積\"}",
    "metric": "{argument name=\"chart metric\" default=\"季度營收\"}",
    "x_axis": "Q1-Q4",
    "y_axis": "億元"
  },
  "core_judgment": {
    "headline": "{argument name=\"core judgment\" default=\"核心增長來自 AI 產品線，需在 Q2 投入更多研發資源\"}"
  },
  "footer": {
    "source": "{argument name=\"source\" default=\"資料來源：內部財務系統\"}",
    "confidentiality": "{argument name=\"confidentiality\" default=\"內部資料 · 僅供討論\"}"
  },
  "constraints": {
    "must_keep": [
      "數字必須最大、最顯眼",
      "趨勢圖與 KPI 資料一致",
      "核心判斷只有一句",
      "色板極簡 ≤ 3 色"
    ],
    "avoid": [
      "資料過於堆疊",
      "出現裝飾性插畫",
      "字型多種類",
      "底色過亮影響數字識別"
    ]
  }
}
```

### 引數策略

- 必問：報告期、主題、關鍵資料
- 可預設：色板、字型、保密標識
- 可隨機：裝飾小元素

### 自動補全策略

- 使用者只給主題時：自動生成 4 個常見 KPI（營收 / 使用者 / 毛利率 / NPS）
- 預設色板商業藍
- 預設 1 句核心判斷使用“因 X，所以 Y”句式

## 變體 1：投資人 pitch 封面

📝 提示詞

```json
{
  "type": "投資人 pitch 封面單頁",
  "header": {
    "main_title": "{argument name=\"company\" default=\"NEX Inc.\"}",
    "subtitle": "{argument name=\"tagline\" default=\"重新定義 AI 工作流\"}"
  },
  "kpi_cards": {
    "items": [
      "ARR ¥ 1.2 億",
      "增長 240% YoY",
      "客戶 4500+"
    ]
  },
  "core_judgment": {
    "headline": "現在是融資的最佳視窗"
  },
  "constraints": {
    "must_feel": "銳利、自信、未來感"
  }
}
```

## 變體 2：年報概覽頁

📝 提示詞

```json
{
  "type": "公司年報概覽頁",
  "header": {
    "main_title": "{argument name=\"year\" default=\"2025 年度報告\"}",
    "subtitle": "全年關鍵成就 + 來年展望"
  },
  "sections": {
    "items": ["全年 KPI", "重要里程碑", "團隊成長", "來年規劃"]
  },
  "constraints": {
    "must_feel": "剋制、有沉澱感"
  }
}
```

## 變體 3：自動補全模式

📝 提示詞

```json
{
  "type": "商業報告頁自動補全模板",
  "mode": "auto-fill",
  "rule": "使用者給業務方向 + 報告期，自動生成 KPI / 趨勢 / 核心判斷",
  "constraints": {
    "must_feel": "可發給投資人 / 高管"
  }
}
```

## 避免事項

- 不要在執行摘要頁裡塞 > 6 個 KPI
- 不要讓趨勢圖與 KPI 矛盾
- 不要使用花哨字型
- 不要讓核心判斷超過 2 句
- 不要讓背景色過深，會讓數字讀不清
