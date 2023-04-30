from enum import Enum
from typing import List


class MorseCode(str, Enum):
    DOT = '.'
    DASH = '-'
    LETTER_SPACE = ' ' * 3
    WORD_SPACE = ' ' * 7

    def __str__(self) -> str:
        return str.__str__(self)


MORSE_MAP = {
    'A': [MorseCode.DOT, MorseCode.DASH],
    'B': [MorseCode.DASH, MorseCode.DOT, MorseCode.DOT, MorseCode.DOT],
    'C': [MorseCode.DASH, MorseCode.DOT, MorseCode.DASH, MorseCode.DOT],
    'D': [MorseCode.DASH, MorseCode.DOT, MorseCode.DOT],
    'E': [MorseCode.DOT],
    'F': [MorseCode.DOT, MorseCode.DOT, MorseCode.DASH, MorseCode.DOT],
    'G': [MorseCode.DASH, MorseCode.DASH, MorseCode.DOT],
    'H': [MorseCode.DOT, MorseCode.DOT, MorseCode.DOT, MorseCode.DOT],
    'I': [MorseCode.DOT, MorseCode.DOT],
    'J': [MorseCode.DOT, MorseCode.DASH, MorseCode.DASH, MorseCode.DASH],
    'K': [MorseCode.DASH, MorseCode.DOT, MorseCode.DASH],
    'L': [MorseCode.DOT, MorseCode.DASH, MorseCode.DOT, MorseCode.DOT],
    'M': [MorseCode.DASH, MorseCode.DASH],
    'N': [MorseCode.DASH, MorseCode.DOT],
    'O': [MorseCode.DASH, MorseCode.DASH, MorseCode.DASH],
    'P': [MorseCode.DOT, MorseCode.DASH, MorseCode.DASH, MorseCode.DOT],
    'Q': [MorseCode.DASH, MorseCode.DASH, MorseCode.DOT, MorseCode.DASH],
    'R': [MorseCode.DOT, MorseCode.DASH, MorseCode.DOT],
    'S': [MorseCode.DOT, MorseCode.DOT, MorseCode.DOT],
    'T': [MorseCode.DASH],
    'U': [MorseCode.DOT, MorseCode.DOT, MorseCode.DASH],
    'V': [MorseCode.DOT, MorseCode.DOT, MorseCode.DOT, MorseCode.DASH],
    'W': [MorseCode.DOT, MorseCode.DASH, MorseCode.DASH],
    'X': [MorseCode.DASH, MorseCode.DOT, MorseCode.DOT, MorseCode.DASH],
    'Y': [MorseCode.DASH, MorseCode.DOT, MorseCode.DASH, MorseCode.DASH],
    'Z': [MorseCode.DASH, MorseCode.DASH, MorseCode.DOT, MorseCode.DOT],
    '1': [MorseCode.DOT, MorseCode.DASH, MorseCode.DASH, MorseCode.DASH, MorseCode.DASH],
    '2': [MorseCode.DOT, MorseCode.DOT, MorseCode.DASH, MorseCode.DASH, MorseCode.DASH],
    '3': [MorseCode.DOT, MorseCode.DOT, MorseCode.DOT, MorseCode.DASH, MorseCode.DASH],
    '4': [MorseCode.DOT, MorseCode.DOT, MorseCode.DOT, MorseCode.DOT, MorseCode.DASH],
    '5': [MorseCode.DOT, MorseCode.DOT, MorseCode.DOT, MorseCode.DOT, MorseCode.DOT],
    '6': [MorseCode.DASH, MorseCode.DOT, MorseCode.DOT, MorseCode.DOT, MorseCode.DOT],
    '7': [MorseCode.DASH, MorseCode.DASH, MorseCode.DOT, MorseCode.DOT, MorseCode.DOT],
    '8': [MorseCode.DASH, MorseCode.DASH, MorseCode.DASH, MorseCode.DOT, MorseCode.DOT],
    '9': [MorseCode.DASH, MorseCode.DASH, MorseCode.DASH, MorseCode.DASH, MorseCode.DOT],
    '0': [MorseCode.DASH, MorseCode.DASH, MorseCode.DASH, MorseCode.DASH, MorseCode.DASH],
    ' ': [MorseCode.WORD_SPACE],
    '.': [MorseCode.DOT, MorseCode.DASH, MorseCode.DOT, MorseCode.DASH, MorseCode.DOT, MorseCode.DASH],
    ',': [MorseCode.DASH, MorseCode.DASH, MorseCode.DOT, MorseCode.DOT, MorseCode.DASH, MorseCode.DASH],
    '?': [MorseCode.DOT, MorseCode.DOT, MorseCode.DASH, MorseCode.DASH, MorseCode.DOT, MorseCode.DOT],
    "'": [MorseCode.DOT, MorseCode.DASH, MorseCode.DASH, MorseCode.DASH, MorseCode.DASH, MorseCode.DOT],
    '!': [MorseCode.DASH, MorseCode.DOT, MorseCode.DASH, MorseCode.DOT, MorseCode.DASH, MorseCode.DASH],
    '/': [MorseCode.DASH, MorseCode.DOT, MorseCode.DOT, MorseCode.DASH, MorseCode.DOT],
    '(': [MorseCode.DASH, MorseCode.DOT, MorseCode.DASH, MorseCode.DASH, MorseCode.DOT],
    ')': [MorseCode.DASH, MorseCode.DOT, MorseCode.DASH, MorseCode.DASH, MorseCode.DOT, MorseCode.DASH],
    '&': [MorseCode.DOT, MorseCode.DASH, MorseCode.DOT, MorseCode.DOT, MorseCode.DOT],
    ':': [MorseCode.DASH, MorseCode.DASH, MorseCode.DASH, MorseCode.DOT, MorseCode.DOT, MorseCode.DOT],
    ';': [MorseCode.DASH, MorseCode.DOT, MorseCode.DASH, MorseCode.DOT, MorseCode.DASH, MorseCode.DOT],
    '=': [MorseCode.DASH, MorseCode.DOT, MorseCode.DOT, MorseCode.DOT, MorseCode.DASH],
    '+': [MorseCode.DOT, MorseCode.DASH, MorseCode.DOT, MorseCode.DASH, MorseCode.DOT],
    '-': [MorseCode.DASH, MorseCode.DOT, MorseCode.DOT, MorseCode.DOT, MorseCode.DOT, MorseCode.DASH],
    '_': [MorseCode.DOT, MorseCode.DOT, MorseCode.DASH, MorseCode.DASH, MorseCode.DOT, MorseCode.DASH],
    '"': [MorseCode.DOT, MorseCode.DASH, MorseCode.DOT, MorseCode.DOT, MorseCode.DASH, MorseCode.DOT],
    '$': [MorseCode.DOT, MorseCode.DOT, MorseCode.DOT, MorseCode.DASH, MorseCode.DOT, MorseCode.DOT, MorseCode.DASH],
    '@': [MorseCode.DOT, MorseCode.DASH, MorseCode.DASH, MorseCode.DOT, MorseCode.DASH, MorseCode.DOT],
}


def char_to_morse(char: str) -> List[MorseCode]:
    """
    Convert a single character to morse code.
    """
    morse_code = []
    if char.upper() in MORSE_MAP:
        morse_code = MORSE_MAP[char.upper()]
    else:
        print(f'Unknown character: {char}')
    return morse_code


def text_to_morse(text: str) -> List[MorseCode]:
    """
    Convert text to morse code.
    NOTE: There will be a trailing LETTER_SPACE at the end (on purpose).
    """
    morse_code = []
    for char in text:
        morse_code.extend(char_to_morse(char))
        morse_code.append(MorseCode.LETTER_SPACE)
    return morse_code
