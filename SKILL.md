# 小红书生成大师 - Xiaohongshu Master

📕 **一站式小红书内容创作工具**

生成爆款文案 + 热点词库 + 违禁词检测 + 13 种风格封面卡片渲染

---

## 核心功能

| 功能 | 描述 | 状态 |
|------|------|------|
| **爆款帖子生成** | 基于主题生成完整笔记方案（标题 + 正文 + 标签 + 互动 + CTA） | ✅ |
| **热点词库生成** | 生成热搜词、长尾词、标题改造方案 | ✅ |
| **违禁词检测** | 三级风险扫描，提供替换建议 | ✅ |
| **封面卡片渲染** | 13 种精美排版主题，生成 1080x1440 图片 | ✅ |

---

## 命令使用

### 基础命令格式

```bash
python3 xiaohongshu.py <command> [options] [input]
```

---

## 子命令详解

### 1. `post` - 生成爆款帖子

基于输入主题生成完整的小红书笔记方案。

```bash
python3 xiaohongshu.py post <主题>
```

**示例：**
```bash
python3 xiaohongshu.py post 学渣逆袭
python3 xiaohongshu.py post 油痘肌护肤
python3 xiaohongshu.py post 通勤穿搭
python3 xiaohongshu.py post AI 工具
```

**输出内容：**
- 📌 **标题**：2 个 emoji + 数据化结论 + 获得感承诺（≤20 字）
- 📝 **正文**：共鸣描述 + 分点说明 + 激励语句（可直接发布）
- 💬 **互动问题**：3 种类型各 1 条（经验/观点/资源）
- 📣 **CTA 策略**：1 硬 1 软引导
- 🏷️ **话题标签**：5 个标签（基础 + 长尾 + 热点）

---

### 2. `keywords` - 生成热点词库

基于输入主题生成 SEO 优化词库。

```bash
python3 xiaohongshu.py keywords <主题>
```

**示例：**
```bash
python3 xiaohongshu.py keywords 通勤穿搭
python3 xiaohongshu.py keywords 学生党护肤
python3 xiaohongshu.py keywords 居家健身
```

**输出内容：**
- 🔥 **热搜词库**：平台热词 + 搜索增长率
- 🌿 **长尾词库**：人群 + 场景 + 需求组合
- 💡 **标题改造**：3 种差异化方案

---

### 3. `check` - 违禁词检测

扫描文本中的违规词，提供替换建议。

```bash
python3 xiaohongshu.py check "<文本内容>"
```

**示例：**
```bash
python3 xiaohongshu.py check "这款面膜全网销量第一，7 天淡化所有皱纹"
python3 xiaohongshu.py check "医院皮肤科都在用，根治痘痘"
```

**输出内容：**
- 🚨 **违规词高亮**：标注问题词汇
- 📋 **违规类型**：引用政策条款
- 💡 **替换建议**：合规表达方案
- 📊 **风险等级**：🔴红色 / 🟡黄色 / 🟢绿色

---

### 4. `render` - 渲染封面卡片（新增）

使用 Playwright 渲染 13 种风格的封面卡片。

```bash
python3 scripts/render_xhs.py <markdown 文件> [选项]
```

**基本用法：**
```bash
# 使用默认孟菲斯风格
python3 scripts/render_xhs.py examples/tool-recommendation.md -t memphis -o ./output

# 使用酸性设计风格
python3 scripts/render_xhs.py examples/tool-recommendation.md -t acid -o ./output

# 使用蒸汽波风格
python3 scripts/render_xhs.py examples/tool-recommendation.md -t vaporwave -o ./output
```

**命令行选项：**
```
必选参数:
  markdown_file         Markdown 文件路径

可选参数:
  -t, --theme           排版主题（默认：memphis）
                        可选：memphis/acid/vaporwave/minimalist/glitch/
                        chinese/glassmorphism/bauhaus/pop-art/
                        art-nouveau/collage/new-ugly/brutalism
  -m, --mode            分页模式（默认：separator）
                        可选：separator/auto-fit/auto-split/dynamic
  -o, --output-dir      输出目录（默认：当前目录）
  -w, --width           图片宽度（默认：1080）
  --height              图片高度（默认：1440）
```

