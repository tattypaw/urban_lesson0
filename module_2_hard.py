def divisors_(number_):
    result = []
    for i in range(1,number_ + 1):
        if number_ % i == 0:
            result.append(i)
    return result

def composition_of_number(number_):
    result = []
    for i in range(1, number_//2 + 1):
        if i != number_ - i:
            result.append([i, number_ - i])
    return result

number = 0
while number < 3 or number > 20:
    number = int(input("Введите число от 3 до 20: "))
    if number < 3 or number > 20:
        print("Вы ошиблись.")
divisors = divisors_(number)
divisors.pop(0)

compositions = []
for i in divisors:
    compositions = compositions + composition_of_number(i)
if compositions[0] == []:
    compositions.pop(0)
compositions = sorted(compositions, key = lambda c: c[0])

code = ''
for i in compositions:
    for j in i:
        code = code + str(j)
print(f"Шифр для числа {number} - {code}")