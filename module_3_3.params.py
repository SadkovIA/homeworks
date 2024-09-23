def print_params(a = 1, b = 'строка', c = True):
    print(a, b , c)

print_params()  # без аргументов
print_params(25)  # с одним аргументом
print_params(b=25)  # с именованным аргументом
print_params(c=[1, 2, 3])  # с именованным аргументом

values_list = [3.14, 'hello', False]
values_dict = {'a': 42, 'b': 'world', 'c': None}

print_params(*values_list)  # распаковка списка
print_params(**values_dict)  # распаковка словаря

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  # распаковка списка + отдельный параметр