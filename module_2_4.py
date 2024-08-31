numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes =[]
not_primes =[]
for number in numbers:
    is_prime = True
    for j in range(0, len(numbers)):
        if number % numbers[j] == 0:
            if number != numbers[j] and numbers[j] != 1:
                is_prime = False
                break
    if is_prime:
        if number != 1:
            primes.append(number)
    else:
        not_primes.append(number)
print('простые числа - ', primes)
print('составные числа - ', not_primes)