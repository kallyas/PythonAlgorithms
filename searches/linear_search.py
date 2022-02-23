"""
 @param list array, a list of integers to search
 @param integer target an integer number to search for in the list
 @return integer the index where the target is found (or -1 if not found)
"""

def linear_search(array: list, target: int) -> int:
    """
    linear search
    """
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1