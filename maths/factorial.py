"""
This program calculates the factorial of a number.
"""

def factorial(number: int) -> int:
    if not isinstance(number, int):
        raise ValueError("Invalid Number")
    if number < 0:
        raise ValueError("Invalid Number")
    if number == 0:
        return 1
    return number * factorial(number-1)