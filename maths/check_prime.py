"""
This program checks if a number is prime.
"""

def is_prime(number: int) -> bool:
    if not isinstance(number, int):
        raise ValueError("Invalid Number")
        
    if number < 2:
        return False
        
    for i in range(2, number):
        if number % i == 0:
            return False

    return True