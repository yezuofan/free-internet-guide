> 本文最初发布于 [huanghaiwan.com](https://huanghaiwan.com/posts/client-setup-guide-2026/)

# 2026科学上网客户端下载安装配置全攻略

很多新手买好机场后卡在最后一步：订阅链接复制了，但不会导入客户端。这篇文章帮你解决这最后一公里。

## 快速选择表

| 客户端 | 平台 | 价格 | 难度 |
|:------|:----|:----|:----|
| **Clash Verge Rev** | Win/Mac/Linux | 免费 | ⭐⭐ |
| **Stash** | iOS/macOS | ¥88 | ⭐⭐ |
| **Shadowrocket** | iOS | $2.99 | ⭐ |
| **v2rayN** | Windows | 免费 | ⭐⭐⭐ |
| **FlClash** | Win/Mac/Android | 免费 | ⭐⭐ |

## Clash Verge Rev（全平台首选）

**下载：** GitHub Releases → 选对应平台的 `.dmg`/`.exe`/`.deb`

**配置：**
1. 打开 → 左侧"订阅"→ 添加 → 粘贴机场订阅链接 → 导入
2. 左侧"代理"→ 选一个节点 → 点击右上角开关
3. 点击"设置" → 开启"系统代理"

**功能：** 延迟测试、自动切换、规则分流，完全满足日常使用。

## Stash（iOS最佳）

**获取：** App Store 搜索（需外区 Apple ID），¥88 买断

**配置：**
1. 打开 → 底部"配置"→ "+"→ 通过 URL 下载 → 粘贴订阅链接
2. 返回首页 → 点击开关 → 允许 VPN 配置
3. 推荐使用"自动选择"策略组

## Shadowrocket（iOS轻量）

**获取：** App Store（外区 ID），$2.99

**配置：**
1. 右上角"+"→ 类型选 Subscribe → URL 处粘贴链接 → 完成
2. 首页选中节点 → 顶部开关 → 允许 VPN 配置
3. 设置 → 开启"全局路由"→ 加载远程规则

## v2rayN（Windows极客）

**获取：** GitHub Releases → 解压到纯英文路径

**配置：**
1. 服务器 → 订阅设置 → 输入订阅链接 → 更新订阅
2. 右键托盘图标 → 系统代理 → 开启代理
3. 设置 → 路由设置 → 预设选"绕过大陆"

## 快速对照

| 场景 | 推荐 |
|:----|:-----|
| Windows 新手 | Clash Verge Rev |
| macOS 新手 | Clash Verge Rev |
| iPhone/iPad | Stash 或 Shadowrocket |
| Android | Surfboard 或 FlClash |
| Linux | Clash Verge Rev |

## 常见问题

**Q：导入订阅后看不到节点？** → 订阅链接过期，回机场后台重新生成

**Q：开启代理后国内网站打不开？** → 设为"规则"模式，开启"绕过大陆"

**Q：所有节点超时？** → 检查网络本身是否正常，重启客户端试试

---

*详细图文版请访问 [huanghaiwan.com](https://huanghaiwan.com/posts/client-setup-guide-2026/)*
