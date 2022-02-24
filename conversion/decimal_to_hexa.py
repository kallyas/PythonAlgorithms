"""
This program converts given decimal number to hexadecimal number
"""

def decimal_to_hexa(number: int) -> str:
    # check if the number is a decimal number
    if not is_decimal(number):
        raise ValueError("Invalid Decimal Number")
    
    # convert decimal number to hexa decimal number
    hexa = ""
    while number > 0:
        hexa += str(hex(number % 16)[2:].upper())
        number //= 16
    return hexa[::-1]


def is_decimal(number: int) -> bool:
    # check if the number is a decimal number
    if number < 0:
        return False
    return True
