import os
import time

for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.getcwd() + root[1:len(root)]
        filetime = os.stat(filepath+'\\'+file).st_mtime
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.stat(filepath+'\\'+file).st_size
        parent_dir = root
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')