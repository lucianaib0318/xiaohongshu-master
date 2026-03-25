# 主题风格指南

本指南介绍 8 种可用的排版主题及其适用场景。

---

## 主题速览

| 主题 | 风格关键词 | 推荐指数 |
|------|------------|----------|
| `memphis` | 活泼/吸睛/年轻 | ⭐⭐⭐⭐⭐ |
| `botanical` | 清新/自然/治愈 | ⭐⭐⭐⭐ |
| `professional` | 专业/商务/正式 | ⭐⭐⭐⭐ |
| `playful-geometric` | 俏皮/时尚/美妆 | ⭐⭐⭐⭐ |
| `neo-brutalism` | 潮流/设计/艺术 | ⭐⭐⭐ |
| `retro` | 怀旧/温暖/手作 | ⭐⭐⭐ |
| `terminal` | 极客/代码/技术 | ⭐⭐⭐⭐ |
| `sketch` | 文艺/手绘/简约 | ⭐⭐⭐ |
| `default` | 通用/渐变/安全 | ⭐⭐⭐ |

---

## 孟菲斯风格（memphis）⭐ 推荐

### 设计特点

- 🎨 高饱和度色彩（黄/红/蓝）
- 🔷 几何图形装饰（圆形/方形/三角形）
- ⬛ 粗黑边框（10px）+ 硬阴影
- 🔴 波点背景图案
- 🌊 波浪线条装饰

### 适用场景

- ✅ 好物推荐/种草
- ✅ 美妆穿搭
- ✅ 生活方式
- ✅ 年轻用户群体

### 使用示例

```bash
python scripts/render_xhs.py content.md -t memphis -m auto-split
```

### 配色方案

| 颜色 | 色值 | 用途 |
|------|------|------|
| 明黄 | #FFD93D | 主背景 |
| 珊瑚红 | #FF6B6B | 强调色 |
| 宝蓝 | #4D96FF | 强调色 |
| 薄荷绿 | #6BCB77 | 装饰色 |
| 纯黑 | #000000 | 边框 |

---

## 植物园风格（botanical）

### 设计特点

- 🌿 森林绿配色
- 🍃 自然有机形状
- 🤎 温暖米色背景
- 📗 柔和渐变

### 适用场景

- ✅ 美食教程
- ✅ 健康生活
- ✅ 植物养护
- ✅ 治愈系内容

### 使用示例

```bash
python scripts/render_xhs.py recipe.md -t botanical -m dynamic
```

---

## 专业商务风格（professional）

### 设计特点

- 💼 深蓝色系
- 📊 简洁布局
- 📐 规整对齐
- ⚪ 大量留白

### 适用场景

- ✅ 职场干货
- ✅ 知识付费
- ✅ 商业分析
- ✅ 专业教程

### 使用示例

```bash
python scripts/render_xhs.py business.md -t professional -m separator
```

---

## 活泼几何风格（playful-geometric）

### 设计特点

- 🎪 Memphis 设计灵感
- 🟣 紫色/粉色/黄色
- 🔺 几何图形
- ✨ 硬阴影效果

### 适用场景

- ✅ 美妆教程
- ✅ 穿搭分享
- ✅ 好物种草
- ✅ 年轻女性用户

### 使用示例

```bash
python scripts/render_xhs.py makeup.md -t playful-geometric -m auto-fit
```

---

## 粗野主义风格（neo-brutalism）

### 设计特点

- ⚫ 极粗黑边框
- 🟡 荧光黄/电光青
- 🔲 原始几何感
- 💥 高对比度

### 适用场景

- ✅ 潮牌穿搭
- ✅ 设计作品
- ✅ 艺术展览
- ✅ 个性表达

### 使用示例

```bash
python scripts/render_xhs.py fashion.md -t neo-brutalism -m dynamic
```

---

## 复古怀旧风格（retro）

### 设计特点

- 📻 棕色/米黄配色
- 🎞️ 怀旧质感
- 📜 复古字体
- 🤎 温暖色调

### 适用场景

- ✅ 复古穿搭
- ✅ 手作工艺
- ✅ 情怀故事
- ✅ 传统美食

### 使用示例

```bash
python scripts/render_xhs.py vintage.md -t retro -m auto-split
```

---

## 终端代码风格（terminal）

### 设计特点

- 💻 深色背景
- 🟢 荧光绿文字
- ⌨️ 代码编辑器风格
- 🔲 等宽字体

### 适用场景

- ✅ 编程教程
- ✅ 技术分享
- ✅ 极客工具
- ✅ 开发者内容

### 使用示例

```bash
python scripts/render_xhs.py coding.md -t terminal -m separator
```

---

## 手绘素描风格（sketch）

### 设计特点

- ✏️ 铅笔灰色调
- 📔 素描纸质感
- 🎨 手绘线条
- ⚪ 极简布局

### 适用场景

- ✅ 插画作品
- ✅ 手账分享
- ✅ 文艺内容
- ✅ 读书心得

### 使用示例

```bash
python scripts/render_xhs.py journal.md -t sketch -m auto-fit
```

---

## 默认风格（default）

### 设计特点

- 🌈 浅灰渐变背景
- 📏 简约布局
- 🔒 安全选择
- ✅ 通用性强

### 适用场景

- ✅ 不确定选啥时
- ✅ 商务通用
- ✅ 测试预览
- ✅ 快速出图

### 使用示例

```bash
python scripts/render_xhs.py content.md -t default -m auto-split
```

---

## 选择指南

### 按内容类型

```
知识干货 → professional / default
好物推荐 → memphis / playful-geometric
生活美食 → botanical / retro
技术编程 → terminal / default
设计艺术 → neo-brutalism / sketch
美妆穿搭 → playful-geometric / memphis
```

### 按目标用户

```
年轻女性 → playful-geometric / memphis / botanical
职场人士 → professional / default
开发者 → terminal / default
文艺青年 → sketch / retro
```

### 按发布目的

```
引流获客 → memphis（吸睛）
专业背书 → professional（信任）
种草转化 → playful-geometric（购买欲）
知识分享 → default / botanical（舒适）
```

---

## 主题对比

### 视觉冲击力

```
memphis > neo-brutalism > playful-geometric > terminal > 
botanical > retro > sketch > professional > default
```

### 阅读舒适度

```
default > botanical > professional > sketch > 
retro > playful-geometric > memphis > terminal > neo-brutalism
```

### 适用广泛度

```
default > memphis > professional > botanical > 
playful-geometric > terminal > sketch > retro > neo-brutalism
```

---

## 快速测试

```bash
# 一键测试所有主题
for theme in memphis botanical professional playful-geometric neo-brutalism retro terminal sketch default; do
  python scripts/render_xhs.py content.md -t $theme -o ./test/$theme
done
```

---

## 自定义主题

1. 复制现有主题 CSS：
```bash
cp assets/themes/memphis.css assets/themes/my-theme.css
```

2. 修改颜色配置

3. 使用新主题：
```bash
python scripts/render_xhs.py content.md -t my-theme
```

---

更多资源：[../examples/](../examples/)
