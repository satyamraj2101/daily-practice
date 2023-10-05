# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
def repeat_string(string, n):
  result = ""
  for i in range(n): 
    result = result + string
  return result

string = input("Enter the string: ")
n = int(input("Enter the number of repetitions: "))

print(repeat_string(string, n))
