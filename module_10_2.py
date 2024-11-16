"""Цель: научиться создавать классы наследованные от класса Thread.

Задача "За честь и отвагу!":"""


import threading

from time import sleep


print(f'Урки мои верные, в акаку!!!')

class Knight(threading.Thread):  # Наследуемся от класса threading. Thread
    def __init__(self, name: str, power: int):
        super().__init__()  # Вызов конструктора родительского класса
        self.name = name
        self.power = power
        self.days = 0
        self.enemies_alive = total_enemies

    def run(self):  # Запуск потока
        print(f'{self.name}, на нас напали!')
        print(f'{self.name}, за моего отца, за Лордерон!!!')
        while self.enemies_alive > 0:
            sleep(1)  # Задержка, чтобы симулировать время боя
            self.days += 1
            self.enemies_alive -= self.power
            # Проверяем, чтобы не было отрицательных значений врагов
            if self.enemies_alive < 0:
                self.enemies_alive = 0
            print(f'{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies_alive} воинов.')

        print(f'{self.name} одержал победу спустя {self.days} день(дня)!')

total_enemies = 100
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

# Ждем окончания сражений
first_knight.join()
second_knight.join()

print("Все битвы закончились!")
# Вывод на консоль:
# Sir Lancelot, на нас напали!
# Sir Lancelot, сражается 1 день(дня)..., осталось 90 воинов.
# Sir Galahad, на нас напали!
# Sir Galahad, сражается 1 день(дня)..., осталось 80 воинов.
# Sir Galahad, сражается 2 день(дня)..., осталось 60 воинов.
# Sir Lancelot, сражается 2 день(дня)..., осталось 80 воинов.
# Sir Lancelot, сражается 3 день(дня)..., осталось 70 воинов.
# Sir Galahad, сражается 3 день(дня)..., осталось 40 воинов.
# Sir Lancelot, сражается 4 день(дня)..., осталось 60 воинов.
# Sir Galahad, сражается 4 день(дня)..., осталось 20 воинов.
# Sir Galahad, сражается 5 день(дня)..., осталось 0 воинов.
# Sir Lancelot, сражается 5 день(дня)..., осталось 50 воинов.
# Sir Lancelot, сражается 6 день(дня)..., осталось 40 воинов.
# Sir Galahad одержал победу спустя 5 дней(дня)!
# Sir Lancelot, сражается 7 день(дня)..., осталось 30 воинов.
# Sir Lancelot, сражается 8 день(дня)..., осталось 20 воинов.
# Sir Lancelot, сражается 9 день(дня)..., осталось 10 воинов.
# Sir Lancelot, сражается 10 день(дня)..., осталось 0 воинов.
# Sir Lancelot одержал победу спустя 10 дней(дня)!
# Все битвы закончились!