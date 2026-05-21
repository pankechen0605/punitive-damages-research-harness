# 工具脚本

## pdf_to_md.py

一个低保真 PDF 转 Markdown 工具。

### 功能

- 输入一个 PDF 文件或一个目录
- 输出 Markdown 文件，保留页码和段落
- 每页前加 `<!-- page: N -->` 标记
- 输出 YAML frontmatter（源文件、提取方式、生成时间）
- 如果提取不到文字，标记 `[NO TEXT EXTRACTED - OCR MAY BE REQUIRED]`

### 使用方式

```bash
# 转换单个文件
python scripts/pdf_to_md.py --input path/to/file.pdf --output 0_raw/papers/extracted_md/

# 转换整个目录
python scripts/pdf_to_md.py --input path/to/pdf_dir --output 0_raw/papers/extracted_md/

# 查看帮助
python scripts/pdf_to_md.py --help
```

### 依赖

```bash
pip install pymupdf
```

### 重要说明

- **PDF 原文仍然是底本**，extracted_md 只是 AI 读取副本。
- 不做 OCR，扫描件可能无法提取文字。
- 输出不是最终摘要，只是机器可读副本。
