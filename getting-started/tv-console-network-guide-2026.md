> 本文最初发布于 [huanghaiwan.com](https://huanghaiwan.com/posts/tv-console-network-guide-2026/)

电视和游戏机配置网络加速跟手机完全不同——大多数电视/游戏机不能直接装代理客户端，需要靠路由器、旁路由或特定设备客户端来解决。本文覆盖6类设备的配置方法。

## 快速参考表

| 设备 | 推荐方案 | 难度 | 成本 |
|:----|:--------|:----:|:----:|
| Apple TV | Surge/Stash直接装 | ⭐ | ¥50-328 |
| Android TV/盒子 | Clash Meta for Android装APK | ⭐ | ¥0 |
| PS5/Xbox | 路由器/旁路由网关 | ⭐⭐⭐ | ¥0-200 |
| Switch | WiFi改代理参数 | ⭐ | ¥0 |
| 智能电视 | 旁路由或外接盒子 | ⭐⭐⭐ | ¥0-1000 |

## 各设备核心要点

**Apple TV（最推荐的电视方案）：** tvOS 17+ 支持 Surge（¥328一次性）和 Stash（¥50/年订阅）。Surge稳定但无规则组，Stash支持完整Clash规则分流。不想花钱可选旁路由方案。

**Android TV/盒子：** 最灵活的电视设备。装 Clash Meta for Android 或 v2rayNG 的APK即可。开启自动启动和全局代理模式，支持手机远程web管理。

**PS5/PS4：** 不能装代理客户端，必须靠路由器/旁路由。推荐旁路由网关方案——把PS5的网关指向旁路由IP。改DNS（OpenDNS/Google DNS）是最低成本半失效方案。

**Xbox Series X/S：** 同PS5的逻辑。额外技巧：可以用常开Windows电脑当代理网关（Clash Verge开「允许局域网连接」）。

**Switch：** 最简单——WiFi设置里直接填HTTP代理信息（IP:端口）即可。代理后eShop地区随节点切换。下载大游戏建议关代理直连。

**智能电视（Samsung/LG等）：** 不支持装客户端，不能改WiFi代理。唯一彻底方案是路由器级别代理。买个Apple TV/小米盒子外接是更好的选择。

## 设备联机带宽参考

| 场景 | 所需带宽 |
|:----|:--------:|
| Netflix 4K HDR | ~25Mbps |
| Disney+ 4K | ~20Mbps |
| YouTube 4K 60fps | ~40Mbps |
| 游戏联机(PS5/Xbox) | 5-10Mbps |

大部分机场香港/日本节点可跑100Mbps+，看4K没问题。

## 常见问题

**一台机场订阅能给电视和游戏机同时用吗？** 可以的。路由器/旁路由配置后，全屋设备共享流量。手机4G用自己客户端独立走。

**流媒体显示「代理检测」怎么解决？** 选原生IP节点（标注「流媒体解锁」的机场），或在规则里把流媒体域名走直连。这个和配置方式无关，取决于机场线路质量。

*原文发布于 [huanghaiwan.com](https://huanghaiwan.com/posts/tv-console-network-guide-2026/)，包含完整FAQ和详细分步教程。*
