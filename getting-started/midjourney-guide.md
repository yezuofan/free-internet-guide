# Midjourney 生图教程：2026年最新入门到精通指南

> Midjourney 是目前公认**审美最好的AI生图工具**。我用它做电商产品图、活动海报、社交媒体配图已经一年多了，这篇文章把我踩过的坑和实战经验全写下来。
>
> **读完你会知道：** 怎么注册、怎么选套餐、提示词怎么写才能出好图、哪些参数值得调。

---

## 一句话总结（不想看全文的看这里）

| 需求 | 推荐方式 | 月费 | 难度 | 我的推荐 |
|:----|:--------|:----|:---:|:-------:|
| 偶尔玩玩 | Discord免费版 | 免费（限25次） | ⭐⭐ | ✅ 先试试水 |
| 日常做图 | Discord Standard | $10/月（200张） | ⭐⭐ | ✅ 性价比之王 |
| 重度创作 | Discord Pro | $30/月（不限量） | ⭐⭐ | ✅ 专业玩家 |
| Web界面 | Web + Standard | $10-$30/月 | ⭐ | ✅ 新手最推荐 |

**最省心方案：** Web版界面（免去学习Discord的成本）+ Standard套餐的性价比组合，配合一个稳定机场，每月花费不超过 ¥60。

---

## 一、Midjourney 是什么？

简单说，Midjourney 是一个**用文字生成图片的AI工具**。你输入一句话（提示词），它能生成4张风格各异的图片。

### 它厉害在哪？

| 维度 | Midjourney | 其他工具（DALL·E / Stable Diffusion） |
|:----|:----------|:-----------------------------------|
| **审美** | 公认最强，画面精美 | 写实但缺乏艺术感 |
| **风格** | 油画/插画/3D渲染/概念设计都很强 | 偏写实，风格单一 |
| **一致性** | V6版本人物/场景一致性明显提升 | 每次生成差异大 |
| **上手难度** | 需要学提示词写法 | 更简单但上限低 |
| **应用场景** | 电商图/海报/游戏原画/室内设计 | 日常创作/教育内容 |

**如果你想要"好看"的结果，Midjourney 目前没有对手。**

### 前期准备

使用 Midjourney 需要两步准备：

1. **一个 Discord 账号** — 因为 Midjourney 最早就是基于 Discord 的（Web版2025年才推出）
2. **一个网络工具** — Midjourney 官网和 Discord 国内都无法直接访问

网络工具这东西，不需要多贵。月付十几块的就行，只要能稳定连香港节点就好：

| 机场 | 月费 | 连Discord/Midjourney体验 | 
|:----|:----|:------------------------|
| 龙猫云 | ¥15起(100G) | 香港IPLC专线，延迟<20ms，刷图秒出 |
| 万达云 | ¥16.8起(150G) | 香港IEPL专线，稳定不丢包 |
| WgetCloud | ¥89起(280G) | 精品线路，适合重度创作用户 |

