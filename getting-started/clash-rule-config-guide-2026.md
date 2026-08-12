---
title: "Clash 规则配置完全指南：分流策略、代理组与实战优化（2026版）"
date: 2026-07-31
tags: ["教程", "新手入门", "Clash"]
---

> 机场买好了、客户端装上了、节点也能连——但总觉得哪里不对？刷抖音走的也是代理、访问 GitHub 走的却是直连、流媒体打开显示"地区限制"？这些问题八成出在**规则配置**上。

这篇文章从零开始讲 Clash 规则体系，覆盖 Clash Meta 内核、Clash Verge、Stash（iOS）等主流客户端。

## 一、为什么需要规则配置？

规则系统的核心价值：让 Clash 自动判断每个请求应该走代理还是直连，不需要你手动干预。

| 场景 | 正确行为 | 错误行为 |
|:----|:--------|:--------|
| 访问 baidu.com | 直连（国内网站） | 走代理（慢+浪费流量） |
| 访问 youtube.com | 走代理 | 直连（打不开） |
| 访问 Netflix | 走流媒体专用节点 | 走普通节点（被检测为代理） |

## 二、Clash 规则引擎工作原理

```
用户请求 → 匹配规则列表（从上到下） → 第一个匹配的规则决定走哪个策略组 → 策略组决定走哪个节点
```

**关键原则：规则从上到下逐条匹配，匹配到第一条就停止。** 精确的规则放前面，兜底的规则放最后。

## 三、规则类型详解

| 规则类型 | 示例 | 说明 |
|:--------|:----|:----|
| DOMAIN | `DOMAIN,www.google.com,PROXY` | 精确匹配单个域名 |
| DOMAIN-SUFFIX | `DOMAIN-SUFFIX,google.com,PROXY` | 匹配域名及其所有子域名 |
| DOMAIN-KEYWORD | `DOMAIN-KEYWORD,google,PROXY` | 域名包含关键词即匹配 |
| GEOIP | `GEOIP,CN,DIRECT` | 国内 IP 直连 |
| IP-CIDR | `IP-CIDR,10.0.0.0/8,DIRECT` | IP 段规则 |
| DST-PORT | `DST-PORT,853,PROXY` | 目标端口规则 |
| PROCESS-NAME | `PROCESS-NAME,chrome.exe,PROXY` | 进程名规则（Clash Meta） |
| RULE-SET | `RULE-SET,url/reject.yaml,REJECT` | 规则集引用 |

## 四、代理组策略

| 类型 | 特点 | 适用场景 |
|:----|:----|:---------|
| **select** | 手动选一个节点 | 想指定用某地区节点 |
| **url-test** | 自动测速选最低延迟 | 日常浏览最常用 |
| **fallback** | 按优先级容灾切换 | 网络波动大的环境 |
| **load-balance** | 轮询负载均衡 | 大流量下载场景 |

## 五、实战配置模板

一份完整配置的核心框架：

```yaml
# proxy-providers（节点来源）
proxy-providers:
  MyProvider:
    type: http
    path: ./providers/my_nodes.yaml
    url: "你的订阅链接"
    interval: 86400
    health-check:
      enable: true
      url: https://www.gstatic.com/generate_204
      interval: 300

# proxy-groups（策略组）
proxy-groups:
  - name: "🎬 流媒体"
    type: url-test
    use:
      - MyProvider
    filter: "流媒体|Netflix|解锁"
    url: https://www.gstatic.com/generate_204
    interval: 300

  - name: "🎮 游戏"
    type: fallback
    use:
      - MyProvider
    filter: "游戏|游戏加速|LowPing"
    url: https://www.gstatic.com/generate_204
    interval: 300

  - name: "🚀 代理"
    type: select
    proxies:
      - "🎬 流媒体"
      - "🎮 游戏"
      - "🚀 自动选择"
      - "DIRECT"

  - name: "🚀 自动选择"
    type: url-test
    use:
      - MyProvider
    url: https://www.gstatic.com/generate_204
    interval: 300

# rules（规则链）
rules:
  # 必须代理的
  - DOMAIN-SUFFIX,google.com,🚀 代理
  - DOMAIN-SUFFIX,youtube.com,🚀 代理
  - DOMAIN-SUFFIX,github.com,🚀 代理
  # 流媒体
  - DOMAIN-SUFFIX,netflix.com,🎬 流媒体
  - DOMAIN-SUFFIX,disney.com,🎬 流媒体
  # 直连—国内服务
  - DOMAIN-SUFFIX,baidu.com,DIRECT
  - DOMAIN-SUFFIX,qq.com,DIRECT
  - DOMAIN-SUFFIX,bilibili.com,DIRECT
  # 游戏
  - DOMAIN-SUFFIX,steamcontent.com,🎮 游戏
  # GeoIP
  - GEOIP,CN,DIRECT
  # 兜底
  - MATCH,🚀 代理
```

## 六、常见问题与避坑

**1. 规则顺序搞反** — MATCH 或 GEOIP,CN 放最前面会导致所有请求都匹配了兜底规则

**2. 流媒体节点必须单独分组** — 自动切换会导致 Netflix 检测到 IP 变化而封禁

**3. 国内网站走代理导致风控** — 银行 App、12306、企业微信必须直连

**4. 社区规则集** — 推荐 blackmatrix7/ios_rule_script 或 Loyalsoldier/clash-rules，每周更新

**5. 测速 URL 备选** — 如果 gstatic.com 被封锁，可用 captive.apple.com/hotspot-detect.html

## 七、总结

Clash 规则配置记住三个要点：
1. **规则自上而下匹配** — 精确放前面，兜底放最后
2. **策略组决定体验** — 日常用 url-test 自动切换，流媒体和游戏用专用节点
3. **直连规则配好** — 国内服务走直连，既快又安全

### 推荐网络加速服务

| 服务商 | 特点 | 月费 |
|:-----|:----|:----:|
| [自由猫](https://api.huanghaiwan.com/go/自由猫) | IEPL专线+MPTCP多路复用，100+节点 | ¥32.8/月起 |
| [万达云](https://api.huanghaiwan.com/go/万达云) | IEPL专线，入门友好 | ¥19.9/月起 |
| [肥猫云](https://api.huanghaiwan.com/go/肥猫云) | 专线线路，性价比均衡 | ¥20/月起 |
| [Cyberguard](https://api.huanghaiwan.com/go/Cyberguard) | IEPL专线，流媒体解锁 | ¥32.8/月起 |
