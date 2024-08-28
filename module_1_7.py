grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# изменение типа множество на список, сортировка списка
students_list = list(students)
students_list.sort()

# вычисление средней оценки студентов и занесение её в новый список
average = list()
for list_ in grades:
    average.append(sum(list_)/len(list_))

# объединение списков и создание словаря
students_grades = dict(zip(students_list, average))
print(students_grades)