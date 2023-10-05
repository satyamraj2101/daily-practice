#  Write a Python program that checks whether a specified value is contained within a group of values.   
def finds(num):
    

    if num in val:
       return "Yes"
    else:
        return "No"

val = [11,5,6,8,6,5,2,5,6,55,55,55,66,898,66,55,55,66,22,26,26,547,52]
number = int(input("Enter the value : - "))
print(finds(number))

    