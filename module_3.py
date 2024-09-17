calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    length = len(string)
    upper_string = string.upper()
    lower_string = string.lower()
    return (length, upper_string, lower_string)

def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    # Приводим строку и все строки в списке к одному регистру
    string_lower = string.lower()
    return any(string_lower == item.lower() for item in list_to_search)

# Примеры вызова функций
print(string_info('Capybara'))  # Например, (8, 'CAPYBARA', 'capybara')
print(string_info('Armageddon'))  # Например, (10, 'ARMAGEDDON', 'armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # True
print(is_contains('cycle', ['recycling', 'cyclic']))  # False

# Вывод общего количества вызовов функций
print(calls)