[👉 龙猫云官网 →](https://inv06.lmaff01.cc/register?aff=dqNRmvru)
[👉 万达云官网 →](https://link.wdyserver.com/register?code=6z6PNS5r)
[👉 WgetCloud官网 →](https://wgetcloud.com/web/#/register?code=djq10H)

> **新手建议：** 先买一个月的龙猫云(¥15)试试，够你刷几百张图了。觉得好用再升级。

---

## 二、方案一：通过 Discord 使用（官方最全功能）

这是 Midjourney 最传统的使用方式，**功能最完整**，但需要学会操作 Discord。

### 注册 Discord

1. 打开 discord.com，点击注册（需要网络工具）
2. 输入邮箱、用户名、密码
3. 验证邮箱
4. 创建或加入一个服务器

### 加入 Midjourney 服务器

1. 访问 [Midjourney 官网](https://www.midjourney.com)（需要网络工具）
2. 点击 "Join the Beta" 或 "Sign Up"
3. 跳转到 Discord，自动加入 Midjourney 服务器
4. 在左侧频道列表找到 `#newbies-*` 开头的频道（新手频道）

### 第一次生图

在频道输入框输入：

```
/imagine prompt: a serene Japanese garden in spring, cherry blossoms, koi pond, digital art --ar 16:9
```

等待约30-60秒，Bot 会返回4张图，下面有 U（放大）和 V（变体）按钮：
- **U1-U4**：选择某一张放大（Upscale）
- **V1-V4**：选择某一张生成变体（Variation）
- **🔄**：重新生成

### Discord版优缺点

| 优点 | 缺点 |
|:----|:----|
| ✅ 功能最全，所有参数都支持 | ❌ 需要学 Discord 操作，有门槛 |
| ✅ 社区活跃，可以看到别人的提示词 | ❌ 出图在公屏，隐私性差 |
| ✅ Bot 私信可以自己用（隐私模式） | ❌ **必须用网络工具**，连接要稳定 |
| ✅ 更新最快，新功能先上 | ❌ 手机端操作不太方便 |

---

## 三、方案二：通过 Web 界面使用（推荐新手）

2025年 Midjourney 终于推出了**独立 Web 界面**，不用再通过 Discord 操作了。界面更直观，体验更像普通的在线工具。

### 怎么用

1. 打开 [Midjourney Web](https://www.midjourney.com/imagine)（需要网络工具）
2. 用 Discord 账号或 Google 账号登录
3. 直接在输入框写提示词，点击生成
4. 结果在右侧展示，点击即可放大或编辑

### Web版优势

- **不用学 Discord** — 打开即用
- **界面美观** — 专门为生图设计的UI
- **图片管理** — 所有生成图在个人页面统一管理
- **图库浏览** — 可以看到社区优秀作品和提示词
- **编辑方便** — 可以直接对图片进行局部修改、扩图等操作

### 注意

Web 版也需要订阅才能使用，只是多了一个更友好的操作界面。

---

## 四、方案对比总结

| 维度 | Discord版 | Web版 |
|:----|:---------|:------|
| 上手难度 | ⭐⭐ 需要学Discord | ⭐ 几分钟上手 |
| 功能完整度 | ⭐⭐⭐⭐⭐ 全功能 | ⭐⭐⭐⭐ 差一些高级参数 |
| 隐私性 | ⭐⭐ 公频出图 | ⭐⭐⭐⭐⭐ 个人空间 |
| 社区氛围 | ⭐⭐⭐⭐⭐ 活跃 | ⭐⭐⭐ 成熟中 |
| 推荐人群 | 重度创作/想学社区技巧 | 新手/日常使用 |

**我的建议：** 入门先用 Web 版，等熟悉了提示词写作后再去 Discord 挖一挖社区优秀作品灵感。

---

## 五、提示词（Prompt）写作指南

这是最核心的部分——**好提示词 = 好图片**。

### 基础公式

```
[主体] + [动作/状态] + [环境/背景] + [风格/媒介] + [光线/色彩] + [参数]
```

**例子：**

```
/imagine prompt: a calico cat wearing a wizard hat, sitting on a stack of ancient spellbooks, dimly lit library with floating candles, oil painting style, dramatic lighting --ar 16:9 --v 6
```

| 部分 | 内容 | 作用 |
|:----|:----|:----|
| 主体 | a calico cat wearing a wizard hat | 核心内容 |
| 动作 | sitting on a stack of ancient spellbooks | 姿态 |
| 环境 | dimly lit library with floating candles | 氛围 |
| 风格 | oil painting style | 艺术风格 |
| 光线 | dramatic lighting | 光影 |
| 参数 | `--ar 16:9 --v 6` | 比例/版本 |

### 常用参数

| 参数 | 用法 | 效果 |
|:----|:----|:----|
| `--ar` | `--ar 16:9` / `--ar 1:1` | 画面比例 |
| `--v` | `--v 6` / `--v 5.2` | 使用哪个版本（默认V6） |
| `--s` | `--s 100` (0-1000) | 风格化程度，越高越艺术 |
| `--c` | `--c 50` (0-100) | 多样性，越高变化越大 |
| `--no` | `--no text, watermark` | 排除不需要的元素 |
| `--iw` | `--iw 2` (0.5-2) | 垫图权重 |
| `--stylize` | `--stylize 250` (0-1000) | 同上 `--s` |
| `--chaos` | `--chaos 50` (0-100) | 同上 `--c` |
| `--tile` | `--tile` | 生成可平铺图案 |

### 实战提示词模板

**电商产品图：**
```
/imagine prompt: minimalist ceramic coffee cup on marble surface, soft natural lighting from left, clean white background, product photography style, 8K detail, shallow depth of field --ar 4:3 --v 6
```

**社交媒体海报：**
```
/imagine prompt: futuristic city skyline at sunset, neon lights reflecting on wet streets, cyberpunk aesthetic, cinematic composition, rich warm colors --ar 9:16 --v 6
```

**头像/角色设计：**
```
/imagine prompt: anime-style warrior girl with long silver hair, blue eyes, wearing white and blue samurai armor, cherry blossom background, detailed character design, vibrant colors --ar 3:4 --v 6
```

---

## 六、常见问题（FAQ）

### Q1：Midjourney 国内能用吗？

可以。**只需要两个前置条件：**
1. 一个 Discord 账号（免费注册）
2. 一个网络工具连接境外网络

我这里列出了几个经过验证的稳定机场，月付十几块就能满足需求。

### Q2：免费能用吗？

可以。注册后系统赠送 **25次免费生成**。用完后需要订阅。

### Q3：哪个套餐最划算？

| 套餐 | 月费 | 月生成量 | 适合人群 |
|:----|:----|:--------|:--------|
| Free | 免费 | 25次 | 尝鲜 |
| Standard | $10/月 | 200张（约¥0.36/张） | ✅ **性价比最高** |
| Pro | $30/月 | 不限量 | 专业/重度用户 |
| Max | $60/月 | 不限量 + 最快速 | 商业用途 |

**Standard 套餐最推荐**——200张/月对大多数人来说绰绰有余。

### Q4：生成的图能商用吗？

可以。Midjourney 的付费用户拥有生成图片的**商业使用权**。但需要注意：如果你的作品在Midjourney社区公开，别人也可以生成类似的图。

### Q5：手机能用吗？

可以。Discord 有手机App，但生图体验不如电脑。Web版对移动端支持一般，还是推荐在电脑浏览器上用。

### Q6：提示词有中文版吗？

Midjourney 目前**只支持英文提示词**。不过你可以：
- 用翻译工具写中文提示词后翻译成英文
- 或者用 Claude/ChatGPT 帮你写提示词（推荐）

### Q7：Midjourney V6 比 V5 强在哪？

V6 的主要改进：
- **更懂自然语言** — 可以写更口语化的提示词
- **人物一致性** — 同一提示词生成的人物更像
- **文字渲染** — 开始能在图里生成有意义的文字
- **细节质量** — 手部/眼睛等细节明显更好

### Q8：生图太慢怎么办？

慢的两个主要原因：
1. 你用的是免费额度（优先权低）→ 订阅即可
2. 网络连接不稳定 → 换一个延迟低的机场

---

## 七、最后说两句

Midjourney 是我用过**最容易出片的AI生图工具**。它的审美上限很高，即使你完全不懂设计，只要愿意花时间琢磨提示词，也能做出让人眼前一亮的作品。

**给新手的3条建议：**
1. **别上来就写复杂提示词** — 先试 `cat --ar 1:1`，看看效果，再一点点加内容
2. **多看社区优秀作品** — 点开别人作品可以看到完整提示词，是最好的学习素材
3. **参数一个一个试** — 一次只改一个参数，才能知道哪个参数起了什么作用

如果你还没注册，不妨从这个月开始试试。花十几块买一个月的网络工具 + $10订阅Midjourney，这个组合够你玩一整个月了。

[👉 龙猫云官网 →](https://inv06.lmaff01.cc/register?aff=dqNRmvru)
[👉 万达云官网 →](https://link.wdyserver.com/register?code=6z6PNS5r)
[👉 WgetCloud官网 →](https://wgetcloud.com/web/#/register?code=djq10H)

---

*本文包含推广链接。作者基于真实使用体验撰写，推荐不影响你的选择或使用成本。*

---
*本文最初发布于 [huanghaiwan.com](https://huanghaiwan.com/ai/midjourney-guide/)*
