from enum import Enum
from typing import List

from mido import Message, MidiFile, MidiTrack

TICK_DURATION = 60
VELOCITY = 64


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


def write_midi_file(morse: List[MorseCode], filename: str, note: int) -> None:
    """
    Write morse code to a midi file.
    """
    file = MidiFile()
    track = MidiTrack()
    file.tracks.append(track)

    track.append(Message('program_change', program=12, time=0))
    for i in range(0, len(morse)):
        code = morse[i]
        match code:
            case MorseCode.DOT:
                track.append(Message('note_on', note=note, velocity=VELOCITY, time=0))
                track.append(Message('note_off', note=note, velocity=VELOCITY, time=TICK_DURATION))
                # If the next character is a dot or dash, then we need to add a space.
                if i < len(morse) - 1 and morse[i + 1] in (MorseCode.DOT, MorseCode.DASH):
                    track.append(Message('note_off', note=0, velocity=VELOCITY, time=TICK_DURATION))
            case MorseCode.DASH:
                track.append(Message('note_on', note=note, velocity=VELOCITY, time=0))
                track.append(Message('note_off', note=note, velocity=VELOCITY, time=TICK_DURATION * 3))
                # If the next character is a dot or dash, then we need to add a space.
                if i < len(morse) - 1 and morse[i + 1] in (MorseCode.DOT, MorseCode.DASH):
                    track.append(Message('note_off', note=0, velocity=VELOCITY, time=TICK_DURATION))
            case MorseCode.LETTER_SPACE:
                track.append(Message('note_off', note=0, velocity=VELOCITY, time=TICK_DURATION * 3))
            case MorseCode.WORD_SPACE:
                track.append(Message('note_off', note=0, velocity=VELOCITY, time=TICK_DURATION * 7))
            case _:
                print(f'Unknown morse code: {code}')

    file.save("tracks/" + filename)


if __name__ == '__main__':
    # BPM MOD TWO SIX
    # Ordered by scale (12 major chords)

    # C / 120 BPM (P=16)
    morse = text_to_morse("It is Wednesday my dudes.")
    write_midi_file(morse, "bit.mid", 60)  # B

    # C# / 113 BPM (I=9)
    morse = text_to_morse("There is no war in Ba Sing Se.")
    write_midi_file(morse, "warp.mid", 61)  # P

    # D / 128 BPM (X=24)
    morse = text_to_morse("According to all known laws of aviation, there is no way a bee should be able to fly.")
    write_midi_file(morse, "mall.mid", 62)  # M

    # D# / 105 BPM (A=1)
    morse = text_to_morse("Ight imma head out.")
    write_midi_file(morse, "might.mid", 63)  # M

    # E / 122 BPM (R=18)
    morse = text_to_morse("Shut up and take my money!")
    write_midi_file(morse, "shout.mid", 64)  # O

    # F / 110 BPM (F=6)
    morse = text_to_morse("It's over, Anakin. I have the high ground.")
    write_midi_file(morse, "dover.mid", 65)  # D

    # F# / 131 BPM (A=1)
    morse = text_to_morse("Somebody once told me the world is gonna roll me, I ain't the sharpest tool in the shed.")
    write_midi_file(morse, "troll.mid", 66)  # T

    # G / 123 BPM (S=19)
    morse = text_to_morse("We're no strangers to love. You know the rules, and so do I.")
    write_midi_file(morse, "now.mid", 67)  # W

    # G# / 124 BPM (T=20)
    morse = text_to_morse("Did you put your name in the goblet of fire? Dumbledore asked calmly.")
    write_midi_file(morse, "pout.mid", 68)  # O

    # A / 115 BPM (K=11)
    morse = text_to_morse("Cash me ousside, how bow dah.")
    write_midi_file(morse, "dash.mid", 69)  # S

    # A# / 113 BPM (I=9)
    morse = text_to_morse("Give your meat a good ol' rub.")
    write_midi_file(morse, "oil.mid", 70)  # I

    # B / 108 BPM (D=4)
    morse = text_to_morse("Omae wa mou shindeiru.")
    write_midi_file(morse, "wax.mid", 71)  # X