**输出文件：**
```
output/
├── cover.png      # 封面图（1080x1440）
├── card_1.png     # 正文卡片 1
├── card_2.png     # 正文卡片 2
└── ...            # 更多卡片（根据内容分页）
```

---

## 13 种主题风格

| 主题代码 | 风格名称 | 适用场景 |
|----------|----------|----------|
| `memphis` | 孟菲斯 | 好物推荐/种草 |
| `acid` | 酸性设计 | 技术编程/数码 |
| `vaporwave` | 蒸汽波 | 生活美食/旅行 |
| `minimalist` | 极简主义 | 知识干货/职场 |
| `glitch` | 故障艺术 | 科技/游戏/数码 |
| `chinese` | 中国风 | 传统文化/国风 |
| `glassmorphism` | 毛玻璃 | 美妆穿搭/护肤 |
| `bauhaus` | 包豪斯 | 设计/建筑/艺术 |
| `pop-art` | 波普艺术 | 时尚/潮流 |
| `art-nouveau` | 新艺术运动 | 艺术/花卉/手作 |
| `collage` | 拼贴艺术 | 创意/手作/旅行 |
| `new-ugly` | 新丑风格 | 个性表达/实验 |
| `brutalism` | 粗野主义 | 极简/工业风 |

**一键测试所有风格：**
```bash
for theme in memphis acid vaporwave minimalist glitch chinese glassmorphism bauhaus pop-art art-nouveau collage new-ugly brutalism; do
  python3 scripts/render_xhs.py examples/tool-recommendation.md -t $theme -o "./output/$theme"
done
```

---

## Markdown 文件格式

渲染封面卡片需要使用特定格式的 Markdown 文件：

```markdown
---
emoji: "🚀"
title: "5 个效率神器"
subtitle: "打工人必备，效率翻倍"
---

# 📝 神器一：Notion

> 全能型笔记工具，支持数据库、看板、日历

## 核心功能

- 数据库视图（表格/看板/日历）
- 双向链接 + 知识图谱
- AI 智能助手集成

---

# ⚡ 神器二：Raycast

快捷键呼出的效率工具，替代 Spotlight。

## 推荐理由

- 启动速度快（<100ms）
- 插件生态丰富
- 原生 Mac 体验
```

**详细说明**：[docs/markdown-format.md](docs/markdown-format.md)

---

## 安装与依赖

### 系统要求

- Python 3.8+
- Node.js 16+（Playwright 依赖）

### 安装步骤

```bash
# 1. 克隆项目
git clone https://github.com/lucianaib0318/xiaohongshu-master.git
cd xiaohongshu-master

# 2. 安装 Python 依赖
pip install -r requirements.txt

# 3. 安装 Playwright 浏览器
playwright install chromium
```

### 依赖说明

| 依赖 | 用途 | 必需 |
|------|------|------|
| `playwright>=1.40.0` | 浏览器渲染（图片生成） | 渲染功能必需 |
| `pyyaml>=6.0` | YAML 解析（Markdown 头部） | 渲染功能必需 |

> 💡 **注意**：文案生成功能（post/keywords/check）无需外部依赖，纯 Python 标准库即可运行。

---

## 文件结构

```
xiaohongshu-master/
│
├── 📄 核心文件
│   ├── SKILL.md               # 技能说明（本文件）
│   ├── README.md              # 项目详细说明
│   ├── LICENSE                # MIT 许可证
│   ├── .gitignore            # Git 忽略文件
│   ├── requirements.txt      # Python 依赖
│   ├── xiaohongshu.py        # 主程序（文案生成）
│   └── run.sh                # 快速启动脚本
│
├── 📦 文案生成模块
│   ├── templates/
│   │   ├── post_templates.json   # 帖子模板
│   │   └── banned_words.json     # 违禁词库
│   └── examples/
│       ├── post_example.md       # 帖子生成示例
│       ├── keywords_example.md   # 词库生成示例
│       └── check_example.md      # 违禁词检测示例
│
├── 🎨 图片渲染模块
│   ├── scripts/
│   │   └── render_xhs.py         # 封面卡片渲染脚本
│   ├── assets/
│   │   ├── cover.html            # 封面 HTML 模板
│   │   ├── card.html             # 卡片 HTML 模板
│   │   ├── styles.css            # 通用样式
│   │   └── themes/               # 13 种主题 CSS
│   ├── docs/
│   │   ├── markdown-format.md    # Markdown 格式规范
│   │   └── theme-guide.md        # 主题风格指南
│   └── examples/
│       ├── tool-recommendation.md    # 工具推荐示例
│       └── tutorial-guide.md         # 教程指南示例
│
└── 🧪 测试
    └── tests/
        └── test_basic.py         # 基础测试
```

