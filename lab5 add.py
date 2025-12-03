import re

with open('task_add.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. 日期（5个）
date_patterns = [
    r'\s(\d{4}[-/.]\d{1,2}[-/.]\d{1,2})',
    r'\s(\d{1,2}[-/.]\d{1,2}[-/.]\d{4})',
    r'\s(\d{1,2}\s+[A-Za-z]{3,9}\s+\d{4})',
    r'\s([A-Za-z]{3,9}\s+\d{1,2},?\s+\d{4})',
]

dates = []
for pattern in date_patterns:
    dates.extend(re.findall(pattern, text))
dates = dates[:5]
print(f"找到的日期: {dates}")

# 2. 邮箱地址（5个）
emails = re.findall(r'\s([\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,})', text)[:5]
print(f"找到的邮箱: {emails}")

# 3. 网站地址（5个）
websites = re.findall(r'\s((?:https?://)?(?:www\.)?[\w.-]+\.[a-zA-Z]{2,})', text)[:5]
print(f"找到的网站: {websites}")