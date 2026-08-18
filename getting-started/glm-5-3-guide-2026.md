# 智谱 GLM-5.3 发布评测 2026：编程能力提升50%、开源第一、两周后开放权重

> 本文最初发布于 [huanghaiwan.com](https://huanghaiwan.com/ai/glm-5-3-guide-2026/)

2026 年 8 月 14 日，智谱（港交所 02513）正式发布 GLM-5.3。这一周大模型圈几乎一天一个新旗舰：Grok 4.6 刚发完、DeepSeek V4 Pro 正式版虚晃一枪，智谱的答卷也到了。但 GLM-5.3 有个不太一样的点：**基座没换**——7430 亿参数跟 GLM-5.2 同一套底子，所有性能提升全部来自后训练 Scaling（官方原话 "scaling post-training is all we did"）。

## 太长不看版

| 维度 | 结论 |
|:----|:-----|
| 发布时间 | 2026-08-14，智谱（港交所 02513） |
| 模型规格 | 7430 亿参数，与 GLM-5.2 同基座，纯后训练升级 |
| 编程能力 | 内部体感评测较 GLM-5.2 提升 50%，Terminal-Bench 3.0 从 4.6 涨到 28.3 |
| 开源排名 | Terminal-Bench 3.0、Agents' Last Exam (CLI) 等公开基准开源第一 |
| 网络安全 | CyberGym 84.5%（开源第一），白盒代码审查追平 Anthropic Mythos 5 |
| Token 效率 | 高思考档位下 31.5% 准确率，超过 Claude Opus 4.8 的 29.5% |
| 开源计划 | 发布两周后开放模型权重（先做安全加固） |
| 当前入口 | GLM Coding Plan、ZCode、AutoClaw 已上线，API 很快上线 |

## 核心性能

**编程能力（主战场）：** 内部自建体感评测较 GLM-5.2 提升 50%。公开基准跃升更直观：

| 基准 | GLM-5.2 | GLM-5.3 |
|:----|:-------|:-------|
| Terminal-Bench 3.0 | 4.6 | 28.3（约 6 倍） |
| DeepSWE v1.1 | 46.2 | 66.9 |
| CyberGym 漏洞推理 | 77.2% | 84.5% |

**Agent 能力：** Agents' Last Exam (CLI) 等公开基准开源模型第一，编程与智能体能力接近 Claude Fable 5 和 GPT-5.6 Sol，编程体感超过其他国产模型；与 Kimi K3 互有胜负，绝大部分基准领先 DeepSeek V4 Pro 正式版。

**Token 效率：** 相同高思考档位下准确率 31.5%（超 Claude Opus 4.8 的 29.5%），任务平均输出约 5 万 token，不到 Opus 的一半——在 OpenAI 刚把 GPT-5.6 Luna API 降价 80% 的价格战背景下，这直接关系 API 账单。

**网络安全（意外涌现）：** 白盒代码审查与漏洞发现任务持平 Anthropic Mythos 5（参数体量仅其十分之一），CyberGym 开源第一。清华 NASP 实验室用它挖出 Cursor 权限校验漏洞。客观说：任务链前端（代码审查、漏洞推理）强，完整漏洞利用链条还有提升空间。

## 定价

**API（bigmodel.cn 官方）：** 输入 8 元 / 百万 token，输出 28 元 / 百万 token，缓存命中 2 元，新品限时免费。上下文 1M，与 GLM-5.2 同价。

**GLM Coding Plan：** 全量开放订阅，按 Token 扣积分计费（7 月底刚从按 prompt 次数改为积分制），8/14 发布当天 13:00 全员额度重置。档位价格以官网实时显示为准。

## 四种接入方式

1. **GLM Coding Plan** — 订阅用户 8/14 当天即可切到 GLM-5.3，零配置
2. **ZCode / AutoClaw** — 智谱官方编程工具（ZCode 偏编程 Agent 工作台，AutoClaw 偏自动化效率），内置 GLM-5.3
3. **兼容主流编码平台** — 兼容 Claude Code、OpenCode 等代码代理工具，改 base_url 和模型名即可；TraeWork/TraeCode、扣子、WorkBuddy/CodeBuddy、Qoder/QwenWork、CatPaw、JoyCode 等已开放抢先体验；范式 PhanRouter 8/17 首批接入，原 API 接口沿用、只改模型名
4. **等开源权重** — 约 8 月底开放完整模型权重（先做分层风险审查和安全加固），想本地部署/微调/自托管的团队直接等

## 竞品怎么选

| 维度 | GLM-5.3 | DeepSeek V4 Pro | Claude Fable 5 |
|:----|:-------|:----------------|:--------------|
| 编程定位 | 开源第一，逼近 Fable 5 | 生产环境 Agent 强 | 闭源标杆 |
| 开源 | 两周后开源权重 | 闭源 API | 闭源 |
| 价格 | 输入 8 元 / 输出 28 元 | 高峰 $1.32/$3.96 | 最高 |
| Token 效率 | 31.5% / 5 万 token | — | Opus 级 29.5% |

一句话：要开源、要自托管、要编程性价比选 GLM-5.3；要生产环境 Agent 稳定选 DeepSeek V4 Pro；预算不敏感要闭源标杆选 Claude Fable 5。

## FAQ

**Q1：GLM-5.3 是开源的吗？** 权重计划发布两周后（约 8 月底）开放，先做安全加固。当前经 GLM Coding Plan、ZCode 和第三方平台（PhanRouter、Trae 等）使用。

**Q2：和 GLM-5.2 有什么区别？** 基座相同（7430 亿参数），所有提升来自后训练。编程 +50%，Terminal-Bench 3.0 从 4.6 涨到 28.3，新增网络安全能力（CyberGym 开源第一）。

**Q3：API 什么时候上线？** 官方口径"很快上线"。bigmodel.cn 定价页已列出 GLM-5.3（输入 8 元 / 输出 28 元 / 1M 上下文），限时免费阶段可先体验。

**Q4：国内开发者可以直接用吗？** 可以。智谱是港股上市公司（02513），bigmodel.cn 开放平台直接注册使用，无需额外网络环境。

**Q5：GLM Coding Plan 值得订阅吗？** 每天高强度用 AI 写代码，订阅按 Token 扣积分比按次付费划算；轻度用户建议等 API 上线按量付费。

## 总结

GLM-5.3 是 2026 年 8 月国产模型混战里性价比很高的一张牌：不换基座纯靠后训练，编程能力冲上开源第一，还白捡一个网络安全技能树。两周后开源权重是最大变量——本地部署、微调、自托管届时全部解锁，价格敏感型团队值得等。

相关教程：[DeepSeek V4 Pro 正式版指南 2026](https://huanghaiwan.com/ai/deepseek-v4-pro-guide-2026/) ｜ [Kimi K3 指南 2026](https://huanghaiwan.com/ai/kimi-k3-guide-2026/) ｜ [Grok 4.6 发布评测](https://huanghaiwan.com/posts/grok-4-6-release-review-2026/) ｜ [DeepSeek Harness 上手指南](https://huanghaiwan.com/ai/deepseek-harness-guide-2026/)
