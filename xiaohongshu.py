#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书生成大师 - 一站式内容创作工具
功能：爆款帖子生成、热点词库、违禁词检测
"""

import sys
import random
import json
from datetime import datetime

# ==================== 模板库 ====================

# 标题模板
TITLE_TEMPLATES = [
    "{emoji1}{emoji2}{数据}个{方法}｜{人群}{结果}｜附{资源}",
    "{emoji1}{emoji2}{颠覆结论}｜{人群}必看｜{获得感}",
    "{emoji1}{emoji2}{痛点}｜{时间}见效｜{人群}友好",
]

# Emoji 库
EMOJIS = {
    'fire': ['🔥', '💥', '✨', '💡', '⚡'],
    'success': ['✅', '💯', '🎯', '🏆', '⭐'],
    'warning': ['⚠️', '❗', '🚨', '💣', '❌'],
    'tool': ['🛠️', '📦', '📚', '💼', '🎁'],
    'heart': ['❤️', '💕', '💗', '🥰', '💖'],
    'think': ['🤔', '💭', '🧠', '👀', '👂'],
}

# 领域词库
DOMAIN_KEYWORDS = {
    '学习': ['学渣逆袭', '学霸秘籍', '高效学习', '考试通关', '时间管理'],
    '护肤': ['油痘肌', '敏感肌', '美白淡斑', '抗初老', '补水保湿'],
    '穿搭': ['通勤穿搭', '小个子穿搭', '微胖穿搭', '学生党穿搭', '约会穿搭'],
    '职场': ['职场新人', '升职加薪', '面试技巧', '人际关系', '工作效率'],
    '减肥': ['减脂餐', '瘦身运动', '懒人减肥', '产后恢复', '局部塑形'],
    '美食': ['快手菜', '减脂餐', '烘焙教程', '便当搭配', '网红甜品'],
    '旅行': ['穷游攻略', '拍照打卡', '小众景点', '亲子游', '独自旅行'],
    '情感': ['恋爱技巧', '婚姻经营', '自我成长', '情绪管理', '人际交往'],
}

# 互动问题模板
INTERACTION_TEMPLATES = {
    'experience': [
        "试过第 2 步的扣 111，效果炸裂的举双手🙌",
        "说一个你踩过最痛的坑，帮新人避雷💣",
        "做到第几步卡住了？评论区蹲答案👇",
    ],
    'opinion': [
        "A 派 VS B 派！用结果说服对方💪",
        "XX 真的必要吗？敢说真话的来👂",
        "你觉得哪个方法最有用？投票选出来📊",
    ],
    'resource': [
        "私藏神器/书单/模板？带图安利抽奖🎁",
        "高赞问题下期专门解答✨",
        "想要完整模板的扣【想要】，抽 3 人送🎉",
    ],
}

# CTA 模板
CTA_TEMPLATES = {
    'hard': [
        "完整模板评论区扣【秘籍】自动触发📩",
        "工具包戳'马上拯救'触发自动回复🚀",
        "需要 XX 清单的评论区举手🙋‍♀️",
    ],
    'soft': [
        "下期揭秘 XX 领域潜规则！关注优先推送🔔",
        "主页整理 100+ 免费资源库，懒人福音📚",
        "收藏=学会，不然刷着刷着就找不到了⭐",
    ],
}

# 违禁词库（支持单字和短语检测）
BANNED_WORDS = {
    '绝对化': ['最', '第一', '国家级', '全网', '顶级', '史上', '永久', '万能', '唯一', '极致', '首选'],
    '医疗': ['根治', '疗效', '修复细胞', '治疗', '药方', '医生推荐', '医院同款', '处方', '疗程', '皮肤科'],
    '效果': ['7 天', '月瘦 20 斤', '立即见效', '100% 有效', '无效退款', '永不反弹', '三天见效', '淡化所有'],
    '引流': ['加微信', '二维码', '私信我', '外链', '公众号', '淘宝店', '微店', '联系方式'],
    '迷信': ['风水', '算命', '转运', '招财', '辟邪', '改运', '开光', '保佑'],
}

# 替换建议
REPLACEMENT_SUGGESTIONS = {
    '最': '个人觉得/实测感受',
    '第一': '累计热销超 X 万/口碑爆款',
    '根治': '帮助改善/缓解',
    '疗效': '使用效果/实测反馈',
    '修复细胞': '帮助强韧肌肤屏障',
    '7 天': '28 天可见改善',
    '100%': '多数人反馈',
    '加微信': '评论区交流',
    '私信我': '评论区留言',
}

# ==================== 功能函数 ====================

def detect_domain(topic):
    """检测主题所属领域"""
    for domain, keywords in DOMAIN_KEYWORDS.items():
        for kw in keywords:
            if kw in topic or topic in kw:
                return domain
    return '通用'

def generate_title(topic, domain):
    """生成标题"""
    emoji1 = random.choice(EMOJIS['fire'])
    emoji2 = random.choice(EMOJIS['success'] + EMOJIS['tool'])
    
    titles = [
        f"{emoji1}{emoji2}亲测{random.choice(['3 个月', '30 天', '半年'])}｜{topic}真的不难｜附工具包",
        f"{emoji1}{emoji2}{random.choice(['3 个', '5 个', '7 个'])}{random.choice(['野路子', '神器', '方法'])}｜{topic}必看｜超详细",
        f"{emoji1}{emoji2}别再{random.choice(['瞎折腾', '走弯路', '交智商税'])}了｜{topic}有捷径｜学生党友好",
        f"{emoji1}{emoji2}{random.choice(['90%', '80%', '70%'])}人不知道的{topic}技巧｜亲测有效｜建议收藏",
    ]
    
    # 确保标题不超过 20 字（emoji 算 2 字）
    selected = random.choice(titles)
    while len(selected) > 25:  # emoji 占位
        selected = selected[:-1]
    
    return selected

def generate_content(topic, domain):
    """生成正文内容"""
    templates = [
        f"""是不是也在为{topic}头疼？试过好多方法都没用😭

