import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        all_data.append(file.readline())


names = [f'./file {number}.txt' for number in range(1, 5)]
'''start = time.time()
for i in range(4):
    read_info(names[i])
end = time.time()
print(end - start)'''

if __name__ == '__main__':
    start = time.time()
    with multiprocessing.Pool(4) as p:
        process = p.map(read_info, names)
    end = time.time()
    print(end - start)
