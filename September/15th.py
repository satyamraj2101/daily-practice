def table(n):
    for i in range(1, 11):
        print(f"{n} * {i} = ", n * i)


print("Enter the number you want table for : ")
n = int(input())
table(n)
