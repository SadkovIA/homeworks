import threading

from random import randint
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 500
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            with self.lock:
                sleep(0.001)
                amount = randint(50, 500)
                self.balance += amount
                print(f'Пополнение: {amount}. Баланс: {self.balance}')

    def take(self):
        for _ in range(100):
            with self.lock:
                sleep(0.001)
                amount = randint(50, 500)
                print(f'Запрос на {amount}')
                if amount <= self.balance:
                    self.balance -= amount
                    print(f'Снятие: {amount}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств')

if __name__ == "__main__":
    bank = Bank()
    threads = [
        threading.Thread(target=bank.deposit),
        threading.Thread(target=bank.take)
    ]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print(f'Итоговый баланс: {bank.balance}')