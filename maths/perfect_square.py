"""
This pogram checks if a number is a perfect square or not.
"""

from numpy import sqrt


def is_perfect_square(number: int) -> bool:
    if not isinstance(number, int):
        raise ValueError("Invalid Number")
    if number < 0:
        raise ValueError("Invalid Number")

    root = int(sqrt(number))
    return root * root == number
