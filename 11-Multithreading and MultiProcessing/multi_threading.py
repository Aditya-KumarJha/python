### Multithreading
## When to use multithreading?
### - When you have I/O-bound tasks (e.g., network requests, file I/O) that can benefit from concurrent execution.
### - When you want to improve the responsiveness of a program by allowing it to perform multiple tasks simultaneously.

import threading
import time

# function to print numbers
def print_numbers():
    for i in range(5):
        time.sleep(2)  # Simulate a time-consuming task
        print(f"Number: {i}")

# function to print letters
def print_letters():
    for letter in 'ABCDE':
        time.sleep(2)  # Simulate a time-consuming task
        print(f"Letter: {letter}")

## create 2 threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

t = time.time()
# print_numbers()
# print_letters()

## start the threads
thread1.start()
thread2.start()

## wait for both threads to finish
thread1.join()
thread2.join()

finished_time = time.time() - t
print(f"Finished in {finished_time} seconds")
