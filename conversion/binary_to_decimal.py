"""
This function converts submitted binary number to decimal number.
 Working of Algorithm
 (10) base 2
 (1 * (2 ^ 1) + 0 * (2 ^ 0)) base 10
 (2 + 0) base 10
 2 base 10
 @param string $binaryNumber
 @return int
"""

def binary_to_decimal(binary_number: str) -> int:
    # check is the submitted binary number is valid
    if not is_binary_number(binary_number):
        # raise exception if the submitted binary number is invalid
        raise ValueError("Invalid binary number")
    # convert the submitted binary number to decimal number
    decimal_number = 0
    for i in range(len(binary_number)):
        decimal_number += int(binary_number[i]) * (2 ** (len(binary_number) - i - 1))
    return decimal_number


def is_binary_number(binary_number: str) -> bool:
    # check if the submitted binary number is valid
    if not binary_number.isdigit():
        # return false if the submitted binary number is invalid
        return False
    # return true if the submitted binary number is valid
    return True
