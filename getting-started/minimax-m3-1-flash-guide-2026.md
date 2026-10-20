> 本文最初发布于 [huanghaiwan.com](https://huanghaiwan.com/ai/minimax-m3-1-flash-guide-2026/)

# MiniMax M3.1 Flash 上手：1 块钱一百万上下文，坑在 thinking 关不掉

**2026 年 10 月更新。** 便宜模型我从来不缺，缺的是能安心塞进 agent 循环里的便宜模型。10 月 19 日 MiniMax M3.1 Flash 上线，我第二天早上第一件事就是把 Claude Code 的默认模型换过去，改完配置第一条请求直接吃了个 400：`model "MiniMax-M3.1-Flash" requires adaptive thinking; thinking.type="disabled" (reasoning.effort=none) is not allowed (2013)`。不是网络问题也不是 key 填错，是我那个「能省则省」的老习惯——顺手想把思考关掉省 token——正好撞在它唯一不让省的地方。

## 太长不看版

| 问题 | 短答 |
|:---|:---|
| 值不值得换 | 值。标准价是 M3 的一半，1M 上下文不加价 |
| 价格 | 每百万 token：输入 **¥1**、输出 **¥4**、缓存读取 **¥0.1**（海外站 $0.15 / $0.60 / $0.015） |
| 接 Claude Code | 能。改 `ANTHROPIC_BASE_URL`，但先 `unset ANTHROPIC_AUTH_TOKEN` 和 `ANTHROPIC_BASE_URL`，环境变量优先级高于 settings.json |
| 自己写代码调 | OpenAI 端点 `api.minimax.io/v1` 用 `reasoning_effort`；Anthropic 端点 `/anthropic` 用 `output_config.effort` |
| 最该记住 | **thinking 关不掉**，传 `disabled` 直接 400 |
| 第二该记住 | `max_tokens` 把思考 token 也算进去，设小了返回空正文 |
| 谁别用 | 要低延迟聊天机器人、要 `service_tier` 优先通道、要随时关思考的场景 |

## 一、先看清它给了什么

10 月 19 日发布，官方定位很直白：**Coding/Agent 优化的轻量级模型**，不是旗舰。

- **上下文 100 万 token**，原生支持文本、图片、视频输入
- **日常输出 200+ TPS，中位数（P50）170+ TPS**，官方说线上推理速度比前代快了近三倍
- 架构上是**更激进的稀疏注意力**，这是速度来源，也是它比同门 M3 便宜的本钱
- 官方基准：DeepSWE v1.1 **73.7%**、OSWorld V2 **61.7 分**、Agents' Last Exam **29.6 分**、CyberGym **82%**、BankerToolBench **76.2 分**，官方口径里 Computer Use 两项是国产第一
- 权重说「稍后开放」，Pro 版本预告了但没给时间

有个细节值得单独提：它正式露脸之前，先以 **Space Bunny** 的匿名身份在第三方路由上跑了超过 **200T token** 的真实负载。这个量级不是实验室压测能凑出来的，等于先让市场用了几个星期再公布名字——比起发布会跑分，我更信这一段。

再说句难听的：这批分数我只认一半。**DeepSWE 73.7% 是自报口径**，各家都在这个榜上刷；OSWorld 61.7 和 Agents' Last Exam 29.6 是外部可复现的活儿，含金量高一些。29.6 听着不高，但那是「让 agent 干现实里的长任务」这种考卷，目前没有谁分数好看。

## 二、价格：别只盯着输入 1 块钱

| 计费项 | 国内站（元 / 百万 token） | 海外站（美元 / 百万 token） |
|:---|:---|:---|
| 输入 | ¥1 | $0.15 |
| 输出 | ¥4 | $0.60 |
| 缓存读取 | ¥0.1 | $0.015 |

跟同门 M3 放一起就明白它的意图：M3 是输入 $0.30、输出 $1.20（512K 以内），M3.1 Flash 正好**全项一半**；缓存读取从 $0.06 砍到 $0.015，是**四分之一**。

官方还说 Agentic 任务综合成本降了 **70%**。这个数字怎么来的，我自己算了一遍——按一个真实的 agent 活儿：**200 轮**工具调用，每轮输入 **12K token**（10.8K 历史命中缓存、1.2K 新工具返回），每轮输出 **1.5K token**（含思考）。

- 输入总量 200 × 12K = **2.4M**，其中命中缓存 2.16M、未命中 0.24M；输出总量 200 × 1.5K = **0.3M**
- 按国内价：0.24×1 + 2.16×0.1 + 0.3×4 = **¥1.66**
- 缓存一次都没命中：2.4×1 + 0.3×4 = **¥3.60**

所以缓存这一层就值 **54%**，再叠上单价相对 M3 的腰斩，才摸到官方说的 70%——**纯看单价只是五折，剩下的靠缓存命中率撑**。这条推论很重要：每轮都换新提示、命中率上不去，你拿到的是五折不是三折。

还有个容易忽略的省心点：**M3 是分档计价的**，超过 512K 输入跳到贵的一档（$0.60 / $2.40）；M3.1 Flash 只有一个价，长上下文不额外加钱。真要往 1M 里塞仓库，这个差别比输入单价差得更狠。

## 三、接 Claude Code，改动最小的路

**第一步，先把环境变量清干净。** 官方文档专门标了红：环境变量优先级高于 `settings.json`，会盖掉你的 MiniMax 配置。改完不生效、`/status` 还显示 anthropic 官方地址的，九成在这里。

```bash
unset ANTHROPIC_AUTH_TOKEN
unset ANTHROPIC_BASE_URL
```

`~/.bashrc` 或 `~/.zshrc` 里 `export` 过这两个的也要删掉，不然新开终端又读回来。

**第二步，改 `~/.claude/settings.json`：**

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.minimaxi.com/anthropic",
    "ANTHROPIC_AUTH_TOKEN": "<你的 MiniMax API Key>",
    "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "524288",
    "ANTHROPIC_MODEL": "MiniMax-M3.1-Flash[1m]",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "MiniMax-M3.1-Flash[1m]",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "MiniMax-M3.1-Flash[1m]",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "MiniMax-M3.1-Flash[1m]"
  }
}
```

三个地方值得说：

- 模型名后面的 **`[1m]` 后缀不是笔误**，是让客户端按百万上下文申报。漏了它，Claude Code 会按默认窗口截断上下文
- `CLAUDE_CODE_AUTO_COMPACT_WINDOW` 设 **524288**（512K）是官方推荐值——**能读 1M 不代表该一次塞 1M**，读得越长每轮重算越贵，压缩点放在 512K 是成本和效果之间的平衡
- 海外账号把 `api.minimaxi.com` 换成 `api.minimax.io`，其余不动

**第三步，进去验。** 起 `claude` 后敲 `/status` 和 `/model`：前者应显示 base url 指向 MiniMax，后者应显示 `MiniMax-M3.1-Flash`。两个都对才算接上。

懒得手改的用官方向导 `npx -y mmx-cli@latest agent setup`，选 Claude Code，它会自己备份并改配置。用 CC Switch 管多家的，把四行模型名全填 `MiniMax-M3.1-Flash`、勾上「声明 1M」、再补 `CLAUDE_CODE_AUTO_COMPACT_WINDOW` 就行。

## 四、两个 SDK 端点，别混着记

同一个能力，两个端点两套写法，混着抄最容易出 400。

| | OpenAI 兼容 | Anthropic 兼容 |
|:---|:---|:---|
| Base URL | `https://api.minimax.io/v1` | `https://api.minimax.io/anthropic` |
| 思考深度参数 | `reasoning_effort` | `output_config.effort` |
| 思考内容字段 | `reasoning_content` | `thinking` 内容块 |
| `temperature` | 传了无效，固定 1 | 可传（0–2），模型侧仍按 1 走 |
| `top_p` | 传了无效，固定 0.95 | 可传（默认 0.95） |

