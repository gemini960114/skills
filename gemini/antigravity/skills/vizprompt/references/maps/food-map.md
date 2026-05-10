# 手繪城市美食地圖模板

本檔案用於生成“某座城市 / 某個區域的吃貨地圖”視覺，常見用途：

- 旅行 / 美食攻略主視覺
- 自媒體引流圖
- 餐飲品牌活動主視覺
- 教育 / 文化科普圖
- 城市 IP 周邊圖

主要特徵：

- 手繪水彩 / 復古插畫風
- 編號點位 + 文字標籤
- 圖例與方向標
- 中心 IP（熊貓 / 城市吉祥物 / 美食吉祥物）
- 邊角裝飾

## 適用範圍

- 城市美食地圖
- 街區美食路線圖
- 節日 / 主題活動美食地圖
- 單一菜系 / 單一品類美食地圖（火鍋 / 茶飲 / 烘焙）

## 何時使用

- 使用者提到“美食地圖 / 吃貨地圖 / 城市美食 / 探店地圖”
- 使用者希望視覺手繪感強，適合社交分享
- 使用者希望有“一張圖能講清楚去哪吃”的感覺

不要使用：

- 使用者要的是“通用城市地圖”（用 `illustrated-city-map.md`）
- 使用者要的是“路線導航圖”（用 `travel-route-map.md`）
- 使用者要的是“門店分佈圖”（用 `store-distribution-map.md`）

## 缺失資訊優先提問順序

1. 城市 / 區域名
2. 主題：美食 / 網紅店 / 小吃 / 飲品
3. 美食條目：使用者指定 or 我幫你列
4. 是否需要包含地標（10 處以內）
5. 風格：復古羊皮紙 / 現代水彩 / Q 萌插畫
6. 是否需要中心吉祥物（熊貓、辣椒、城市象徵）
7. 語言：中文 / 雙語

## 主模板：復古手繪城市美食地圖

📖 描述

整體為一張復古紋理羊皮紙或米色背景，上面繪有道路、河流、公園等抽象底圖；地標與美食以編號小插畫形式分佈在地圖上，右下角圖例，畫面中心一個吉祥物，邊角點綴植物。

📝 提示詞

```json
{
  "type": "手繪地圖資訊圖",
  "goal": "生成一張高完成度的城市美食地圖，可作為旅遊攻略 / 自媒體首圖 / 城市文化主視覺",
  "style": "{argument name=\"art style\" default=\"復古羊皮紙上的水彩墨水手繪插畫\"}",
  "title_section": {
    "city": "{argument name=\"city name\" default=\"成都\"}",
    "title_text": "{argument name=\"map title\" default=\"吃貨暴走地圖\"}",
    "mascot": "{argument name=\"title mascot\" default=\"戴著墨鏡並豎起大拇指的卡通紅辣椒\"}"
  },
  "border": "{argument name=\"border decoration\" default=\"綠葉與紅辣椒藤蔓\"}",
  "layout": {
    "background": "{argument name=\"background description\" default=\"帶有黃色道路、藍色河流和綠色公園區域的紋理米色羊皮紙\"}",
    "sections": [
      {
        "title": "地標建築",
        "count": "{argument name=\"landmark count\" default=\"6\"}",
        "illustrations": "{argument name=\"landmark illustrations\" default=\"傳統涼亭、傳統寺院、帶攀爬熊貓的現代摩天大樓、電視塔、傳統牌坊、工業建築\"}",
        "labels": "{argument name=\"landmark labels\" default=\"人民公園、文殊院、IFS、339電視塔、寬窄巷子、東郊記憶\"}"
      },
      {
        "title": "美食地點",
        "count": "{argument name=\"food count\" default=\"12\"}",
        "illustrations": "{argument name=\"food illustrations\" default=\"麻婆豆腐、紅油水餃、冷鍋串串、三大炮、蛋烘糕、九宮格火鍋、肥腸粉、缽缽雞、冒菜、蓋碗茶、冰粉、兔頭\"}",
        "labels": "{argument name=\"food labels\" default=\"1 陳麻婆豆腐、2 鍾水餃、3 春熙路、4 寬窄巷子·三大炮、5 建設路·葉婆婆蛋烘糕、6 玉林路·小龍坎火鍋、7 香香巷·肥腸粉、8 武侯祠大街·缽缽雞、9 東郊記憶·冒椒火辣、10 人民公園·鶴鳴茶社、11 錦裡古街·冰粉、12 雙流老媽兔頭\"}"
      },
      {
        "title": "圖例",
        "position": "右下角",
        "items": ["紅點：美食地點", "綠色建築：地標景點", "綠樹：公園綠地", "藍線：河流湖泊", "黃色雙線：主要道路"]
      }
    ],
    "centerpiece": "{argument name=\"centerpiece\" default=\"坐著吃竹子的大熊貓\"}",
    "extras": [
      "{argument name=\"compass\" default=\"帶有東南西北方向的復古羅盤\"}",
      "{argument name=\"disclaimer\" default=\"帶有紅辣椒圖示的免責宣告：溫馨提示：吃辣需謹慎，腸胃要保護~\"}"
    ]
  },
  "constraints": {
    "must_keep": [
      "美食條目數量與編號必須一致",
      "標籤文字清晰可讀",
      "中心吉祥物視覺搶眼但不搶圖例位置",
      "整體保持手繪水彩風"
    ],
    "avoid": [
      "出現真實地圖比例（這是插畫地圖）",
      "美食條目過多導致擁擠",
      "標籤字型多種風格混用",
      "圖例缺失或與點位不對應"
    ]
  }
}
```

