def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding = 'utf-8')
    dict = {}
    line = 1
    for string in strings:
        position = file.tell()
        file.write(string + '\n')
        dict[(line, position)] = string
        line += 1
    file.close()
    return dict

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)