```python
from openai import OpenAI

client = OpenAI(api_key="<你的 MiniMax API Key>", base_url="https://api.minimax.io/v1")

resp = client.chat.completions.create(
    model="MiniMax-M3.1-Flash",
    reasoning_effort="high",          # low / medium / high / xhigh / max
    messages=[{"role": "user", "content": "把这个函数的边界情况列出来"}],
)
print(resp.choices[0].message.reasoning_content)   # 思考
print(resp.choices[0].message.content)             # 正文
```

`temperature` 那栏值得单独提醒：OpenAI 端点文档明写「暂不支持，传了没效果」，模型恒为 1 和 0.95。**别指望靠调温度治它发挥不稳**，这条路是堵的，要稳只能改 prompt 或提思考档位。

## 五、effort 五档，默认值是个坑

`low` / `medium` / `high` / `xhigh` / `max`，**不填就是 `max`**。这个默认值很不客气：每次请求都往死里想，思考 token 全按输出价（¥4/百万）计费。拿它批量改文件名、做格式转换，等于花满档的钱办一档的事。

| 档位 | 我用来干什么 |
|:---|:---|
| `low` | 改名、格式转换、写正则、单行修复——要快和便宜 |
| `medium` | 改单个文件里的小功能，不用通盘想 |
| `high` | 新增模块、写测试，需要它自己盘一遍边界 |
| `xhigh` | 跨两三个文件改接口 |
| `max` | 跨文件重构、排查没头绪的 bug，值得让它想透 |

