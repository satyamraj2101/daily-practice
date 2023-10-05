a = int(input("Enter the number : - "))


def divisior(a):
    for i in range(1, a+1):
        if a % i == 0:
            print(i)


divisior(a)