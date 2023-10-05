def calculator(a,b,c):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        return a//b 

a,b,c = int(input("Enter First Number")), int(input("Enter Second Number")) , input("Choose the operation(+ , - , * , /)")
print(calculator(a,b,c))
    