"""
This program calculates an exponential using the fast exponential algorithm.
"""

def fast_exponential(base: int, exponent: int) -> int:
    if not isinstance(base, int):
        raise ValueError("Invalid Base")
    if not isinstance(exponent, int):
        raise ValueError("Invalid Exponent")
    if exponent < 0:
        raise ValueError("Invalid Exponent")
    if base == 0:
        return 0
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    if exponent % 2 == 0:
        return fast_exponential(base, exponent//2)**2
    else:
        return base * fast_exponential(base, (exponent-1)//2)**2