import pytest

from duodecimal_notation.convert import (
    from_duodecimal,
    from_midi,
    to_color,
    to_duodecimal,
    apply_mode,
    to_frequency,
    to_midi,
)

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


frequency_test_cases = [
    ("00", 16.35),  # C0
    ("01", 17.32),  # C♯0/D♭0
    ("02", 18.35),  # D0
    ("03", 19.45),  # D♯0/E♭0
    ("04", 20.60),  # E0
    ("05", 21.83),  # F0
    ("06", 23.12),  # F♯0/G♭0
    ("07", 24.50),  # G0
    ("08", 25.96),  # G♯0/A♭0
    ("09", 27.50),  # A0
    ("0X", 29.14),  # A♯0/B♭0
    ("0E", 30.87),  # B0
    ("10", 32.70),  # C1
    ("11", 34.65),  # C♯1/D♭1
    ("12", 36.71),  # D1
    ("13", 38.89),  # D♯1/E♭1
    ("14", 41.20),  # E1
    ("15", 43.65),  # F1
    ("16", 46.25),  # F♯1/G♭1
    ("17", 49.00),  # G1
    ("18", 51.91),  # G♯1/A♭1
    ("19", 55.00),  # A1
    ("1X", 58.27),  # A♯1/B♭1
    ("1E", 61.74),  # B1
    ("20", 65.41),  # C2
    ("21", 69.30),  # C♯2/D♭2
    ("22", 73.42),  # D2
    ("23", 77.78),  # D♯2/E♭2
    ("24", 82.41),  # E2
    ("25", 87.31),  # F2
    ("26", 92.50),  # F♯2/G♭2
    ("27", 98.00),  # G2
    ("28", 103.83),  # G♯2/A♭2
    ("29", 110.00),  # A2
    ("2X", 116.54),  # A♯2/B♭2
    ("2E", 123.47),  # B2
    ("30", 130.81),  # C3
    ("31", 138.59),  # C♯3/D♭3
    ("32", 146.83),  # D3
    ("33", 155.56),  # D♯3/E♭3
    ("34", 164.81),  # E3
    ("35", 174.61),  # F3
    ("36", 185.00),  # F♯3/G♭3
    ("37", 196.00),  # G3
    ("38", 207.65),  # G♯3/A♭3
    ("39", 220.00),  # A3
    ("3X", 233.08),  # A♯3/B♭3
    ("3E", 246.94),  # B3
    ("40", 261.63),  # C4
    ("41", 277.18),  # C♯4/D♭4
    ("42", 293.66),  # D4
    ("43", 311.13),  # D♯4/E♭4
    ("44", 329.63),  # E4
    ("45", 349.23),  # F4
    ("46", 369.99),  # F♯4/G♭4
    ("47", 392.00),  # G4
    ("48", 415.30),  # G♯4/A♭4
    ("49", 440.00),  # A4
    ("4X", 466.16),  # A♯4/B♭4
    ("4E", 493.88),  # B4
    ("50", 523.25),  # C5
    ("51", 554.37),  # C♯5/D♭5
    ("52", 587.33),  # D5
    ("53", 622.25),  # D♯5/E♭5
    ("54", 659.25),  # E5
    ("55", 698.46),  # F5
    ("56", 739.99),  # F♯5/G♭5
    ("57", 783.99),  # G5
    ("58", 830.61),  # G♯5/A♭5
    ("59", 880.00),  # A5
    ("5X", 932.33),  # A♯5/B♭5
    ("5E", 987.77),  # B5
    ("60", 1046.50),  # C6
    ("61", 1108.73),  # C♯6/D♭6
    ("62", 1174.66),  # D6
    ("63", 1244.51),  # D♯6/E♭6
    ("64", 1318.51),  # E6
    ("65", 1396.91),  # F6
    ("66", 1479.98),  # F♯6/G♭6
    ("67", 1567.98),  # G6
    ("68", 1661.22),  # G♯6/A♭6
    ("69", 1760.00),  # A6
    ("6X", 1864.66),  # A♯6/B♭6
    ("6E", 1975.53),  # B6
    ("70", 2093.00),  # C7
    ("71", 2217.46),  # C♯7/D♭7
    ("72", 2349.32),  # D7
    ("73", 2489.02),  # D♯7/E♭7
    ("74", 2637.02),  # E7
    ("75", 2793.83),  # F7
    ("76", 2959.96),  # F♯7/G♭7
    ("77", 3135.96),  # G7
    ("78", 3322.44),  # G♯7/A♭7
    ("79", 3520.00),  # A7
    ("7X", 3729.31),  # A♯7/B♭7
    ("7E", 3951.07),  # B7
    ("80", 4186.01),  # C8
]


@pytest.mark.parametrize("duodecimal, frequency", frequency_test_cases)
def test_to_frequency(duodecimal, frequency):
    assert to_frequency(duodecimal) == pytest.approx(frequency, 0.01)


midi_test_cases = [
    # Cases for midi notes 0 to 11 not defined yet.
    ("00", 12),  # C0
    ("01", 13),  # C♯0/D♭0
    ("02", 14),  # D0
    ("03", 15),  # D♯0/E♭0
    ("04", 16),  # E0
    ("05", 17),  # F0
    ("06", 18),  # F♯0/G♭0
    ("07", 19),  # G0
    ("08", 20),  # G♯0/A♭0
    ("09", 21),  # A0
    ("0X", 22),  # A♯0/B♭0
    ("0E", 23),  # B0
    ("10", 24),  # C1
    ("40", 60),  # C4
    ("97", 127),  # G9
]


@pytest.mark.parametrize("duodecimal, midi", midi_test_cases)
def test_midi(duodecimal, midi):
    assert to_midi(duodecimal) == midi
    assert from_midi(midi) == duodecimal


color_test_cases = [
    ("0", "#FF6666"),
    ("1", "#FF9966"),
    ("2", "#FFCC66"),
    ("3", "#FFFF66"),
    ("4", "#CCFF66"),
    ("5", "#99FF66"),
    ("6", "#66FF66"),
    ("7", "#66FF99"),
    ("8", "#66FFCC"),
    ("9", "#66CCFF"),
    ("X", "#9999FF"),
    ("E", "#CC66FF"),
    ("00", "#FF6666"),
    ("01", "#FF9966"),
    ("02", "#FFCC66"),
    ("03", "#FFFF66"),
    ("04", "#CCFF66"),
    ("05", "#99FF66"),
    ("06", "#66FF66"),
    ("07", "#66FF99"),
    ("08", "#66FFCC"),
    ("09", "#66CCFF"),
    ("0X", "#9999FF"),
    ("0E", "#CC66FF"),
    ("90", "#FF6666"),
    ("9E", "#CC66FF"),
]


@pytest.mark.parametrize("duodecimal, color", color_test_cases)
def test_to_color(duodecimal, color):
    assert to_color(duodecimal) == color
