> 本文最初发布于 [huanghaiwan.com](https://huanghaiwan.com/posts/node-conversion-guide-2026/)

# 节点转换指南：vmess、ss 链接怎么变成 Clash 配置（2026）

**2026 年 11 月。** 最常见的提问是这一句：手里一条 `vmess://eyJ2IjoiMiIsInBzIjoi...`，怎么塞进 Clash？我的回答是塞不进去：Clash 和 Mihomo 只读 YAML，sing-box 内核只读 JSON，而服务商后台发给你的通常是一条 base64 糊起来的分享链接。中间这层翻译活，就叫**节点转换**。

第一次碰这东西的人常犯的错，是把一条 ss 链接直接粘进 Clash 配置文件，客户端启动就报错退出——不是节点坏了，就是格式不对。

边界先说清：订阅管理（多条订阅怎么合并、多设备同步）另有一篇专文，这里只管**格式层**——一长串字符长什么样、怎么解码、怎么变成客户端认的 YAML 或 JSON。

## 太长不看版

| 你手上的东西 | 想用在哪 | 该怎么办 |
|:--|:--|:--|
| 一条 `vmess://` / `ss://` / `trojan://` 链接 | Shadowrocket、v2rayN、NekoBox | 直接粘贴导入，多数能认 |
| 同一条链接 | Clash Verge、Mihomo Party | 手写进 YAML 的 `proxies:` 段，或用转换器出配置 |
| 订阅链接，客户端报格式错误 | 换一个客户端 | 用 subconverter 换 `target` 重新生成 |
| 两三家服务想合成一条 | 任意客户端 | subconverter 的 `url` 用竖线隔开多个源 |

## 一、先把 5 种链接分清楚

很多人以为「节点」和「订阅」是一回事，其实中间隔着一层编码。

| 类型 | 典型长相 | 谁能直接吃 |
|:--|:--|:--|
| 单节点分享链接 | `vmess://` 后接一长串 base64；`trojan://密码@域名:443` | Shadowrocket、v2rayN、sing-box 图形客户端 |
| base64 订阅 | 一坨无结构字母数字，解码后一行一条链接 | v2rayN、Shadowrocket |
| Clash YAML 订阅 | 纯文本，开头是 `proxies:` | Clash Verge、Mihomo、Stash |
| sing-box JSON | `{"outbounds":[...]}` | SFA / SFI |
| 二维码 | 后台那张方图 | 手机扫码，本质还是上面某一种 |

判断手上这条是什么，一条命令够用：

```bash
curl -sL "你的订阅链接" | head -c 200
```

开头是 `proxies:` 就是 YAML，是 `{"` 就是 JSON，是 `A-Za-z0-9+/=` 就是 base64，是 `<html` 说明你要么复制了网页地址，要么请求被挡了返回了错误页——最后这种我见得最多。

## 二、一条 vmess 链接里装了什么

vmess 是唯一把内容 base64 的协议，`vmess://` 后面解码出来是 JSON：

```bash
python3 -c "
import base64, json
s = 'eyJ2IjoiMiIsInBzIjoi...'
s += '=' * (-len(s) % 4)
print(json.dumps(json.loads(base64.b64decode(s)), ensure_ascii=False, indent=2))
"
```

关键字段：`add` 服务器地址、`port` 端口（常见 443）、`id` 就是 UUID 等于账号密码、`aid` 旧版 alterId 现在基本是 0、`net` 传输方式（ws 必须配 `path`）、`tls` 是否走 TLS、`ps` 备注名。

其余四种都是标准 URL，不 base64：`ss://` 用 SIP002 形态（`ss://base64(加密方式:密码)@域名:端口`，插件在 `?plugin=`）；`trojan://` 密码在用户名位；`vless://` 的 UUID 是用户名，靠 `security=reality`、`pbk`、`sid`、`fp`、`flow` 这一组参数；`hysteria2://`（也写 `hy2://`）密码同样在用户名位，常见 `insecure=1`、`obfs=salamander`。

看清格式的意义是：出问题时你能定位到具体字段。我帮人排查 10 次，里面有 8 次是参数抄漏了一个。

## 三、路线一：客户端自己导入

一条链接、一台设备，真不需要转换器。Shadowrocket 最宽容（单链接、二维码、base64 订阅、甚至 Clash YAML 都吃）；v2rayN 认 share link 和 base64 订阅；Clash Verge Rev / Mihomo Party 只吃 YAML，单条链接要靠剪贴板导入或新建本地配置。

sing-box 图形客户端能导入订阅，但内核只吃 JSON，配置错一个字段就起不来，改完先校验：

```bash
sing-box check -c config.json
```

## 四、路线二：subconverter（多源合并与格式互转）

出现下面任一需求就该上转换器：两家以上服务想合并、手上一堆零散链接要统一入口、一份订阅要喂三种客户端、想批量改名或按地区筛。

```bash
docker run -d --name subconverter --restart=always -p 25500:25500 tindy2013/subconverter:latest
curl -s http://127.0.0.1:25500/version
```

接口是标准 GET：

```
http://127.0.0.1:25500/sub?target=clash&url=<URL 编码后的订阅>&emoji=true
```

常用参数：`target` 决定输出格式（`clash`、`singbox`、`v2ray`、`surge`、`quanx`、`loon`、`mixed`）；`url` 是源订阅，**多个源用竖线隔开**，编码后是 `%7C`；`config` 指定外部规则模板，不传就用内置模板、策略组基本是空的；`emoji` 给节点加国旗；`rename`、`include_remarks`、`exclude_remarks` 负责批量改名和按关键字筛选。

两个必须提醒的点：

1. `singbox` 这个 target 只有较新版本才有，老镜像会报不支持。先 `curl /version` 看版本，再决定升级还是先转 `v2ray` 让客户端自己吃。
2. **填进手机客户端时不要写 `127.0.0.1`**——手机上的 `127.0.0.1` 指手机自己。要填电脑内网地址，比如 `http://192.168.1.10:25500/sub?...`，并放行 25500 端口。这个坑我踩过，排查了半小时才发现是地址写错。

## 五、路线三：在线转换站

粘链接、选格式、3 秒出结果，不用装东西。代价是：**订阅链接本身就是账号凭证**，里面带着 UUID 或密码，谁拿到谁就能用你的流量；而且转换结果可以被投毒，返回的未必是你原来那些节点。

我的做法：临时应急用完立刻去后台重置订阅链接；长期用就在自己机器或 VPS 上跑一份。

## 六、最容易翻车的 5 个地方

| 症状 | 真实原因 | 怎么处理 |
|:--|:--|:--|
| 导入后节点数为 0 | 返回的是 HTML，或 base64 缺 `=` 填充 | `curl -sL <链接> \| head -c 200` 看返回体 |
| 节点能看到，一点就超时 | ss 加密方式不被支持，或旧 vmess 的 `aid` 不为 0 | 换节点或换支持插件的客户端 |
| 转换后策略组和规则全空 | 没传 `config`，用了默认模板 | 指定自己的规则模板 |
| 手机填本地转换链接失败 | 写了 `127.0.0.1` | 改电脑内网 IP，放行 25500 |
| sing-box 报 unknown field | 配置字段与内核版本对不上 | 用对应版本示例，改完 `sing-box check` |

转换只改格式，**不改线路**。所以「转完还是慢」的时候别怀疑转换器，直接查节点本身。

## 七、什么时候我不用转换器

一家服务一台设备：官方订阅直接填；服务商直接给 YAML：Clash 加订阅就行；只在 iPhone 上用：扫码。真正需要转换的只有三种：多机场合并、一份订阅喂多个客户端、需要统一的规则模板。为了「看起来专业」去部署一套转换服务，最后多半是自己在维护一个没人用的中间层。

## FAQ

**转换会影响速度或流量统计吗？** 不影响。转换只换写法，请求最后走服务商线路，流量也在那边计。唯一变化是转换出的订阅要定期更新。

**转换后的订阅多久刷新一次？** 客户端填的是转换链接，每次拉取时转换器都会重新取源订阅。间隔别设太短，10 分钟一刷既没必要也可能被源站限流，12 小时（1 天刷 2 次）比较稳。

**同一条链接手机能用、电脑不行？** 大概率是客户端协议支持差异，新协议在激进更新的客户端上先落地，老版本电脑客户端不认。

## 顺手推荐几家在用的服务

| 服务 | 起步价 | 流量 | 设备 | 线路 |
|:--|:--|:--|:--|:--|
| [自由猫](https://api.huanghaiwan.com/go/自由猫) | ¥8/月 | 30GB | 1 台 | IEPL + MPTCP，110+ 节点 |
| [仙路湾](https://api.huanghaiwan.com/go/仙路湾) | ¥10/月 | 50GB | 3 台 | IEPL/IPLC + 港台原生 IP，优惠码 `xlw9` 九折 |
| [瑶瑶领先](https://api.huanghaiwan.com/go/瑶瑶领先) | ¥9.9/月 | 384GB | 3 台 | SS + BGP 中转，大流量低价档 |
| [SS-ID](https://api.huanghaiwan.com/go/SS-ID) | ¥20/月 | 100GB | 5 台 | IEPL 专线，流媒体解锁 |

自由猫那档 ¥8 只给 1 台设备，要手机电脑一起用就从 ¥12/100GB/3 台 那档起。仙路湾适合需要原生 IP 的场景，20 个地区。瑶瑶领先胜在流量给得狠，¥19.8 能到 768GB，但是 SS 加 BGP 中转、不是专线，晚高峰体感有差别。

原文还有订阅管理、节点检测两条延伸路径，需要的话看博客版：<https://huanghaiwan.com/posts/node-conversion-guide-2026/>
