# NIAR PPTX Skill 使用說明

這份 README 說明如何使用 `$niar-pptx` skill 產出 NIAR / 國家實驗研究院風格的可編輯 PowerPoint 簡報。

這個 skill 的重點是：**不需要每次讀取 `niar.pptx` 原始檔**，也能重現 NIAR 簡報的主要視覺規則，例如右上 Logo、安全區、橘紅金漸層封面、白底內容頁、頁碼頁尾、微軟正黑體與固定版面節奏。

## 適合使用的情境

- 根據 Word、PDF、Markdown、Excel 或文字資料製作 NIAR 風格簡報。
- 把研究報告、季度執行情形、主管摘要、政策說明整理成 8-12 頁簡報。
- 把既有簡報改成 NIAR 風格，但保留主要內容。
- 需要所有文字、標題、表格與圖表標籤都能在 PowerPoint 裡編輯。
- 想避免讀取大型 `niar.pptx` 樣板造成不必要的 token 或時間成本。

## 關於 `niar.pptx` 與 token 成本

把 `niar.pptx` 放在資料夾裡，本身不會造成大量 token 消耗。只有在模型真的去讀取、解壓、抽文字、分析投影片或擷取圖片時，才會增加成本。

建議做法：

- 可以保留 `niar.pptx` 作為原始樣板備份。
- 若擔心誤讀，可移到 `archive/`，例如 `archive/niar.pptx`。
- 也可以改名為 `_reference_only_niar.pptx`，讓用途更清楚。
- 在 prompt 裡明確寫「不要讀取 niar.pptx，請使用 niar-pptx skill 內建資產與規則」。

## 基本 Prompt 骨架

```text
[$niar-pptx](D:\antigravity\pptx2\example\.agents\skills\niar-pptx\SKILL.md)
請根據 [資料來源] 製作一份 NIAR 風格、文字可編輯的 PowerPoint 簡報。

簡報主題：
「[主題名稱]」

請整理成 [頁數] 頁，適合給 [受眾] 快速了解重點。

內容請包含：
- 封面
- 背景
- 執行重點
- 主要成果
- 重要數據或里程碑
- 遇到的問題
- 後續工作
- 結語

請使用 NIAR 風格。
請保留右上 Logo、配色、字型、頁碼與頁尾風格。
所有文字都要可以在 PowerPoint 裡編輯。
請不要讀取 niar.pptx；請直接使用 niar-pptx skill 內建 NIAR 資產與風格規則。

完成後請確認簡報可以開啟、頁數正確、版面沒有跑掉。
```

## 輸出時應確認的項目

完成簡報後，建議要求驗證：

- PowerPoint 可以開啟。
- 頁數符合要求。
- 文字是可編輯物件，不是整頁截圖。
- Logo 區沒有被文字、圖片或圖表遮住。
- 頁碼與頁尾一致。
- 深色頁的頁碼與頁尾可讀。
- 沒有 placeholder、lorem ipsum、xxxx 或未替換樣板文字。
- 沒有物件超出版面。
- 重要來源或圖片來源有交代。

## 三個不同狀況範例

### 狀況一：根據 Word 報告製作主管摘要簡報

適合季度報告、執行情形、政策計畫、研究進度這類文件。這種情境通常不需要逐段搬運原文，而是整理成主管能快速判斷的摘要。

```text
[$niar-pptx](D:\antigravity\pptx2\example\.agents\skills\niar-pptx\SKILL.md)
請根據 [第2季執行情形-微生物相在精準健康之研發及應用(2_4)_0605_v1.docx](第2季執行情形-微生物相在精準健康之研發及應用(2_4)_0605_v1.docx)
製作一份 NIAR 風格、文字可編輯的 PowerPoint 簡報。

簡報主題：
「微生物相在精準健康之研發及應用：第2季執行情形」

請整理成 8-10 頁，適合給主管快速了解重點。

內容請包含：
- 封面
- 計畫背景
- 第2季執行重點
- 主要成果
- 重要數據或里程碑
- 遇到的問題
- 後續工作
- 結語

請使用 NIAR 風格。
請保留右上 Logo、配色、字型、頁碼與頁尾風格。
所有文字都要可以在 PowerPoint 裡編輯。
請不要讀取 niar.pptx；請直接使用 niar-pptx skill 內建 NIAR 資產與風格規則。

完成後請確認簡報可以開啟、頁數正確、版面沒有跑掉。
```

### 狀況二：只有主題，先做一份可討論的初稿

適合還沒有完整資料，但想先建立簡報架構、視覺方向與主管溝通版本。

```text
[$niar-pptx](D:\antigravity\pptx2\example\.agents\skills\niar-pptx\SKILL.md)
請以「國家級 AI 算力基礎建設」為主題，製作一份 8 頁 NIAR 風格 PowerPoint 初稿。

受眾是政府與研究單位主管。

請包含：
- 封面
- 為什麼現在需要建置
- 國際趨勢
- 台灣需求
- 核心建設項目
- 推動路線
- 風險與配套
- 結語

請使用正式、簡潔、給主管看的語氣。
所有文字都要可編輯。
請不要讀取 niar.pptx；請直接使用 niar-pptx skill 內建 NIAR 資產與風格規則。

完成後請驗證 PPTX 可開啟、頁數正確、沒有物件越界。
```

### 狀況三：把既有簡報改成 NIAR 風格

適合已經有內容簡報，但版面不一致、樣式不正式，或需要改成 NIAR / 國研院品牌風格。

```text
[$niar-pptx](D:\antigravity\pptx2\example\.agents\skills\niar-pptx\SKILL.md)
請把 [draft.pptx](D:\path\to\draft.pptx) 改成 NIAR 風格簡報。

請保留原本的主要內容與頁數，但重做：
- 封面與結語頁
- 標題層級
- 右上 Logo 安全區
- NIAR 配色
- 微軟正黑體字型
- 頁碼與頁尾
- 表格與圖表樣式

請不要讀取 niar.pptx；請直接使用 niar-pptx skill 內建 NIAR 資產與風格規則。
所有文字、圖表標籤與表格文字都要可以在 PowerPoint 裡編輯。

完成後請確認：
- PowerPoint 可以開啟
- 頁數與原簡報一致
- 版面沒有跑掉
- 沒有 placeholder 或未替換文字
- Logo 沒有被遮住
```

## 建議的檔案管理方式

若資料夾內同時有來源文件、輸出簡報與樣板檔，建議命名如下：

```text
source/
  report.docx
  metrics.xlsx

archive/
  niar.pptx

output/
  project_summary_NIAR.pptx
```

如果不想調整資料夾，也可以保留在同一層，但把原始樣板改名：

```text
_reference_only_niar.pptx
```

## 最重要的一句話

如果想避免模型誤讀原始樣板，請在 prompt 裡加上：

```text
請不要讀取 niar.pptx；請直接使用 niar-pptx skill 內建 NIAR 資產與風格規則。
```
