"""Задание: Декораторы в Python
Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Напишите 2 функции:

Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime),
которая распечатывает "Простое", если результат 1ой функции будет простым числом и
"Составное" в противном случае.
"""
# Пример:
# result = sum_three(2, 3, 6)
# print(result)
#
# Результат консоли:
# Простое
# 11

def sum_three(a, b, c):
    result = a + b + c
    return result

# первый вариант
def is_prime(sum_three):
    def wrapper(*args, **kwargs):
        result = sum_three(*args, **kwargs)
        if result % 2 == 0:
            print("Составное")
        else:
            print("Простое")
        return result
    return wrapper

result = is_prime(sum_three)(2, 3, 6)
print(result)

#  второй вариант
@is_prime
def sum_three(a, b, c):
    result = a + b + c
    return result

print(sum_three(2, 3, 6))