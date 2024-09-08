def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print("Задание 1.")
print_params(1,"2,3")
print_params(1, 3)
print_params(1)
print_params('1',2, 2>3)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
# во всех случаях вывод происходит

print("Задание 2.")
values_list = [1, "string", False]
values_dict = {'a': 4, 'b': 'dictionary', 'c': True}
print_params(*values_list)
print_params(**values_dict)

print("Задание 3.")
values_list_2 = [2.45, "hello"]
print_params(*values_list_2, 42)

values_list_3 = [2.45, "hello"]
print_params(5.6, *values_list_3,)