# 主题风格指南

本指南介绍 13 种可用的排版主题及其适用场景，帮助你快速选择最适合的风格。

---

## 🎨 主题速览表

| 主题代码 | 风格名称 | 风格关键词 | 适用场景 | 推荐指数 |
|----------|----------|------------|----------|----------|
| `memphis` | 孟菲斯 | 活泼/吸睛/年轻 | 好物推荐/种草 | ⭐⭐⭐⭐⭐ |
| `acid` | 酸性设计 | 金属/霓虹/潮流 | 技术编程/数码 | ⭐⭐⭐⭐⭐ |
| `vaporwave` | 蒸汽波 | 粉紫/复古/梦幻 | 生活美食/旅行 | ⭐⭐⭐⭐ |
| `minimalist` | 极简主义 | 留白/黑白灰/商务 | 知识干货/职场 | ⭐⭐⭐⭐⭐ |
| `glitch` | 故障艺术 | 像素错位/赛博朋克 | 科技/游戏/数码 | ⭐⭐⭐⭐ |
| `chinese` | 中国风 | 水墨/传统/国风 | 传统文化/美食 | ⭐⭐⭐⭐ |
| `glassmorphism` | 毛玻璃 | 磨砂/渐变/轻奢 | 美妆穿搭/护肤 | ⭐⭐⭐⭐⭐ |
| `bauhaus` | 包豪斯 | 几何/原色/构成 | 设计/建筑/艺术 | ⭐⭐⭐⭐ |
| `pop-art` | 波普艺术 | 高饱和/重复/时尚 | 时尚/潮流/艺术 | ⭐⭐⭐ |
| `art-nouveau` | 新艺术运动 | 曲线/自然/花卉 | 艺术/花艺/手作 | ⭐⭐⭐ |
| `collage` | 拼贴艺术 | 多层/混合/创意 | 创意/手作/旅行 | ⭐⭐⭐ |
| `new-ugly` | 新丑风格 | 反常规/冲突/实验 | 个性表达/艺术 | ⭐⭐ |
| `brutalism` | 粗野主义 | 原始/粗犷/工业 | 极简/工业风/建筑 | ⭐⭐⭐ |

---

## 🎯 快速选择指南

### 按内容类型选择

```
📦 好物推荐/种草      → memphis / pop-art / glassmorphism
💄 美妆穿搭/护肤      → glassmorphism / vaporwave / art-nouveau
🍳 生活美食/旅行      → vaporwave / chinese / collage
💼 知识干货/职场      → minimalist / bauhaus / professional
💻 技术编程/数码      → acid / glitch / terminal
🎨 设计/建筑/艺术     → bauhaus / art-nouveau / brutalism
🏮 传统文化/国风      → chinese / art-nouveau
🎭 个性表达/实验      → new-ugly / brutalism / glitch
```

### 按目标用户选择

```
👩 年轻女性 (18-25)   → memphis / glassmorphism / vaporwave
👨‍💼 职场人士 (25-35)   → minimalist / bauhaus / acid
👨‍💻 开发者/极客       → acid / glitch / minimalist
🎨 设计师/艺术家      → bauhaus / art-nouveau / brutalism
📚 文艺青年          → chinese / art-nouveau / collage
```

### 按发布目的选择

```
🔥 引流获客 (吸睛)    → memphis / acid / glitch
📖 专业背书 (信任)    → minimalist / bauhaus
💰 种草转化 (购买欲)  → glassmorphism / vaporwave / pop-art
📚 知识分享 (舒适)    → minimalist / chinese / art-nouveau
```

---

## 📐 13 种主题详解

### 1. 孟菲斯风格 (memphis) ⭐⭐⭐⭐⭐

**风格关键词**：活泼 · 吸睛 · 年轻 · 几何

**设计特点**：
- 🎨 高饱和度色彩（明黄/珊瑚红/宝蓝）
- 🔷 几何图形装饰（圆形/方形/三角形）
- ⬛ 粗黑边框 (10px) + 硬阴影
- 🔴 波点背景图案

**适用场景**：
- ✅ 好物推荐/种草
- ✅ 美妆穿搭
- ✅ 生活方式
- ✅ 年轻用户群体

**使用示例**：
```bash
python scripts/render_xhs.py content.md -t memphis -o ./output
```

---

### 2. 酸性设计风格 (acid) ⭐⭐⭐⭐⭐

**风格关键词**：金属 · 霓虹 · 潮流 · 未来感

**设计特点**：
- 🌌 深色背景（黑/深紫/深绿）
- 💚 霓虹绿/电光紫强调色
- 🔮 金属质感渐变
- ⚡ 锐利几何线条

