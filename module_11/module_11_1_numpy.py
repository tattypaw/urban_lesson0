import numpy as np

A = np.array([[0.5, 0.7], [-3, -7.2]])
B = np.array([[1, 2], [3, 4]])

x = np.arange(0, 2 * np.pi, np.pi / 6)
y = np.sin(x)
for k in range(len(x)):
    print(f'{x[k]},\t {y[k]}')

print('функция dot')
print(np.dot(x, y))
print(np.dot(A, B))
print('Массив А')
print(A)
print("Сумма", A.sum())
print("Сумма по столбцу 0", A.sum(axis=0))
print("Сумма по столбцу 1", A.sum(axis=1))
print("Минимум", A.min())
