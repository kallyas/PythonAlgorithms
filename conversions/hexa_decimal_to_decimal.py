"""
This function converts given hexadecimal number to decimal number
"""


def hexa_decimal_to_decimal(number: str) -> int:
    # check if the number is a hexa decimal number
    if not is_hexa_decimal(number):
        raise ValueError("Invalid Hexa Decimal Number")
    
    # convert hexa decimal number to decimal
    decimal = 0
    for i in range(len(number)):
        decimal += int(number[i], 16) * (16 ** (len(number) - i - 1))

    return decimal


def is_hexa_decimal(number: str) -> bool:
    # check if the number is a hexa decimal number
    if len(number) == 0:
        return False
    for i in range(len(number)):
        if number[i] not in "0123456789ABCDEF":
            return False
    return True

    

    