### 引數策略

- 必問：城市名、主題、美食列表（或允許我幫列）、風格
- 可預設：背景紋理、圖例、羅盤
- 可隨機：地標具體名稱（在該城市內合理）

### 自動補全策略

- 使用者只給城市名時：從該城市知名美食裡挑 8-12 項 + 6 處經典地標
- 風格預設“復古水彩 + 米色羊皮紙”
- 中心吉祥物按城市選：成都熊貓、重慶熊貓拿火鍋、廣州燒鵝、北京龍、長沙臭豆腐
- slogan 不超過 12 字

## 變體 1：單品類美食地圖（火鍋 / 茶飲 / 甜品）

📝 提示詞

```json
{
  "type": "單品類美食地圖",
  "city": "{argument name=\"city\" default=\"重慶\"}",
  "category": "{argument name=\"category\" default=\"火鍋\"}",
  "title_text": "{argument name=\"title\" default=\"火鍋地圖\"}",
  "mascot": "{argument name=\"mascot\" default=\"舉著紅湯勺的卡通熊貓\"}",
  "sections": [
    {
      "title": "推薦門店",
      "count": "{argument name=\"store count\" default=\"10\"}"
    },
    {
      "title": "圖例",
      "items": ["紅點：門店", "辣椒數：辣度等級", "金標：必吃"]
    }
  ],
  "constraints": {
    "must_feel": "門店主題鮮明，不要混入其它品類"
  }
}
```

## 變體 2：現代扁平風美食地圖

📝 提示詞

```json
{
  "type": "扁平插畫風格美食地圖",
  "city": "{argument name=\"city\" default=\"上海\"}",
  "style": "扁平向量插畫，柔和粉色 + 米色 + 灰藍",
  "title_text": "{argument name=\"title\" default=\"週末探店地圖\"}",
  "centerpiece": "卡通女孩拿地圖",
  "constraints": {
    "must_feel": "適合小紅書 / 朋友圈分享，乾淨不復古"
  }
}
```

## 變體 3：自動補全模式

📝 提示詞

```json
{
  "type": "美食地圖自動補全模板",
  "mode": "auto-fill",
  "rule": "使用者只給城市，自動決定地標、美食列表、風格、吉祥物",
  "constraints": {
    "must_feel": "完整、可分享、不使用者不需要再補任何資訊"
  }
}
```

## 避免事項

- 不要把美食地圖畫成真實地理比例尺地圖
- 不要讓美食條目超過 15 個，太多會讓標籤彼此擠壓
- 不要讓圖例位置與地標重疊
- 不要在一張地圖裡混 “美食 + 路線 + 門店分佈”三種功能（拆開為不同模板）
- 不要讓吉祥物比標題更顯眼（吉祥物是輔助）