---

## 输出规范

### post 命令输出标准

| 元素 | 规范 | 示例 |
|------|------|------|
| 标题 | 2 个 emoji + 数据化结论 + 获得感（≤20 字） | `💥🔥用学霸不敢说的 3 个野路子｜学渣逆袭真不难` |
| 正文 | 场景共鸣 + 模块化方法论 + 低门槛呼吁 | 见示例输出 |
| 标签 | 5 个（基础 2+ 长尾 2+ 热点 1） | `#学渣逆袭 #干货分享 #信息差` |
| 互动 | 3 种类型（经验/观点/资源） | `试过第 2 步的扣 111` |
| CTA | 1 硬 1 软 | `评论区扣【秘籍】` + `关注优先推送` |

### check 命令输出标准

| 风险等级 | 含义 | 处理建议 |
|----------|------|----------|
| 🔴 红色 | 发现严重违规词 | 必须修改后发布 |
| 🟡 黄色 | 发现潜在风险词 | 建议修改 |
| 🟢 绿色 | 未发现明显问题 | 可安全发布 |

---

## 最佳实践

### ✅ 推荐做法

1. **文案生成后先检测**：用 `check` 命令扫描违禁词
2. **结合热点词库**：用 `keywords` 优化标题和标签
3. **选择合适的渲染风格**：参考 `docs/theme-guide.md`
4. **测试多种风格**：一键生成 13 种风格对比效果

### ❌ 避免做法

1. **直接使用未检测的文案**：可能违规限流
2. **标题超过 20 字**：影响点击率
3. **标签过多或过少**：固定 5 个最佳
4. **忽略互动设计**：降低笔记活跃度

---

## 常见问题

### Q: 生成的文案能直接发布吗？
**A:** 可以！正文部分输出的是不经任何修改能直接复制粘贴发布的内容。但建议先用 `check` 命令检测违禁词。

### Q: 渲染图片需要联网吗？
**A:** 需要。Playwright 会从 Google Fonts 加载字体，请确保网络通畅。如有代理请提前配置。

### Q: 如何自定义文案模板？
**A:** 修改 `templates/post_templates.json` 文件，添加你的模板。

### Q: 违禁词库多久更新一次？
**A:** 建议每月更新一次，关注平台最新监管规则。

### Q: 如何自定义渲染主题？
**A:** 复制 `assets/themes/` 下的现有主题 CSS，修改配色后使用新主题名渲染。

---

## 相关文档

- [README.md](README.md) - 项目详细说明
- [docs/markdown-format.md](docs/markdown-format.md) - Markdown 格式规范
- [docs/theme-guide.md](docs/theme-guide.md) - 主题风格指南
- [examples/](examples/) - 使用示例

---

## 更新日志

### v2.0.0 (2026-03-25)
- ✨ 新增 13 种风格封面卡片渲染功能
- ✨ 新增 Playwright 浏览器渲染支持
- ✨ 新增 Markdown 格式规范文档
- ✨ 新增主题风格指南
- 📦 合并 xhs-note-creator 项目

### v1.0.0 (初始版本)
- ✨ 爆款帖子生成
- ✨ 热点词库生成
- ✨ 违禁词检测

---

<div align="center">

**版本：v2.0.0** | **作者：LucianaiB** | **许可证：MIT**

[GitHub](https://github.com/lucianaib0318/xiaohongshu-master) · [问题反馈](https://github.com/lucianaib0318/xiaohongshu-master/issues)

</div>
