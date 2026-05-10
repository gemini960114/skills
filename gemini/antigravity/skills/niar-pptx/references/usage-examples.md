# NIAR PPTX Skill 使用說明與範例

這份文件說明如何使用 `$niar-pptx` skill 產出接近 `niar.pptx` 品牌風格的可編輯 PowerPoint 簡報。目標是讓使用者不需要每次帶入或重讀 `niar.pptx` 原始檔，也能重現 NIAR / 國家實驗研究院風格：橘紅金漸層、右上 NIAR Logo、白底內容頁、淡金波紋、頁碼頁尾、微軟正黑體與清楚的版面節奏。

## 什麼時候使用

使用 `$niar-pptx` 適合以下任務：

- 根據一個簡單主題直接生成 NIAR 風格簡報。
- 根據一份文件、新聞稿、研究摘要、會議紀錄製作簡報。
- 從多份文件中抽出指定主題，整理成簡報。
- 從文件或表格中抽取數字、指標、時程，轉成圖表或表格頁。
- 把既有簡報改成 NIAR 風格。
- 把主管簡報、政策簡報、技術簡報做成更正式的發布會風格。
- 需要固定 Logo、配色、頁碼、底圖與版面比例，不想每次重新分析 `niar.pptx`。

## 基本提示詞骨架

```text
[$niar-pptx](D:\antigravity\pptx2\.agents\skills\niar-pptx\SKILL.md)
請根據 [資料來源] 製作一份文字可編輯、版面清楚的 PowerPoint 簡報。

主題：[簡報主題]
受眾：[主管 / 研究團隊 / 產業夥伴 / 對外發布]
頁數：[例如 8-12 頁]
要求：
- 使用 NIAR 風格，不要讀取 niar.pptx 原始檔。
- 使用 skill 內建底圖、Logo 區、安全區、頁碼頁尾與配色規範。
- 所有標題、正文、圖表文字都要可編輯。
- 若資料來源很多，請先建立 source-inventory.md、evidence-table.md、outline.md。
- 每頁要有清楚目標、來源脈絡與可編輯的 PowerPoint 物件。
- 完成後請驗證 PPTX 可開啟、頁數正確、無物件越界。
```

## 10 個範例用法

### 1. 簡單題目直接做簡報

適合只有一個題目，還沒有資料文件，但想先產出可討論的初稿。

```text
[$niar-pptx](D:\antigravity\pptx2\.agents\skills\niar-pptx\SKILL.md)
請以「國家級 AI 算力基礎建設」為主題，製作一份 8 頁可編輯 PowerPoint。
受眾是政府與研究單位主管。
請使用 NIAR 風格，包含封面、背景、政策定位、核心建設、推動路線、風險與結語。
不要讀 niar.pptx 原始檔，直接使用 skill 內建風格與底圖。
```

### 2. 把一個問題整理成說明簡報

適合使用者先提出一個問題，請 Codex 把回答整理成簡報。

```text
[$niar-pptx](D:\antigravity\pptx2\.agents\skills\niar-pptx\SKILL.md)
問題：為什麼國家需要投資高速量子運算？
請把這個問題整理成一份 6 頁 NIAR 風格簡報，內容要包含：
1. 問題背景
2. 國家安全與產業需求
3. 半導體與 AI 算力的關聯
4. 國際合作必要性
5. 推動策略
6. 結論
請讓文字可編輯，語氣正式、適合主管簡報。
```

### 3. 根據單一文件製作簡報

適合新聞稿、政策文件、研究摘要或企劃書。

```text
[$niar-pptx](D:\antigravity\pptx2\.agents\skills\niar-pptx\SKILL.md)
請根據 [hpc.md](D:\antigravity\pptx2\hpc.md) 製作一份 10-12 頁可編輯 PowerPoint。
簡報主題：「AI新十大建設-高速量子運算國家戰略發佈會」
請先萃取文件重點，再套用 NIAR 風格：
- 封面
- 核心訊息
- 戰略背景
- 四大策略
- 基礎設施
- 供應鏈價值
- 國際合作
- 推動路線
- 結語
文件中的圖片若可用，請優先使用；不足時再用純圖形與版面設計補足。
```

### 4. 附帶文件並提出特定問題

適合不是要整份摘要，而是圍繞某個問題做簡報。

```text
[$niar-pptx](D:\antigravity\pptx2\.agents\skills\niar-pptx\SKILL.md)
請閱讀 [report.md](D:\path\report.md)，只回答並整理這個問題：
「這份報告對國家級算力中心的建置優先順序有什麼啟示？」
請製作 7 頁 NIAR 風格簡報：
1. 問題與結論
2. 報告中的直接證據
3. 建置優先順序
4. 資源需求
5. 風險與限制
6. 建議決策
7. 下一步
請保留引用來源頁碼或段落標記在備註或小字說明中。
```

### 5. 從多份文件中抽出指定主題做簡報

適合一個資料夾裡有很多 Markdown、PDF、Word 或文字檔，只要抽取其中一個主題。

