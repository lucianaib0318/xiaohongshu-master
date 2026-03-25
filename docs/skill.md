---
name: xhs-note-creator
description: 小红书笔记素材创作技能。功能：撰写笔记内容 + 生成图片卡片 + 发布笔记。触发词：小红书笔记、小红书素材、xhs 笔记、笔记卡片、生成封面、排版设计、发布小红书
dependency:
  python:
    - markdown>=3.4.0
    - PyYAML>=6.0
    - playwright>=1.40.0
    - xhs>=0.4.0
    - python-dotenv>=1.0.0
  system:
    - "if [ ! -f .env ]; then touch .env; fi"
---

# 小红书笔记创作技能

## 1. 目标是什么

根据用户提供的资料或主题，创作完整的小红书笔记素材：
- ✍️ 撰写符合小红书风格的笔记正文（标题 + 正文 + Tags）
- 🎨 生成精美的图片卡片（封面 + 正文卡片）
- 📤 可选：直接发布到小红书

**最终交付**：可直接发布的笔记文案 + 3-5 张精美图片卡片

---

## 2. 什么情况下触发

用户提到以下需求时触发：

| 触发词 | 示例 |
|--------|------|
| 小红书笔记 | 「帮我写一篇小红书笔记」 |
| 小红书素材 | 「生成小红书素材」 |
| xhs 笔记 | 「xhs 笔记怎么写」 |
| 笔记卡片 | 「做个笔记卡片」 |
| 生成封面 | 「生成个封面图」 |
| 排版设计 | 「排版好看点」 |
| 发布小红书 | 「发布到小红书」 |

---

## 3. 什么情况下不要触发

- ❌ 用户只问小红书运营知识（不创作内容）
- ❌ 用户要写公众号/知乎/抖音（其他平台）
- ❌ 用户只要纯文字稿（不要图片卡片）
- ❌ 用户没有明确说「小红书」相关

**处理**：礼貌说明这是小红书专用技能，询问是否需要。

---

## 4. 开始前先收集什么信息

### 必需信息

| 信息 | 用途 | 缺失时处理 |
|------|------|------------|
| 笔记主题 | 确定内容方向 | 追问：「你想写什么主题？」 |
| 目标受众 | 调整语言风格 | 默认：18-35 岁女性 |
| 核心卖点 | 突出内容亮点 | 追问：「最想强调什么？」 |

### 可选信息

| 信息 | 用途 | 缺失时处理 |
|------|------|------------|
| 参考素材 | 提高准确性 | 没有则自行创作 |
| 字数要求 | 控制内容长度 | 默认：300-600 字 |
| 主题风格 | 选择卡片主题 | 默认：根据内容推荐 |

### 信息收集示例

```
用户：帮我写一篇小红书笔记

你：好的！需要确认几个问题：
1. 你想写什么主题？（如：好物推荐/教程/种草）
2. 目标受众是谁？（如：学生党/职场人/宝妈）
3. 最想强调的卖点是什么？

你：收到！我推荐用「playful-geometric」主题，活泼吸睛，适合好物推荐。确认吗？
```

---

## 5. 按什么顺序干活

### 步骤 1：撰写笔记正文（发布用）

**输出格式**：

```markdown
标题：[不超过 20 字，吸睛]

正文：
[小红书风格文案，段落清晰，适量 Emoji]

[5-10 个 SEO Tags]
```

**决策分支**：

- 如果用户提供了详细资料 → 提炼核心信息，转化为小红书风格
- 如果用户只给主题 → 自行创作，确保信息准确
- 如果内容涉及专业领域（医疗/法律/金融）→ 添加「仅供参考」提示

**示例**：

```
标题：3 个 AI 写作神器！打工人必备🔥

正文：
家人们！今天分享 3 个超好用的 AI 写作工具，亲测有效！

📝 工具一：Jasper
- 全能型 AI 写作助手
- 支持博客、邮件、广告文案
💰 价格：$39/月起

⚡ 工具二：Copy.ai
- 专注营销文案
- 一键生成产品描述
💰 价格：免费版可用

#AI 写作 #效率工具 #打工人 #自媒体 #文案工具
```

---

### 步骤 2：生成渲染用 Markdown（卡片用）

