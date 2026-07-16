---
name: "expose-local-service-via-cloudflared"
description: "用 cloudflared quick tunnel 把本機 HTTP 服務（localhost:PORT）對外公開為 https://*.trycloudflare.com，無需帳號。"
---

# Expose Local Service via Cloudflared Quick Tunnel

## 何時使用

- 本機跑了一個 HTTP 服務（預設 port，如 `python -m http.server 8000`、`vite`、`next dev`、自寫的 Flask/FastAPI/Express…）想讓遠端的人（或自己用別台裝置）能打開。
- 環境裡**沒有**已登入的 Cloudflare 帳號，不想為了展示一個頁面申請 token、設定 named tunnel、綁網域。
- 需要 HTTPS（瀏覽器擋 http、service worker、地理位置 API 等場景）。
- 使用者明確要「對外」「公開」「給我網址」「我人在別台」「龍蝦/聊天視窗打不開 localhost」等情境。

## 不適用

- 需要穩定長期網址（quick tunnel 重新啟動網址會變，請改用 named tunnel + 自己的網域）。
- TCP/UDP（非 HTTP）對外公開：cloudflared 可以，但本 skill 只處理 HTTP。
- 需要帳號層級的存取控制、Cloudflare Access 政策、rate limiting。

## 先決條件

- 一個本機 HTTP 服務正在跑（預期在 `http://localhost:PORT`）。
- 環境是 Linux x86_64（其它 arch 換下載 URL）。
- 對外網路可訪問 `github.com`（下載 cloudflared）。
- 使用者已批准安裝 `cloudflared` 到 `~/.local/bin/cloudflared`（預設使用者目錄，不需要 root；不要嘗試寫 `/usr/local/bin/`）。

## 流程

### 1. 確認本機服務可達

```bash
curl -sS -o /dev/null -w "HTTP %{http_code}\n" http://localhost:PORT/
```

不通的話停下來修；tunnel 只是個通道，後端服務本身要健康。

### 2. 安裝 cloudflared（若未安裝）

下載最新 stable binary 到使用者目錄：

```bash
mkdir -p ~/.local/bin
curl -fsSL https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o ~/.local/bin/cloudflared
chmod +x ~/.local/bin/cloudflared
~/.local/bin/cloudflared --version
```

**注意**：
- 不要寫到 `/usr/local/bin/`，沙箱環境通常無 root。
- 用 `latest/download/cloudflared-linux-amd64`（注意 `-amd64.deb` 是另一個檔，不要用）。
- 如果環境是 arm64（少見），改成 `cloudflared-linux-arm64`。

### 3. 啟動 quick tunnel（背景）

```bash
~/.local/bin/cloudflared tunnel --url http://localhost:PORT --no-autoupdate 2>&1
```

丟到背景跑（`background: true`）。記下回傳的 sessionId，後續 poll log 用。

`--no-autoupdate` 避免 cloudflared 在背景偷偷更新、卡住。

### 4. 抓公網網址

Poll log 等待這幾行：

```
INF +--------------------------------------------------------------------------------------------+
INF |  Your quick Tunnel has been created! Visit it at (it may take some time to be reachable):  |
INF |  https://<random>.trycloudflare.com                                                       |
INF +--------------------------------------------------------------------------------------------+
```

網址格式固定是 `https://<3-word-subdomain>.trycloudflare.com`。用 regex 抓：

```
https://[a-z0-9-]+\.trycloudflare\.com
```

第一次啟動通常 5–10 秒就出現。

### 5. 驗證對外可達

```bash
curl -sS -o /dev/null -w "HTTP %{http_code} • %{size_download} bytes\n" \
  https://<random>.trycloudflare.com/
```

預期 `HTTP 200`。可能需要 1–2 次重試（DNS 與 TLS 握手傳播）。

### 6. 回報給使用者

提供：
- 完整 https 網址（單獨一行、可點選）。
- 提醒網址是**臨時**的，session 結束或重啟就失效。
- 想停服務時的指令 / 跟 AI 講一聲。

## 清理 / 停止

兩個 process 都要管：

```bash
# tunnel
process(action=kill, sessionId=<tunnel-session-id>)
# 本機 HTTP 服務
process(action=kill, sessionId=<server-session-id>)
```

或一句「關服務」讓 AI 自己找 session 殺掉。

## 已知陷阱

| 現象 | 原因 | 解法 |
|------|------|------|
| `curl: (23) Failure writing output` 寫到 `/usr/local/bin/` | 沒 root 權限 | 改寫到 `~/.local/bin/` |
| tunnel 啟動後 curl 回 `HTTP 000` exit 6 | DNS/TLS 還在傳播 | 等 10–20 秒重試；用 `process action=log` 看 `Registered tunnel connection` |
| 同一個 port 多個 tunnel 衝突 | cloudflared 不擋，但 QUIC 連線可能閃退 | 一次只跑一個 tunnel |
| log 出現 `ping_group_range` warning | container 沒給 ICMP 權限 | 無害，cloudflared 會 fallback 不做 ICMP probe，**可忽略** |
| log 出現 `failed to sufficiently increase receive buffer size` | UDP buffer 太小 | 無害，效能影響輕微，**可忽略** |

## 範例對話（節錄）

> User: 我用龍蝦網址 xxx，但打不開 localhost
> Agent: 我用 cloudflared 開個 tunnel 把本機服務丟到公網
> Agent: 跑 `curl --version` 確認網路 → 裝 cloudflared 到 `~/.local/bin/` → 背景啟動 tunnel → poll log 抓網址 → curl 驗證 200 → 回報網址
> User: 可以
> Agent: 玩得開心。要關服務跟我說

## 變體

- **換不同 port**：`--url http://localhost:3000` 等，只改 PORT。
- **改用 named tunnel**（需 Cloudflare 帳號 + 已登入的 tunnel）：超出本 skill 範圍，但安裝步驟相同，後續用 `cloudflared tunnel run <name>`。
- **同網域多服務**：起多個 tunnel 進程，每個會拿到不同 trycloudflare 子網域。
