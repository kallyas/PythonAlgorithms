"""
This module contains the Jump Search algorithm.
"""
import math

def jump_search(arr: list, x: int, n: int) -> int:
    """
    This function implements the Jump Search algorithm.
    """
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == x:
        return prev
    return -1