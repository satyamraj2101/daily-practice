# Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

def Calculate(num):
    if num > 17 :
        return (2*(num - 17))
    else:
        return 17 - num

print(Calculate(21))