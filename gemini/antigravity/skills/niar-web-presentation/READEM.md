# niar-web-presentation 使用說明

`niar-web-presentation` 用來製作 **NIAR / 國家實驗研究院風格的網頁投影片**。

輸出不是 `.pptx`，而是一個可以直接開啟的 **靜態 HTML 網頁簡報資料夾**。使用者只要打開 `index.html` 就能播放給主管、客戶、評審或合作方看，也可以用桌面錄影工具錄成影片。

預設不要求使用者執行 `npm install`、`npm run dev` 或任何建置指令。需要 React / Vite / TypeScript 原始專案時，必須由使用者另外指定。

## 核心特色

- 固定 `1920 x 1080` 的 16:9 舞台。
- 支援上一頁 / 下一頁。
- 支援同一頁內元素依序出現。
- 控制列可隱藏，適合正式展示或桌面錄影。
- 使用 NIAR 背景、右上 Logo 區、橘紅金漸層、深藍文字面板、白底內容頁與微軟正黑體。
- 多文件任務可先建立來源盤點與證據表，再製作簡報。

## 使用方式

在需求中指定這個 skill：

```text
[$niar-web-presentation](D:\antigravity\pptx2\.agents\skills\niar-web-presentation\SKILL.md)
```

若要快速建立 HTML 簡報骨架，可使用：

```powershell
python .agents\skills\niar-web-presentation\scripts\scaffold-niar-web-presentation.py .\presentation --title "簡報標題" --project-id "project-id"
```

建立後直接開啟：

```text
presentation\index.html
```

正式交付前請確認：

- `index.html` 可在瀏覽器直接開啟。
- 背景圖片與 Logo 區正確顯示。
- 在 `1920 x 1080`、`1366 x 768`、`1280 x 720` 視窗下，舞台都置中且沒有偏移。
- 點擊、鍵盤、頁內 reveal、clean mode 都正常。
- 文字、面板、控制列沒有互相重疊，也沒有超出安全區。
- 主要文字可選取、可複製，頁面使用語義化 HTML，不把正文做成圖片或全塞進 canvas。
- 表格使用真正的 HTML table；圖表若用 canvas/SVG，需保留文字標籤或摘要。
- 若有多個 HTML 頁面，頁面之間的連結可正常跳轉。

## 範例 1：簡單主題製作網頁簡報

```text
[$niar-web-presentation](D:\antigravity\pptx2\.agents\skills\niar-web-presentation\SKILL.md)

請以「國家級 AI 算力基礎建設」為主題，製作一份 NIAR 風格 web slide presentation。

要求：
- 可以直接用瀏覽器播放給主管看。
- 每頁可以用點擊讓元素依序出現。
- 風格要一看就是 NIAR 樣板延伸。
- 請輸出可直接開啟的 HTML 資料夾，不需要 npm。
- 主要內容要是可選取的 HTML 文字，不要做成圖片。
- 完成後確認 index.html 可直接播放。
```

## 範例 2：根據單一文件製作網頁簡報

```text
[$niar-web-presentation](D:\antigravity\pptx2\.agents\skills\niar-web-presentation\SKILL.md)

請根據 [第2季執行情形-微生物相在精準健康之研發及應用(2_4)_0605_v1.docx](D:\antigravity\pptx2\第2季執行情形-微生物相在精準健康之研發及應用(2_4)_0605_v1.docx)
製作一份 NIAR 風格網頁簡報。

簡報主題：
「微生物相在精準健康之研發及應用：第2季執行情形」

請先整理 outline.md，再建立 web presentation。

內容請包含：
- 計畫背景
- 第2季執行重點
- 主要成果
- 重要數據或里程碑
- 遇到的問題
- 後續工作
- 結語

完成後請確認可以在瀏覽器直接播放，不需要 npm。
請保留可選取的 HTML 文字、語義化標題與來源註記。
```

## 範例 3：從多份文件整理主題後製作網頁簡報

```text
[$niar-web-presentation](D:\antigravity\pptx2\.agents\skills\niar-web-presentation\SKILL.md)

請從 D:\project\docs 裡的多份文件中，整理出「量子運算主機建置」相關內容，
製作一份 NIAR 風格 web slide presentation。

請先產出：
- source-inventory.md
- evidence-table.md
- outline.md

要求：
- 不要依照檔案順序摘要，要用主題式整理。
- 每個重點要保留來源文件或章節。
- 如果文件之間有矛盾，請標示「待確認」。
- 每頁要有 NIAR 樣板識別，例如背景、Logo 區、標籤、深藍面板或橘色強調線。
- 每頁要使用結構化 HTML；數據表格請用真正的 table，不要截圖。
- 完成後確認 navigation、reveal、clean mode 與 HTML 直接開啟都正常。
```
