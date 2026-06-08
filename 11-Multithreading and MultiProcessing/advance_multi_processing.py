## Multiprocessing with ProcessPoolExecutor
### The `concurrent.futures` module provides a high-level interface for asynchronously executing callables using threads or processes. The `ProcessPoolExecutor` class allows us to execute tasks in separate processes

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(1)
    return f"Square: {number * number}"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3]

if __name__ == "__main__":

    t = time.time()
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)

    for result in results:
        print(result)
        
    print(f"Total time taken: {time.time() - t}")