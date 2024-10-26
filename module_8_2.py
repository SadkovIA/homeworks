"""Задача "План перехват":
Напишите 2 функции:
Функция personal_sum(numbers),
Функция calculate_average(numbers)"""


def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for number in numbers:
        if isinstance(number, (int, float)):
            result += number
        else:
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        # Проверяем, является ли numbers коллекцией
        if not isinstance(numbers, (list, tuple, set)):
            raise TypeError

        total_sum, incorrect_count = personal_sum(numbers)

        # Вычисляем среднее, если некорректных данных нет
        count = len([num for num in numbers if isinstance(num, (int, float))])
        if count == 0:
            return 0

        average = total_sum / count
        return average

    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


# Примеры вызовов функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