反过来说，**它没有 `none`**。传 `none` 是 400，想要「别思考直接答」这个模型给不了。

## 六、六个坑，按我踩的顺序

1. **thinking 关不掉，关了就 400。** `thinking: {"type": "disabled"}` 或 `reasoning_effort: "none"` 都返回 400 和错误码 2013。同门 M3 允许关（默认还就是关的），从 M3 迁过来的代码最容易在这步炸。
2. **`max_tokens` 把思考 token 一起算。** 设 `max_tokens=512` 想看一句短回答，结果思考就烧掉 400，正文一个字没有、`stop_reason` 是 `max_tokens`。新代码用 `max_completion_tokens`，并且至少 2048 起。
3. **`reasoning_split` 不能设 false。** 这个参数本来选「思考放 `reasoning_content`」还是「塞进 `content` 的 `<think>` 标签」，M3.1 Flash 设 `false` 会报错。好处是解析简单：思考永远在 `reasoning_content`，正文永远在 `content`。
4. **`service_tier` 不支持。** 想花钱买 priority 优先通道买不到，传了没用。M3 才有（标准价的 1.5 倍）。高峰期被排队时这个差别会让人有点烦。
5. **多轮对话必须把思考块原样回传。** 工具调用尤其明显：下一轮要带上完整的上一条 assistant 消息（含 `thinking` / `reasoning_content` 全部内容块），否则推理链断在中间，模型重想一遍——钱多花一遍，结论还可能不一样。只回传 `content` 是最常见的错法。
6. **一批 OpenAI 参数直接被忽略。** `top_k`、`stop_sequences`、`mcp_servers`、`context_management`、`container`、`presence_penalty`、`frequency_penalty`、`logit_bias` 都不生效；`n` 只支持 1；老的 `function_call` 不支持，得用 `tools`。

六条加起来其实是一句话：**它接受 Anthropic 和 OpenAI 两套外壳，但内核只有一套规矩，外壳上多出来的旋钮基本是假的。**

## 七、100 万上下文怎么花才不亏

**该压就压。** 官方自己推荐在 512K 处压缩，不是保守，是算过账：每轮请求都要重读历史，历史越长每轮越贵。1M 是给你偶尔啃整个仓库用的，不是日常挂着的。

**把不变的东西放最前面。** 缓存读取 ¥0.1 对比输入 ¥1，差十倍。系统提示、仓库骨架、接口文档这些每轮都一样的部分放前面，命中率能拉得很高——这也是前面那笔账省下 54% 的来源。

**截图 debug 记得降 detail。** 图片三档精度：`low` 通常几百 token（上限 600 上下）、`default` 常在 1K–3K、`high` 几千到 15K 以上。看报错截图用 `low` 基本够认字，用 `high` 是给模型买显微镜。

