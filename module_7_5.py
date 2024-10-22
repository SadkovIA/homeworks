"""Цель задания:
Освоить работу с файловой системой в Python, используя модуль os.
Научиться применять методы
os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize
и использование модуля time для корректного отображения времени."""

import os
import time

# Укажите путь к каталогу
directory = "."

# Обход каталога с использованием os.walk
for root, dirs, files in os.walk(directory):
    for file in files:
        # Формирование полного пути к файлу
        filepath = os.path.join(root, file)

        # Получение времени последнего изменения
        filetime = os.path.getmtime(filepath)

        # Форматирование времени
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получение размера файла
        filesize = os.path.getsize(filepath)

        # Получение родительской директории
        parent_dir = os.path.dirname(filepath)

        # Печать информации о файле
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')