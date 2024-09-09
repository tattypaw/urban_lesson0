def get_multiplied_digits (number):
    str_number = str(number)
    first = int(str_number[0])
    if first == 0:
        first = 1
    str_number = str_number[1:]
    if len(str_number) < 1:
        return first
    else:
        return first * get_multiplied_digits(str_number)

print(get_multiplied_digits(120345))
print(get_multiplied_digits(1203450))
result = get_multiplied_digits(40203)
print(result)