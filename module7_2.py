from pprint import pprint

def custom_write(file_name, strings):
    string_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for index, string in enumerate(strings):
        key = (index+1, file.tell())
        string_positions[key] = string
        file.write(string + '\n')
    file.close()
    return string_positions

info = ['Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!']
custom_write('Test_File.txt', info)
result = custom_write('Test_File.txt', info)
for elem in result.items():
    print(elem)