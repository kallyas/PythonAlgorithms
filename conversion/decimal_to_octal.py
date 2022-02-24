"""
This function converts submitted decimal number to octal number
"""


def decimal_to_octal(decimal: str) -> str:
    # check is the value is not a decimal
    if not is_decimal_number(decimal):
        raise ValueError("Invalid decimal number")

    octal_number = ""
    # convert the decimal number to octal number
    while int(decimal) > 0:
        octal_number = str(int(decimal) % 8) + octal_number
        decimal = int(decimal) // 8
    return octal_number


def is_decimal_number(number: str) -> bool:
    if not number.isdecimal():
        return False
    else:
        return True