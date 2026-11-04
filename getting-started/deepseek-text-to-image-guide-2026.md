> 本文最初发布于 [huanghaiwan.com](https://huanghaiwan.com/ai/deepseek-text-to-image-guide-2026/)

# DeepSeek 文生图指令怎么写？三个必应下拉词背后，是三条真出图的路

「deepseek 文生图」这个词在必应的下拉框里能拉出六条建议：文生图指令、文生图提示词、文生图模型、文生图怎么用、文生图如何使用。我第一反应是——这么多人搜，网上教程应该一抓一把吧？

先别急着抄指令，往下看完再动手。

**核心前提：DeepSeek 官方的对话产品和付费 API，到 2026 年 11 月依然没有任何生图端点。** API 里有 `chat/completions`，有图片输入，但没有 `images/generations` 这类生成端点。指令写得再漂亮，发给它也只有文字回来。2025 年 1 月开源的 Janus-Pro 确实是文生图模型，但它只有开源权重，从没接进网页端、App 或付费 API——开源模型存在，和你聊天框里能画图，是两件事。

想通了这点，三条路的分野就清楚了：让 DeepSeek 干它擅长的（把你的想法翻译成精准提示词），落笔交给真正的生图模型。

## 路线 A：提示词工程，零门槛，人人能用

适合偶尔出几张图、不想折腾配置的人。用中文把画面描述给 DeepSeek，让它产出给 Midjourney / 即梦 / 通义万相用的英文提示词，复制过去生图。我现在每周大概用这法子出 10 次，全程没花过 1 块钱。

直接抄的指令模板：

```text
你是文生图提示词专家。我要生成一张图，画面是：【用中文随便描述】。请输出一段英文提示词，要求：
1. 主体、环境、光线、风格四个要素齐全；
2. 不要堆形容词，控制在 60 词以内；
3. 最后给一行对应的中文直译，让我确认它理解对了。
```

大多数人写不好生图提示词，卡点不在想象力，在「不知道生图模型吃哪一套格式」。让 DeepSeek 翻译一次，出图命中率明显比自己憋的高。缺点是要在两个工具之间来回粘贴，量大了烦。

## 路线 B：API 串联，批量出图的正经解法

适合每天要出几十张图的场景——电商素材、文章配图、批量换背景。第一步调 DeepSeek 拿提示词，第二步把提示词喂给生图服务拿图，一个脚本串起来：

```python
import requests

r1 = requests.post("https://api.deepseek.com/chat/completions",
    headers={"Authorization": "Bearer DS_KEY"},
    json={"model": "deepseek-chat",
          "messages": [{"role": "user", "content": "把这句话扩写成英文生图提示词：圣诞主题产品图"}]})
prompt = r1.json()["choices"][0]["message"]["content"]

r2 = requests.post("https://生图服务地址/v1/images/generations",
    headers={"Authorization": "Bearer IMG_KEY"},
    json={"model": "生图模型名", "prompt": prompt, "size": "1024x1024"})
print(r2.json()["data"][0]["url"])
```

成本账（2026 年 10 月价格）：DeepSeek 生成一条提示词不到半分钱，即梦 API 一张 1024 图约 0.15~0.2 元，合计一张图 0.18 元上下。

两个坑：一是**并发别拉满**——生图 API 普遍限流，20 并发掉了三分之一，降到 5 并发加重试就稳了；二是**生图服务的出口在境外**，批量传素材对上行带宽敏感，链路一抖就超时重传，这段挂专线跑基本不再掉链子。

## 路线 C：装插件，在对话里直接出图

已经在用 DeepSeek Harness（dsh）的人，装 `dsh-image-gen` 插件（要求 Node.js 22.19 或 24.0 以上）就能在对话里直接文生图、图生图、连续编辑，背后可接云端生图服务或本地 ComfyUI：

```bash
pnpm dsh plugin add dsh-image-gen
```

装完直接说「画一张……」，想要多张候选就开 Studio 工作台一次出 2~4 张。部署 dsh 的完整步骤见原文的 Harness 上手指南。

## 三条路怎么选

| 你的情况 | 走哪条 | 一次成本 |
|:--|:--|:--|
| 一周出几张图，怕折腾 | A：提示词工程 | 0 元 |
| 每天批量出图 | B：API 串联 | 约 0.18 元/张 |
| 已在用 dsh | C：插件 | 本地 ComfyUI 免费 |

## 在用且跑 API 较稳的几家

| 用途 | 推荐 | 套餐参考 |
|:--|:--|:--|
| 跑批主力，稳定优先 | [自由猫](https://api.huanghaiwan.com/go/%E8%87%AA%E7%94%B1%E7%8C%AB) | IEPL + MPTCP，¥8/30GB 起，¥12/100GB 支持 3 台 |
| 大流量，下载素材多 | [瑶瑶领先](https://api.huanghaiwan.com/go/%E7%91%B6%E7%91%B6%E9%A2%86%E5%85%88) | ¥9.9/384GB（3 台）、¥19.8/768GB（6 台） |
| 账号环境，原生 IP | [仙路湾](https://api.huanghaiwan.com/go/%E4%BB%99%E8%B7%AF%E6%B9%BE) | IEPL/IPLC + 港台原生 IP，¥10/月起，优惠码 xlw9 九折 |
| 多设备共享兜底 | [SS-ID](https://api.huanghaiwan.com/go/SS-ID) | IEPL 专线，¥20/100G 起，5 台设备 |

完整版（含高频疑问解答）见 [huanghaiwan.com](https://huanghaiwan.com/ai/deepseek-text-to-image-guide-2026/)。
