num_terms = int(input("Enter the number : -  "))
power_of_two = lambda x: 2 ** x

for i in range(num_terms+1):
    print(f"The value of 2 raised to power {i} is {power_of_two(i)}")
