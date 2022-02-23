"""
The XOR cipher is a type of additive cipher.
Each character is bitwise XORed with the key.
We loop through the input string, XORing each
character with the key.
"""

def xor_cipher(input_string: str, key: str) -> str:
    """
    XOR cipher function.
    """
    output_string = ""
    for i in range(len(input_string)):
        output_string += chr(ord(input_string[i]) ^ ord(key[i % len(key)]))
    return output_string