# DeepSeek Harness 上手指南 2026：官方开源的 Agent 框架，3 天 star 破 11 万

> 本文最初发布于 [huanghaiwan.com](https://huanghaiwan.com/ai/deepseek-harness-guide-2026/)

2026 年 8 月 13 日晚，DeepSeek 正式开源了它的第一个 Agent 产品——DeepSeek Harness（简称 dsh）。上线 12 小时 star 破 5 万，3 天冲到 11 万以上。这篇文章讲清楚它是什么、和 Claude Code 有什么不一样、本地怎么跑起来，以及现在这个版本适合谁。

## 太长不看版

| 维度 | 结论 |
|:----|:----|
| 定位 | DeepSeek 官方开源的 agent harness（智能体框架），与 Claude Code / OpenCode 同类 |
| 发布时间 | 2026-08-13 晚，v0.1 开发者预览版 |
| 开源协议 | MIT，商用无限制 |
| 热度 | 12 小时破 5 万 star，8/16 已 11.4 万+ |
| 核心设计 | 一切皆插件（Everything is a Plugin），基于 Cordis 元框架 |
| 上手成本 | 装 Node.js，一行 `npx @deepseek-ai/dsh web` |
| 适合谁 | 开发者、想研究 agent 架构的人；不适合要开箱即用的普通用户 |

## 核心概念：Model + Harness = Agent

官方定义：**Model + Harness = Agent**。模型是脑子，Harness 是手脚。聊天机器人交给你一段话，Agent 交给你一件做完的事。

DeepSeek 之前在模型层面已经站住了，但模型只解决"想"，不解决"做"。要让 AI 真正干活——改代码、查资料、跑流程——得有人把模型和工具、文件、命令行、浏览器这些执行能力接起来。这个"接起来"的壳就是 harness，DeepSeek 选择把它做成 MIT 开源框架。

## 一切皆插件

dsh 的核心口号是 **"Everything is a Plugin"**——一切皆插件，这是架构事实：

- 模型适配器、工具注册表、会话日志、agent 主循环都是插件
- 甚至整个前端 UI 都可以换（有人用 Prompt 就把默认界面改成了洋红色主题）

整套框架基于 Cordis 插件元框架构建（论文《A Programming Paradigm for Spatiotemporal Composability》）。Cordis 只负责插件加载卸载和依赖管理，dsh 全部业务组件都是独立插件，通过服务与事件机制协同，开发者不用改源码就能在配置层自由拼装。

预置四种运行模式：

| 模式 | 加载的插件 | 适合场景 |
|:----|:----|:----|
| 标准模式 | 全套工具（文件、shell、联网检索、技能调用） | 通用开发 |
| PTC 模式 | 程序化工具调用，模型生成代码编排多轮工具链 | 复杂任务自动化 |
| 极简模式 | 只保留 Shell 和文件编辑 | 最小环境基准测试 |
| 创造模式 | 查看运行时状态、内存内调试插件、自定义新模式 | 插件开发 |

内置能力：项目管理、长周期任务协作、多智能体编排、上下文管理。

## 上手体验

dsh 不是云端服务，数据全在本地。装好 Node.js 后：

```sh
npx @deepseek-ai/dsh web
```

浏览器打开 `http://127.0.0.1:3080`，就是它的全部界面。会话、日志、数据都留在本地。两种 profile 模板：`web`（带浏览器 UI）和 `headless`（一次性运行，无服务器）。从源码跑：clone 后 `pnpm install && pnpm run build && pnpm dsh web`。

极客公园发布当晚实测两件活：照 The Verge 风格重构官网、调 GitHub 接口画出 dsh 涨星曲线，都交付了，全程 token 不到 3 块钱。当然它还是毛坯：界面偏开发者向，官方明确标注 v0.1 预览版，核心接口未来几个月会快速演化。

## 和 Claude Code 的区别

| 维度 | DeepSeek Harness | Claude Code / OpenCode |
|:----|:----|:----|
| 定位 | 通用 agent 框架 | 编程助手为主 |
| 模型绑定 | 模型是插件，可换 | 深度绑定自家模型 |
| 架构 | 一切皆插件，主循环都可换 | 相对固定单体 + 工具调用 |
| 数据归属 | 全本地，会话可 fork/resume | 本地 CLI + 云端混合 |
| 成熟度 | v0.1 预览，将有破坏性变更 | 相对成熟，生产可用 |
| 授权 | MIT 开源 | 闭源（Claude Code）/ 开源（OpenCode） |

Claude Code 是"开箱即用的编程助手"，dsh 是"可以自己组装成任何 agent 的乐高"。想立刻干活选前者；想研究 agent 架构、定制执行引擎，dsh 的插件化设计值得拆开看。

## 现在适合谁用

**适合：** 开发者研究 agent 框架架构；想用 DeepSeek 模型跑本地 agent、数据不上云的人；愿意折腾、能接受 API 变化的人。

**不适合：** 要开箱即用的普通用户；生产环境依赖（官方声明"THERE WILL BE COMPATIBILITY-BREAKING CHANGES"，等稳定版更稳妥）。

## FAQ

**Q1：DeepSeek Harness 是什么？**
DeepSeek AI 官方开源的 agent 框架，核心公式 Model + Harness = Agent。MIT 协议，2026-08-13 发布 v0.1 开发者预览版。

**Q2：和 Claude Code 有什么区别？**
Claude Code 是深度绑定 Claude 的编程助手，开箱即用；dsh 是模型、工具、UI 全部可替换的通用 agent 框架，需要自己组装。

**Q3：怎么开始用？**
装 Node.js，然后 `npx @deepseek-ai/dsh web`，浏览器打开 `http://127.0.0.1:3080`。模型适配器是插件，可接 DeepSeek API 或其他模型。

**Q4：免费吗？**
框架本身 MIT 开源完全免费。调用模型 API 按 token 计费，用 DeepSeek V4 系列成本是主流闭源模型的零头。

**Q5：现在适合普通用户用吗？**
不建议。当前是开发者预览版，界面偏技术向，官方警告会有破坏兼容性的变更。想省心的等正式版。

**Q6：国内可以用吗？**
可以。框架本地部署，数据不出本机；模型 API 用 DeepSeek 官方即可，无需额外网络配置。

## 相关教程

- [DeepSeek 入门到精通指南](https://huanghaiwan.com/ai/deepseek-guide/)
- [DeepSeek V4 Pro 正式版指南（API 接入）](https://huanghaiwan.com/ai/deepseek-v4-pro-guide-2026/)
- [AI Agent 完全指南（LangChain/AutoGen/CrewAI）](https://huanghaiwan.com/ai/ai-agent-frameworks-guide/)
- [Claude Code 上手指南](https://huanghaiwan.com/ai/claude-code-guide-2026/)
