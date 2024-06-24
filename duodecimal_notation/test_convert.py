import pytest

from duodecimal_notation.convert import from_duodecimal, to_duodecimal

test_cases = [
    ("0", None, "C"),
    ("0", "sharp", "C"),
    ("0", "flat", "C"),
    ("1", None, "C#"),
    ("1", "sharp", "C#"),
    ("1", "flat", "Db"),
    ("2", None, "D"),
    ("2", "sharp", "D"),
    ("2", "flat", "D"),
    ("3", None, "D#"),
    ("3", "sharp", "D#"),
    ("3", "flat", "Eb"),
    ("4", None, "E"),
    ("4", "sharp", "E"),
    ("4", "flat", "E"),
    ("5", None, "F"),
    ("5", "sharp", "F"),
    ("5", "flat", "F"),
    ("6", None, "F#"),
    ("6", "sharp", "F#"),
    ("6", "flat", "Gb"),
    ("7", None, "G"),
    ("7", "sharp", "G"),
    ("7", "flat", "G"),
    ("8", None, "G#"),
    ("8", "sharp", "G#"),
    ("8", "flat", "Ab"),
    ("9", None, "A"),
    ("9", "sharp", "A"),
    ("9", "flat", "A"),
    ("X", None, "A#"),
    ("X", "sharp", "A#"),
    ("X", "flat", "Bb"),
    ("E", None, "B"),
    ("E", "sharp", "B"),
    ("E", "flat", "B"),
]


@pytest.mark.parametrize("duodecimal,hint, note", test_cases)
def test_from_duodecimal(duodecimal, hint, note):
    assert from_duodecimal(duodecimal, hint) == note


@pytest.mark.parametrize("duodecimal,hint,note", test_cases)
def test_to_duodecimal(duodecimal, hint, note):
    assert to_duodecimal(note) == duodecimal
