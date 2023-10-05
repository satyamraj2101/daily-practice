def armstrong(number):

    num_string = str(number)

    num_length = len(num_string)

    digit_sum = sum(int(digit) ** num_length for digit in num_string)

    return digit_sum == number

print("Enter the value of num: - ")
num = int(input())
if armstrong(num):
    print("Armstrong number")
else:
    print("Not an armstrong number")