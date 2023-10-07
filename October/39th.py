# Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
import os
import multiprocessing

def get_cpu_count():
    # Use os.cpu_count() to get the number of logical CPUs
    cpu_count = os.cpu_count()
    return cpu_count

if __name__ == "__main__":
    # Get the number of CPUs
    num_cpus = get_cpu_count()
    
    if num_cpus is not None:
        print(f"Number of CPUs: {num_cpus}")
    else:
        print("Number of CPUs could not be determined.")
