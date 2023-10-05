#Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.

def copy_first_2_chars(input_string, n):
    if len(input_string) < 2:
        return input_string * n
    else:
        first_2_chars = input_string[:2]
        return first_2_chars * n

# Get user input for the string and n
input_string = input("Enter a string: ")
n = int(input("Enter a non-negative integer n: "))

# Check if n is non-negative
if n < 0:
    print("Please enter a non-negative integer for n.")
else:
    result = copy_first_2_chars(input_string, n)
    print("Result:", result)
