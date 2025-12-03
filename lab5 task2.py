import re

with open(r'C:/Users/32589/Desktop/VS Code/.vscode/task2.html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = r'(?:src|href|content)\s*=\s*["\']([^"\']+\.(?:png|jpg|jpeg|gif|svg|webp)(?:[\?#][^"\']*)?)["\']'

image_links = re.findall(pattern, content, re.IGNORECASE)

unique_links = list(set(image_links))

print(f"找到 {len(unique_links)} 个唯一的图片链接：\n")
for i, link in enumerate(unique_links, 1):
    print(f"{i:3}. {link}")