**视频有硬上限。** URL 或 base64 最多 50MB，图片 10MB，整个请求体 64MB。更长的先传 Files API 再用 `mm_file://{file_id}` 引用，上限能到 512MB。`fps` 默认 1、范围 0.2 到 5，这个参数直接影响 token，别默认全给。

## 八、谁该用，谁别用

| 适合 | 不适合 |
|:---|:---|
| 天天跑 Claude Code / Codex 这类 agent、成本敏感的 | 低延迟客服机器人，用户等不了思考那几秒 |
| 要把整个中型仓库塞进上下文的活儿 | 只需要一句话问答的轻量场景，满档思考是浪费 |
| 需要图像/视频理解的自动化流水线 | 依赖 `service_tier` 优先通道的线上业务 |
| 从 M3 迁过来想省一半钱的 | 需要随时关思考做确定性输出的场景 |

## 九、网络这层先弄对，模型才跑得顺

说实话，模型这层的坑踩完了，最后卡人的往往是网络：拉依赖、传大文件、流式输出断在半路，全跟线路稳定性有关，跟模型没关系。按场景分四家：

| 服务 | 起点价 | 适合谁 |
|:---|:---|:---|
| [自由猫](https://api.huanghaiwan.com/go/自由猫) | ¥8 / 30GB / 1 台 | IEPL + MPTCP 多路复用、100+ 节点。agent 长时间挂着不掉线是我最看重的。注意最低档只给 1 台设备，多设备得往上挑（¥12/100G 三台、¥19.9/200G 十台） |
| [仙路湾](https://api.huanghaiwan.com/go/仙路湾) | ¥10 起 / 50G / 3 台 | 港台原生 IP 家宽 + IEPL/IPLC 专线、20 个地区。要注册海外 API 账号、养账号环境的，比机房 IP 省事。优惠码 `xlw9` 九折 |
| [瑶瑶领先](https://api.huanghaiwan.com/go/瑶瑶领先) | ¥9.9 / 384GB / 3 台 | 大流量低价档，适合天天拉模型、下依赖。动态倍率：晚高峰 1 倍、白天 0.6 倍、夜间 0.3 倍；**SS + BGP 中转，不是专线也不带住宅 IP** |
| [SS-ID](https://api.huanghaiwan.com/go/SS-ID) | ¥20 / 100G / 5 台 | 全线 IEPL、全 1 倍率，5 台同时在线。要「计费透明不算计」的选它 |

套餐和设备数按各家在售的写，价格会变，下单前以官网为准。四家都是分成链接，点了我们有佣金——这事不藏着，选不选你自己看。

## 常见问题

**M3.1 Flash 和 M3 怎么选？** 要便宜快、主要跑代码和 agent 选 M3.1 Flash，标准价只要一半。要能关思考、要买优先通道、要更大参数量的稳，还是 M3。两个都是 1M 上下文，这点没差。

**国内能用吗？** 能。国内站端点是 `api.minimaxi.com`（Anthropic 协议 `api.minimaxi.com/anthropic`），人民币计费；海外账号换 `api.minimax.io`，按美元走。

**能免费用吗？** API 按量付费。免费额度、订阅套餐（M Plan）这些档位我没在官方定价页上核到具体数字，别照别人截图里的额度做预算，自己登录后台看。

**Claude Code 里显示 200K 上下文，是没接上吗？** 先看模型名有没有带 `[1m]`，再看 `CLAUDE_CODE_AUTO_COMPACT_WINDOW` 有没有设。两样都在还是 200K，那是客户端自己的申报逻辑，实际能不能读到 1M 得压测。

**会不会把思考写进最终回答？** 不会。走 OpenAI 端点时思考在 `reasoning_content`、正文在 `content`，字段分得开。

**要不要所有活儿都拉 max？** 不要。`max` 是默认值就已经够费，批量任务老实降到 `low` 或 `medium`，省下来的钱够多跑几轮实验。

---

**收口一句：它便宜得让人想立刻换上，但便宜的那部分是省在「思考写得短」，不是省在「不许你思考」——想把思考关掉省钱的人，会先撞上那个 400。**
