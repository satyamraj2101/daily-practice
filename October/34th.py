# Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20

def sums(a,b):
    sum = a + b
    if sum in range(15,21):
        return 20
    else:
        return sum
    
print(sums(1,15))