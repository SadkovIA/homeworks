def calculate_structure_sum(data):
    total_sum = 0

    # Обрабатываем каждый элемент в структуре данных
    for element in data:
        # Если элемент - это число, добавляем его к сумме
        if isinstance(element, (int, float)):
            total_sum += element
        # Если элемент - это строка, добавляем её длину к сумме
        elif isinstance(element, str):
            total_sum += len(element)
        # Если элемент - это список, кортеж или множество, рекурсивно вызываем функцию
        elif isinstance(element, (list, tuple, set)):
            total_sum += calculate_structure_sum(element)
        # Если элемент - это словарь, обрабатываем ключи и значения
        elif isinstance(element, dict):
            # Обрабатываем ключи
            for key in element:
                if isinstance(key, (int, float)):
                    total_sum += key
                elif isinstance(key, str):
                    total_sum += len(key)
            # Обрабатываем значения
            for value in element.values():
                if isinstance(value, (int, float)):
                    total_sum += value
                elif isinstance(value, str):
                    total_sum += len(value)
                # Если значение - это список, кортеж или множество, рекурсивно вызываем функцию
                elif isinstance(value, (list, tuple, set)):
                    total_sum += calculate_structure_sum(value)
                # Если значение - это словарь, обрабатываем его
                elif isinstance(value, dict):
                    total_sum += calculate_structure_sum(value)

    return total_sum

# Пример использования
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)  # Вывод: 99