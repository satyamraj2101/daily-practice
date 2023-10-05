# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

a = int(input("Enter a : "))
b = int(input("Enter a : "))
c = int(input("Enter a : "))

def sum(a,b,c):
    if a == b == c:
        return 3*(a+b+c)
    else:
        return a+b+c
print(sum(a,b,c))