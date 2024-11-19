"""Цель: понять разницу между линейным и многопроцессным подходом, выполнив операции обоими способами.

Задача "Многопроцессное считывание"""

import time
from multiprocessing import Pool

def read_info(name):
    all_data = []  # Создаем локальный список для хранения данных
    try:
        with open(name, 'r') as file:  # Открываем файл для чтения
            while True:
                line = file.readline()  # Считываем строку
                if line == '':  # Проверяем, является ли строка пустой
                    break  # Выходим из цикла, если строка пустая
                all_data.append(line.strip())  # Добавляем строку в список
    except FileNotFoundError:
        print(f"Файл '{name}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]  # Список названий файлов

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f"{linear_duration:.6f} (линейный)")

    # Многопроцессный
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multiprocess_duration = time.time() - start_time
    print(f"{multiprocess_duration:.6f} (многопроцессный)")