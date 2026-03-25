#!/usr/bin/env python3
"""
小红书卡片渲染 - Playwright HTML 版本
使用浏览器渲染，支持 Emoji、加粗、复杂布局
"""

import argparse
import yaml
import re
from pathlib import Path
from playwright.sync_api import sync_playwright

# 脚本目录
SCRIPT_DIR = Path(__file__).parent
ASSETS_DIR = SCRIPT_DIR.parent / "assets"

def parse_markdown(md_file):
    """解析 Markdown 文件，提取 YAML 头部和正文"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            yaml_content = parts[1]
            body = parts[2].strip()
            meta = yaml.safe_load(yaml_content)
        else:
            meta = {}
            body = content
    else:
        meta = {}
        body = content
    
    pages = body.split('\n---\n')
    return meta, pages

def markdown_to_html(md_text):
    """
    将 Markdown 转换为 HTML
    支持：标题、段落、列表、引用、代码块、表格、Emoji
    """
    html = md_text
    
    # 1. 处理 Emoji（用 <span class="emoji">包裹）
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Symbols & Pictographs
        "\U0001F680-\U0001F6FF"  # Transport & Map
        "\U0001F1E0-\U0001F1FF"  # Flags
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251"  # Enclosed characters
        "]+",
        flags=re.UNICODE
    )
    html = emoji_pattern.sub(lambda m: f'<span class="emoji">{m.group(0)}</span>', html)
    
    # 2. 处理代码块（先处理，避免被其他规则干扰）
    html = re.sub(r'```(\w*)\n(.*?)```', r'<pre><code>\2</code></pre>', html, flags=re.DOTALL)
    
    # 3. 处理行内代码
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    
    # 4. 处理引用块
    html = re.sub(r'^> (.+)$', r'<blockquote><p>\1</p></blockquote>', html, flags=re.MULTILINE)
    
    # 5. 处理标题（按顺序，避免 H1 匹配 H2）
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    
    # 6. 处理加粗和斜体
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    html = re.sub(r'__(.+?)__', r'<strong>\1</strong>', html)
    html = re.sub(r'_(.+?)_', r'<em>\1</em>', html)
    
    # 7. 处理列表
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'^\* (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'^(\d+)\. (.+)$', r'<li>\2</li>', html, flags=re.MULTILINE)
    
    # 8. 处理段落（空行分隔）
    paragraphs = html.split('\n\n')
    processed = []
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('<'):
            p = f'<p>{p}</p>'
        processed.append(p)
    html = '\n'.join(processed)
    
    # 9. 包裹列表为 ul/ol
    html = re.sub(r'(<li>.*?</li>\n?)+', lambda m: f'<ul>{m.group(0)}</ul>', html)
    
    return html

def render_cover(meta, output_file, theme='memphis', width=1080, height=1440):
    """渲染封面"""
    # 读取 HTML 模板
    template_file = ASSETS_DIR / "cover.html"
    with open(template_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 替换变量
    html = html.replace('{{THEME}}', theme)
    html = html.replace('{{EMOJI}}', meta.get('emoji', '🚀'))
    html = html.replace('{{TITLE}}', meta.get('title', '标题'))
    html = html.replace('{{SUBTITLE}}', meta.get('subtitle', '副标题'))
    
    # 使用 Playwright 渲染
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_viewport_size({'width': width, 'height': height})
        page.set_content(html)
        page.screenshot(path=output_file, full_page=True)
        browser.close()
    
    print(f"  ✅ 已生成：{output_file} ({width}x{height})")

def render_card(content, page_num, total_pages, output_file, theme='memphis', width=1080, height=1440):
    """渲染正文卡片"""
    # 读取 HTML 模板
    template_file = ASSETS_DIR / "card.html"
    with open(template_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Markdown 转 HTML
    html_content = markdown_to_html(content)
    
    # 替换变量
    html = html.replace('{{THEME}}', theme)
    html = html.replace('{{CONTENT}}', html_content)
    html = html.replace('{{PAGE_NUMBER}}', f'{page_num}/{total_pages}')
    
    # 使用 Playwright 渲染
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_viewport_size({'width': width, 'height': height})
        page.set_content(html)
        page.screenshot(path=output_file, full_page=True)
        browser.close()
    
    print(f"  ✅ 已生成：{output_file} ({width}x{height})")

def main():
    parser = argparse.ArgumentParser(description='小红书卡片渲染工具 (Playwright 版)')
    parser.add_argument('markdown_file', help='Markdown 文件路径')
    parser.add_argument('-o', '--output-dir', default='.', help='输出目录')
    parser.add_argument('-t', '--theme', default='memphis', help='排版主题（memphis/acid/vaporwave/minimalist/glitch/chinese/glassmorphism/bauhaus/pop-art/art-nouveau/collage/new-ugly/brutalism）')
    parser.add_argument('-m', '--mode', default='separator', help='分页模式')
    parser.add_argument('-w', '--width', type=int, default=1080, help='图片宽度')
    parser.add_argument('--height', type=int, default=1440, help='图片高度')
    
    args = parser.parse_args()
    
    print(f"🎨 开始渲染：{args.markdown_file}")
    print(f"  🎨 主题：{args.theme}")
    print(f"  📏 模式：{args.mode}")
    print(f"  📐 尺寸：{args.width}x{args.height}")
    
    meta, pages = parse_markdown(args.markdown_file)
    print(f"  📄 检测到 {len(pages)} 张正文卡片")
    
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 渲染封面
    cover_file = output_dir / "cover.png"
    print(f"  📷 生成封面...")
    render_cover(meta, str(cover_file), args.theme, args.width, args.height)
    
    # 渲染正文卡片
    for i, page_content in enumerate(pages, 1):
        card_file = output_dir / f"card_{i}.png"
        print(f"  📷 生成卡片 {i}/{len(pages)}...")
        render_card(page_content, i, len(pages), str(card_file), args.theme, args.width, args.height)
    
    print(f"\n✨ 渲染完成！图片已保存到：{output_dir}")

if __name__ == '__main__':
    main()
