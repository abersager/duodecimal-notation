import pytest

from duodecimal_notation.convert import from_duodecimal, to_duodecimal, apply_mode

convert_test_cases = [
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


@pytest.mark.parametrize("duodecimal,hint, note", convert_test_cases)
def test_from_duodecimal(duodecimal, hint, note):
    assert from_duodecimal(duodecimal, hint) == note


@pytest.mark.parametrize("duodecimal,hint,note", convert_test_cases)
def test_to_duodecimal(duodecimal, hint, note):
    assert to_duodecimal(note) == duodecimal


mode_test_cases = [
    ("0", "I", "0"),
    ("0", "II", "2"),
    ("0", "III", "4"),
    ("0", "IV", "5"),
    ("0", "V", "7"),
    ("0", "VI", "9"),
    ("0", "VII", "E"),
    ("1", "I", "1"),
    ("1", "II", "3"),
    ("1", "III", "5"),
    ("1", "IV", "6"),
    ("1", "V", "8"),
    ("1", "VI", "X"),
    ("1", "VII", "0"),
    ("2", "I", "2"),
    ("2", "II", "4"),
    ("2", "III", "6"),
    ("2", "IV", "7"),
    ("2", "V", "9"),
    ("2", "VI", "E"),
    ("2", "VII", "1"),
    ("3", "I", "3"),
    ("3", "II", "5"),
    ("3", "III", "7"),
    ("3", "IV", "8"),
    ("3", "V", "X"),
    ("3", "VI", "0"),
    ("3", "VII", "2"),
    ("4", "I", "4"),
    ("4", "II", "6"),
    ("4", "III", "8"),
    ("4", "IV", "9"),
    ("4", "V", "E"),
    ("4", "VI", "1"),
    ("4", "VII", "3"),
    ("5", "I", "5"),
    ("5", "II", "7"),
    ("5", "III", "9"),
    ("5", "IV", "X"),
    ("5", "V", "0"),
    ("5", "VI", "2"),
    ("5", "VII", "4"),
    ("6", "I", "6"),
    ("6", "II", "8"),
    ("6", "III", "X"),
    ("6", "IV", "E"),
    ("6", "V", "1"),
    ("6", "VI", "3"),
    ("6", "VII", "5"),
    ("7", "I", "7"),
    ("7", "II", "9"),
    ("7", "III", "E"),
    ("7", "IV", "0"),
    ("7", "V", "2"),
    ("7", "VI", "4"),
    ("7", "VII", "6"),
    ("8", "I", "8"),
    ("8", "II", "X"),
    ("8", "III", "0"),
    ("8", "IV", "1"),
    ("8", "V", "3"),
    ("8", "VI", "5"),
    ("8", "VII", "7"),
    ("9", "I", "9"),
    ("9", "II", "E"),
    ("9", "III", "1"),
    ("9", "IV", "2"),
    ("9", "V", "4"),
    ("9", "VI", "6"),
    ("9", "VII", "8"),
    ("X", "I", "X"),
    ("X", "II", "0"),
    ("X", "III", "2"),
    ("X", "IV", "3"),
    ("X", "V", "5"),
    ("X", "VI", "7"),
    ("X", "VII", "9"),
    ("E", "I", "E"),
    ("E", "II", "1"),
    ("E", "III", "3"),
    ("E", "IV", "4"),
    ("E", "V", "6"),
    ("E", "VI", "8"),
    ("E", "VII", "X"),
]


@pytest.mark.parametrize("duodecimal, mode, result", mode_test_cases)
def test_modes(duodecimal, mode, result):
    assert apply_mode(duodecimal, mode) == result


def test_composition():
    assert from_duodecimal(apply_mode(to_duodecimal("C"), "VI")) == "A"
