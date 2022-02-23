"""
Encode text to Morse Code.
@param string text to encode
"""

def morse_encode(text: str) -> str:
    """
    Encode text to Morse Code.
    @param string text to encode
    """
    morse_code = {
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
        "1" : ".----",
        "2" : "..---",
        "3" : "...--",
        "4" : "....-",
        "5" : ".....",
        "6" : "-....",
        "7" : "--...",
        "8" : "---..",
        "9" : "----.",
        "0" : "-----",
        " " : "/"
    }

    # check if its a valid string
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    output_string = ""
    for i in range(len(text)):
        output_string += morse_code[text[i]] + " "
    return output_string.strip()


def morse_decode(text: str) -> str:
    """
    Decode text from Morse Code.
    @param string text to decode
    """
    morse_code = {
        ".-" : "A",
        "-..." : "B",
        "-.-." : "C",
        "-.." : "D",
        "." : "E",
        "..-." : "F",
        "--." : "G",
        "...." : "H",
        ".." : "I",
        ".---" : "J",
        "-.-" : "K",
        ".-.." : "L",
        "--" : "M",
        "-." : "N",
        "---" : "O",
        ".--." : "P",
        "--.-" : "Q",
        ".-." : "R",
        "..." : "S",
        "-" : "T",
        "..-" : "U",
        "...-" : "V",
        ".--" : "W",
        "-..-" : "X",
        "-.--" : "Y",
        "--.." : "Z",
        ".----" : "1",
        "..---" : "2",
        "...--" : "3",
        "....-" : "4",
        "....." : "5",
        "-...." : "6",
        "--..." : "7",
        "---.." : "8",
        "----." : "9",
        "-----" : "0",
        "/" : " "
    }

    # check if its a valid string
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    output_string = ""
    for i in range(len(text)):
        output_string += morse_code[text[i]]
    return output_string.strip()