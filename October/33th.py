# Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.

def sum(a,b,c):
    if a == b or b==c or a==c:
        return "Sum:0(Two input parameters are same)"
    else:
        return "Sum:" + str(a + b + c)
    
print(sum(1,2,3))
print(sum(1,3,3))
        