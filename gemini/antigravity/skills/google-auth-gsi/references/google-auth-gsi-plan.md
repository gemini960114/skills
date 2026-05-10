# Google Auth Implementation Plan

## 目標

為本專案建立一套穩定的 Google Auth 登入模組，範圍只包含目前程式碼內已存在的 Google Identity Services 登入、邀請碼驗證、後端 token 簽發、環境變數設定、Cloud Run 部署變數，以及本次排查出的關鍵 header 問題與解法。

本計畫不包含完整 OAuth authorization code flow、不包含資料庫使用者系統、不包含 refresh token、不包含角色權限模型。

## 目前程式碼架構

### 前端

檔案：`frontend/app.js`

目前前端登入流程如下：

1. `LoginPage` 初始載入時呼叫 `GET /api/auth/config`。
2. 後端回傳：
   - `authEnabled`
   - `googleClientId`
   - `invitationHint`
3. 若 `authEnabled=false`，前端直接進入工作台。
4. 若 `googleClientId` 為空，前端只顯示邀請碼登入按鈕，呼叫 `POST /api/auth/login`。
5. 若 `googleClientId` 有值，前端等待使用者輸入邀請碼後初始化 Google Identity Services button。
6. Google button callback 收到 `resp.credential` 後，前端呼叫 `POST /api/auth/google`。
7. 後端驗證成功後回傳本系統 token，前端存入 `localStorage`：
   - `gpt_image2_auth_token`
   - `gpt_image2_auth_email`
8. 後續 API request 透過 `Authorization: Bearer <token>` 傳給後端。

關鍵前端程式位置：

- `fetch('/api/auth/config')`
- `window.google.accounts.id.initialize({ client_id, callback })`
- `window.google.accounts.id.renderButton(...)`
- `fetch('/api/auth/google', { credential, invitationCode })`
- `storeSession(token, email)`
- `authHeaders(token)`

### 後端

檔案：`backend/server.js`

目前後端登入流程如下：

1. `AUTH_ENABLED=true` 時啟用登入檢查。
2. `GET /api/auth/config` 將 Google Client ID 與邀請碼提示回傳給前端。
3. `POST /api/auth/login` 只驗證邀請碼，成功後簽發本系統 token。
4. `POST /api/auth/google` 先驗證邀請碼，再驗證 Google ID token。
5. Google ID token 透過 `https://oauth2.googleapis.com/tokeninfo?id_token=...` 驗證。
6. 若有設定 `GOOGLE_CLIENT_ID`，後端會檢查 `info.aud === GOOGLE_CLIENT_ID`。
7. 成功後以 Google email 作為 user，簽發本系統 token。
8. `requireAuth` 驗證 `Authorization: Bearer <token>`。

關鍵後端程式位置：

- `isAuthEnabled()`
- `createToken(user)`
- `verifyToken(token)`
- `requireAuth(req, res, next)`
- `enforceRateLimit(req, res)`
- `GET /api/auth/config`
- `POST /api/auth/login`
- `POST /api/auth/google`

## 必要環境變數

### 本機 `.env`

檔案：`backend/.env`

建議必要設定：

```env
AUTH_ENABLED=true
INVITATION_CODE=change-this-code
INVITATION_HINT=optional-display-hint
SESSION_SECRET=replace-with-at-least-32-random-characters
GOOGLE_CLIENT_ID=your-web-client-id.apps.googleusercontent.com
```

說明：

| 變數 | 必填 | 用途 |
| --- | --- | --- |
| `AUTH_ENABLED` | 建議必填 | `true` 啟用登入，`false` 開放存取 |
| `INVITATION_CODE` | 啟用 auth 時必填 | 第一層邀請碼驗證 |
| `INVITATION_HINT` | 選填 | 顯示在登入頁的提示 |
| `SESSION_SECRET` | 必填 | 本系統 token HMAC 簽名密鑰 |
| `GOOGLE_CLIENT_ID` | Google 登入時必填 | Google OAuth Web Client ID |

### Cloud Build / Cloud Run

檔案：`cloudbuild.yaml`

Cloud Run 部署時要透過 `_GOOGLE_CLIENT_ID` 傳入，並在 `--set-env-vars` 中設定為 `GOOGLE_CLIENT_ID=${_GOOGLE_CLIENT_ID}`。

建議 substitution：

```yaml
_AUTH_ENABLED: 'true'
_INVITATION_CODE: 'change-me'
_SESSION_SECRET: 'change-me-to-a-long-random-secret'
_GOOGLE_CLIENT_ID: 'your-web-client-id.apps.googleusercontent.com'
```

注意：Cloud Run 實際環境中的 `GOOGLE_CLIENT_ID` 必須與 Google Cloud Console 中設定 Authorized JavaScript origins 的 OAuth Client 是同一支。

## Google Cloud Console 設定

### OAuth Client 類型

必須建立：

```text
Application type: Web application
```

不要使用 Android、iOS、Desktop 類型的 client ID。

### Authorized JavaScript origins

Google Identity Services button 會檢查目前頁面的 `location.origin`。這裡必須加入所有會開啟前端頁面的 origin。

