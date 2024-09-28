def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызов inner_function внутри test_function
    inner_function()


# Вызовем test_function, чтобы увидеть результат
test_function()

# Попробуем вызвать inner_function вне test_function
try:
    inner_function()  # Это вызовет ошибку
except NameError as e:
    print(f"Ошибка: {e}")  # Выводим сообщение об ошибке



