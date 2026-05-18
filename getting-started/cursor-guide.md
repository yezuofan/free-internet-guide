# Cursor入门到精通：AI编程的正确姿势（2026教程）

> Cursor 是目前最火的 AI IDE，基于 VS Code 深度改造，内置 AI 对话、代码补全、多文件编辑等能力。本文从零开始，帮你把 Cursor 用到极致。

---

## 一句话结论

| 场景 | 推荐功能 | AI模型 |
|:----|:--------|:------|
| 日常写代码 | Tab 自动补全 | Cursor Tab |
| 改一段代码 | Ctrl+K 内联编辑 | Claude / GPT-4o |
| 写一个新功能 | Composer（Ctrl+I） | Claude Sonnet |
| 调试 Bug | Chat（Ctrl+L） | Claude Sonnet |
| 跨文件重构 | Composer Agent 模式 | Claude Sonnet |
| 批量代码审查 | Chat + @Files | Claude Sonnet |

**日常用 Tab 补全（最快），写功能用 Composer（最爽），调试用 Chat（最稳）。**

---

## 快速上手：3种使用方式

### 方式 1：Cursor Tab 自动补全（最强生产力）

安装 Cursor 后，写代码时会自动出现灰色提示，按 Tab 接受：

- **单行补全**：写一半自动预测下一段
- **多行补全**：写函数/方法时自动补完整块代码
- **上下文感知**：不仅看当前文件，还看你打开的其他文件

