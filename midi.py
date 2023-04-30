from typing import List

from mido import Message, MidiFile, MidiTrack

from morse import MorseCode

TICK_DURATION = 60
VELOCITY = 64


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
