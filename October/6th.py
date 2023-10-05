# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
a = input("Enter the sequence seperated by , :" )
list_num = a.split(",")
tuple_num = tuple(list_num)

print(f"The list is : - {(list_num)}")
print(f"The Tuple  is : - {(tuple_num)}")