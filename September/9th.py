def check_largest(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    if c >= a and c >= b:
        return c


print("Enter the value of a")
a = int(input())
print("Enter the value of b")
b = int(input())
print("Enter the value of c")
c = int(input())
print(check_largest(a,b,c))
