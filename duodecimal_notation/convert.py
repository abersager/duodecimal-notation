import typing


duodecimal_map_sharp = {
    "0": "C",
    "1": "C#",
    "2": "D",
    "3": "D#",
    "4": "E",
    "5": "F",
    "6": "F#",
    "7": "G",
    "8": "G#",
    "9": "A",
    "X": "A#",
    "E": "B",
}

duodecimal_map_flat = {
    "0": "C",
    "1": "Db",
    "2": "D",
    "3": "Eb",
    "4": "E",
    "5": "F",
    "6": "Gb",
    "7": "G",
    "8": "Ab",
    "9": "A",
    "X": "Bb",
    "E": "B",
}

reverse_duodecimal_map_sharp = {v: k for k, v in duodecimal_map_sharp.items()}
reverse_duodecimal_map_flat = {v: k for k, v in duodecimal_map_flat.items()}
reverse_duodecimal_map = {**reverse_duodecimal_map_sharp, **reverse_duodecimal_map_flat}


def from_duodecimal(note: str, hint: typing.Literal["sharp", "flat", None] = None):
    map = duodecimal_map_flat if hint == "flat" else duodecimal_map_sharp
    return map[note]


def to_duodecimal(note: str):
    return reverse_duodecimal_map[note]
