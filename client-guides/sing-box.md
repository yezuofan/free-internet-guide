# Sing-Box 使用教程

> Sing-Box 是目前支持协议最全面的代理客户端，支持 VLESS、Trojan、VMess、Shadowsocks、WireGuard 等所有主流协议。

## 下载安装

| 平台 | 下载地址 |
|------|---------|
| Windows | https://github.com/SagerNet/sing-box/releases |
| macOS | https://github.com/SagerNet/sing-box/releases |
| Android | https://github.com/SagerNet/sing-box/releases |
| iOS | App Store 搜索「SingBox」或使用 TestFlight |

**注意**：iOS 版需要非中国区 Apple ID。

---

## 基本配置

### 方式一：订阅链接导入（推荐）

1. 打开 SingBox
2. 点击「配置」→ 「订阅」
3. 点击「+」添加订阅
4. 粘贴机场订阅链接
5. 设置备注名称
6. 点击「更新」
7. 选择节点，点击启动

### 方式二：手动导入

1. 点击「配置」→ 「配置文件」
2. 点击「+」
3. 选择「JSON」或「URI」
4. 粘贴节点信息
5. 保存并选择该配置

---

## 协议支持

| 协议 | 支持情况 |
|------|---------|
| VLESS + Reality | ✅ 完全支持 |
| VLESS + XTLS | ✅ 完全支持 |
| Trojan | ✅ 完全支持 |
| VMess | ✅ 完全支持 |
| Shadowsocks | ✅ 完全支持 |
| WireGuard | ✅ 完全支持 |
| Hysteria2 | ✅ 完全支持 |

---

## 分流模式

### 规则分流（推荐）

1. 点击「路由」→ 「规则」
2. 选择「domain»rule」或「rule»domain」模式
3. 自定义规则：
   - `domain:netflix.com` → Netflix 节点
   - `domain:google.com` → 代理节点
   - `geoip:cn` → 直连

### 全局/直连

- **全局**：所有流量走代理
- **直连**：所有流量直连

---

## 设置

### 开机启动

设置 → 常规 → 开机自启

### TUN 模式

开启 TUN 模式可以接管所有系统流量：

1. 设置 → TUN → 开启 TUN
2. 推荐开启「自动路由」
3. iOS 需要开启「增强模式」

### DNS 设置

推荐使用安全 DNS：

```
https://1.1.1.1/dns-query
https://8.8.8.8/dns-query
```

---

## 常见问题

**Q: 为什么显示已连接但无法上网？**
A: 尝试切换节点，可能当前节点被封锁。或检查 TUN 模式是否正确开启。

**Q: 如何导入多个订阅？**
A: 在「订阅」页面点击「+」多次添加即可。支持同时管理多个机场配置。

**Q: Sing-Box 和 Clash 有何区别？**
A: Sing-Box 支持更多协议（如 WireGuard、Hysteria2），配置更灵活，但界面相对复杂。

---

## 相关阅读

- [Clash Verge（Windows/Mac）](./clash-verge.md)
- [Clash for Android](./clash-for-android.md)
- [机场推荐](../airport-reviews/README.md)
