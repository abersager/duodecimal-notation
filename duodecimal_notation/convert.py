import typing

Duodecimal = (
    typing.Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "X", "Z"] | str
)
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
    "Z": 11,
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
    "Z": "B",
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
    "Z": "B",
}

reverse_duodecimal_map_sharp = {v: k for k, v in duodecimal_map_sharp.items()}
reverse_duodecimal_map_flat = {v: k for k, v in duodecimal_map_flat.items()}
reverse_duodecimal_map = {**reverse_duodecimal_map_sharp, **reverse_duodecimal_map_flat}

color_map = {
    "0": "#FF6666",
    "1": "#FF9966",
    "2": "#FFCC66",
    "3": "#FFFF66",
    "4": "#CCFF66",
    "5": "#99FF66",
    "6": "#66FF66",
    "7": "#66FF99",
    "8": "#66FFCC",
    "9": "#66CCFF",
    "X": "#9999FF",
    "Z": "#CC66FF",
}


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


def to_decimal(duodecimal: str) -> int:
    note = duodecimal[-1]
    doh = int(duodecimal[:-1])
    return 12 * doh + value_map[note]


def to_frequency(duodecimal: str) -> float:
    decimal = to_decimal(duodecimal)
    n = decimal - 57  # 57 is the decimal number of halftones from 00 / C0 to 49 / A4
    return 440 * 2 ** (n / 12)


def to_midi(duodecimal: str) -> int:
    return to_decimal(duodecimal) + 12


def from_midi(midi: int) -> str:
    doh = midi // 12 - 1
    note = reverse_value_map[midi % 12]
    return f"{doh}{note}"


def to_color(duodecimal: str) -> str:
    return color_map[duodecimal[-1]]
