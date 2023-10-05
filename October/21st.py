# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
def Check(num):
    if num % 2 == 0:
        return "Even"
    elif num % 2 != 0:
        return "Odd"

print(Check(7))