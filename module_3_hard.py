def all_list(data): # Проверка, есть ли в данных списки, кортежи, множества, словари
    flag = True
    for i in data:
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, dict) or isinstance(i, set):
            return False
    return flag

def structure_in_list(data): # Преобразование всех данных в список
    result = []
    for i in data:
        if isinstance(i, list):
           result = result + i
        elif isinstance(i, tuple) or isinstance(i, set):
           result = result + list(i)
        elif isinstance(i, dict):
           result = result + list(i.keys()) + list(i.values())
        else:
           result.append(i)
    if all_list(result):
        return result
    else:
        result = structure_in_list(result)
    return result

def calculate_structure_sum(data): # Запуск основных действий
    data = structure_in_list(data)
    return list_sum(0, data)

def list_sum(summa, data): # Сложение чисел и длин строк
    if len(data) == 0:
        return summa
    else:
        j = data[0]
        data.pop(0)
        if isinstance(j, int) or isinstance(j, float):
            summa += j
        else:
            summa += len(j)
        return list_sum(summa, data)

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
     "Hello",
     ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)