本機常用設定：

```text
http://localhost:3000
http://localhost:3001
http://localhost:8080
http://127.0.0.1:3000
```

正式站設定：

```text
https://gpt2image.biobank.org.tw
```

Cloud Run 直連設定範例：

```text
https://gpt-image2-studio-xxxx-de.a.run.app
```

規則：

- 只填 `scheme + host + port`。
- 不要加 path。
- 不要加尾端 `/`。
- `localhost` 與 `127.0.0.1` 是不同 origin，要分開加。
- `http` 與 `https` 是不同 origin，要分開加。
- 不同 port 是不同 origin，要分開加。

### Authorized redirect URIs

目前這份程式碼使用 Google Identity Services credential button，不是傳統 redirect callback flow，因此本功能主要依賴 Authorized JavaScript origins。

若未來改成 redirect mode，才需要加入 redirect URI，例如：

```text
https://gpt2image.biobank.org.tw/oauth/callback
```

但目前 `/oauth/callback` 不是這份程式碼的登入入口。

## 關鍵 Header 問題與標準解法

### 問題現象

曾出現以下現象：

```text
[GSI_LOGGER]: The given origin is not allowed for the given client ID.
```

或 Google popup 開啟後停在：

```text
https://accounts.google.com/gsi/transform
```

畫面空白、卡住，手機也同樣卡住。

### 根因

本專案使用 `helmet()` 設定安全 header。Helmet 預設 header 對一般網站是合理的，但 Google Identity Services popup 登入需要父頁與 Google popup 能完成跨視窗通訊。

若使用過嚴的預設值，例如：

```text
Cross-Origin-Opener-Policy: same-origin
Referrer-Policy: no-referrer
```

可能導致：

1. Google 無法正確判斷來源 origin。
2. Google popup 無法和父頁完成必要通訊。
3. 即使 Google Console 已加入正確 Authorized JavaScript origin，仍可能出現 GSI origin/client id 錯誤或 popup 卡住。

### 解法

在 `backend/server.js` 中明確設定 Helmet：

```js
app.use(helmet({
  contentSecurityPolicy: false,
  crossOriginOpenerPolicy: { policy: 'same-origin-allow-popups' },
  referrerPolicy: { policy: 'strict-origin-when-cross-origin' },
}));
```

這兩個設定不可省略：

| Header | 建議值 | 原因 |
| --- | --- | --- |
| `Cross-Origin-Opener-Policy` | `same-origin-allow-popups` | 允許 Google popup 與父頁完成登入通訊 |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | 讓 Google 能看到正確 origin 以比對 client allowlist |

部署後應確認 response header：

```text
Cross-Origin-Opener-Policy: same-origin-allow-popups
Referrer-Policy: strict-origin-when-cross-origin
```

## Implementation Steps

### Step 1：整理環境變數

1. 在 `backend/.env.example` 補齊 auth 相關範例：

```env
AUTH_ENABLED=true
INVITATION_CODE=change-me
INVITATION_HINT=change-me
SESSION_SECRET=change-me-to-a-long-random-secret
GOOGLE_CLIENT_ID=
```

2. 確認 `backend/.env` 不提交到 git。
3. 確認 production 透過 Cloud Run env vars 設定，不把 secret 寫死在程式碼。

### Step 2：確認後端 auth config

維持 `GET /api/auth/config` 回傳：

```json
{
  "authEnabled": true,
  "googleClientId": "...apps.googleusercontent.com",
  "invitationHint": "ai4all"
}
```

驗證方式：

```powershell
Invoke-WebRequest -UseBasicParsing http://localhost:3000/api/auth/config
```

或正式站：

```powershell
Invoke-WebRequest -UseBasicParsing https://gpt2image.biobank.org.tw/api/auth/config
```

### Step 3：確認前端 GSI 初始化條件

前端應維持以下條件：

1. 未輸入邀請碼時，不初始化 Google button。
2. 有 `googleClientId` 且邀請碼非空時，才呼叫 `window.google.accounts.id.initialize`。
3. callback 收到 `resp.credential` 後，連同 `invitationCode` 傳給 `/api/auth/google`。
4. 不在前端信任 email 或 token payload，最終驗證以後端為準。

### Step 4：後端驗證 Google credential

後端 `/api/auth/google` 應維持：

1. 先檢查 `AUTH_ENABLED`。
2. 套用 `enforceRateLimit`。
3. 先驗證 `INVITATION_CODE`。
4. 呼叫 Google tokeninfo 驗證 `id_token`。
5. 檢查 `info.aud` 是否等於 `GOOGLE_CLIENT_ID`。
6. 成功後簽發本系統 token。

最低限度防護：

```js
if (googleClientId && info.aud !== googleClientId) {
  throw new Error('Google Client ID 不符');
}
```

### Step 5：設定 Google Cloud Console

1. 建立或確認 Web OAuth Client。
2. 在 Authorized JavaScript origins 加入實際 `location.origin`。
3. 本機與正式站分開加。
4. 儲存後等待 1 到 5 分鐘。
5. 使用無痕視窗測試，避免舊 iframe/cache 影響判斷。