别急！今天分享{random.choice(['3 个', '5 个'])}亲测有效的{domain}小技巧👇

🚀 {random.choice(['第一步', '方法一', '核心'])}：具体操作说明
💡 {random.choice(['第二步', '方法二', '进阶'])}：关键注意事项
⚠️ {random.choice(['第三步', '方法三', '避坑'])}：常见误区提醒

{random.choice(['学生党', '打工人', '零基础'])}也完全 OK！
其实{topic}没那么难，只是你没找对方法❗

亲测{random.choice(['3 个月', '半年'])}，效果真的绝了💯""",
        
        f"""刷到这篇你在被大数据拯救❗️

{random.choice(['经历过', '踩过'])}{topic}的坑才懂这些痛😭
{random.choice(['熬夜', '反复尝试', '花了好多钱'])}都没效果...

直到我发现了{random.choice(['这套方法', '这个思路', '这些技巧'])}👇

✨ 重点 1：核心方法说明
✨ 重点 2：关键细节提醒
✨ 重点 3：常见误区避雷

{random.choice(['300 人验证', '亲测 3 月有效', '粉丝反馈超好'])}
别再{random.choice(['瞎折腾', '走弯路'])}了，直接抄作业📝""",
    ]
    
    return random.choice(templates)

def generate_tags(topic, domain):
    """生成标签矩阵"""
    tags = []
    
    # 基础标签
    tags.append(f"#{topic}")
    tags.append("#干货分享")
    
    # 长尾标签（人群 + 场景）
    longtail = [
        f"#{random.choice(['学生党', '打工人', '新手'])}{random.choice(['必备', '自救', '攻略'])}",
        f"#{random.choice(['零基础', '小白', '懒人'])}{random.choice(['友好', '福音', '适用'])}",
    ]
    tags.extend(random.sample(longtail, min(2, len(longtail))))
    
    # 热点标签
    hot = ["#信息差", "#认知开挂", "#自我提升", "#成长记录", "#经验分享"]
    tags.append(random.choice(hot))
    
    return tags[:5]  # 确保 5 个标签

def generate_post(topic):
    """生成完整帖子"""
    domain = detect_domain(topic)
    
    title = generate_title(topic, domain)
    content = generate_content(topic, domain)
    tags = generate_tags(topic, domain)
    
    # 互动问题
    interaction = {
        'experience': random.choice(INTERACTION_TEMPLATES['experience']),
        'opinion': random.choice(INTERACTION_TEMPLATES['opinion']),
        'resource': random.choice(INTERACTION_TEMPLATES['resource']),
    }
    
    # CTA
    cta = {
        'hard': random.choice(CTA_TEMPLATES['hard']),
        'soft': random.choice(CTA_TEMPLATES['soft']),
    }
    
    return {
        'title': title,
        'content': content,
        'tags': tags,
        'interaction': interaction,
        'cta': cta,
    }

def generate_keywords(topic):
    """生成热点词库"""
    # 模拟热搜词（实际应调用 API）
    hot_keywords = [
        (f"{topic}神器", random.randint(150, 400)),
        (f"{topic}攻略", random.randint(120, 350)),
        (f"{topic}避雷", random.randint(100, 280)),
        (f"{topic}亲测", random.randint(80, 220)),
        (f"{topic}分享", random.randint(60, 180)),
    ]
    
    # 长尾词
    longtail = [
        f"{random.choice(['学生党', '打工人', '新手'])}{topic}{random.choice(['必备', '指南', '教程'])}",
        f"{random.choice(['零基础', '小白', '懒人'])}{topic}{random.choice(['方法', '技巧', '心得'])}",
        f"{topic}{random.choice(['注意事项', '常见误区', '避坑指南'])}",
    ]
    
    # 标题改造
    title_rewrites = [
        f"「{topic}」→「{random.choice(['打工人', '学生党'])}{random.choice(['生存', '逆袭', '必备'])}{random.choice(['指南', '秘籍', '攻略'])}」",
        f"「{topic}」→「{random.choice(['90%', '80%'])}人都不知道的{random.choice(['潜规则', '真相', '技巧'])}」",
        f"「{topic}」→「从{random.choice(['小白', '零基础'])}到{random.choice(['大神', '高手'])}的{random.choice(['进阶', '成长'])}路」",
    ]
    
    return {
        'hot': hot_keywords,
        'longtail': longtail,
        'rewrites': title_rewrites,
    }

def check_banned_words(text):
    """违禁词检测"""
    violations = []
    
    for category, words in BANNED_WORDS.items():
        for word in words:
            if word in text:
                violations.append({
                    'word': word,
                    'category': category,
                    'suggestion': REPLACEMENT_SUGGESTIONS.get(word, '建议修改为更客观的表述'),
                })
    
    # 风险等级评估
    if len(violations) >= 5:
        level = '🔴 红色'
    elif len(violations) >= 2:
        level = '🟡 黄色'
    else:
        level = '🟢 绿色'
    
    return {
        'violations': violations,
        'level': level,
        'count': len(violations),
    }

def format_post_output(result):
    """格式化帖子输出"""
    output = []
    output.append("=" * 50)
    output.append("📕 小红书爆款文案")
    output.append("=" * 50)
    output.append(f"\n📌 标题：{result['title']}")
    output.append(f"\n📝 正文：\n{result['content']}")
    output.append(f"\n🏷️ 话题标签：{' '.join(result['tags'])}")
    output.append(f"\n💬 互动问题：\n  • 经验：{result['interaction']['experience']}\n  • 观点：{result['interaction']['opinion']}\n  • 资源：{result['interaction']['resource']}")
    output.append(f"\n📣 CTA 策略：\n  • 硬转化：{result['cta']['hard']}\n  • 软引导：{result['cta']['soft']}")
    output.append("=" * 50)
    return "\n".join(output)

def format_keywords_output(result, topic):
    """格式化词库输出"""
    output = []
    output.append("=" * 50)
    output.append(f"🔥 热点词库 - {topic}")
    output.append("=" * 50)
    output.append(f"\n🔥 热搜词库")
    for kw, growth in result['hot']:
        output.append(f"   {kw}（↑{growth}%）")
    output.append(f"\n🌿 长尾词库")
    for kw in result['longtail']:
        output.append(f"   {kw}")
    output.append(f"\n💡 标题改造")
    for rw in result['rewrites']:
        output.append(f"   {rw}")
    output.append("=" * 50)
    return "\n".join(output)

def format_check_output(result, text):
    """格式化检测结果输出"""
    output = []
    output.append("=" * 50)
    output.append("🛡️ 违禁词检测报告")
    output.append("=" * 50)
    output.append(f"\n📄 检测文本：{text[:50]}...")
    output.append(f"\n📊 综合风险等级：{result['level']}（发现{result['count']}处问题）\n")
    
    if result['violations']:
        for i, v in enumerate(result['violations'], 1):
            output.append(f"🚨【违规词{i}】\"{v['word']}\"")
            output.append(f"   类型：{v['category']}类违规")
            output.append(f"   建议改为：\"{v['suggestion']}\"")
            output.append("")
    else:
        output.append("✅ 未发现明显违规词")
    
    output.append("=" * 50)
    return "\n".join(output)

# ==================== 主程序 ====================

def main():
    if len(sys.argv) < 2:
        print("小红书生成大师 - 一站式内容创作工具")
        print("\n用法：xiaohongshu <command> [input]")
        print("\n命令:")
        print("  post <主题>        生成爆款帖子")
        print("  keywords <主题>    生成热点词库")
        print("  check \"<文本>\"     违禁词检测")
        print("\n示例:")
        print("  xiaohongshu post 学渣逆袭")
        print("  xiaohongshu keywords 通勤穿搭")
        print("  xiaohongshu check \"这款面膜全网销量第一\"")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == 'post':
        if len(sys.argv) < 3:
            print("❌ 请提供主题，例如：xiaohongshu post 学渣逆袭")
            sys.exit(1)
        topic = " ".join(sys.argv[2:])
        result = generate_post(topic)
        print(format_post_output(result))
    
    elif command == 'keywords':
        if len(sys.argv) < 3:
            print("❌ 请提供主题，例如：xiaohongshu keywords 通勤穿搭")
            sys.exit(1)
        topic = " ".join(sys.argv[2:])
        result = generate_keywords(topic)
        print(format_keywords_output(result, topic))
    
    elif command == 'check':
        if len(sys.argv) < 3:
            print("❌ 请提供检测文本，例如：xiaohongshu check \"这款面膜全网销量第一\"")
            sys.exit(1)
        text = " ".join(sys.argv[2:])
        result = check_banned_words(text)
        print(format_check_output(result, text))
    
    else:
        print(f"❌ 未知命令：{command}")
        print("可用命令：post, keywords, check")
        sys.exit(1)

if __name__ == "__main__":
    main()
