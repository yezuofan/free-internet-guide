# DeepSeek V4-Flash Vision 视觉版指南 2026：官方首个看图 API，一张图最多 384 token

> 原文链接：[DeepSeek V4-Flash Vision 视觉版指南 2026](https://huanghaiwan.com/ai/deepseek-v4-flash-vision-guide-2026/)（博客全文含完整代码示例与基准表）

2026 年 8 月 21 日下午，DeepSeek 官方 API 文档里悄悄多了一个新名字：`deepseek-v4-flash-vision-exp`。V4 系列第一款原生支持图片输入的视觉模型就这么上线了，没有发布会、没有预告。一周前 DeepSeek 刚开源 Harness 智能体框架，GitHub 讨论区里"怎么让 DeepSeek 看图"还是高频问题（传截图直接报 `MODEL_DOES_NOT_SUPPORT_IMAGES`，社区只能自己写 vision bridge 插件），现在官方自己把这块拼图补上了。

## 太长不看版

| 维度 | 结论 |
|:----|:----|
| 模型名 | `deepseek-v4-flash-vision-exp`（Exp = 实验版） |
| 上线时间 | 2026-08-21，V4 系列首款原生视觉模型 |
| 文本能力 | 与 V4-Flash 正式版持平，看图不降智 |
| 视觉能力 | 多模态 Agent 基准接近 Opus-4.8 |
| 图片计费 | 一张图最多 384 token，价格与 V4-Flash 一致 |
| 传图方式 | Base64 内联 / 外部 URL / Files API 三种 |
| 接口兼容 | OpenAI 格式 + Anthropic 格式 + Responses API |

一句话：**DeepSeek 从纯文本模型正式迈进了多模态 Agent 底座，价格延续 Flash 系列的性价比路线。**

## 背景：DeepSeek 终于"睁眼"了

8 月 13 日 DeepSeek 开源 Harness——"一切皆插件"的智能体框架，能调终端、文件、代码和外部工具，12 小时 star 破 5 万。但尴尬的是：V4 Flash 和 V4 Pro 都是纯文本模型，往 Harness 里传截图直接报错 `MODEL_DOES_NOT_SUPPORT_IMAGES`。社区只好自己"装眼睛"：前面接 Qwen-VL 把图转成文字，或改 Harness 加视觉插件，几天内 GitHub 冒出好几个 vision bridge。

一周后官方出手。`deepseek-v4-flash-vision-exp` 上线，V4 系列第一次原生支持图片输入，Agent 终于能"自己看图、自己理解、自己推理、自己调工具"。

## 核心能力：看图不降智

官方明确：在 Agent、推理、世界知识等纯文本基准上，Vision-Exp 与 V4-Flash 正式版**持平**——不是"为了看图牺牲文本"的特化模型。

视觉部分提升是结构性的，多模态 Agent 基准：

| 基准 | V4-Flash-Vision-Exp | V4-Flash | Opus-4.8 |
|:----|:----:|:----:|:----:|
| Terminal Bench 2.1 | 83.9 | 82.7 | 85.0 |
| Toolathlon-Verified | 75.9 | 70.3 | 76.2 |
| DeepSWE | 59.3 | 54.4 | 58.0 |
| NL2Repo | 57.7 | 54.2 | 69.7 |

DeepSWE 甚至超过了 Opus-4.8（59.3 vs 58.0）。官方总评"多模态 Agent 能力已接近 Opus-4.8"，考虑到价格差，含金量不低。

## 价格：一张图最多 384 token

图片按尺寸换算成 token，与文本一起计费，**价格和 V4-Flash 完全一致**——输入 $0.14/百万 tokens（缓存命中 $0.0028），输出 $0.28/百万 tokens，无视觉溢价。

进模型前每张图自动缩放：小于约 384×384 的放大，更大的缩小到约 800×800 总像素。所以每张图 token 有硬上限：**384 个**。2000×2000 和 5000×5000 的图消耗相同。

对比隔壁：GPT 和 Claude 处理同等分辨率通常消耗 800-1100 token。**同一张图，DeepSeek 开销不到竞品一半**——背后是 "Thinking with Visual Primitives" 框架，把视觉元素压缩成空间坐标式原语，而不是拆成密密麻麻的图像 patch。

## 接入教程：三种传图方式

模型参数设 `deepseek-v4-flash-vision-exp`，base_url 用 `https://api.deepseek.com`，标准 OpenAI 兼容格式。

**1. Base64 内联（本地文件最简单）**

```python
import base64
from openai import OpenAI

client = OpenAI(api_key="你的API密钥", base_url="https://api.deepseek.com")

with open("image.jpg", "rb") as f:
    b64 = base64.b64encode(f.read()).decode("utf-8")

response = client.chat.completions.create(
    model="deepseek-v4-flash-vision-exp",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "这张图片里有什么？"},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}},
        ],
    }],
)
print(response.choices[0].message.content)
```

**2. 外部图片 URL**（图片已在网上）：`image_url` 直接填 `https://example.com/image.jpg`。URL 最长 8192 字符，图片最大 32 MiB，需 60 秒内下载完成。

**3. Files API（多请求复用同一张图）**：上传一次拿 `file_id` 反复引用。图片超过 32 MiB 或请求体接近 48 MiB 限制时是唯一解（支持单图最大 64 MiB）。

```python
response = client.chat.completions.create(
    model="deepseek-v4-flash-vision-exp",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "这张图片里有什么？"},
            {"type": "file", "file_id": "file-api-xxxxxxxxxxxxxxxx"},
        ],
    }],
)
```

**Anthropic 兼容格式**：base_url 换成 `https://api.deepseek.com/anthropic`，图片用 `image` 块（source 为 base64/url/file 之一）。

**detail 参数**：`low`（缩放至 512×512，更快更省 token）/ `high`（保留原图）/ `auto`（等价 original）。批量 OCR 用 low，读小字细线条用 high。

## 限制清单

| 限制项 | 数值 |
|:----|:----|
| 支持格式 | JPEG、PNG、GIF、WebP |
| 请求体大小 | 48 MiB |
| 单图最大（base64 / URL） | 32 MiB |
| 单图最大（Files API） | 64 MiB |
| 单请求最大图片数 | 600 张 |
| 图片最大尺寸 | 单边 8192 像素（≥15 张图时降为 4096） |

两个硬性规则：**图片只能出现在 `user` 消息里**（system/assistant 带图返回 400）；只有 Vision-Exp 接受图片，其他模型传图也 400。

## 适合谁用

| 人群 | 推荐理由 |
|:----|:--------|
| Agent 开发者 | 不用再外接视觉模型做 bridge，原生看图让 Harness 类框架闭环 |
| 文档/流程自动化 | 界面截图解析、报错截图识别、图表数据提取一条龙 |
| 前端工程师 | 设计稿截图转描述、UI 重构参考 |
| 成本敏感的个人开发者 | 一张图最多 384 token，价格碾压同级别视觉模型 |

## FAQ

**Q：Exp 后缀能用生产吗？** A：实验版，官方提示快速迭代、可能有破坏性变更，生产先小流量验证。
**Q：图片怎么计费？** A：按尺寸换算 token，每张最多 384 个，与文本一起按 V4-Flash 价格计费，无溢价。
**Q：纯文本任务用这个模型会变贵吗？** A：不会，纯文本能力与价格都和 V4-Flash 持平；但纯文本场景直接用 V4-Flash 更省心。
**Q：图片能放 system 消息吗？** A：不能，只支持 user 消息，否则 400。
**Q：和 Qwen-VL 这类视觉模型怎么选？** A：已用 DeepSeek 生态的话，Vision-Exp 免桥接、格式统一、token 开销不到一半。

## 总结

V4-Flash-Vision-Exp 是 DeepSeek 补齐多模态闭环的关键一步：模型能看图了，Agent 才算真正"睁眼"。一张图最多 384 token、文本不降级、多模态 Agent 逼近 Opus-4.8，对开发者是实打实的低成本选项。Exp 后缀提醒还在快速迭代，但方向明确：**DeepSeek 的下半场，是能看、能想、能干活的多模态 Agent。**

想第一时间跑通自己的 Agent 项目，稳定的跨境网络加速服务是基础配置：[自由猫](https://api.huanghaiwan.com/go/自由猫)（IEPL+MPTCP 主力首选）、[悠兔](https://api.huanghaiwan.com/go/悠兔)（老牌稳定）、[SKYLUMO](https://api.huanghaiwan.com/go/SKYLUMO)（¥6.99 入门）、[万达云](https://api.huanghaiwan.com/go/万达云)（IEPL 高性价比）。

延伸阅读：[DeepSeek V4-Flash 正式版指南](https://huanghaiwan.com/ai/deepseek-v4-flash-guide-2026/)、[DeepSeek Harness 上手指南](https://huanghaiwan.com/ai/deepseek-harness-guide-2026/)、[DeepSeek 入门到精通](https://huanghaiwan.com/ai/deepseek-guide/)
