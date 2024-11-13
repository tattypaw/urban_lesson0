from time import sleep
from random import randint
from queue import Queue
from threading import Thread
import threading

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name


    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *args):
        self.tables = []
        for arg in args:
            self.tables.append([arg.number, arg.guest])
        self.q = Queue()

    def guest_arrival(self, *args):
        for guest in args:
            check = True
            for i in range(len(self.tables)):
                if self.tables[i][1] == None:
                    self.tables[i][1] = guest.name
                    print(f'{guest.name} сел(-а) за стол номер {i + 1}')
                    guest.start()
                    guest.join()
                    check = False
                    break
            if check:
                self.q.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.q.empty():
            for i in range(len(self.tables)):
                if self.tables[i][1] != None:
                    if not Guest(self.tables[i][1]).is_alive():
                        print(f'{self.tables[i][1]} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {self.tables[i][0]} свободен')
                        self.tables[i][1] = None
                else:
                    self.tables[i][1] = self.q.get().name
                    print(f'{self.tables[i][1]} вышел(-ла) из очереди и сел(-а) за стол номер {i+1}')
                    Guest(self.tables[i][1]).start()
                    if not self.q.empty():
                        continue
                    else:
                        break
        for i in range(len(self.tables)):
            if self.tables[i][1] != None:
                if not Guest(self.tables[i][1]).is_alive():
                    print(f'{self.tables[i][1]} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {self.tables[i][0]} свободен')
                    self.tables[i][1] = None
            else:
                continue



# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
