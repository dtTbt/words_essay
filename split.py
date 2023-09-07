index = 0
num = 15
list_tmp = []
with open('1.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        index += 1
        if index % num == 1:
            list_tmp.append(str(( index // num ) + 1) + '.')
        list_tmp.append(line)

with open('11.txt', 'w') as f:
    for line in list_tmp:
        if line[-1] == '.':
            if line.replace('.','') == '1':
                f.write(line + '\n')
            else:
                f.write('\n' + line + '\n')
        else:
            f.write(line + ', ')
