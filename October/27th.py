# Write a Python program that concatenates all elements in a list into a string and returns it.
def concatenate( items ):
    string = " "
    for item in items:
        string += str(item)
    print(string)
concatenate([2,5,8,6,"gssg" , 5,5.3])