**适用场景**：
- ✅ 技术编程/数码评测
- ✅ 潮流穿搭
- ✅ 音乐/亚文化
- ✅ Z 世代内容

**使用示例**：
```bash
python scripts/render_xhs.py tech.md -t acid -o ./output
```

---

### 3. 蒸汽波风格 (vaporwave) ⭐⭐⭐⭐

**风格关键词**：复古 · 梦幻 · 粉紫 · 80 年代

**设计特点**：
- 🌆 粉紫渐变背景
- 🌴 复古元素（棕榈树/落日）
- 💜 柔和霓虹色
- 📼 80 年代美学

**适用场景**：
- ✅ 生活美食
- ✅ 旅行分享
- ✅ 复古穿搭
- ✅ 治愈系内容

**使用示例**：
```bash
python scripts/render_xhs.py travel.md -t vaporwave -o ./output
```

---

### 4. 极简主义风格 (minimalist) ⭐⭐⭐⭐⭐

**风格关键词**：留白 · 黑白灰 · 商务 · 专业

**设计特点**：
- ⚪ 大量留白
- ⚫ 黑白灰主色调
- 📏 严格对齐
- 🔤 清晰排版

**适用场景**：
- ✅ 知识干货
- ✅ 职场进阶
- ✅ 商业分析
- ✅ 专业教程

**使用示例**：
```bash
python scripts/render_xhs.py business.md -t minimalist -o ./output
```

---

### 5. 故障艺术风格 (glitch) ⭐⭐⭐⭐

**风格关键词**：像素错位 · 赛博朋克 · 科技 · 未来

**设计特点**：
- 📺 像素错位效果
- 🔴🔵 色彩分离 (RGB Split)
- ⚡ 电子干扰纹理
- 🖥️ 赛博朋克美学

**适用场景**：
- ✅ 科技数码
- ✅ 游戏内容
- ✅ 程序员日常
- ✅ 未来感主题

**使用示例**：
```bash
python scripts/render_xhs.py gaming.md -t glitch -o ./output
```

---

### 6. 中国风风格 (chinese) ⭐⭐⭐⭐

**风格关键词**：水墨 · 传统 · 国风 · 典雅

**设计特点**：
- 🖌️ 水墨元素
- 🏮 传统纹样（云纹/回纹）
- 🎋 竹/梅/兰/菊装饰
- 📜 竖排文字可选

**适用场景**：
- ✅ 传统文化
- ✅ 国风美食
- ✅ 茶道/花道
- ✅ 历史故事

**使用示例**：
```bash
python scripts/render_xhs.py culture.md -t chinese -o ./output
```

---

### 7. 毛玻璃风格 (glassmorphism) ⭐⭐⭐⭐⭐

**风格关键词**：磨砂 · 渐变 · 轻奢 · 高级感

**设计特点**：
- 🪟 磨砂玻璃效果
- 🌈 柔和渐变背景
- ✨ 轻微阴影 + 模糊
- 💎 高级质感

**适用场景**：
- ✅ 美妆护肤
- ✅ 穿搭分享
- ✅ 轻奢生活
- ✅ 女性向内容

**使用示例**：
```bash
python scripts/render_xhs.py beauty.md -t glassmorphism -o ./output
```

---

### 8. 包豪斯风格 (bauhaus) ⭐⭐⭐⭐

**风格关键词**：几何 · 原色 · 构成 · 理性

**设计特点**：
- 🔴🔵🟡 红黄蓝原色
- 📐 几何构成（圆/方/三角）
- ⬜ 非对称布局
- 🏗️ 功能主义美学

**适用场景**：
- ✅ 设计分享
- ✅ 建筑艺术
- ✅ 创意作品
- ✅ 美学教育

**使用示例**：
```bash
python scripts/render_xhs.py design.md -t bauhaus -o ./output
```

---

### 9. 波普艺术风格 (pop-art) ⭐⭐⭐

**风格关键词**：高饱和 · 重复 · 时尚 · 安迪沃霍尔

**设计特点**：
- 🎨 高饱和度色块
- 🔁 重复图案
- 💥 漫画风格
- 🍕 流行文化元素

**适用场景**：
- ✅ 时尚穿搭
- ✅ 潮流单品
- ✅ 艺术展览
- ✅ 流行文化

**使用示例**：
```bash
python scripts/render_xhs.py fashion.md -t pop-art -o ./output
```

---

### 10. 新艺术运动风格 (art-nouveau) ⭐⭐⭐

**风格关键词**：曲线 · 自然 · 花卉 · 优雅

**设计特点**：
- 🌿 有机曲线
- 🌸 花卉植物装饰
- 🦋 自然元素（昆虫/鸟类）
- 🎭 优雅女性形象

