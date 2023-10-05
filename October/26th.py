# Write a Python program to create a histogram from a given list of integers.

def histogram( items ):
    for n in items:
        star = '*' * n
        print(star)

histogram([2, 3, 6, 5,25])