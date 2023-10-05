# 0 1 1 2 3 5 8 13

def fibonacci(n):
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)
    for i in range(n-2):
        n1 , n2 = n2 , (n1 + n2)
        # n1 = n2
        print(n2)
    # return n2

print("Enter num: ")
n = int(input())
# print("nth number of fibonacci seq. is:",fibonacci(n))
fibonacci(n)