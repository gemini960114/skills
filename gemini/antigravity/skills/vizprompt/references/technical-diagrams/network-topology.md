# 網路拓撲圖模板

> ⚠️ **本模板生成的是點陣圖（PNG）**，不是 NetBox / Cisco Packet Tracer / draw.io 可編輯網路拓撲。
> 需要可編輯請用 NetBox / Lucidchart / draw.io / Cisco Packet Tracer。

本檔案用於生成"工程感網路拓撲圖"：

- 公司 / 資料中心 網路拓撲
- 多區域 / 多 zone 部署拓撲
- 微服務 / 服務網格 拓撲
- VPC / 子網 / 路由表拓撲
- 邊緣 / CDN / 多雲互聯拓撲

特徵：

- 裝置節點用型別化 glyph：路由器（菱形交叉）/ 交換機（矩形多埠）/ 伺服器（帶散熱條小機箱）/ 防火牆（磚牆）/ 雲（雲朵）/ DB（圓柱）
- 物理連線用粗線，邏輯連線用虛線
- 大虛線框包圍 zone / VLAN / VPC
- 頻寬 / 協議標線上上（如 "10 Gbps" / "BGP" / "TLS 1.3"）
- 暗色 grid + 等寬字型（沿用視覺系統）

## 適用範圍

- 資料中心 / 機房網路拓撲
- 雲架構網路拓撲（VPC / subnet / NAT / IGW）
- 多區域 / 多雲互聯
- 服務網格拓撲（service mesh）
- 邊緣 / CDN / 公網入口拓撲

## 何時使用

- 使用者提到 "網路拓撲 / network topology / 部署拓撲 / VPC / 子網 / 資料中心 / 機房 / 服務網格"
- 使用者希望「帶網路裝置 glyph + 區域分組 + 連線頻寬標註」標準網路圖
- 使用者接受點陣圖

不要使用：

- 使用者要的是「應用層系統架構」 → 用 `technical-diagrams/system-architecture.md`
- 使用者要的是「業務流程」 → 用 `technical-diagrams/flowchart-decision.md`
- 使用者要的是「時序圖」 → 用 `technical-diagrams/sequence-diagram.md`

## 缺失資訊優先提問順序

1. 拓撲名稱（"AWS VPC 拓撲 / 公司機房拓撲 / 多區域部署"）
2. 主要 zones / subnets / VPCs（建議 2-5 個區域）
3. 每個區域內的裝置 / 例項（路由器 / 交換機 / 伺服器 / DB / 負載均衡）
4. 區域間的連線（VPN / Peering / IGW / Direct Connect）
5. 連線的協議 / 頻寬（可選）
6. 是否標 IP 段 / CIDR
7. 比例（預設 16:9 橫版）

## 主模板：標準雲 / 資料中心 網路拓撲圖

📖 描述

整張圖按 zone / VPC 劃分大虛線框區域，每個區域內放裝置節點（帶型別化 glyph），節點間用粗線連線（標頻寬 / 協議），跨區域連線用專門的閘道器 / VPN 節點。整體在暗色 grid 背景上呈現工程感。

📝 提示詞

