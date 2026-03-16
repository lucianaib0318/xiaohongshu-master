# 小红书生成大师

生成小红书爆款文案、热点词库、违禁词检测的一站式内容创作工具。

## 命令

```bash
xiaohongshu <command> [options] [input]
```

## 子命令

### `post` - 生成爆款帖子

基于输入主题生成完整的小红书笔记方案（标题 + 正文 + 标签 + 互动 + CTA）

```bash
xiaohongshu post <主题>
```

**示例:**
```bash
xiaohongshu post 学渣逆袭
xiaohongshu post 油痘肌护肤
xiaohongshu post 通勤穿搭
```

### `keywords` - 生成热点词库

基于输入主题生成热搜词、长尾词、标题改造方案

```bash
xiaohongshu keywords <主题>
```

**示例:**
```bash
xiaohongshu keywords 通勤穿搭
xiaohongshu keywords 学生党护肤
```

### `check` - 违禁词检测

扫描文本中的违规词，提供替换建议

```bash
xiaohongshu check "<文本内容>"
```

**示例:**
```bash
xiaohongshu check "这款面膜全网销量第一，7 天淡化所有皱纹"
```

## 输出格式

### post 命令输出
- **标题**: 2 个 emoji + 数据化结论 + 获得感承诺（≤20 字）
- **正文**: 共鸣描述 + 分点说明 + 激励语句（可直接发布）
- **互动问题**: 3 种类型各 1 条
- **CTA 策略**: 1 硬 1 软引导
- **话题标签**: 5 个标签（基础 + 长尾 + 热点）

### keywords 命令输出
- **热搜词库**: 平台热词 + 搜索增长率
- **长尾词库**: 人群 + 场景 + 需求组合
- **标题改造**: 3 种差异化方案

### check 命令输出
- **违规词高亮**: 🚨标注
- **违规类型**: 引用政策条款
- **替换建议**: 合规表达方案
- **风险等级**: 🔴红色/🟡黄色/🟢绿色

## 依赖

- Python 3.8+
- 无外部依赖（纯本地运行）

## 文件结构

```
xiaohongshu-master/
├── SKILL.md           # 技能说明
├── xiaohongshu.py     # 主脚本
└── templates/         # 文案模板库
    ├── post_templates.json
    ├── keyword_templates.json
    └── banned_words.json
```

## 注意事项

1. **正文输出**: 直接可复制粘贴发布，无注释性信息
2. **标题长度**: 严格控制在 20 字以内（含 emoji）
3. **标签数量**: 固定 5 个，按矩阵规则组合
4. **违禁词库**: 基于最新《广告法》和平台规则

---

*版本：v1.0.0 | 作者：LucianaiB*
