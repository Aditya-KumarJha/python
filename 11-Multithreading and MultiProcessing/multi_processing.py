## Processes that run in parallel
### Multiprocessing allows us to run multiple processes in parallel, which can be useful for CPU-bound tasks. The `multiprocessing` module in Python provides a simple way to create and manage separate processes.
### CPU bound tasks are tasks that require a lot of CPU time, such as complex calculations or data processing. By using multiprocessing, we can take advantage of multiple CPU cores to speed up the execution of these tasks.

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)  # Simulate a time-consuming task
        print(f"Square: {i * i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)  # Simulate a time-consuming task
        print(f"Cube: {i * i * i}")
        

if __name__ == "__main__":
    ## create 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t = time.time()

    ## start the processes
    p1.start()
    p2.start()

    ## wait for both processes to finish
    p1.join()
    p2.join()

    print(f"Total time taken: {time.time() - t}")
