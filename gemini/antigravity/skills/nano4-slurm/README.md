# nano4-slurm — 自然語言使用範例

本文件示範使用者如何以自然語言向 Agent 描述需求，  
Agent 應依據 `SKILL.md` 的 **Section 0 互動工作流程** 正確解析並產出 Slurm script。

---

## 🟢 情境 A：完全不知道自己有什麼資源（初次使用）

**用戶說：**
> 我有哪些可以使用的計畫帳號？可以用什麼 partition？

**Agent 應做：**
1. 執行 `sacctmgr show user $USER withassoc format=Account -n | awk '{print $2}' | sort -u` 列出帳號
2. 執行 `sinfo --format="%P %a %l %D %C %G" | column -t` 列出可用 partition
3. 整理成表格呈現給用戶，請用戶選擇

---

## 🟢 情境 B：指定 partition，要求最大規格

**用戶說：**
> 幫我用 ngs250g 跑一個 sleep infinity，要最大規格，不要浪費資源

**Agent 應做：**
1. 查詢帳號清單，請用戶確認要用哪個帳號（或列出並讓用戶選）
2. 查 QoS：`sacctmgr show qos p_ngs250g format=Name,MaxTRESPerUser -n` → `cpu=32, mem=256000M`
3. 產出 script：`--cpus-per-task=32 --mem=250G`（填天花板，不是 1）
4. `mkdir -p logs && sbatch <script>.slurm`
5. 確認 Job ID 與狀態

**關鍵詞識別：** 「最大規格」、「不要浪費」、「full」、「用滿」、「全部」

---

## 🟢 情境 C：指定資源數量

**用戶說：**
> 我要用計畫 gov109028，在 ngs62g 跑 BWA 比對，需要 8 個 CPU 和 60G 記憶體，時間大概 2 天

**Agent 應做：**
1. 確認 `gov109028` 在用戶帳號清單中
2. 確認 `ngs62g` 的 QoS 上限：8 CPU / 62G → 用戶要求 8 CPU / 60G，**合法**
3. 產出 script：`--account=gov109028 --partition=ngs62g --cpus-per-task=8 --mem=60G --time=2-00:00:00`
4. 送出並回報

---

## 🟢 情境 D：GPU 工作

**用戶說：**
> 我要跑 PyTorch 訓練，用 4 張 H200，給我一個 GPU script

**Agent 應做：**
1. 列出用戶帳號，並說明 GPU partition 需要特定帳號
2. 執行 `scontrol show partition 8gpus | grep AllowAccounts` 確認哪些帳號有權限
3. 請用戶確認使用的 GPU 帳號
4. 產出 script：`--partition=8gpus --gres=gpu:H200:4 --cpus-per-task=48 --mem=800G`
5. 送出並回報

---

## 🟢 情境 E：互動式 session

**用戶說：**
> 我想要開一個互動式的 CPU session 來測試指令

**Agent 應做：**
1. 列出用戶帳號，請選擇
2. 執行：`srun -p ngstest --account=<選定帳號> --cpus-per-task=4 --mem=32G --pty bash`

---

## 🟢 情境 F：查看目前工作狀態

**用戶說：**
> 我的 job 跑了多久了？還有哪些在跑？

**Agent 應做：**
```bash
squeue -u $USER -o "%.18i %.9P %.20j %.8T %.10M %.9l %R"
```

---

## 🟢 情境 G：取消工作

**用戶說：**
> 幫我取消 job 137106

**Agent 應做：**
```bash
scancel 137106
squeue -u $USER   # 確認已取消
```

---

## 🟢 情境 H：大記憶體需求

**用戶說：**
> 我需要 3TB 記憶體跑 de novo assembly，幫我用最大 CPU 派一個 job

**Agent 應做：**
1. 識別需要 MPN 節點：`ngs3t`（3000 GB，64 CPU 上限）
2. 查帳號，請用戶確認
3. 查 QoS：`sacctmgr show qos p_ngs3t format=Name,MaxTRESPerUser -n`
4. 產出 script：`--partition=ngs3t --cpus-per-task=64 --mem=3000G`（最大規格）

---

## 🔴 常見錯誤情境（Agent 不應這樣做）

| ❌ 錯誤行為 | ✅ 正確行為 |
|:---|:---|
| 用戶說「ngs250g 最大規格」→ agent 寫 `--cpus-per-task=1` | 應寫 `--cpus-per-task=32 --mem=250G` |
| 直接假設帳號是 `mst109178` | 應執行 `sacctmgr` 查詢並讓用戶確認 |
| GPU job 用 CPU 帳號 | 應先查 `AllowAccounts` 再請用戶選正確 GPU 帳號 |
| 沒有 `mkdir -p logs` 就直接 `sbatch` | 必須先確認 logs 目錄存在 |
| 寫完 script 沒有送出 | 用戶說「寫完送出」→ 必須執行 `sbatch` 並回報 Job ID |

---

## 📋 快速參考：關鍵詞 → 行為對應

| 用戶關鍵詞 | Agent 行為 |
|:---|:---|
| 「我有什麼帳號」、「可用計畫」 | `sacctmgr show user $USER withassoc ...` |
| 「可用 partition」、「可以用什麼隊列」 | `sinfo --format=...` |
| 「最大規格」、「用滿」、「不要浪費」 | 填 QoS 天花板（見 SKILL.md Section 2E） |
| 「sleep infinity」、「佔位」 | 內容為 `sleep infinity`，無限時間 partition |
| 「送出」、「派送」、「submit」 | 執行 `sbatch`，回報 Job ID |
| 「取消」、「cancel」 | 執行 `scancel <JOB_ID>` |
| 「查看」、「狀態」、「幾個在跑」 | 執行 `squeue -u $USER` |
| 「互動式」、「interactive」 | 執行 `srun ... --pty bash` |
