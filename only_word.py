import json

# 打开你的json文件
list_ap = []

with open('CET6_3.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.replace('{', '')
        line = line.split('"')[5]
        list_ap.append(line)

with open('333.txt', 'w') as f:
    for line in list_ap:
        f.write(line + '\n')
