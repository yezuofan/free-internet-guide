# Surge for iOS 使用教程

> Surge 是 iOS 平台最强大的代理客户端，支持所有主流协议，稳定高效。iOS/Mac 一体化。

## 下载安装

**注意**：Surge 是付费应用（¥328），App Store 购买。

- iOS：App Store 搜索「Surge」
- macOS：App Store 搜索「Surge」

**iOS 版需要非中国区 Apple ID** 才能下载。

---

## 基本配置

### 方式一：订阅链接导入（推荐）

1. 打开 Surge
2. 点击「配置」→ 「订阅」
3. 点击「+」添加订阅
4. 粘贴机场订阅链接
5. Surge 会自动识别并导入节点
6. 点击「完成」

### 方式二：手动导入

1. 点击「配置」→ 「编辑器」
2. 点击「+」新建配置
3. 选择「从剪贴板导入」或手动编辑
4. 粘贴节点信息（支持 vmess://、vless://、trojan:// 等格式）

---

## 代理规则

### 规则模式

Surge 支持多种规则模式：

| 模式 | 说明 |
|------|------|
| **规则（Rule）** | 按自定义规则分流（推荐） |
| **全局（Global）** | 所有流量走代理 |
| **直连（Direct）** | 所有流量直连 |

### 内置规则集

Surge 内置了常用规则集：

```ini
[Rule]
# Netflix 分流
DOMAIN-SUFFIX,netflix.com,Netflix
DOMAIN-SUFFIX,nflxvideo.net,Netflix

# ChatGPT 分流
DOMAIN-SUFFIX,openai.com,Proxy
DOMAIN-SUFFIX,chatgpt.com,Proxy

# Google 服务
DOMAIN-SUFFIX,google.com,Proxy
DOMAIN-SUFFIX,youtube.com,Proxy

# 中国大陆直连
GEOIP,CN,DIRECT
FINAL,Proxy
```

### 自定义规则

1. 点击「配置」→ 「规则」
2. 点击「编辑」
3. 添加或修改规则

---

## 设置

### 开机启动

设置 → 通用 → 开机自启 → 开启

### Wi-Fi 代理

Surge 可以接管特定 Wi-Fi 的代理：

1. 设置 → Wi-Fi 代理
2. 选择要代理的 Wi-Fi
3. 设置代理方式（全局/规则）

### TUN 模式

开启后接管所有应用流量：

1. 设置 → TUN 模式 → 开启
2. 推荐开启「增强模式」

### DNS 设置

推荐使用安全 DNS：

```
https://1.1.1.1/dns-query
https://dns.google/dns-query
```

---

## 进阶功能

### 节点延迟测试

长按节点名称即可测试延迟。

### 节点分组

Surge 支持分组管理：

```ini
[Proxy Group]
Proxy = select, 香港, 日本, 美国, 手动
Netflix = select, 香港, 日本
```

### 脚本功能

Surge 支持 JavaScript 脚本，可实现高级分流逻辑。

---

## 常见问题

**Q: 为什么 Surge iOS 需要付费？**
A: Surge 是专业工具，¥328 一次性买断。功能强大，稳定可靠，是 iOS 上最好的代理客户端之一。

**Q: iOS 版 Surge 和 Mac 版有何区别？**
A: 两者配置互通，Mac 版功能更全（支持更多协议），iOS 版针对移动场景优化。

**Q: 如何更新订阅？**
A: 点击「配置」→ 选择订阅 → 点击「更新」。

**Q: Surge 支持哪些协议？**
A: VLESS、Trojan、VMess、Shadowsocks、WireGuard 等全部支持。

---

## 相关阅读

- [Clash Verge（Windows/Mac）](./clash-verge.md)
- [Clash for Android](./clash-for-android.md)
- [机场推荐](../airport-reviews/README.md)
