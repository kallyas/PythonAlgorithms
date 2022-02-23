"""
implementation of binary search
"""

def binary_search(array: list, target: int) -> int:
    """
    binary search
    """
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1


def binary_search_recursive(array: list, target: int) -> int:
    """
    binary search using recursion
    """
    if len(array) == 0:
        return -1

    mid = len(array) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search_recursive(array[mid + 1:], target)
    else:
        return binary_search_recursive(array[:mid], target)