**重要**：此 Markdown 专用于生成图片卡片，格式与笔记正文不同！

**输出格式**：

```markdown
---
emoji: "🚀"
title: "大标题"
subtitle: "副标题"
---

# 一级标题

> 引用内容

## 二级标题

- 列表项
- 列表项

---

# 下一页
```

**决策分支**：

- 如果内容<300 字 → 用 `auto-fit` 模式，单页填满
- 如果内容 300-600 字 → 用 `auto-split` 模式，自动切分
- 如果内容>600 字 → 用 `separator` 模式，手动分页
- 如果内容类型不确定 → 用 `dynamic` 模式，动态高度

**主题选择**：

| 内容类型 | 推荐主题 | 命令 |
|----------|----------|------|
| 知识干货 | `professional` | `-t professional` |
| 好物推荐 | `playful-geometric` | `-t playful-geometric` |
| 生活美食 | `botanical` | `-t botanical` |
| 技术编程 | `terminal` | `-t terminal` |
| 不确定 | `default` | `-t default` |

**需要参考格式时**：读取 `references/markdown-template.md`

**完整示例**：读取 `references/output-example.md`

---

### 步骤 3：渲染图片卡片

**执行命令**：

```bash
cd /root/.openclaw/workspace/skills/xhs-note-creator
python scripts/render_xhs.py <markdown 文件> -t <主题> -m <模式> -o <输出目录>
```

**输出文件**：

```
<输出目录>/
├── cover.png      # 封面图（1080x1440）
├── card_1.png     # 正文卡片 1
├── card_2.png     # 正文卡片 2
└── ...
```

**决策分支**：

- 如果渲染失败 → 检查 Markdown 格式，确保 YAML 头部正确
- 如果图片模糊 → 增加 `--dpr 3` 参数提高清晰度
- 如果文字溢出 → 改用 `auto-fit` 或 `auto-split` 模式
- 如果卡片太多（>6 张）→ 建议精简内容或分多篇笔记

**常用命令**：

```bash
# 万能组合（不知道选啥时用）
python scripts/render_xhs.py content.md -t default -m auto-split -o ./output

# 好物推荐（活泼吸睛）
python scripts/render_xhs.py content.md -t playful-geometric -m dynamic -o ./output

# 知识干货（专业感）
python scripts/render_xhs.py content.md -t professional -m separator -o ./output

# 技术内容（极客风）
python scripts/render_xhs.py content.md -t terminal -m auto-split -o ./output
```

**需要选主题时**：读取 `references/theme-guide.md`

---

### 步骤 4：发布小红书笔记（可选）

**前置条件检查**：

1. 检查 `.env` 文件是否存在
2. 检查 `XHS_COOKIE` 是否已配置
3. 如果未配置 → 指导用户获取 Cookie

**执行命令**：

```bash
cd /root/.openclaw/workspace/skills/xhs-note-creator
python scripts/publish_xhs.py --title "笔记标题" --desc "笔记描述" --images cover.png card_1.png card_2.png
```

**决策分支**：

- 如果发布成功 → 返回笔记链接，记录到日志
- 如果 Cookie 过期 → 指导用户重新获取 Cookie
- 如果图片太大 → 压缩图片后重试
- 如果网络错误 → 重试 3 次，仍失败则提示手动发布

**Cookie 获取指引**：

```
1. 浏览器登录小红书（https://www.xiaohongshu.com）
2. 按 F12 打开开发者工具
3. Network 标签刷新页面
4. 复制请求头中的 Cookie 字符串
5. 填入 .env 文件：XHS_COOKIE=你的 cookie
```

---

## 6. 输出必须长什么样

### 交付清单

| 文件 | 格式 | 说明 |
|------|------|------|
| 笔记正文 | Markdown | 可直接复制发布 |
| 封面图 | PNG | 1080x1440px |
| 正文卡片 | PNG | 1080x1440px（3-5 张） |
| 渲染用 Markdown | MD | 可重复修改渲染 |

### 质量标准

| 检查项 | 标准 | 验证方法 |
|--------|------|----------|
| 标题长度 | ≤20 字 | 数字符 |
| Tags 数量 | 5-10 个 | 数个数 |
| 卡片数量 | 3-6 张 | 数文件 |
| 图片尺寸 | 1080x1440 | 查看属性 |
| 文字清晰 | 无溢出/截断 | 目视检查 |
| 主题匹配 | 符合内容调性 | 主观判断 |

