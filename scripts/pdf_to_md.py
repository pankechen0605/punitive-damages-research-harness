#!/usr/bin/env python3
"""
pdf_to_md.py — 低保真 PDF 转 Markdown 工具

功能：
- 将 PDF 文件转为 Markdown，保留页码和段落
- 每页前加 <!-- page: N --> 标记
- 输出 YAML frontmatter
- 如果提取不到文字，标记 [NO TEXT EXTRACTED - OCR MAY BE REQUIRED]

注意：
- PDF 原文仍然是底本
- extracted_md 只是 AI 读取副本，不是最终摘要
- 不做 OCR
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path


def extract_pdf_to_md(pdf_path: str) -> str:
    """从 PDF 提取文本并转为 Markdown 格式。"""
    try:
        import fitz  # pymupdf
    except ImportError:
        print("错误：请先安装 pymupdf：pip install pymupdf", file=sys.stderr)
        sys.exit(1)

    doc = fitz.open(pdf_path)
    source_file = os.path.basename(pdf_path)
    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # YAML frontmatter
    lines = [
        "---",
        f"source_file: {source_file}",
        "extraction_method: pymupdf",
        f"generated_at: {generated_at}",
        "type: extracted_md",
        "---",
        "",
    ]

    has_text = False

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()

        lines.append(f"<!-- page: {page_num + 1} -->")
        lines.append("")

        if text.strip():
            has_text = True
            lines.append(text.strip())
        else:
            lines.append("[NO TEXT EXTRACTED - OCR MAY BE REQUIRED]")

        lines.append("")

    doc.close()

    if not has_text:
        lines.append("")
        lines.append("[全文未提取到文字 - 可能是扫描件，需要 OCR]")

    return "\n".join(lines)


def process_single_file(pdf_path: str, output_dir: str) -> str:
    """处理单个 PDF 文件，返回输出文件路径。"""
    pdf_path = os.path.abspath(pdf_path)
    output_dir = os.path.abspath(output_dir)

    if not os.path.isfile(pdf_path):
        print(f"错误：文件不存在：{pdf_path}", file=sys.stderr)
        sys.exit(1)

    if not pdf_path.lower().endswith(".pdf"):
        print(f"错误：不是 PDF 文件：{pdf_path}", file=sys.stderr)
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)

    # 生成输出文件名
    stem = Path(pdf_path).stem
    output_path = os.path.join(output_dir, f"{stem}.md")

    # 提取并写入
    md_content = extract_pdf_to_md(pdf_path)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    return output_path


def process_directory(input_dir: str, output_dir: str) -> list:
    """处理目录中的所有 PDF 文件，返回输出文件路径列表。"""
    input_dir = os.path.abspath(input_dir)
    output_dir = os.path.abspath(output_dir)

    if not os.path.isdir(input_dir):
        print(f"错误：目录不存在：{input_dir}", file=sys.stderr)
        sys.exit(1)

    pdf_files = sorted(
        [f for f in os.listdir(input_dir) if f.lower().endswith(".pdf")]
    )

    if not pdf_files:
        print(f"警告：目录中没有 PDF 文件：{input_dir}", file=sys.stderr)
        return []

    output_paths = []
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_dir, pdf_file)
        output_path = process_single_file(pdf_path, output_dir)
        output_paths.append(output_path)
        print(f"已转换：{pdf_file} -> {os.path.basename(output_path)}")

    return output_paths


def main():
    parser = argparse.ArgumentParser(
        description="低保真 PDF 转 Markdown 工具",
        epilog=(
            "示例：\n"
            "  python pdf_to_md.py --input paper.pdf --output 0_raw/papers/extracted_md/\n"
            "  python pdf_to_md.py --input ./pdfs/ --output 0_raw/papers/extracted_md/"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--input",
        required=True,
        help="输入 PDF 文件路径或包含 PDF 的目录路径",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="输出目录路径",
    )

    args = parser.parse_args()

    input_path = os.path.abspath(args.input)
    output_dir = os.path.abspath(args.output)

    if os.path.isfile(input_path):
        output_path = process_single_file(input_path, output_dir)
        print(f"已转换：{os.path.basename(input_path)} -> {output_path}")
    elif os.path.isdir(input_path):
        output_paths = process_directory(input_path, output_dir)
        print(f"\n共转换 {len(output_paths)} 个文件，输出到：{output_dir}")
    else:
        print(f"错误：输入路径不存在：{input_path}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
