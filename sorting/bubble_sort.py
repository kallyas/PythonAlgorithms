"""
This module contains the Bubble Sort algorithm.
"""

def bubble_sort(numbers: list) -> list:
    """
    This function implements the Bubble Sort algorithm.
    """
    # check if the list is empty
    if len(numbers) == 0:
        raise ValueError("Empty List")
    # check if the list contains only numbers
    for number in numbers:
        if not isinstance(number, int):
            raise ValueError("Invalid Number")
    # sort the list
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def optimized_bubble_sort(numbers: list) -> list:
    """
    This function implements the Optimized Bubble Sort algorithm.
    """
    # check if the list is empty
    if len(numbers) == 0:
        raise ValueError("Empty List")
    # check if the list contains only numbers
    for number in numbers:
        if not isinstance(number, int):
            raise ValueError("Invalid Number")
    # sort the list
    for i in range(len(numbers)):
        swapped = False
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break
    return numbers

print(bubble_sort([12, 65, 1, 34, 100]))

