def is_prime(a):
    check_prime = True
    for i in range(2, a):
        if a % i == 0:
            check_prime = False
            break
    return check_prime

def print_prime_numbers(start, end):
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Example usage:
start_range = int(input("Enter the start range: "))
end_range = int(input("Enter the end range: "))

result = print_prime_numbers(start_range, end_range)
print("Prime numbers between", start_range, "and", end_range, "are:", result)
