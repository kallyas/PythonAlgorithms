"""
This program finds fibonacci numbers.
"""
import time

def fibonacci(number: int) -> int:
    if not isinstance(number, int):
        raise ValueError("Invalid Number")
    if number < 0:
        raise ValueError("Invalid Number")
    if number == 0:
        return 0
    if number == 1:
        return 1
    return fibonacci(number-1) + fibonacci(number-2)


# calculate execution time
start_time = time.time()
print(fibonacci(100))
print("--- %s seconds ---" % (time.time() - start_time))