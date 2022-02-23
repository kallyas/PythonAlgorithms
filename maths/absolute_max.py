"""
This program finds the absolute maximum of a list of numbers.
"""

def absolute_max(numbers: list) -> int:
    # check if the list is empty
    if len(numbers) == 0:
        raise ValueError("Empty List")
    # check if the list contains only numbers
    for number in numbers:
        if not isinstance(number, int):
            raise ValueError("Invalid Number")
    # find the absolute maximum
    maximum = numbers[0]
    for number in numbers:
        if abs(number) > abs(maximum):
            maximum = number
    return maximum