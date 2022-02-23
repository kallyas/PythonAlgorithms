"""
This program converts an octal number to decimal.
"""

def octal_to_decimal(octal_number: str) -> int:
    # check if the number is a octal number
    if not is_octal(octal_number):
        raise ValueError("Invalid Octal Number")

    decimal_number = 0
    for digit in octal_number:
        decimal_number = decimal_number * 8 + int(digit)
    return decimal_number


def is_octal(octal_number: str) -> bool:
    # check if the number is a octal number
    if len(octal_number) == 0:
        return False
    for digit in octal_number:
        if digit not in "01234567":
            return False
    return True