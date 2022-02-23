"""
This program finds the absolute minimum of a list of numbers
"""


def absolute_min(numbers: list) -> int:
    # check if the list is empty
    if len(numbers) == 0:
        raise ValueError("Empty List")

    # check if the list contains only numbers, cater for negative numbers
    for number in numbers:
        if not is_number(number):
            raise ValueError("List contains non-numeric values")

    # find the absolute minimum
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum


def is_number(number: str) -> bool:
    try:
        int(number)
        return True
    except ValueError:
        return False
