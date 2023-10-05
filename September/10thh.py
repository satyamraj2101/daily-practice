def is_prime(a):
    check_prime = True
    for i in range(2, a):
        if a % i == 0:
            check_prime = False
            break
    if check_prime:
        print("Prime")
    else:
        print("Not Prime")

print("Enter the number")
num = int(input())
is_prime(num)
