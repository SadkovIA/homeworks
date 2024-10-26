class IncorrectVinNumber(Exception):
    pass

class IncorrectCarNumbers(Exception):
    pass

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = self.__is_valid_vin(vin)
        self.__numbers = self.__is_valid_numbers(numbers)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int) or not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Некорректный vin номер')
        return vin_number

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str) or len(numbers) != 6:
            raise IncorrectCarNumbers('Некорректный номер автомобиля')
        return numbers

# Пример выполняемого кода:
for model, vin, numbers in [
    ('Model1', 1000000, 'f123dj'),
    ('Model2', 300, 'т001тр'),
    ('Model3', 2020202, 'нет номера')
]:
    try:
        car = Car(model, vin, numbers)
    except IncorrectVinNumber as exc:
        print(exc)
    except IncorrectCarNumbers as exc:
        print(exc)
    else:
        print(f'{car.model} успешно создан')