---

## 7. 做到什么程度算完成

**完成标准**（全部满足）：

- ✅ 笔记正文撰写完成（标题 + 正文+Tags）
- ✅ 渲染用 Markdown 生成完成（YAML 头部 + 格式化内容）
- ✅ 图片卡片渲染完成（封面 + 至少 2 张正文卡片）
- ✅ 所有文件保存到输出目录
- ✅ 向用户交付完整文件清单

**可选完成**：

- ⭕ 笔记已发布到小红书（需 Cookie 配置）
- ⭕ 额外生成了变体版本（不同主题/文案）

**示例交付**：

```
✅ 完成！已生成以下文件：

📝 笔记正文（可直接发布）：
标题：3 个 AI 写作神器！打工人必备🔥
正文：[已生成，含 8 个 Tags]

🎨 图片卡片（4 张）：
- cover.png（封面）
- card_1.png（Jasper 介绍）
- card_2.png（Copy.ai 介绍）
- card_3.png（Notion AI 介绍）

📂 文件位置：/root/.openclaw/workspace/skills/xhs-note-creator/output/

需要我帮你发布到小红书吗？（需配置 Cookie）
```

---

## 8. 搞不定的时候怎么处理

### 常见问题处理

| 问题 | 原因 | 解决方法 |
|------|------|----------|
| 渲染失败 | Markdown 格式错误 | 检查 YAML 头部，确保 `---` 成对 |
| 图片模糊 | DPR 太低 | 加 `--dpr 3` 参数 |
| 文字溢出 | 字数太多 | 改用 `auto-split` 或精简内容 |
| 主题不好看 | 主题不匹配 | 换主题，参考 `theme-guide.md` |
| 发布失败 | Cookie 过期 | 重新获取 Cookie |
| 网络错误 | 代理/防火墙 | 检查网络，重试 3 次 |

### 升级处理

以下情况请求人工确认：

- 涉及敏感话题（医疗建议/投资理财/法律意见）
- 用户要求批量生成（>10 篇笔记）
- 需要调用外部 API（用户未授权）
- 连续失败 3 次以上

### 降级处理

以下情况简化输出：

- 用户只要文案 → 跳过图片渲染
- 用户只要封面 → 只生成 cover.png
- 时间紧迫 → 用默认主题 + 自动分页

---

## 9. 什么时候去读参考文件

| 场景 | 读取文件 | 用途 |
|------|----------|------|
| 不确定 Markdown 格式 | `references/markdown-template.md` | 查看完整模板 |
| 需要输入输出示例 | `references/output-example.md` | 参考完整案例 |
| 不知道选哪个主题 | `references/theme-guide.md` | 根据内容选主题 |
| 用户问主题区别 | `references/theme-guide.md` | 解释各主题特点 |
| 分页模式选择困难 | `references/theme-guide.md` | 根据字数选模式 |

**读取示例**：

```
用户：这个 Markdown 怎么写？

你：我查一下模板...（读取 references/markdown-template.md）

你：格式是这样的：
1. YAML 头部（emoji、title、subtitle）
2. 用 # 写一级标题
3. 用 --- 分页
...
```

---

## 技能资源

### 脚本文件

- `scripts/render_xhs.py` - 图片渲染脚本
- `scripts/publish_xhs.py` - 小红书发布脚本

### 资源文件

- `assets/cover.html` - 封面 HTML 模板
- `assets/card.html` - 正文卡片 HTML 模板
- `assets/themes/*.css` - 8 种主题样式

### 参考文件

- `references/markdown-template.md` - Markdown 格式模板
- `references/output-example.md` - 完整输入输出示例
- `references/theme-guide.md` - 主题选择指南

---

## 快速上手

```bash
# 1. 准备 Markdown 文件
cat > content.md << EOF
---
emoji: "🚀"
title: "我的标题"
subtitle: "副标题"
---

# 内容页 1

...

---

# 内容页 2

...
EOF

# 2. 渲染图片
python scripts/render_xhs.py content.md -t default -m auto-split -o ./output

# 3. 查看结果
ls -la ./output/
```
