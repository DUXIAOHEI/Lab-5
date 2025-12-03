import re
import csv

with open(r'C:/Users/32589/Desktop/VS Code/.vscode/task3.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

patterns = {
    'ID': [r'\b\d{1,5}\b', r'\bID[_-]?\d+\b', r'\b[A-Z]{2}\d{3,5}\b'],
    'Surname': [r'\b[A-Z][a-z]{2,20}\b'],
    'Email': [r'\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}\b'],
    'Date': [
        r'\b\d{4}[-/]\d{1,2}[-/]\d{1,2}\b',
        r'\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b',
        r'\b\d{1,2}\.\d{1,2}\.\d{4}\b'
    ],
    'Website': [
        r'\bhttps?://(?:www\.)?[\w.-]+\.[a-zA-Z]{2,}\b',
        r'\bwww\.[\w.-]+\.[a-zA-Z]{2,}\b'
    ]
}

def identify_field(text):
    for field, field_patterns in patterns.items():
        for pattern in field_patterns:
            if re.fullmatch(pattern, text.strip()):
                return field
    return None

organized_data = []
for line in lines:
    items = re.split(r'[,\s;]+', line.strip())
    items = [item for item in items if item]
    
    row = {'ID': 'N/A', 'Surname': 'N/A', 'Email': 'N/A', 'Date': 'N/A', 'Website': 'N/A'}
    
    for item in items:
        field = identify_field(item)
        if field and row[field] == 'N/A':
            row[field] = item
        elif not field:
            if '@' in item and '.' in item and row['Email'] == 'N/A':
                row['Email'] = item
            elif re.search(r'http|www', item, re.I) and row['Website'] == 'N/A':
                row['Website'] = item
    
    organized_data.append([row['ID'], row['Surname'], row['Email'], row['Date'], row['Website']])

with open('organized_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Surname', 'Email', 'Date', 'Website'])
    writer.writerows(organized_data)

print(f"已保存 {len(organized_data)} 行数据到 organized_data.csv")