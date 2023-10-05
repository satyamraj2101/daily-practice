# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n = int(input("Enter the value of n: "))

n1 = n 
n2 = n*n
n3 = n*n*n

result = n1 + n2 + n3

print(result)