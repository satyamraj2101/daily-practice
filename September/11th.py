import random


def print_random_number(start, end):
    random_number = random.randint(start, end)
    print("Random number:", random_number)


# Example usage:
start_range = 1
end_range = 100
print_random_number(start_range, end_range)
