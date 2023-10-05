# Write a Python program to test whether a number is within 100 of 1000 or 2000
def Check_num(num):
    if num <= 1000 :
        return 1000
    elif num <= 2000:
        return 2000

print(Check_num(1500))