> 本文最初发布于 [huanghaiwan.com](https://huanghaiwan.com/ai/codex-cli-guide-2026/)

# Codex CLI 使用教程：装完别急着敲命令，先过登录、网络、权限这三关

**2026 年 11 月。** `openai/codex` 现在 133,340 star、21,127 fork，最新 release 0.166.0（2026 年 10 月 29 日），Rust 写、Apache-2.0。它是跑在终端里的编程 Agent：进项目目录敲 `codex`，它读文件、改代码、执行命令——不是编辑器补全，方向和补全相反。

## 装：挑一条路，别装两遍

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh   # macOS / Linux 官方脚本
npm install -g @openai/codex                            # 需要 Node
brew install --cask codex                               # macOS 包管理器
```

Windows 原生用 PowerShell：`irm https://chatgpt.com/codex/install.ps1 | iex`。装完 `codex --version` 能出版本号才算成。两个坑：npm 全局 bin 不在 PATH 会 `command not found`；脚本装的升级也是重跑同一条脚本，别去 npm 里找。混装两遍，两个二进制打架。

## 第一关：登录，ChatGPT 账号 vs API Key

- **Sign in with ChatGPT**：浏览器授权，额度跟订阅共享。注意档位差别：官网套餐页给 Free 和 Go 写的是「ChatGPT 桌面版里的 Codex，轻量任务」，Codex CLI 的权益从 Plus 才开始列；只想试命令行又不想开 Plus，走 API Key 更实在。
- **API Key**：按量计费，适合 CI 和团队统一出口，配置上要多写几步。

登录后本地生成 `~/.codex/auth.json`，里面是访问令牌，**当密码看**：不进 git、不贴工单、不截图。

## 第二关：终端不跟着浏览器走代理

| 症状 | 原因 | 处理 |
|:--|:--|:--|
| 授权页转圈、回调没反应 | 浏览器在境外出口，CLI 直连 | 终端也走代理，或开 TUN |
| 登录成功，一改代码就超时 | 终端没继承代理环境变量 | `export https_proxy=...` 或 TUN 接管 |
| 跑五分钟断一次 | 节点抖动，长任务被掐 | 换稳定线路，别用公共试用节点跑长任务 |

0.166.0 新增 `codex doctor --network-only`，把配置、连通性、WebSocket 单独查一遍。装完先跑一次，比出事再翻日志省事。

**账号环境比峰值速度重要**：登录态对 IP 变化敏感，一天之内在七八个国家之间跳，被要求手机验证甚至临时限制的概率明显上升。稳定优先于快，住宅 IP 优先于机房 IP。

## 第三关：权限模型（比登录更容易劝退）

两个轴：`approval_policy` 管什么时候停下问你，`sandbox_mode` 管它能碰什么。配置在 `~/.codex/config.toml`，项目级 `.codex/config.toml` 只在信任该项目时加载。

```toml
approval_policy = "on-request"
sandbox_mode = "workspace-write"
```

`workspace-write` 能改工作区，但 `.git`、`.codex`、`.agents`、`.aws` 是受保护路径，改不动。

**2026 年的大坑**：从 0.149.0 起 `untrusted` 审批策略被移除，旧教程抄来的配置会让程序直接起不来，报错原文 `approval_policy = "untrusted" is no longer supported; remove this setting.` 打开 `~/.codex/config.toml`（Windows 是 `%USERPROFILE%\.codex\config.toml`）删掉那行即可。想要更严格，用 `sandbox_mode = "read-only"` 配 `on-request`。沙箱三档：`read-only`、`workspace-write`、`danger-full-access`（会话里也能用 `/permissions` 切），最后一个只在容器或一次性 runner 里用。

## 额度别烧在复述需求上

`/status` 看剩余额度，`/model` 调模型与推理档，`/init` 生成 AGENTS.md（写清技术栈、目录约定、哪些文件别动，等于把重复解释压缩成一次）。`web_search` 默认是 `cached`，查的是索引缓存不是实时网页，需要最新数据再切 `live`。最省额度的一条不是调参数，是一次把目标、约束、验收标准说完整——来回问三轮比重写一遍提示词贵得多。

## codex exec：脚本化和批量

```bash
codex exec "把测试跑一遍，列出失败项和最可能的原因"
codex exec --sandbox workspace-write "把 utils 里重复的三个函数合并掉"
```

默认在**只读沙箱**里跑，要改文件必须显式 `--sandbox workspace-write`。`--full-auto` 已不支持（2025 年的教程还在写它），自动批准用 `--approve-for-me`。要机器可读加 `--json`（JSONL 流），要固定结构加 `--output-schema`，只取最后一段用 `-o 文件`。另有一条硬要求：必须在 git 仓库里跑，确实要绕过加 `--skip-git-repo-check`——先问自己这目录有没有备份。

## 网络这层怎么配（2026 年 11 月现行价）

这类工具要的不是峰值带宽，是长时间连接稳定加 IP 别乱跳。一个任务跑十几分钟，中间断一次就得重来，损失的是额度不是流量。

| 场景 | 推荐 | 起价 |
|:--|:--|:--|
| 账号登录、单人日常 | [仙路湾](https://api.huanghaiwan.com/go/仙路湾)（机房 + ISP 住宅 IP 混合；¥10 档是普通中转入口，IEPL 从专业档起） | ¥10 / 50G / 3 台 |
| 大流量、天天拉依赖 | [瑶瑶领先](https://api.huanghaiwan.com/go/瑶瑶领先)（SS + BGP 中转，非专线） | ¥9.9 / 384G / 3 台 |
| 多设备 + 住宅 IP 兜底 | [大象网络](https://api.huanghaiwan.com/go/大象网络)（旗舰档 600G 不限设备，美国原生住宅 IP） | ¥55 |
| 要专线但便宜 | [SS-ID](https://api.huanghaiwan.com/go/SS-ID)（IEPL 专线） | ¥20 / 100G / 5 台 |

自由猫 ¥8 / 30G 最便宜，但套餐说明写明不支持第三方客户端，命令行这种用法先问客服再下单。另外别指望最低档扛长任务：连续跑两小时 agent 会话，晚高峰一抖，前面烧的 token 全白费。

## 五问速答

**Windows 用原生还是 WSL2？** 依赖 Linux 工具链就直接 WSL2，Codex 看到的是完整 Linux 环境。
**npm 装完找不到命令？** 全局 bin 没进 PATH。
**能登录但一发任务就断？** 先 `codex doctor --network-only`，再查终端代理变量。
**启动报 approval_policy 错？** 删掉旧配置里的 `untrusted`。
**额度用完？** 等周期重置、买 credit 或升档。

---

*本文包含推广链接，均为核对过的真实推荐。*
