#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书生成大师 - 基础测试用例
"""

import sys
import os

# 添加主脚本路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from xiaohongshu import (
    generate_post,
    generate_keywords,
    check_banned_words,
    detect_domain,
    generate_title,
    generate_tags,
)

def test_generate_post():
    """测试帖子生成"""
    print("测试：帖子生成")
    result = generate_post("学渣逆袭")
    
    assert 'title' in result, "缺少标题"
    assert 'content' in result, "缺少正文"
    assert 'tags' in result, "缺少标签"
    assert 'interaction' in result, "缺少互动问题"
    assert 'cta' in result, "缺少 CTA"
    
    # 标题长度检查（emoji 算 2 字）
    title_len = len(result['title'])
    assert title_len <= 25, f"标题过长：{title_len}字"
    
    # 标签数量检查
    assert len(result['tags']) == 5, f"标签数量应为 5 个，实际{len(result['tags'])}个"
    
    print("✅ 帖子生成测试通过\n")

def test_generate_keywords():
    """测试热点词库生成"""
    print("测试：热点词库生成")
    result = generate_keywords("通勤穿搭")
    
    assert 'hot' in result, "缺少热搜词"
    assert 'longtail' in result, "缺少长尾词"
    assert 'rewrites' in result, "缺少标题改造"
    
    # 热搜词数量检查
    assert len(result['hot']) >= 3, "热搜词至少 3 个"
    
    # 标题改造数量检查
    assert len(result['rewrites']) == 3, "标题改造应为 3 个"
    
    print("✅ 热点词库生成测试通过\n")

def test_check_banned_words():
    """测试违禁词检测"""
    print("测试：违禁词检测")
    
    # 高风险文本
    result1 = check_banned_words("这款面膜全网销量第一！医院皮肤科都在用")
    assert result1['count'] >= 2, "应检测到至少 2 个违规词"
    
    # 低风险文本
    result2 = check_banned_words("这款精华液我用了三个月，肤质确实有改善")
    assert result2['count'] == 0, "不应检测到违规词"
    
    print("✅ 违禁词检测测试通过\n")

def test_detect_domain():
    """测试领域检测"""
    print("测试：领域检测")
    
    assert detect_domain("学渣逆袭") == '学习', "学习领域检测失败"
    assert detect_domain("油痘肌") == '护肤', "护肤领域检测失败"
    assert detect_domain("通勤穿搭") == '穿搭', "穿搭领域检测失败"
    
    print("✅ 领域检测测试通过\n")

def test_generate_title():
    """测试标题生成"""
    print("测试：标题生成")
    
    title = generate_title("学渣逆袭", "学习")
    
    # 检查是否包含 emoji
    assert any(ord(c) > 127 for c in title), "标题应包含 emoji"
    
    # 检查长度
    assert len(title) <= 25, f"标题过长：{len(title)}字"
    
    print("✅ 标题生成测试通过\n")

def test_generate_tags():
    """测试标签生成"""
    print("测试：标签生成")
    
    tags = generate_tags("学渣逆袭", "学习")
    
    # 检查标签数量
    assert len(tags) == 5, f"标签数量应为 5 个，实际{len(tags)}个"
    
    # 检查标签格式
    for tag in tags:
        assert tag.startswith('#'), f"标签应以#开头：{tag}"
    
    print("✅ 标签生成测试通过\n")

def run_all_tests():
    """运行所有测试"""
    print("=" * 50)
    print("🧪 小红书生成大师 - 测试套件")
    print("=" * 50)
    print()
    
    try:
        test_detect_domain()
        test_generate_title()
        test_generate_tags()
        test_generate_post()
        test_generate_keywords()
        test_check_banned_words()
        
        print("=" * 50)
        print("✅ 所有测试通过！")
        print("=" * 50)
        return True
    except AssertionError as e:
        print("=" * 50)
        print(f"❌ 测试失败：{e}")
        print("=" * 50)
        return False
    except Exception as e:
        print("=" * 50)
        print(f"❌ 测试异常：{e}")
        print("=" * 50)
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
