import threading
import time
#from symbol import power

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!"')
        counter = 0
        warriors = 100
        while warriors:
            time.sleep(1)
            counter +=1
            warriors -= self.power
            print(f'{self.name} сражается {counter} день(дня) ..., осталось {warriors} воинов.        ')
        print(f'{self.name} одержал победу спустя {counter} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')