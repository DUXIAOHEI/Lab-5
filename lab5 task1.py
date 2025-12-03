import re

with open(r'C:/Users/32589/Desktop/VS Code/.vscode/task1-en.txt', 'r', encoding='utf-8') as f:
    text = f.read()

integers = re.findall(r'\b[0-9]\b', text)
print(f"小于10的整数: {integers}")

alphanumeric = re.findall(r'\b(?=\w*\d)(?=\w*[a-zA-Z])\w+\b', text)
print(f"字母数字组合: {alphanumeric[:10]}...")
print(f"共找到 {len(alphanumeric)} 个字母数字组合")