```json
{
  "type": "工程感網路拓撲圖",
  "goal": "生成一張工程感網路拓撲圖作為部署文件 / 網路架構 review / 培訓材料",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"16:9\"}",
    "background": "deep slate #0F172A with subtle 1px grid #1E293B at 32px spacing",
    "outer_padding": "60px"
  },
  "title_strip": {
    "title": "{argument name=\"title\" default=\"AWS Multi-AZ VPC Topology\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"production · ap-northeast-1\"}",
    "position": "top-left, JetBrains Mono / SF Mono, light gray"
  },
  "device_glyphs": {
    "rule": "每種裝置使用統一的極簡幾何 glyph，避免使用真實廠商圖示",
    "types": [
      { "type": "router", "glyph": "diamond shape with X cross inside", "color": "amber #FBBF24" },
      { "type": "switch", "glyph": "rectangle with multiple port dots along the bottom edge", "color": "amber #FBBF24" },
      { "type": "firewall", "glyph": "stylized brick wall pattern (small rectangles in 2-3 rows)", "color": "rose #FB7185" },
      { "type": "load_balancer", "glyph": "trapezoid funnel with 3 lines coming in, 1 going out", "color": "blue #60A5FA" },
      { "type": "server", "glyph": "small rack rectangle with 3-4 horizontal slots", "color": "emerald #34D399" },
      { "type": "container", "glyph": "rounded square with sail / shipping container symbol", "color": "emerald #34D399" },
      { "type": "database", "glyph": "cylinder (3D-suggested)", "color": "violet #A78BFA" },
      { "type": "cloud_service", "glyph": "cloud outline with abbreviation inside (e.g. 'S3', 'CDN')", "color": "cyan #22D3EE" },
      { "type": "user", "glyph": "stick figure", "color": "cyan #22D3EE" },
      { "type": "internet", "glyph": "globe with latitude / longitude lines", "color": "slate #94A3B8" },
      { "type": "nat_gateway", "glyph": "small rectangle labeled 'NAT'", "color": "amber #FBBF24" },
      { "type": "vpn_gateway", "glyph": "small rectangle with key icon, labeled 'VPN'", "color": "rose #FB7185" }
    ]
  },
  "zones": {
    "count": "{argument name=\"zone_count\" default=\"4\"}",
    "items": [
      { "id": "Z1", "label": "Public Internet", "color_border": "slate #94A3B8 dashed", "cidr": "0.0.0.0/0" },
      { "id": "Z2", "label": "VPC · ap-northeast-1\\n10.0.0.0/16", "color_border": "amber #FBBF24 dashed", "cidr": "10.0.0.0/16" },
      { "id": "Z3", "label": "Public Subnet · 10.0.1.0/24 (AZ-a)", "color_border": "blue #60A5FA dashed", "parent": "Z2" },
      { "id": "Z4", "label": "Private Subnet · 10.0.2.0/24 (AZ-a)", "color_border": "emerald #34D399 dashed", "parent": "Z2" }
    ],
    "zone_label_position": "top-left of each zone box, mono 11pt with CIDR on second line"
  },
  "nodes": {
    "items": [
      { "id": "N1", "type": "user", "label": "End Users", "zone": "Z1" },
      { "id": "N2", "type": "internet", "label": "Internet", "zone": "Z1" },
      { "id": "N3", "type": "cloud_service", "label": "CloudFront\\n(CDN)", "zone": "Z1" },
      { "id": "N4", "type": "load_balancer", "label": "ALB", "zone": "Z3" },
      { "id": "N5", "type": "nat_gateway", "label": "NAT GW", "zone": "Z3" },
      { "id": "N6", "type": "container", "label": "ECS Tasks\\n(2 instances)", "zone": "Z4" },
      { "id": "N7", "type": "database", "label": "RDS PostgreSQL\\n(Multi-AZ)", "zone": "Z4" },
      { "id": "N8", "type": "cloud_service", "label": "S3\\n(static assets)", "zone": "Z1" }
    ],
    "node_label_format": "device name + optional second line with detail (count / class / role)，mono 10pt 標在 glyph 下方"
  },
  "connections": {
    "items": [
      { "from": "N1", "to": "N2", "type": "physical", "label": "" },
      { "from": "N2", "to": "N3", "type": "physical", "label": "HTTPS / TLS 1.3" },
      { "from": "N3", "to": "N4", "type": "physical", "label": "Origin pull" },
      { "from": "N4", "to": "N6", "type": "physical", "label": "HTTP" },
      { "from": "N6", "to": "N7", "type": "physical", "label": "TCP 5432" },
      { "from": "N6", "to": "N5", "type": "physical", "label": "egress" },
      { "from": "N5", "to": "N2", "type": "physical", "label": "" },
      { "from": "N3", "to": "N8", "type": "physical", "label": "Origin pull" }
    ],
    "line_style": {
      "physical": "solid line 2px slate #94A3B8 (carries actual traffic)",
      "logical": "dashed line 1.5px slate #64748B (logical relation, e.g. 'IAM allows access')",
      "redundant": "double-line in violet #A78BFA (HA pair, redundant link)",
      "encrypted": "solid line 2px emerald #34D399 with small lock glyph in middle"
    },
    "label_format": "protocol + optional bandwidth, e.g. 'HTTPS / 443' / '10 Gbps' / 'BGP' / 'TLS 1.3'，mono 9pt 標線上中央",
    "rule_routing": "正交走線為主；跨 zone 時穿過 zone 邊界畫"
  },
  "annotations": {
    "ip_cidr_labels": {
      "enabled": "{argument name=\"ip_labels_enabled\" default=\"true\"}",
      "rule": "每個 zone 標 CIDR；關鍵節點標 IP 或 hostname"
    },
    "az_labels": {
      "enabled": "{argument name=\"az_labels_enabled\" default=\"true\"}",
      "rule": "雲環境下標可用區 (AZ-a / AZ-b)"
    }
  },
  "legend": {
    "enabled": true,
    "position": "bottom-right",
    "content": "device glyph → device type，line style → connection type (physical / logical / redundant / encrypted)，zone color → zone type",
    "style": "small panel, semi-transparent bg, mono 10pt"
  },
  "constraints": {
    "must_keep": [
      "每種裝置 glyph 一致，不混用",
      "zone 用大虛線框清晰包圍",
      "zone 標籤含 CIDR / AZ（雲環境）或 VLAN ID（資料中心）",
      "連線粗細 / 顏色編碼反映連線型別",
      "暗色 grid 背景 + 等寬字型",
      "legend 必畫"
    ],
    "avoid": [
      "用真實廠商 logo (Cisco / AWS / Azure 真實圖示) → 容易侵權 + 破壞統一視覺",
      "裝置 glyph 不一致 (一個用方框一個用真實圖示)",
      "用 emoji 當裝置圖示",
      "zone 不用虛線框 → 失去區域感",
      "連線無 protocol 標 → 失去工程價值",
      "節點 > 15 個 → 擁擠，考慮分子圖",
      "用 3D / 漸變 / 玻璃質感",
      "聲稱這是可編輯 SVG"
    ]
  }
}
```

