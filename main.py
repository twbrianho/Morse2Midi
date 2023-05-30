from midi import write_midi_file
from morse import text_to_morse


class FileConfig:
    def __init__(self, filename, note, text):
        self.filename = filename  # the filename of the midi file & the resulting track
        self.note = note  # the pitch of the note; known only as "note" in midi
        self.text = text  # original text to be converted to morse

    def __str__(self):
        return f'FileConfig({self.filename})'

    def __repr__(self):
        return str(self)


# NOTE: Tracks should be sorted alphabetically by track title on the album.
FILE_CONFIGS = [
    # "B" / C / 120 BPM (P=16)
    FileConfig('bit.mid', 60, "It is Wednesday my dudes."),
    # "P" / C# / 113 BPM (I=9)
    FileConfig('warp.mid', 61, "There is no war in Ba Sing Se."),
    # "M" / D / 128 BPM (X=24)
    FileConfig('mall.mid', 62,
               "According to all known laws of aviation, there is no way a bee should be able to fly."),
    # "M" / D# / 105 BPM (A=1)
    FileConfig('might.mid', 63, "Ight imma head out."),
    # "O" / E / 122 BPM (R=18)
    FileConfig('shout.mid', 64, "Shut up and take my money!"),
    # "D" / F / 110 BPM (F=6)
    FileConfig('dover.mid', 65, "It's over, Anakin! I have the high ground!"),
    # "T" / F# / 131 BPM (A=1)
    FileConfig('troll.mid', 66,
               "Somebody once told me the world is gonna roll me, I ain't the sharpest tool in the shed."),
    # "W" / G / 123 BPM (S=19)
    FileConfig('now.mid', 67, "We're no strangers to love. You know the rules, and so do I."),
    # "O" / G# / 124 BPM (T=20)
    FileConfig('pout.mid', 68, "Did you put your name in the Goblet of Fire, Harry?"),
    # "S" / A / 115 BPM (K=11)
    FileConfig('show.mid', 69, "Cash me ousside, how bow dah?"),
    # "I" / A# / 113 BPM (I=9)
    FileConfig('oil.mid', 70, "Give your meat a good ol' rub."),
    # "X" / B / 108 BPM (D=4)
    FileConfig('wax.mid', 71, "Omae wa mou shindeiru."),
]

if __name__ == '__main__':
    """
    Solve process:
    1. Identify and convert morse to text for each track. Each one is a meme.
    2. Order tracks by note (C, C#, D, D#, E, F, F#, G, G#, A, A#, B). Exactly 12 tracks = 12 notes in an octave.
    3. Find extra letter in each track title by comparing to one of the words in morse -> "BPM MOD TWO SIX".
    4. Get the BPM for each track (e.g. using an app / website), then mod by 26 to get the letter -> "PIXAR FAST KID".
    5. Answer is "DASH" — which is thematic to morse code!
    """

    for file_config in FILE_CONFIGS:
        write_midi_file(text_to_morse(file_config.text), file_config.filename, file_config.note)
