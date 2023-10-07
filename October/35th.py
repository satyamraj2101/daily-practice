# Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.
def sums(a, b):
    sum = a + b
    diff = a - b

    if a == b:
        return True
    elif sum == 5 or diff == 5:
        return True
    else:
        return sum

print(sums(10,5),"Should return : True\n ")
print(sums(5,5),"Should return : True\n")
print(sums(2,3),"Should return : True\n")
print(sums(4,9),"Should return : 13\n")
