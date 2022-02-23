"""
This program checks if a number is prime.
"""

def is_prime(number: int) -> bool:
    if not isinstance(number, int):
        raise ValueError("Invalid Number")
    # check if the number is less than 2
    if number < 2:
        return False
    # check if the number is divisible by 2
    if number % 2 == 0:
        return False
    # check if the number is divisible by any odd number
    for i in range(3, int(number**0.5)+1, 2):
        if number % i == 0:
            return False
    return True

