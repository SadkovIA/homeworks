"""Цель: понять как работают потоки на практике, решив задачу

Задача "Потоковая запись в файлы":
Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>"."""


import threading
from time import sleep, time

# функция для записи слов в файл:
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(word_count):
            f.write(f'Какое-то слово № {i + 1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

# Функция для замера времени выполнения:
def measure_time(func, *args):
    start_time = time()
    func(*args)
    end_time = time()
    return end_time - start_time
# После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:
if __name__ == '__main__':
    time_1 = measure_time(write_words, 10, 'file_1.txt')
    time_2 = measure_time(write_words, 30, 'file_2.txt')
    time_3 = measure_time(write_words, 200, 'file_3.txt')
    time_4 = measure_time(write_words, 100, 'file_4.txt')
    print(f'Время записи в файл file_1.txt: {time_1}')
    print(f'Время записи в файл file_2.txt: {time_2}')
    print(f'Время записи в файл file_3.txt: {time_3}')
    print(f'Время записи в файл file_2.txt: {time_4}')
    print(f'Время работы потоков: {time_1 + time_2 + time_3 + time_4:.6f} секунд')

#После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
# Создание и запуск потоков
    threads = []
    time5_start = time()

    # Создание потоков с аргументами
    thread1 = threading.Thread(target=write_words, args=(10, 'file_5.txt'))
    thread2 = threading.Thread(target=write_words, args=(30, 'file_6.txt'))
    thread3 = threading.Thread(target=write_words, args=(200, 'file_7.txt'))
    thread4 = threading.Thread(target=write_words, args=(100, 'file_8.txt'))

    # Запуск потоков
    threads += [thread1, thread2, thread3, thread4]
    for thread in threads:
        thread.start()

    # Ожидание завершения потоков
    for thread in threads:
        thread.join()

    time5_end = time()
    print(f'Работа потоков {time5_end - time5_start:.6f} секунд')

# Вывод на консоль:
# Завершилась запись в файл example1.txt
# Завершилась запись в файл example2.txt
# Завершилась запись в файл example3.txt
# Завершилась запись в файл example4.txt
# Работа потоков 0:00:34.003411 # Может быть другое время
# Завершилась запись в файл example5.txt
# Завершилась запись в файл example6.txt
# Завершилась запись в файл example8.txt
# Завершилась запись в файл example7.txt
# Работа потоков 0:00:20.071575 # Может быть другое время
