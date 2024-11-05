def is_prime(func):
    def wrapper(*args):
        check = False
        result = func(*args)
        if 0 <= abs(result) <= 2:
            check = False
        else:
            for i in range(3,result):
                if result % i == 0:
                    check = True
                    break
        if check:
            print("Составное")
        else:
            print("Простое")
        return result
    return wrapper

@is_prime
def sum_three(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

result = sum_three(2, 3, 6)
print(result)
