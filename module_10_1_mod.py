
"""Улучшения:
Использование кортежей: Вместо нескольких отдельных переменных для названий файлов и их количеств, я использую списки кортежей. 
Это позволяет легко добавлять или изменять набор данных.
Циклы для вызовов функций: Я использую один цикл для запуска функций write_words и замера времени, что делает код более компактным.
Функция main(): Основные операции помещены в функцию main(), что делает структуру программы более организованной и удобочитаемой.
Упрощенный вывод: Я вынес вывод времени для каждого файла в отдельный цикл, что позволяет избежать дублирования кода и делать его более лаконичным.
Импорт модуля signal: Этот модуль позволяет управлять сигналами.
Добавлен обработчик сигналов signal_handler: При получении сигнала SIGINT (например, Ctrl+F2), программа выводит сообщение о прерывании,
ожидает завершения всех потоков и завершает выполнение.
Список threads: Я добавил глобальный список threads для хранения всех созданных потоков.
Это позволяет ожидать их завершения в обработчике сигналов."""

import threading
import signal
import sys

from time import sleep, time

# Список потоков для отслеживания
threads = []


def write_words(word_count, file_name):
    """Записывает заданное количество слов в файл с паузой."""
    try:
        with open(file_name, 'w', encoding='utf-8') as f:
            for i in range(1, word_count + 1):
                f.write(f'Какое-то слово № {i}\n')
                sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')
    except Exception as e:
        print(f'Ошибка при записи в файл {file_name}: {e}')


def measure_time(func, *args):
    """Замеряет время выполнения функции."""
    start_time = time()
    func(*args)
    return time() - start_time


def signal_handler(sig, frame):
    """Обработчик сигналов для прерывания программы."""
    print("\nПрограмма прервана. Ожидание завершения потоков...")
    for thread in threads:
        thread.join()  # Ждем завершения потоков
    sys.exit(0)  # Завершение программы


def main():
    # Установка обработчика сигнала
    signal.signal(signal.SIGINT, signal_handler)

    # Запуск функций и вывод времени записи
    files = [('example1.txt', 10), ('example2.txt', 30),
             ('example3.txt', 200), ('example4.txt', 100)]

    total_time = sum(measure_time(write_words, count, name) for name, count in files)

    print(f'Общее время записи: {total_time:.6f} секунд')

    # Создание и запуск потоков
    files_to_thread = [('example5.txt', 10), ('example6.txt', 30),
                       ('example7.txt', 200), ('example8.txt', 100)]

    time5_start = time()

    for name, count in files_to_thread:
        thread = threading.Thread(target=write_words, args=(count, name))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Работа потоков {time() - time5_start:.6f} секунд')


if __name__ == '__main__':
    main()