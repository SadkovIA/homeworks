"""Цель: освоить блокировки потоков, используя объекты класса Lock и его методы.

Задача "Банковские операции":"""


import threading

from random import randint
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0  # Устанавливаем начальный баланс
        self.lock = threading.Lock()  # Создаем объект блокировки

    def deposit(self):
        for i in range(100):  # Производим 100 транзакций пополнения
            with self.lock:  # Используем блокировку
                sleep(0.001)  # Имитируем скорость выполнения
                deposit_amount = randint(50, 500)  # Случайная сумма для пополнения
                self.balance += deposit_amount  # Увеличиваем баланс
                if self.balance >= 500 and self.lock.locked():  # Если баланс больше или равен 500 и замок заблокирован
                    self.lock.release()  # Разблокируем его
            print(f'Пополнение: {deposit_amount}. Баланс: {self.balance}')  # Выводим информацию о пополнении

    def take(self):
        for i in range(100):  # Производим 100 транзакций снятия
            with self.lock:  # Используем блокировку
                sleep(0.001)  # Имитируем скорость выполнения
                take_amount = randint(50, 500)  # Случайная сумма для снятия
                print(f'Запрос на {take_amount}')  # Выводим информацию о запросе
                if take_amount <= self.balance:  # Если сумма снятия меньше или равна балансу
                    self.balance -= take_amount  # Уменьшаем баланс
                    print(f'Снятие: {take_amount}. Баланс: {self.balance}')  # Выводим информацию о снятии
                else:  # Если сумма снятия больше баланса
                    print('Запрос отклонён, недостаточно средств')  # Выводим сообщение об ошибке
                    self.lock.acquire()  # Блокируем поток

bk = Bank()  # Создаем объект класса Bank

# Создаем 2 потока для методов deposit и take
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()  # Запускаем потоки
th2.start()

th1.join()  # Ждем завершения потока
th2.join()  # Ждем завершения потока

print(f'Итоговый баланс: {bk.balance}')  # Выводим итоговый баланс