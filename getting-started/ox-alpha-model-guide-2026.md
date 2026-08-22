# 神秘"牛来"大模型 Ox Alpha：编程测试超 GPT-5.6 的匿名模型怎么免费体验

> 原文发表于 [huanghaiwan.com](https://huanghaiwan.com/ai/ox-alpha-model-guide-2026/)，2026-08-23 更新

## 太长不看版

| 项目 | 信息 |
|:----|:-----|
| 是什么 | 8月20日 OpenRouter 匿名上线的神秘模型，代号 Ox Alpha（国内网友叫"牛来"） |
| 免费窗口 | 上线一周内免费调用 |
| 硬指标 | 约 104.8 万 token 上下文、最大输出 13.1 万 token、支持文本/图像/视频输入 |
| 编程测试 | DeepSWE 10 个任务通过 8 个（80%），高于 Claude Fable 5（65%）和 GPT-5.6 Sol（52%） |
| 身份猜测 | 技术指纹高度指向智谱 GLM-5.x 系列，官方未确认 |
| 怎么用 | OpenRouter 网页直接聊，或 API 调用；OpenCode 已接入 |
| 注意 | 匿名模型不背书、样本量小，别拿生产环境赌 |

## 一款来历不明的模型，48 小时刷屏

8 月 20 日，AI 模型聚合平台 OpenRouter 上线一款代号 **Ox Alpha** 的匿名新模型，官方描述为"面向编码、长时间智能体任务和实际生产环境的前沿模型"，开发方一个字没提。

参数：上下文约 104.8 万 token，最大输出 13.1 万 token，支持文本、图像和视频输入，预览期免费。开源终端编程智能体 **OpenCode** 当天宣布接入，并准备了每天 100 万亿 token 的调用容量。

独立研究员 Ben Davis 用 DeepSWE 基准 10 个子任务测试：Ox Alpha 通过率约 80%，高于 Claude Fable 5（65%）、GLM-5.3 和 Grok 4.6（62%）、GPT-5.6 Sol（52%）。其中 meriyah-explicit-resource-declarations 任务它一次通过，其余几家此前都是 0/4；51,469 项回归测试全部通过。

Ox 在英文里是"牛"的意思，国内网友叫它 **"牛来"大模型**。

## 它到底是谁家的？

社区猜测四个方向：小米 MiMo（曾以 Hunter Alpha 匿名测试）、智谱 Z.ai（Pony Alpha → GLM-5 先例）、腾讯混元、Google Gemini。

Ben Davis 表示 **99% 确定属于智谱 GLM-5.x 系列**，证据链：

- **视频编码器**：与 GLM-5V-Turbo 的 video token 消耗完全一致（帧率无关帧采样、约每秒 147 token 时长缩放、逐帧分辨率缩放）
- **分词器**：25 个提示词测试 token 计数与 GLM-5.3 完全吻合，仅差固定 +75 token 隐藏封装，基本共享同一词表
- **音频行为**：拒绝音频输入与 GLM-5V 一致；支持音频的 MiMo v2.5 可能性被削弱
- **输出风格**：每千字符约 1.3 个 emoji，与 GLM/Qwen 接近；Claude、GPT-5.6、Grok 接近于零

不过这些是个人测试和技术推断，智谱官方未确认。同一模型被问及身份时自称过 Gemini——匿名模型完全可能生成看似合理实则失实的答案。身份等官宣。

## 为什么值得关注

1. **免费**：上线一周内零成本调用，对比 GPT-5.6 Sol 和 Claude Fable 5 都要订阅或按量付费
2. **生态接入**：OpenCode（用户刚破 20 万）已接入，模型中立可自由切换
3. **能力能打**：即使剔除小样本数据，51,469 项回归测试全过、单一任务一次通过也说明不是花架子
4. **格局信号**：DeepSeek 开源 Harness（8/13）、OpenAI 开源 Codex Harness（8/21）、DeepSeek V4 免费通道下线——AI 编程赛道进入新一轮军备竞赛

## 怎么免费体验

### 方式一：OpenRouter 网页直接聊

打开 OpenRouter，搜索 `stealth/ox-alpha`（或直接访问模型页面），免费期内直接对话，可传图传视频测长上下文。

### 方式二：OpenRouter API 调用

拿到 API Key 后，请求里 model 参数写成 `stealth/ox-alpha`：

```bash
curl https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer 你的API密钥" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "stealth/ox-alpha",
    "messages": [{"role": "user", "content": "写一个 Python 快速排序"}]
  }'
```

免费期内不扣费；结束后按页面实时价格计费。

### 方式三：OpenCode 里直接用

OpenCode 已原生接入 Ox Alpha，安装后在模型列表选 `ox-alpha` 即可，适合直接丢进真实代码仓库做重构、修 bug、写测试。

## 客观说几句

- **样本小**：DeepSWE 只测 10 个任务，各模型测试次数不一致，Ox Alpha 还没进官方排行榜
- **匿名不背书**：没有 system card、没有安全评估报告，跑生产环境风险自负
- **免费窗口有限**：一周后大概率收费或下架，想测趁早

## FAQ

**Q：Ox Alpha 和 GLM-5.3 是什么关系？**
A：多项技术指纹指向同一家族，但智谱未官宣。即便同源，DeepSWE 表现也优于 GLM-5.3，可能是更新版本或编码优化变体。

**Q：它比 GPT-5.6 强吗？**
A：小样本测试通过率更高（80% vs 52%），真实能力需要更大规模验证，说"全面超越"为时过早。

**Q：中国用户能访问 OpenRouter 吗？**
A：OpenRouter 需要跨境网络才能顺畅访问，建议选择支持 IEPL 专线的服务商保障 API 调用稳定。

## 相关教程

- [GLM-5.3 上手指南](https://huanghaiwan.com/ai/glm-5-3-guide-2026/)
- [DeepSeek Harness 框架解读](https://huanghaiwan.com/ai/deepseek-harness-guide-2026/)
- [Claude Code 完整指南](https://huanghaiwan.com/ai/claude-code-guide-2026/)
- [DeepSeek V4-Flash 正式版指南](https://huanghaiwan.com/ai/deepseek-v4-flash-guide-2026/)

## 跨境网络加速方案推荐

测试 Ox Alpha、调用 OpenRouter API、体验 OpenCode，都离不开稳定的跨境网络：

| 需求 | 推荐 | 特点 |
|:----|:----|:----|
| 主力推荐 | [自由猫](https://api.huanghaiwan.com/go/自由猫) | IEPL 专线，MPTCP 多路复用，100+ 节点，不限设备 |
| 开发测试 | [万达云](https://api.huanghaiwan.com/go/万达云) | IEPL 线路，稳定性好，性价比高 |
| 团队协作 | [SS-ID](https://api.huanghaiwan.com/go/SS-ID) | IEPL 专线，流媒体解锁，5 设备，月付 ¥20 起 |
| 预算入门 | [SKYLUMO](https://api.huanghaiwan.com/go/SKYLUMO) | 全球 80+ 地区覆盖，¥6.99/月起 |

> 定价以各服务商官网实时显示为准。
