#!/usr/bin/env python3
"""clean_pkulaw.py — 清理北大法宝剪藏文件中的网页噪音"""

import os
import re
import sys
from pathlib import Path


def clean_pkulaw_content(text: str) -> str:
    """清理北大法宝剪藏内容，只保留案例正文。"""
    lines = text.split("\n")
    result = []
    in_content = False
    content_started = False

    # 找到 YAML frontmatter 结束位置
    fm_end = 0
    after_dash = 0
    for i, line in enumerate(lines):
        if line.strip() == "---" and i > 0:
            fm_end = i + 1
            break

    # 保留 frontmatter 但清理 description
    frontmatter = []
    for i in range(fm_end):
        line = lines[i]
        if line.startswith("description:"):
            line = 'description: ""'
        frontmatter.append(line)

    # 从 frontmatter 之后开始扫描正文
    i = fm_end
    skip_until_content = True

    while i < len(lines):
        line = lines[i]

        # 跳过 frontmatter 后到正文之间的所有网页噪音
        if skip_until_content:
            # 检测正文开始：以【法宝引证码】或案号信息或案件标题开始
            if "【法宝引证码】" in line or "法宝引证码" in line:
                skip_until_content = False
                in_content = True
                result.append(line)
            elif re.match(r'^- \*\*案\s*号：\*\*', line):
                skip_until_content = False
                in_content = True
                result.append(line)
            i += 1
            continue

        if in_content:
            # 检测正文结束标志
            if line.strip().startswith("- 最新推出") and "法宝智能订阅" in line:
                break
            if line.strip().startswith("北大法宝1985年创始于"):
                break
            if line.strip().startswith("#### 法宝产品资讯"):
                break
            if line.strip().startswith("### 法宝联想"):
                break
            if line.strip().startswith("已进入法宝V6"):
                break
            if line.strip().startswith("已开启安全支付"):
                break
            if line.strip().startswith("法宝V5已停止运营"):
                break

            # 跳过 action buttons 区域
            if line.strip() in ["加入类案报告", "复制全文", "打印", "*下载*", "下载",
                                 " 保留字段信息", "保留本篇右侧的法宝联想",
                                 "分享", "法宝版", "法宝版 纯净版"]:
                i += 1
                continue

            # 跳过页面宽度设置
            if "页面宽度(px)" in line or "页面宽度范围为" in line:
                i += 1
                continue

            # 跳过导航链接
            if line.strip() in ['[Previous](# "Previous") [Next](# "Next")']:
                i += 1
                continue

            # 跳过监控日报
            if "监控日报" in line or "您的订阅推送" in line:
                i += 1
                continue

            # 跳过续费/满意度
            if "立即续费" in line or "满意度调查" in line:
                i += 1
                continue

            # 跳过 CARSI 登录
            if "CARSI" in line or "Caris登录" in line or "个人账号登录" in line:
                i += 1
                continue

            # 跳过 V6 升级提示
            if "已进入法宝V6" in line or "您所在高校已由IP登录" in line:
                i += 1
                continue

            # 跳过图片链接
            if line.strip().startswith("![](https://libresource"):
                i += 1
                continue

            # 跳过目录区域
            if line.strip() == "目录" and i + 1 < len(lines) and lines[i+1].strip() == "目录":
                i += 2
                continue

            # 跳过高亮设置代码块
            if line.strip() == "```" and i + 1 < len(lines) and "高亮设置" in lines[i+1]:
                # 跳过整个代码块
                i += 1
                while i < len(lines) and lines[i].strip() != "```":
                    i += 1
                i += 1  # 跳过结束的 ```
                continue

            # 跳过 "[查看更多]" 链接
            if line.strip().startswith("[查看更多]") and "apps/sub" in line:
                i += 1
                continue

            # 跳过 "数据库即将到期"
            if "数据库即将到期" in line:
                i += 1
                continue

            # 跳过空的锚点链接行
            if re.match(r'^\[(当事人|审理经过|二审上诉人诉称|原告诉称|一审法院查明|一审法院认为|本院查明|本院认为|争议焦点|裁判依据|裁判结果|落款|裁判要旨|案情|审判|评析|关键词|裁判要点|相关法条|基本案情|裁判理由)\]', line.strip()):
                i += 1
                continue

            result.append(line)

        i += 1

    # 清理尾部空行
    while result and result[-1].strip() == "":
        result.pop()

    # 重建 frontmatter
    cleaned_frontmatter = "\n".join(frontmatter)
    cleaned_content = "\n".join(result)

    return cleaned_frontmatter + "\n" + cleaned_content + "\n"


def process_file(input_path: str, output_path: str):
    """处理单个文件。"""
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    cleaned = clean_pkulaw_content(content)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(cleaned)


def main():
    input_dir = sys.argv[1] if len(sys.argv) > 1 else "Clippings"
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "0_raw/authoritative_cases/typical_cases"

    input_dir = os.path.abspath(input_dir)
    output_dir = os.path.abspath(output_dir)

    if not os.path.isdir(input_dir):
        print(f"错误：目录不存在：{input_dir}", file=sys.stderr)
        sys.exit(1)

    md_files = sorted([f for f in os.listdir(input_dir) if f.endswith(".md")])

    if not md_files:
        print(f"警告：目录中没有 .md 文件：{input_dir}")
        return

    for md_file in md_files:
        input_path = os.path.join(input_dir, md_file)
        output_path = os.path.join(output_dir, md_file)
        process_file(input_path, output_path)
        print(f"已清理：{md_file}")

    print(f"\n共清理 {len(md_files)} 个文件，输出到：{output_dir}")


if __name__ == "__main__":
    main()