**适用场景**：
- ✅ 花艺分享
- ✅ 手工艺品
- ✅ 艺术鉴赏
- ✅ 优雅生活

**使用示例**：
```bash
python scripts/render_xhs.py flowers.md -t art-nouveau -o ./output
```

---

### 11. 拼贴艺术风格 (collage) ⭐⭐⭐

**风格关键词**：多层 · 混合 · 创意 · 手作感

**设计特点**：
- ✂️ 拼贴效果
- 📰 多材质混合
- 🎭 层次叠加
- 🖼️ 手帐质感

**适用场景**：
- ✅ 旅行手帐
- ✅ 创意手作
- ✅ 生活记录
- ✅ 混合媒介

**使用示例**：
```bash
python scripts/render_xhs.py journal.md -t collage -o ./output
```

---

### 12. 新丑风格 (new-ugly) ⭐⭐

**风格关键词**：反常规 · 冲突 · 实验 · 前卫

**设计特点**：
- 🎨 冲突色彩
- 📐 故意错位
- 🔤 非常规排版
- 🤪 反美学设计

**适用场景**：
- ✅ 个性表达
- ✅ 实验艺术
- ✅ 前卫设计
- ✅ 亚文化

**使用示例**：
```bash
python scripts/render_xhs.py experimental.md -t new-ugly -o ./output
```

---

### 13. 粗野主义风格 (brutalism) ⭐⭐⭐

**风格关键词**：原始 · 粗犷 · 工业 · 混凝土

**设计特点**：
- 🏢 粗犷线条
- ⚫ 黑白灰主色
- 🧱 原始质感
- 📐 极简几何

**适用场景**：
- ✅ 建筑设计
- ✅ 工业风
- ✅ 极简生活
- ✅ 男性向内容

**使用示例**：
```bash
python scripts/render_xhs.py architecture.md -t brutalism -o ./output
```

---

## 🎯 主题对比排行

### 视觉冲击力（吸睛度）
```
memphis > acid > glitch > pop-art > vaporwave > 
glassmorphism > bauhaus > new-ugly > brutalism > 
chinese > art-nouveau > collage > minimalist
```

### 阅读舒适度
```
minimalist > chinese > art-nouveau > glassmorphism > 
vaporwave > bauhaus > collage > brutalism > 
memphis > pop-art > glitch > acid > new-ugly
```

### 适用广泛度
```
minimalist > memphis > glassmorphism > acid > 
vaporwave > bauhaus > chinese > glitch > 
brutalism > art-nouveau > pop-art > collage > new-ugly
```

### 小红书爆款潜力
```
memphis > glassmorphism > acid > vaporwave > 
minimalist > glitch > bauhaus > chinese > 
pop-art > art-nouveau > brutalism > collage > new-ugly
```

---

## 🧪 快速测试所有主题

```bash
# 一键生成 13 种风格预览
for theme in memphis acid vaporwave minimalist glitch chinese glassmorphism bauhaus pop-art art-nouveau collage new-ugly brutalism; do
  python scripts/render_xhs.py examples/tool-recommendation.md -t $theme -o "./output/$theme"
done

# 查看结果
ls -la ./output/
```

---

## 🎨 自定义主题

### 步骤 1：复制现有主题

```bash
cd assets/themes
cp memphis.css my-custom-theme.css
```

### 步骤 2：修改配色

编辑 `my-custom-theme.css`，修改 CSS 变量：

```css
.my-custom-theme-container {
  --bg-color: #your-color;
  --text-color: #your-color;
  --accent-color: #your-color;
  /* ... */
}
```

### 步骤 3：使用新主题

```bash
python scripts/render_xhs.py content.md -t my-custom-theme -o ./output
```

---

## 📊 主题选择决策树

```
开始
│
├─ 内容类型？
│  ├─ 好物推荐 → memphis / glassmorphism
│  ├─ 知识干货 → minimalist / bauhaus
│  ├─ 美妆穿搭 → glassmorphism / vaporwave
│  ├─ 技术编程 → acid / glitch
│  ├─ 生活美食 → vaporwave / chinese
│  └─ 设计艺术 → bauhaus / art-nouveau
│
├─ 目标用户？
│  ├─ 年轻女性 → memphis / glassmorphism
│  ├─ 职场人士 → minimalist / bauhaus
│  ├─ 开发者 → acid / glitch
│  └─ 文艺青年 → chinese / art-nouveau
│
└─ 不确定？→ 用 memphis（最安全）
```

---

## 📚 相关文档

- [Markdown 格式规范](markdown-format.md) - 学习如何编写渲染用的 Markdown 文件
- [使用示例](../examples/) - 查看各主题的示例图片

---

<div align="center">

**🎨 选择最适合你内容的风格，让笔记更吸睛！**

</div>
