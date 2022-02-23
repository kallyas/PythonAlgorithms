"""
  Encrypt given text using caesar cipher.
  @param string text text to be encrypted
  @param int shift number of shifts to be applied
  @return string new encrypted text
"""

def encrypt(text: str, shift: int) -> str:
    """
    Encrypt given text using caesar cipher.
    @param string text text to be encrypted
    @param int shift number of shifts to be applied
    @return string new encrypted text
    """
    output_string = ""
    for i in range(len(text)):
        output_string += chr((ord(text[i]) + shift) % 256)
    return output_string
    

def decrypt(text: str, shift: int) -> str:
    """
    Decrypt given text using caesar cipher.
    @param string text text to be decrypted
    @param int shift number of shifts to be applied
    @return string new decrypted text
    """
    output_string = ""
    for i in range(len(text)):
        output_string += chr((ord(text[i]) - shift) % 256)
    return output_string