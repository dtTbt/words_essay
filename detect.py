import os.path

day = 2
book = 'CET6_1228'

split_book_name = book + '_s.txt'
essays_folder_path = os.path.join('essays', split_book_name[:-6])
essay_path = os.path.join(essays_folder_path, str(day) + '.txt')
with open(essay_path, 'r', encoding='utf-8') as f:
    txt = f.read()
    txt = txt.strip()
    words = []
    day_now = 0
    with open('split_books/' + split_book_name, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if day_now == day:
                words = line.replace(',', '').strip().split(' ')
                break
            if line[-1] == '.':
                day_now = int(line[:-1])
                continue
    next_book_words =[]
    next_book_path = 'next_books/' + split_book_name[:-6] + '_n.txt'
    if not os.path.exists(next_book_path):
        with open(next_book_path, 'w') as file:
            pass
    with open(next_book_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            next_book_words.append(line)
    for word in words:
        if word not in txt:
            next_book_words.append(word)
    with open(next_book_path, 'w') as file:
        for line in next_book_words:
            print(line)
            file.write(line + '\n')
