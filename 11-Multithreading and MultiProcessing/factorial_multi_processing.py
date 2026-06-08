'''
    Real World Example: Multithreading for CPU Bound Tasks
    Scenario: Factorial Calculation
    Factorial calculation specially for large numbers,
    involve significant computational work. Multiprocessing
    can be used to distribute the workload across multiple
CPU cores, improving performance.
'''

import multiprocessing
import math
import time
import sys

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(1000000)

## function to compute factorial of a given number
def compute_factorial(n):
    print(f"Computing factorial of {n}...")
    result = math.factorial(n)
    print(f"Factorial of {n} is {result}")
    return result
if __name__ == "__main__":
    numbers = [5000, 6000, 7000, 8000]
    
    start_time = time.time()
    
    ## create a pool of worker processses
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()
    print(f"Results: {results}")
    print(f"Total time taken: {end_time - start_time} seconds")