```python
# 写一个函数，Cursor 会自动补全
def fibonacci(n):
    # Cursor 会自动补全这个函数
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

**技巧**：换行后光标停在空白处，按 `Ctrl+Enter` 触发补全。

### 方式 2：Chat 对话（Ctrl+L）

按 `Ctrl+L` 打开对话面板，像 ChatGPT 一样和 AI 聊天讨论代码：

- 选中代码后按 `Ctrl+L` → 自动把选中代码发给 AI
- 可在对话中引用文件：输入 `@file` 选择文件
- 引用文档：输入 `@docs` 引入官方文档
- 引用 Web：输入 `@web` 联网搜索

**最佳实践：** 调试 Bug 时，选中报错代码 → `Ctrl+L` → "这个函数为什么会报 `IndexError`？"

### 方式 3：Composer（Ctrl+I）— 多文件编辑

Composer 是 Cursor 最强大的功能，可以同时编辑多个文件：

- **普通模式**：只改当前文件
- **Agent 模式（推荐）**：自动创建、修改、删除多个文件

```bash
# 用 Composer Agent 写一个 Express API
"创建一个 Express 后端，包含用户 CRUD 接口和 SQLite 数据库"
# Cursor 会自动创建：server.js, routes/, models/, db/ 等文件
```

---

## 核心功能详解

### 1. Tab 自动补全

| 功能 | 说明 | 快捷键 |
|:----|:-----|:------|
| Tab 补全 | 接受 AI 建议 | Tab |
| 拒绝建议 | 继续打字 | Esc |
| 换行触发生成 | 在新行等待 AI 建议 | Ctrl+Enter |
| 多行 Diff 预览 | 一次显示多行修改 | 自动 |

### 2. Ctrl+K 内联编辑

选中一段代码，按 `Ctrl+K` 输入指令，AI 直接修改选中代码：

```
选中代码 → Ctrl+K → "加错误处理" / "用async/await重写"
```

### 3. Chat（Ctrl+L）

| 功能 | 用法 |
|:----|:----|
| 代码审查 | 选中代码 → Ctrl+L → "审查这段代码" |
| 解释代码 | 选中代码 → Ctrl+L → "解释这段代码在做什么" |
| 添加测试 | 选中代码 → Ctrl+L → "为这个函数写 Jest 测试" |
| 引用文件 | @file + 文件名 → 文件内容进入上下文 |
| 引用 Web | @web + 搜索词 → 联网搜索最新文档 |

### 4. Composer Agent 模式

按 `Ctrl+I` 切换到 Agent 模式，可以实现：

- **创建新项目**：一句话生成完整项目结构
- **跨文件重构**：同时修改多个文件
- **添加功能**：在现有项目中加新功能
- **修复 Bug**：定位问题 → 修复 → 写测试

---

## 10 个实战 Prompt 模板（直接复制可用）

### 模板 1：创建 REST API
```
创建一个 Express.js REST API，包含：
- 用户 CRUD（GET/POST/PUT/DELETE）
- SQLite 数据库（用 better-sqlite3）
- JWT 认证
- 错误处理中间件
- 按功能拆分成 routes/ controllers/ models/ 目录结构
```

### 模板 2：写单元测试
```
为 src/utils/helpers.js 中的所有函数写 Jest 单元测试：
- 覆盖正常输入、边界值、错误输入
- 用 describe/it 组织
- Mock 外部依赖
- 测试覆盖率达到 90%+
- 添加测试覆盖率报告配置
```

### 模板 3：代码重构
```
重构这个函数：
- 拆分超过 50 行的函数
- 提取重复逻辑到公共函数
- 改用 TypeScript 类型
- 添加 JSDoc 注释
- 保持对外接口不变
```

### 模板 4：添加新功能
```
在现有项目中添加一个新功能：
- 用户可以通过邮箱重置密码
- 发送 6 位验证码到邮箱
- 验证码有效期 5 分钟
- 重置后强制重新登录
- 所有新旧密码不能相同
```

### 模板 5：性能优化
```
分析这段代码的性能瓶颈：
1. 找出 O(n²) 及以上复杂度的代码
2. 提出优化方案
3. 改为更高效的实现
4. 添加性能基准测试
5. 对比优化前后的执行时间
```

### 模板 6：数据库查询优化
```
优化这个 SQL 查询：
- 用 EXPLAIN ANALYZE 分析执行计划
- 建议需要添加的索引
- 重写 N+1 查询为 JOIN
- 添加查询缓存策略
- 标注修改前后的查询时间对比
```

### 模板 7：前端组件开发
```
用 React + TypeScript 创建一个数据表格组件：
- 支持排序（点击表头）
- 支持搜索过滤
- 支持分页（客户端）
- 支持行选中（多选）
- 列宽可拖动调整
- 导出为 CSV 功能
```

### 模板 8：Git Commit 信息生成
```
分析 git diff，生成规范化的 commit 信息：
- 遵循 Conventional Commits 格式
- 提取关键变更
- 分类型列出（feat/fix/refactor/docs）
- 每行不超过 72 字
```

### 模板 9：API 文档生成
```
为 server/routes/ 下的所有路由生成 API 文档：
- OpenAPI 3.0 格式
- 包含请求参数和响应格式
- 用 @openapi 标签标注
- 自动生成 markdown 文档
```

### 模板 10：Code Review 助手
```
审查这个 PR 的代码：
1. 安全漏洞（SQL注入/XSS/认证绕过）
2. 性能问题（N+1查询/内存泄漏）
3. 代码质量（重复/可读性/命名）
4. 测试覆盖（缺少的测试用例）
5. 架构问题（耦合度/扩展性）
按严重程度排序，每个问题附修改建议
```

---

## 7 个进阶技巧

### 1. @docs 引用文档
Cursor 可以引入第三方库的官方文档。输入 `@docs` 后选择「Add Docs」，粘贴文档 URL，Cursor 会自动抓取并索引。

**常用配置：**
- Next.js 官方文档
- React 文档
- Tailwind CSS 文档
- 你项目的内部文档

### 2. .cursorrules 规则文件
在项目根目录创建 `.cursorrules` 文件，定义 Cursor 的行为规则：

```
You are an expert in Node.js and TypeScript.
- Always use TypeScript with strict mode
- Use functional components in React
- Write unit tests for all new functions
- Keep functions under 30 lines
- Use async/await over Promises
```

### 3. 项目级别的上下文配置
`.cursorignore` 文件排除不需要索引的目录，提升 AI 响应质量：

```
node_modules/
dist/
build/
.git/
*.min.js
```

### 4. Cursor Tab 的 Cmd+K 内联编辑
选中一段代码 → `Cmd+K` → 输入修改指令，AI 直接修改代码，显示 Diff 对比。

**高级用法：** 选中代码后输入 "final" — Cursor 会把代码改为更完善的版本。

### 5. Chat History 复用
Cursor 保存所有对话历史。遇到类似问题时，可以直接引用之前的对话：

- `Ctrl+Shift+P` → "Chat: History" 查看历史
- 在对话中上箭头浏览历史消息
- 同一项目的相似问题可以复用之前的解决方案

### 6. Composer 的 Checkpoint 回退
Composer 每次修改都会自动创建 Checkpoint。如果修改出问题：

1. 在 Composer 面板中找到上一次 Checkpoint
2. 点击「Restore」回退
3. 所有文件瞬间回到修改前

**相当于 Composer 自动帮你做了 git stash。**

### 7. 多行 Cursor Tab + Vim 模式
Cursor 完全支持 VS Code 的 Vim 插件，可以同时使用 Vim 快捷键和 AI 补全：

- 正常模式（Normal Mode）：用 `hjkl` 移动
- 插入模式（Insert Mode）：AI 补全自动工作
- 可视化模式 + `Ctrl+K`：选中区域用 AI 编辑

---

## FAQ

### Q1: Cursor 免费吗？
Cursor 提供免费套餐（每月 2000 次 Tab 补全 + 50 次 Composer）。Pro 版 $20/月（无限 Tab + 500 Composer/月）。**个人开发免费版完全够用。**

### Q2: Cursor 和 Copilot 哪个好？
| 对比项 | Cursor | GitHub Copilot |
|:------|:------|:--------------|
| 自动补全 | ✅ 更强（多行 + 上下文） | ✅ 强 |
| 多文件编辑 | ✅ Composer Agent | ❌ 不支持 |
| 对话能力 | ✅ 内置 Chat | ✅ Chat 面板 |
| AI 模型 | Claude / GPT-4o 可选 | OpenAI 系列 |
| 免费额度 | 2000 Tab + 50 Composer | 有限使用 |

**结论：** Cursor 在多文件编辑和模型选择上更灵活，Copilot 胜在和 GitHub 生态深度集成。

### Q3: Cursor 支持哪些语言？
所有主流语言都支持。Python、JavaScript/TypeScript、Java、Go、Rust、C++ 等表现最好。

### Q4: 用 Cursor 需要好的网络连接吗？
Cursor 需要访问海外 AI 服务（Claude、GPT-4o）。国内用户需要稳定的网络工具来连接 AI API：

| 方案 | 推荐指数 | 月费 | 说明 |
|:----|:-------:|:----|:-----|
| 网络工具（低延迟） | ⭐⭐⭐⭐⭐ | ~¥20-30 | 稳定连接 Cursor 服务，香港节点延迟最低 |
| API 中转 | ⭐⭐⭐ | ¥15-50/按量 | 技术门槛高，不适合新手 |

**推荐网络工具：** 需要稳定、低延迟的网络工具来保证 Cursor 的正常使用。👉 [点击查看推荐的网络工具 →](https://hongxingyun.club/web/#/register?code=OBEi3O69)

### Q5: Cursor 支持远程开发吗？
支持。Cursor 完美兼容 VS Code 的 Remote SSH 和 Dev Containers 插件。本地运行 Cursor，代码在远程服务器，体验和本地完全一致。

### Q6: Cursor 会泄露我的代码吗？
Cursor 的隐私政策允许使用代码训练模型（默认开启）。可以在 Settings → Privacy 中关闭「Improve Cursor with usage data」。**涉及商业项目建议关闭。**

---

## 优缺点总结

### ✅ 优点

| 优点 | 说明 |
|:----|:-----|
| 多文件编辑能力强 | Composer Agent 模式是目前最好的多文件 AI 编辑体验 |
| 模型选择自由 | 可切换 Claude Sonnet、GPT-4o，各取所长 |
| Tab 补全质量高 | 上下文理解准确，多行补全很少出错 |
| VS Code 生态 | 插件、主题、快捷键全部兼容，零迁移成本 |
| 代码审查效率高 | Chat + @Files 可以快速理解完整项目 |

### ❌ 缺点

| 缺点 | 说明 |
|:----|:-----|
| 价格偏贵 | Pro $20/月，相比 Copilot $10/月贵一倍 |
| 需要海外网络 | 国内直连延迟高，需要配合网络工具 |
| 偶尔幻觉 | Composer 改多文件时可能引入不存在的 API |
| 长期使用内存高 | 运行一整天后占 2-3GB 内存 |
| 企业支持弱 | 相比 Copilot 的企业管理功能差距明显 |

---

## 写在最后

Cursor 是目前个人开发者最佳的 AI 编程工具。Tab 补全 + Composer Agent 组合让日常开发效率提升 2-3 倍。

**一句话建议：** 免费版先用起来，Tab 补全和 Chat 体验远超 Copilot。Pro 版等你确认自己需要 Composer Agent 的批量编辑能力再升级。

---

*本文包含推广链接，如果你通过链接注册，我们可能会获得少量佣金，但这不影响我们的评分和推荐。*