### Step 6：部署與重啟

本機：

```powershell
cd D:\antigravity\gpt-image2\web-studio\backend
$env:DEBUG="1"
node server.js
```

或若從 repo root 啟動：

```powershell
cd D:\antigravity\gpt-image2\web-studio
$env:DEBUG="1"
node backend\server.js
```

注意：建議以 `backend` 作為工作目錄啟動，因為 `.env`、`references`、`SKILL.md` 等路徑都以 backend 目錄較穩。

正式站：

1. 確認 `cloudbuild.yaml` 有傳入 `_GOOGLE_CLIENT_ID`。
2. 部署 Cloud Run。
3. 確認 Cloud Run env vars 中有正確 `GOOGLE_CLIENT_ID`。
4. 確認正式站 response headers 已更新。

## 驗證清單

### Console 驗證

在登入頁 DevTools console 執行：

```js
location.origin
document.referrer
```

`location.origin` 的輸出必須與 Google Console 的 Authorized JavaScript origins 完全一致。

### Header 驗證

檢查 response header 必須包含：

```text
Cross-Origin-Opener-Policy: same-origin-allow-popups
Referrer-Policy: strict-origin-when-cross-origin
```

PowerShell 範例：

```powershell
$r = Invoke-WebRequest -UseBasicParsing https://gpt2image.biobank.org.tw
$r.Headers
```

### 功能驗證

1. 開啟登入頁。
2. 輸入正確邀請碼。
3. Google button 應正常 render。
4. 點擊 Google button 後不應卡在空白 popup。
5. Google 登入成功後，前端應收到 `/api/auth/google` 回傳的 token。
6. `localStorage` 應出現：
   - `gpt_image2_auth_token`
   - `gpt_image2_auth_email`
7. 呼叫受保護 API 時應帶：

```text
Authorization: Bearer <token>
```

## 常見問題與排查

### 1. `The given origin is not allowed for the given client ID`

檢查：

1. `location.origin` 是否已加入 Authorized JavaScript origins。
2. `GOOGLE_CLIENT_ID` 是否與 Google Console 中正在編輯的 OAuth Client 相同。
3. 是否已儲存並等待 1 到 5 分鐘。
4. 是否 response header 包含 `Referrer-Policy: strict-origin-when-cross-origin`。
5. 是否用無痕視窗排除快取與 Google iframe 狀態。

### 2. Google popup 開啟後空白或卡住

檢查：

1. 是否 response header 包含 `Cross-Origin-Opener-Policy: same-origin-allow-popups`。
2. 是否手機與桌機都重現。
3. 是否部署後服務仍回舊 header。

若仍不穩，下一版可考慮將 GSI 從 popup mode 改成 redirect mode。

### 3. 本機可以，正式站不行

檢查：

1. 正式站 origin 是否加入 Google Console。
2. Cloud Run env var `GOOGLE_CLIENT_ID` 是否正確。
3. 正式站是否已部署最新 `backend/server.js`。
4. CDN、proxy、反向代理是否覆蓋或移除關鍵 headers。

### 4. 正式站可以，本機不行

檢查：

1. 本機開的是 `localhost` 還是 `127.0.0.1`。
2. port 是 `3000`、`3001` 還是 `8080`。
3. 對應 origin 是否都有加入 Google Console。

### 5. `/api/auth/google` 回 `Google Client ID 不符`

代表 Google credential 的 `aud` 與後端 `GOOGLE_CLIENT_ID` 不一致。

檢查：

1. 前端 `/api/auth/config` 回傳的 client id。
2. Cloud Run env var 中的 `GOOGLE_CLIENT_ID`。
3. Google Console 正在使用的 OAuth Client。

## 建議保留的安全邊界

1. 邀請碼與 Google credential 都必須由後端驗證。
2. 前端不得自行解 JWT 後當作登入成功依據。
3. `SESSION_SECRET` 不可使用預設值。
4. `backend/.env` 不可提交。
5. `GOOGLE_CLIENT_ID` 可以出現在前端，但 `SESSION_SECRET`、邀請碼正式值不可暴露在前端 bundle。
6. 登入 endpoint 保留 rate limit。
7. 受保護 API 必須經過 `requireAuth`。

## 最小完成定義

一個 Google Auth 登入模組在本專案中算完成，必須同時滿足：

1. `GET /api/auth/config` 回傳正確 auth 設定。
2. 邀請碼登入在無 `GOOGLE_CLIENT_ID` 時可用。
3. Google button 在有 `GOOGLE_CLIENT_ID` 時可正常 render。
4. Google popup 在桌機與手機都不會卡住。
5. `/api/auth/google` 會驗證邀請碼與 Google token `aud`。
6. 成功登入後前端能存 token 並呼叫受保護 API。
7. 正式站 response headers 包含：
   - `Cross-Origin-Opener-Policy: same-origin-allow-popups`
   - `Referrer-Policy: strict-origin-when-cross-origin`
8. Google Console Authorized JavaScript origins 包含所有實際使用 origin。

