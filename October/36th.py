# Write a Python program to add two objects if both objects are integers.

def sum(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a+b
    else:
        return "Enter an integer value"


print(sum(1, 2))
print(sum(1, "l"))
