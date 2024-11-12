import threading

from random import randint
from time import sleep

lock = threading.Lock()

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = lock

    def deposit(self):
        for i in range(100):
            random_num = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += random_num
            print(f'Пополнение: {random_num}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            random_num = randint(50, 500)
            print(f'запрос на {random_num}')
            if random_num <= self.balance:
                self.balance -= random_num
                print(f'Снятие: {random_num}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')