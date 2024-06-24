import typing

Duodecimal = typing.Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "X", "E"]
Mode = typing.Literal["I", "II", "III", "IV", "V", "VI", "VII"]

value_map = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "X": 10,
    "E": 11,
}

reverse_value_map = {v: k for k, v in value_map.items()}

mode_map = {
    "I": 0,
    "II": 2,
    "III": 4,
    "IV": 5,
    "V": 7,
    "VI": 9,
    "VII": 11,
}

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


def from_duodecimal(
    note: Duodecimal, hint: typing.Literal["sharp", "flat", None] = None
):
    map = duodecimal_map_flat if hint == "flat" else duodecimal_map_sharp
    return map[note]


def to_duodecimal(note: str):
    return reverse_duodecimal_map[note]


def apply_mode(duodecimal: Duodecimal, mode: Mode) -> Duodecimal:
    duodecimal_value = value_map[duodecimal]
    mode_value = mode_map[mode]
    return reverse_value_map[(duodecimal_value + mode_value) % 12]