```text
[$niar-pptx](D:\antigravity\pptx2\.agents\skills\niar-pptx\SKILL.md)
請從資料夾 [D:\project\docs] 裡的文件中，只抽取「量子運算主機建置」相關內容，
整理成 9 頁 NIAR 風格 PowerPoint。

要求：
- 不要逐份文件做流水帳摘要，要整合成一條簡報敘事。
- 請先產出 source-inventory.md、evidence-table.md、outline.md。
- 每頁保留資料來源檔名或章節。
- 若多份文件對同一件事有不同說法，請在簡報中標示「待確認」。
- 版面使用 NIAR 白底內容頁、表格頁、路線圖頁與結語頁。
```

### 6. 從文件或表格中抽取數據並做成圖表

適合把數字、時程、預算、KPI、效能、用量整理成表格或圖表頁。

```text
[$niar-pptx](D:\antigravity\pptx2\.agents\skills\niar-pptx\SKILL.md)
請從 [metrics.xlsx](D:\path\metrics.xlsx) 和 [summary.md](D:\path\summary.md)
抽取與「算力資源、節點數、預算、使用率、排程等待時間」相關的數據，
製作一份 8 頁 NIAR 風格簡報。

請包含：
- 1 頁數據總覽
- 2-3 頁圖表或表格
- 1 頁問題診斷
- 1 頁建議改善方向
- 1 頁決策事項
所有圖表標題、數字標籤、表格文字都要可編輯；不要把表格截圖貼上。
```

### 7. 把既有簡報改成 NIAR 風格

適合已經有內容簡報，但風格不一致或太粗糙。

```text
[$niar-pptx](D:\antigravity\pptx2\.agents\skills\niar-pptx\SKILL.md)
請把 [draft.pptx](D:\path\draft.pptx) 改成 NIAR 風格簡報。
請保留原本的主要內容與頁數，但重做：
- 封面與結語頁
- 標題層級
- 頁碼與頁尾
- 底圖與 Logo 安全區
- 色彩與字型
- 圖表與表格樣式
請不要讀 niar.pptx 原始檔，直接使用 `$niar-pptx` 的內建背景與 style guide。
```

### 8. 指定風格加上正式發布會語氣

適合內容已有，但希望變成對外發布、典禮或政策宣布風格。

```text
[$niar-pptx](D:\antigravity\pptx2\.agents\skills\niar-pptx\SKILL.md)
請根據 [launch-notes.md](D:\path\launch-notes.md)
製作一份「正式發布會」語氣的 NIAR 風格簡報。

語氣要求：
- 標題要像政策發布或重大建設啟動
- 每頁只保留一個明確訊息
- 用深色分頁強調國家戰略與國際合作
- 用白底內容頁呈現推動路線、任務分工與時程
請輸出可編輯 PPTX，並驗證可開啟。
```

### 9. 產出給主管看的決策簡報

適合把大量技術內容壓縮成主管可以快速決策的版本。

```text
[$niar-pptx](D:\antigravity\pptx2\.agents\skills\niar-pptx\SKILL.md)
請把 [technical-plan.md](D:\path\technical-plan.md) 改寫成給主管看的 6 頁 NIAR 風格決策簡報。

請不要放太多技術細節，重點放在：
1. 為什麼現在要做
2. 目前進度
3. 需要決策的事項
4. 預期效益
5. 主要風險
6. 建議下一步
請把技術細節移到備註或附錄頁，不要塞滿正文。
```

### 10. 從資料夾整理成主題式簡報並搭配 NIAR 風格

適合一次交給 Codex 一包資料，讓它自己檢索、整理、做簡報。

```text
[$niar-pptx](D:\antigravity\pptx2\.agents\skills\niar-pptx\SKILL.md)
請掃描 [D:\project\source-materials] 中的 Markdown、PDF、Word、Excel 檔，
找出與「AI 基礎設施、HPC、量子運算、資安加密」有關的內容，
整理成一份 12 頁 NIAR 風格簡報。

要求：
- 先建立主題分類，不要依檔案順序排列。
- 請建立 source-inventory.md、evidence-table.md、outline.md 後再製作 PPTX。
- 每個主題要列出來源文件。
- 有數據就做成表格或圖表。
- 沒有數據的內容做成策略、流程或路線圖頁。
- 輸出文字可編輯的 PPTX。
- 完成後驗證頁數、開啟狀態與是否有超出版面。
```

## 搭配其他 Skill 的建議

- 做 `.pptx` 時，搭配 project `pptx` skill 負責 PowerPoint 產生、編輯與驗證。
- 處理 Excel / CSV 數據時，先用 spreadsheet 相關能力抽取數據，再用 `$niar-pptx` 做視覺呈現。
- 處理 Word / PDF 報告時，先萃取章節與引用，再用 `$niar-pptx` 做簡報結構。
- 若要從大量本地資料夾檢索內容，可先做資料檢索與主題分類，再進入 NIAR 簡報製作。

## 交付檢查清單

完成簡報前請檢查：

- PPTX 可以開啟。
- 頁數符合要求。
- 文字、標題、圖表標籤保持可編輯。
- 表格、來源註記、重要數字保持可編輯；不要用截圖替代正文或表格。
- Logo 區沒有被文字或圖片遮住。
- 深色頁的頁碼與頁尾可讀。
- 白底頁沒有把內容壓到底部波紋區。
- 沒有 placeholder、lorem ipsum、未替換樣板文字。
- 圖片來源清楚，官方圖片優先。
- 若從多文件整理，簡報中有保留來源脈絡，並已檢查 evidence-table.md 對應到投影片。
