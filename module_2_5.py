
def get_matrix(n, m, value):
    matrix=[]
    for i in range(n):
        list_=[]
        for j in range(m):
            list_.append(value)
        matrix.append(list_)

    return matrix

n=3 # задаем количество строк
m=5 # задаем количество столбцов
list_=get_matrix(n,m,"Yes!") # выполняем функцию get_matrix
# выводим список в виде матрицы (построчно)
for i in range(n):
    print(list_[i])