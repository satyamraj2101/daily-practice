# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20
def is_divisible(x):
    for i in range(1, 21):
        if x % i != 0:
            return False
    return True

x = 20
while True:
    if is_divisible(x):
        print(x)
        break
    x += 20