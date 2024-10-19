"""Задача "Найдёт везде":
Напишите класс WordsFinder, объекты которого создаются следующим образом:
WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов
и записывать их в атрибут file_names в виде списка или кортежа.
"""

import string


class WordsFinder:
    def __init__(self, *file_names):
        # Сохраняем имена файлов в виде кортежа
        self.file_names = file_names

    def get_all_words(self):
        # Создаем пустой словарь для хранения файлов и их слов
        all_words = {}

        # Перебираем названия файлов и открываем каждый из них
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read()  # Читаем содержимое файла
                    content = content.lower()  # Переводим в нижний регистр

                    # Убираем пунктуацию
                    translator = str.maketrans("", "", string.punctuation)
                    content = content.translate(translator)

                    # Разбиваем строку на слова
                    words = content.split()

                    # Добавляем в словарь: ключ - название файла, значение - список слов
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
                all_words[file_name] = []  # Для отсутствующих файлов создаем пустой список

        return all_words

    def find(self, word):
        # Получаем все слова из файлов
        all_words = self.get_all_words()
        result = {}

        # Перебираем все файлы и их слова
        for file_name, words in all_words.items():
            # Приводим слово для поиска к нижнему регистру
            word_lower = word.lower()
            # Проверяем, есть ли слово в списке слов
            if word_lower in words:
                position = words.index(word_lower) + 1  # Позиция слова (считаем с 1)
                result[file_name] = position

        return result

    def count(self, word):
        # Получаем все слова из файлов
        all_words = self.get_all_words()
        result = {}

        # Перебираем все файлы и их слова
        for file_name, words in all_words.items():
            # Приводим слово для подсчета к нижнему регистру
            word_lower = word.lower()
            count = words.count(word_lower)  # Подсчитываем количество вхождений
            result[file_name] = count

        return result


# Пример использования
if __name__ == "__main__":
    finder2 = WordsFinder('test_file.txt')

    # Получение всех слов из файла
    print(finder2.get_all_words())

    # Поиск позиции слова
    print(finder2.find('TEXT'))  # Позиция слова 'TEXT'

    # Подсчет количества вхождений слова
    print(finder2.count('teXT'))  # Количество слов 'teXT'