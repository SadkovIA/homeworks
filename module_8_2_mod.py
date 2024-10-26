def personal_sum(numbers):
    result, incorrect_data = 0, 0

    for number in numbers:
        if isinstance(number, (int, float)):
            result += number
        else:
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    if not isinstance(numbers, (list, tuple, set)):
        print('В numbers записан некорректный тип данных')
        return None

    total_sum, incorrect_count = personal_sum(numbers)
    valid_count = len(numbers) - incorrect_count

    return total_sum / valid_count if valid_count > 0 else 0

# Примеры вызовов функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать