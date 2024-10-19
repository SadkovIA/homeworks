"""Задача "Записать и запомнить":
Создайте функцию custom_write(file_name, strings),
которая принимает аргументы file_name - название файла для записи,
strings - список строк для записи."""


def custom_write(file_name, strings):
    strings_positions = {}  # Создаем пустой словарь для хранения позиций строк
    # Открываем файл для записи в режиме "w" с кодировкой "utf-8"
    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings, start=1):  # Проходим по всем строкам из списка strings
            byte_start = file.tell()  # Получаем текущую позицию байта
            file.write(string + '\n')  # Записываем строку в файл с переводом строки
            strings_positions[(index, byte_start)] = string  # Сохраняем в словарь

    return strings_positions   # Возвращаем словарь с записями


# Пример выполняемого кода
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)