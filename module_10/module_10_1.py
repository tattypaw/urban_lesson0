from time import sleep, time
import threading


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding = 'utf-8') as file:
        for count in range(word_count):
            file.write(f'Какое-то слово № {count + 1}\n')
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

start = time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

ending = time()
print('Работа потоков', ending - start)

start = time()
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread1.start()
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread2.start()
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread3.start()
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread4.start()

ending = time()
print('Работа потоков', ending - start)