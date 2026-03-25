#!/bin/bash
# 小红书生成大师 - 快速启动脚本
# 用法：./run.sh <command> [options] [input]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 显示帮助信息
show_help() {
    cat << EOF
📕 小红书生成大师 - Xiaohongshu Master

用法：./run.sh <command> [options] [input]

命令:
  post <主题>              生成爆款帖子
  keywords <主题>          生成热点词库
  check "<文本内容>"       违禁词检测
  render <md 文件>         渲染封面卡片（使用 scripts/render_xhs.py）

示例:
  ./run.sh post 学渣逆袭
  ./run.sh keywords 通勤穿搭
  ./run.sh check "这款面膜全网销量第一"
  ./run.sh render examples/tool-recommendation.md -t memphis -o ./output

主题风格 (render 命令):
  memphis, acid, vaporwave, minimalist, glitch, chinese,
  glassmorphism, bauhaus, pop-art, art-nouveau, collage,
  new-ugly, brutalism

文档:
  README.md                项目详细说明
  docs/theme-guide.md      主题风格指南
  docs/markdown-format.md  Markdown 格式规范

EOF
}

# 检查参数
if [ $# -eq 0 ] || [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    show_help
    exit 0
fi

# 处理 render 命令（调用 scripts/render_xhs.py）
if [ "$1" = "render" ]; then
    shift
    python3 "$SCRIPT_DIR/scripts/render_xhs.py" "$@"
    exit $?
fi

# 其他命令调用主程序
python3 "$SCRIPT_DIR/xiaohongshu.py" "$@"
