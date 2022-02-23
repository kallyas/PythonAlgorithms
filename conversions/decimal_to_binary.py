"""
This function converts submitted decimal number to binary number
"""

def decimal_to_binary(decimal: str) -> str:
    # check is the value is not a decimal
    if not is_decimal_number(decimal):
        raise ValueError("Invalid decimal number")

    binary_number = ""
    # convert the decimal number to binary number
    while int(decimal) > 0:
        binary_number = str(int(decimal) % 2) + binary_number
        decimal = int(decimal) // 2
    return binary_number

def is_decimal_number(number: str) -> bool:
    if not number.isdecimal():
        return False
    else:
        return True