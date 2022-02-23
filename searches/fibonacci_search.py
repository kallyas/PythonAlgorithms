"""
 Function to find nth number in Fibonaccu sequence.
 Uses a version of memoization and runs very fast!
"""

def fibonacci_search(num: int, array: list) -> int:
    """
    @param int num position to check
    @param list array to store solved trees
    """
    if num < 2:
        return num

    array[num] = fibonacci_search(num - 1, array) + fibonacci_search(num - 2, array)
    return array[num]