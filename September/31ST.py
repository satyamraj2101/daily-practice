prime_count = 0
num = 2

while True:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_count += 1
    if prime_count == 10001:
        print(num)
        break
    num += 1
