# 2026 DNS防污染完全指南：DoH/DoT配置解决网页打不开与解析劫持

> 本文最初发布于 [huanghaiwan.com](https://huanghaiwan.com/posts/dns-pollution-guide-2026/)

> 节点连上了、线路也通，但网页就是打不开，或者打开全是广告、跳到莫名其妙的页面？十有八九是 DNS 解析环节出了问题。这篇指南把 DNS 污染的原理、判断方法和三种配置方案讲清楚。

## 太长不看版

| 问题 | 症状 | 最快解法 |
|:----|:----|:--------|
| 网页打不开但节点正常 | 浏览器转圈后报错 | 客户端开启 DoH（加密 DNS） |
| 打开的是广告/错误页面 | 域名被解析到错误 IP | 切换公共 DoH 服务商 |
| 国内站快、国外站慢 | 解析走运营商 DNS 被干扰 | 配置国内外分流 DNS |
| 全设备都异常 | 路由器/系统 DNS 被改 | 路由器级 DNS 全局覆盖 |

**一句话结论：** 给客户端或系统配上加密 DNS（DoH/DoT），把域名解析从明文裸奔变成加密通道，污染问题就解决了大半。

## 一、DNS 污染是什么

DNS 是互联网的"电话簿"——输入域名，DNS 服务器翻译成服务器 IP 地址。整个过程默认**明文传输**，中间设备可以看到你查了什么域名，也能**篡改返回结果**。

| 污染类型 | 表现 |
|:--------|:----|
| 返回错误 IP | 打开的是广告页/反诈页/空白页 |
| 解析超时 | 域名一直转圈，nslookup 无响应 |
| 返回本地地址 | 指向 127.0.0.1 等异常 IP |
| 部分污染 | 国内域名正常、国外域名异常 |

**为什么连了跨境网络还会被污染？** 很多客户端默认 DNS 仍走本地运营商线路，或 fake-ip 模式下的 fallback 解析没配置好。节点修好了"路"，但"查地址"这一步还在被干扰。

## 二、判断是不是 DNS 问题（3 个命令）

```bash
# 1. 用默认 DNS 解析国外域名
nslookup www.google.com
# 2. 换公共 DNS 对比结果
nslookup www.google.com 1.1.1.1
# 3. 解析国内域名做对照
nslookup www.baidu.com
```

**判读：** 默认 DNS 解析超时/返回 127.0.0.1，而 1.1.1.1 正常 → 确认被污染。两个 DNS 都解析到同一 IP 但打不开 → 查节点/线路。

## 三、方案一：客户端配置加密 DNS（推荐首选）

### Clash Verge Rev / Clash Meta

```yaml
dns:
  enable: true
  listen: 0.0.0.0:1053
  ipv6: false
  enhanced-mode: fake-ip
  fake-ip-range: 198.18.0.1/16
  nameserver:
    - 223.5.5.5
    - 119.29.29.29
    - https://dns.alidns.com/dns-query
  fallback:
    - https://cloudflare-dns.com/dns-query
    - https://dns.google/dns-query
  fallback-filter:
    geoip: true
    geoip-code: CN
```

要点：国内域名走 `nameserver`（阿里/DNSPod），国外域名经 `fallback-filter` 分流到 Cloudflare/Google DoH——**国内外分流**兼顾速度与抗污染。

### Stash（iOS/macOS）

「设置 → DNS」打开 DoH：主 DNS 填 `https://dns.alidns.com/dns-query`（国内快），备用填 `https://cloudflare-dns.com/dns-query`（抗污染），打开 Fallback 分流国外域名。

### Shadowrocket（iOS）

「设置 → DNS」手动添加：国内 `223.5.5.5` 或 `https://dns.alidns.com/dns-query`，国外 `https://cloudflare-dns.com/dns-query`，打开「使用 DNS 代理」。

### sing-box

```json
{
  "dns": {
    "servers": [
      { "tag": "local", "address": "223.5.5.5" },
      { "tag": "remote", "address": "https://cloudflare-dns.com/dns-query" }
    ],
    "rules": [
      { "rule_set": ["geosite-cn"], "server": "local" },
      { "rule_set": ["geosite-geolocation-!cn"], "server": "remote" }
    ]
  }
}
```

## 四、方案二：系统级配置 DoH/DoT

| 平台 | 配置路径 |
|:----|:--------|
| Windows 11 | 设置 → 网络 → 属性 → DNS 编辑 → 手动 1.1.1.1/8.8.8.8，加密选「仅加密（DoH）」 |
| macOS | 系统设置 → 网络 → 详细信息 → DNS 添加 1.1.1.1/8.8.8.8（DoH 需客户端/描述文件） |
| iOS | 无线局域网 → Wi-Fi ⓘ → 配置 DNS → 手动 1.1.1.1/8.8.8.8 |
| Android | 设置 → 网络 → 私人 DNS → `1dot1dot1dot1.cloudflare-dns.com`（原生 DoT） |
| Firefox | 设置 → 隐私与安全 → 启用基于 HTTPS 的 DNS |

Android 私人 DNS 原生走 DoT，是所有平台里系统级配置最简单的。

## 五、方案三：路由器/旁路由全局覆盖

1. **OpenWrt**：安装 `https-dns-proxy` 插件，上游填 DoH 端点
2. **AdGuard Home**：软路由/旁路由部署，上游国内外分流（国内 223.5.5.5、国外 DoH），自带缓存+广告过滤
3. **旁路由**：树莓派/旧盒子跑 AdGuard Home，DHCP 下发 DNS 指向它

普通用户按方案一（客户端）已能解决 90% 问题。

## 六、公共 DNS 服务商对比

| 服务商 | 普通 DNS | DoH 端点 | 特点 |
|:------|:--------|:--------|:-----|
| 阿里 AliDNS | 223.5.5.5 | `https://dns.alidns.com/dns-query` | 国内快、适合国内分流 |
| 腾讯 DNSPod | 119.29.29.29 | `https://doh.pub/dns-query` | 国内快、稳定 |
| Cloudflare | 1.1.1.1 | `https://cloudflare-dns.com/dns-query` | 国际快、隐私强、抗污染好 |
| Google | 8.8.8.8 | `https://dns.google/dns-query` | 国际通用、解析记录全 |
| Quad9 | 9.9.9.9 | `https://dns.quad9.net/dns-query` | 自带威胁情报过滤 |

**选型：** 国内域名用阿里/DNSPod，国外域名用 Cloudflare/Google DoH。不要全走国际 DNS——国内域名绕一圈反而慢。

## FAQ

**Q1：换了 DoH 还是打不开？** 先确认 DoH 生效（nslookup 看解析源），再查节点本身。DNS 只是链路一环，节点挂了解析再对也没用。

**Q2：fake-ip 要开吗？** 推荐开启——给域名分配虚拟 IP，真实解析交给客户端内部处理，加速首连、减少 DNS 泄漏。配合 fallback 分流效果最好。

**Q3：DoH 和 DoT 区别？** DoH 走 443 端口与网页流量混在一起难识别；DoT 走 853 端口专用通道。日常用 DoH 即可。

**Q4：全用国际 DNS 行吗？** 不建议。国内域名走国际 DNS 会绕路变慢。正确姿势是国内/国外分流。

**Q5：nslookup 返回 127.0.0.1？** 典型污染特征，换公共 DNS 或开 DoH 后恢复。客户端 fake-ip 下显示 198.18.x.x 是正常的。

**Q6：手机流量也会被污染？** 会。手机端优先客户端方案（Clash/Stash/Shadowrocket 的 DoH），Wi-Fi 和流量都覆盖。

## 总结

DNS 污染是"节点正常但网页打不开"的头号隐形原因。三步解法：**① 客户端配 DoH**（Clash/Stash/Shadowrocket，覆盖 90% 场景）→ **② 系统级配置**（Windows DoH、Android 私人 DNS）→ **③ 路由器全局覆盖**（AdGuard Home，全家多设备）。

如果你的网络服务商解析慢、晚高峰不稳定，可以对比下面的方案选一个主力：

| 方案 | 适合谁 | 特点 | 入口 |
|:----|:------|:----|:----|
| 自由猫 | 主力长期用 | IEPL 专线 + MPTCP 多路复用，晚高峰稳 | [👉 访问自由猫官网](https://api.huanghaiwan.com/go/自由猫) |
| 万达云 | 入门/预算敏感 | IEPL 专线 + 中转，性价比高 | [👉 访问万达云官网](https://api.huanghaiwan.com/go/万达云) |
| 悠兔 | 年付党 | 自有机房 IEPL 专线，年付折合低价 | [👉 访问悠兔官网](https://api.huanghaiwan.com/go/悠兔) |
| SKYLUMO | 轻量/学生 | 全球 80+ 地区覆盖，¥6.99 入门 | [👉 访问SKYLUMO官网](https://api.huanghaiwan.com/go/SKYLUMO) |

> 相关教程：[Clash 规则配置指南](https://huanghaiwan.com/posts/clash-rule-config-guide-2026/) ｜ [客户端安装配置全攻略](https://huanghaiwan.com/posts/client-setup-guide-2026/) ｜ [线路类型科普](https://huanghaiwan.com/posts/network-line-type-guide-2026/)

*最后更新：2026-08-31*
