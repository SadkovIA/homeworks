def add_everything_up(a, b):
    try:
        result = a + b
        return round(result, 3) if isinstance(result, (int, float)) else str(result)
    except TypeError:
        return str(a) + str(b)


# Примеры использования
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))  # Вывод: яблоко4215
print(add_everything_up(123.456, 7))  # Вывод: 130.456