### 引數策略

- **必問**：`title`、zones 列表（含 CIDR / 名稱）、nodes 列表（含 type + zone）、connections（含 from/to）
- **可預設**：`background`（暗色 grid）、`device_glyphs`（預設全套）、`ip_labels_enabled`（true）、`az_labels_enabled`（true）
- **可隨機**：節點擺放位置（在 zone 內自動佈局）

### 自動補全策略

- 使用者給"AWS 單 AZ VPC + ALB + ECS + RDS" → 用 default 拓撲
- 使用者沒給 CIDR → 反問（不能瞎編 IP 段）
- 使用者說"加多 AZ HA" → 複製 private subnet 到 AZ-b，標 redundant 連線
- 使用者說"加 WAF / Shield" → 在 ALB 前加 firewall glyph
- 使用者說要 light 模式 → 用變體 1

## 變體 1：淺色 Light 網路拓撲

```json
{
  "modify": {
    "background": "warm off-white #F8FAFC + faint grid #E2E8F0",
    "node_glyph_fill": "device color × 8% opacity",
    "node_glyph_border": "1.5px solid (deeper shade for white bg)",
    "label_color": "deep slate #0F172A",
    "zone_border_color": "deeper shade",
    "vibe": "白底文件 / 印刷版"
  }
}
```

## 變體 2：服務網格 (Service Mesh) 拓撲

```json
{
  "modify": {
    "title_format": "Service Mesh Topology",
    "node_emphasis": "每個 service node 旁邊貼一個小 sidecar (proxy) glyph，表達 sidecar 模式",
    "connections_emphasis": "service-to-service 連線全部經過 sidecar；標 mTLS 加密",
    "extras": "可加 control plane node (Istio / Linkerd) 在右上角，連線用虛線表示控制流",
    "use_case": "Istio / Linkerd / Consul / Cilium service mesh 文件"
  }
}
```

適用：服務網格架構、零信任網路、SRE 培訓材料。

## 變體 3：多雲互聯拓撲（hybrid cloud）

```json
{
  "modify": {
    "zones": "橫向並排畫多個雲的大框：'AWS Region' + 'GCP Region' + 'On-Prem DC'",
    "interconnect": "雲間用 'Direct Connect' / 'Cloud Interconnect' / 'VPN' 粗連線連線，標頻寬 / SLA",
    "extras": "可加 transit gateway / 中央 routing hub 在畫布中央",
    "use_case": "混合雲 / 多雲架構、災備拓撲、遷移規劃"
  }
}
```

適用：混合雲架構、多雲部署、災備 / DR 拓撲。

## 避免事項

- 用真實廠商圖示（容易侵權）
- 裝置 glyph 不一致（同一種裝置用不同形狀）
- 用 emoji 當裝置圖示
- zone 沒有虛線框 → 失去區域感
- 連線無 protocol / 頻寬標 → 失去工程價值
- 節點 > 15 → 視覺爆炸
- 用 3D / 漸變 / 玻璃質感（破壞工程感）
- 中央 hub-and-spoke 但中心節點沒標"作什麼"
- 把"應用層"元件塞進網路拓撲（應該用 system-architecture）
- 假裝這是可匯出可編輯的 SVG
- IP / CIDR 資訊缺失（雲環境網路圖核心資訊）
