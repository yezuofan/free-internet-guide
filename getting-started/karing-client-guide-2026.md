> 本文最初发布于 [huanghaiwan.com](https://huanghaiwan.com/posts/karing-client-guide-2026/)

# Karing 使用教程：sing-box 内核的跨平台客户端怎么用

**2026 年 11 月。** Karing 这两年悄悄长起来的：GitHub 上 `KaringX/karing` 已经 15,941 个 star，最新正式版 1.2.25（2026 年 9 月 10 日）。它不是 Clash Verge 的换皮，Flutter 界面底下挂的是自己改造过的 sing-box 内核——**内核不同，能吃的配置就不同**。

## 支持什么配置

Clash 配置完整支持，clash.meta 部分支持，另外吃 V2ray / V2fly、sing-box、Shadowsocks 和普通订阅链接、GitHub 订阅。市面上绝大多数机场给的订阅链接都能直接导入。

## 系统要求

Windows 10+（仅 64 位）、Android 8+、iOS 15+、macOS 12+、tvOS 17+、Linux 64 位且 glibc ≥ 2.38。最后这条是坑：Ubuntu 22.04 及更早、Debian 12 之前的系统直接 `dpkg -i` 会报依赖错误，别硬改系统库。

## 下载只认这几个入口

- iOS / tvOS：App Store 搜 `karing vpn`（id6472431552），或 TestFlight
- Android：karing.app/download、GitHub Releases、APKPure、Amazon AppStore
- Windows / macOS / Linux：karing.app/download、GitHub Releases，Mac 可 `brew install karing`

官方 README 专门声明过：Karing 没有在任何视频平台开过账号。所以短视频教程里挂的下载链接，一个都别点；搜出来那些「绿色版/便携版」也别装——客户端攥着你全部订阅和流量，来源不明的包风险不对称。

## 订阅怎么导

1. **订阅链接**（推荐）：面板里那串 `https://.../api/v1/client/subscribe?token=xxx`，进订阅页粘贴保存，默认 7 天自动更新一次。
2. **二维码**：手机端扫码比手打链接靠谱。
3. **配置文件**：现成的 Clash yaml 或 GitHub 订阅可直接喂 URL 或本地文件。clash.meta 的部分字段它认不全，导完数一眼节点数。

## 路由三模式

**规则模式**（日常用，内置 geo-IP / geo-site / ACL 规则集，默认规则组开箱可用）、**全局模式**（只在排查节点时短开，长期挂着等于自己加延迟）、**直连模式**（怀疑是节点还是网站的问题时，切过去两秒出结论）。它还支持一套路由规则同时套在多个订阅上，主力 + 备用的组合不用来回切配置。

## 多设备同步

四条路：iCloud（iOS / macOS）、局域网同步、WebDAV、ZIP 导入导出。前三条自动，代价是信任那个中间人；ZIP 最土但最不会出错。

## 五个会卡住的地方

订阅导入后节点为空（多半是把单节点链接当订阅塞进去了）；浏览器能走但某个软件不走（开 TUN，装虚拟网卡驱动会弹权限确认）；iOS 切后台被系统回收；Linux 的 glibc 版本不够；tvOS 16 的老盒子装不上。

## 最容易被忽略的一条：机场让不让用第三方客户端

有些机场的套餐说明里白纸黑字写着不支持第三方客户端——比如自由猫，每一档都写「不支持第三方客户端，介意勿买」，买了就只能用它的官方客户端，Clash、sing-box、Karing 统统不行。下单前翻一遍套餐说明，Ctrl+F 搜「客户端」三个字，能省掉一次白买。

## 节点从哪来（2026 年 11 月现行价）

| 服务 | 起价 | 客户端情况 | 适合 |
|:-----|:-----|:-----------|:-----|
| [仙路湾](https://api.huanghaiwan.com/go/仙路湾) | ¥10 / 50GB / 3 台 | 官方列 14 款客户端，Clash、sing-box 一键导入 | 原生 IP 家宽、港台出口（码 `xlw9` 九折） |
| [SS-ID](https://api.huanghaiwan.com/go/SS-ID) | ¥20 / 100GB / 5 台 | Clash、小火箭、Surge 直接导 | 办公商务，IEPL 专线 |
| [瑶瑶领先](https://api.huanghaiwan.com/go/瑶瑶领先) | ¥9.9 / 384GB / 3 台 | SS 协议，通用客户端都能吃 | 纯跑量，¥0.026/GB |
| [新华云](https://api.huanghaiwan.com/go/新华云) | ¥5.19 起（VIP1 20GB / 1 台） | 官方写「全平台通用」，以面板为准 | 预算紧、只国内访问；VIP1 不给 AI 与流媒体 |
| [自由猫](https://api.huanghaiwan.com/go/自由猫) | ¥8 / 30GB / 1 台 | 写明不支持第三方客户端 | 不用 Karing 的人；要用 Karing 就跳过 |

## 顺序别搞反

**先确认机场允许你用通用客户端，再挑客户端。** 先把客户端折腾明白、买完才发现订阅导不进去，是最常见的一条冤枉路。真想少踩坑，先花 10 块钱买一份最小月付试一次，比看十篇教程都准。

---

*本文包含推广链接，均为核对过的真实推荐。*
