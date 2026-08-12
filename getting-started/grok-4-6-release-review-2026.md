# Grok 4.6 发布快评 2026：61分追平GPT-5.6 Sol，API价格砍掉六成

> 北京时间 8 月 13 日凌晨，SpaceXAI 正式发布新一代大模型 Grok 4.6。官方口径：Artificial Analysis Intelligence Index 综合 61 分，与 GPT-5.6 Sol 持平；GDPval-AA v2 拿到 1753 Elo，反超 Claude Fable 5。API 每百万 token 输入 2 美元、输出 6 美元，对比 GPT-5.6 Sol 的 5/30 美元，输出价砍到五分之一。同一夜 DeepSeek V4 Pro 正式版（0813）悄然上线。

## 太长不看版

| 维度 | 结论 |
|:----|:----|
| 发布 | 2026-08-12（美东），SpaceXAI |
| 定位 | Grok 4.5 升级版，主打长时间运行的智能体任务和复杂交互、视觉工作 |
| 综合成绩 | AA Intelligence Index 61 分，与 GPT-5.6 Sol 打平；仅次于 Claude Fable 5（62） |
| 亮点基准 | GDPval-AA v2 1753 分超 Fable 5；CursorBench 3.2 达 69.9% |
| 定价 | API $2/$6 每百万 token，约为 GPT-5.6 Sol 的三分之一 |
| 上线渠道 | grok.com、X、App、Cursor、Grok Build（首周 2x 用量）、API |
| 注意点 | DeepSWE（65.9%）和 Terminal-Bench（26%）仍落后 GPT-5.6 Sol |

## 核心基准数据

| 基准 | Grok 4.6 | GPT-5.6 Sol Max | Fable 5 Max |
|:----|:----:|:----:|:----:|
| AA Intelligence Index | 61 | 61 | 62 |
| GDPval-AA v2 | 1753 | 1728 | 1741 |
| CursorBench v3.2 | 69.9% | 67.2% | 70.5% |
| DeepSWE v1.1 | 65.9% | 73% | 70% |
| AA-Briefcase | 1577 | 1502 | 1574 |
| Harvey LAB (Vals) | 15.8% | 2.5% | 11.3% |

三条线：① 综合智能打平第一梯队（61 vs 61）；② 知识工作/代理任务反超（GDPval 1753、AA-Briefcase 1577 均第一）；③ 纯编码终端仍不是最强（DeepSWE、Terminal-Bench 落后），定位是"知识工作 + 长程智能体 + 从想法到成品"。

## 价格战：2/6 美元意味着什么

| 模型 | 输入（$/百万token） | 输出（$/百万token） |
|:----|:----:|:----:|
| Grok 4.6 | 2 | 6 |
| GPT-5.6 Sol | 5 | 30 |
| Claude Opus 5 | 5 | 25 |
| DeepSeek V4 Pro | 0.435 | 0.87 |
| Qwen3.8-Max（国内） | 约 1.7（¥12） | 约 5（¥36） |

- 对标 GPT-5.6 Sol，输出价砍掉 80%，性能打平、价格三分之一
- 但打不过 DeepSeek 的绝对低价（输出 0.87 美元，是 Grok 的七分之一）
- Cursor 和 Grok Build 首周 2x included usage，想测趁早

## 同夜主角：DeepSeek V4 Pro 正式版

低调上线：API 文档把 `deepseek-v4-pro` 切到 `DeepSeek-V4-Pro-0813`，调用方式不变。100 万 token 上下文、单次最大输出 38.4 万 token、思考模式默认开启。价格维持：缓存命中 0.003625 / 未命中 0.435 / 输出 0.87 美元。官方预告过 API 要整体涨价，当前可能是过渡定价。九项智能体测试相比预览版平均提升约 25.7 分，终端操作接近 Kimi K3 和 Fable 5。

## 4 种方式用上 Grok 4.6

| 方式 | 门槛 | 说明 |
|:----|:----|:----|
| grok.com / X / App | 免费 | 网页端、iOS/Android 直接选模型 |
| Cursor | 订阅 | 编辑器内选 Grok 4.6，首周 2x 用量 |
| Grok Build | SuperGrok 订阅 | 终端编码 agent，首周 2x 用量 |
| API | 开发者 | console.x.ai 申请，或走 OpenRouter/Vercel/Cloudflare |

## 新模型选型参考

| 需求 | 优先考虑 | 理由 |
|:----|:----|:----|
| 综合智能 + 知识工作 | Grok 4.6 / GPT-5.6 Sol | AA 指数第一梯队 |
| 预算敏感的长程 agent | DeepSeek V4 Pro | 输出 0.87 美元，agent 测试逼近 Fable 5 |
| 中文生态 + 开源权重 | Qwen3.8-Max | 2.4T 参数首次开源 |
| 长上下文 + 开源 | Kimi K3 | 2.8T 参数开源，百万 token 上下文 |
| 纯编码终端 | GPT-5.6 Sol / Claude 系 | DeepSWE、Terminal-Bench 仍领先 |

## FAQ

**Q：Grok 4.6 免费能用吗？** 能。grok.com 网页版、X、iOS/Android App 直接用；SuperGrok 订阅解锁更高额度和 Grok Build。

**Q：和 Grok 4.5 差多少？** 综合指数 56→61，GDPval 1526→1753，Terminal-Bench 15.7%→26%，提升集中在长程智能体、知识工作。

**Q：API 真比 GPT-5.6 Sol 便宜那么多？** 是。输出 6 vs 30 美元，五分之一。另有速度翻倍的更高档位。

**Q：DeepSeek V4 Pro 涨价了吗？** 没有，但官方预告近期整体上调，当前可能是过渡定价。

**Q：国内能直接访问 grok.com 吗？** grok.com 和 xAI API 属境外服务，需跨境网络环境。国内开发者可优先选国产平台（千问、DeepSeek），或经 OpenRouter 等 API 中转。

## 写在最后

Grok 4.6 把"第一梯队性能"和"半价"焊在一起，DeepSeek 同夜跟进，Qwen3.8 前脚开源——2026 下半年模型竞争从"谁更强"变成"谁更划算"。用上这些海外 AI 服务，稳定的跨境网络是前提：

| 服务商 | 适合场景 | 特点 |
|:----|:----|:----|
| [自由猫](https://api.huanghaiwan.com/go/自由猫) | 多设备、长期使用 | IEPL 专线 + MPTCP 多路复用 |
| [万达云](https://api.huanghaiwan.com/go/万达云) | 入门体验 | IEPL 专线，经济型套餐 |
| [SS-ID](https://api.huanghaiwan.com/go/SS-ID) | 流媒体 + 办公 | IEPL 专线，流媒体解锁，5 设备 |
| [MESL](https://api.huanghaiwan.com/go/MESL) | 稳定备用 | IEPL 专线，中转入门 |

原文：[Grok 4.6 发布快评 2026（完整版）](https://huanghaiwan.com/ai/grok-4-6-release-review-2026/)
