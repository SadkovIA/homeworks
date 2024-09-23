def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если длина строки равна 1, возвращаем единственную цифру
    if len(str_number) <= 1:
        return int(str_number)

    # Получаем первую цифру и преобразуем её в целое число
    first = int(str_number[0])

    # Рекурсивно вызываем функцию для оставшейся части строки
    return first * get_multiplied_digits(int(str_number[1:]))


# Пример использования
result = get_multiplied_digits(140587)
print(result)