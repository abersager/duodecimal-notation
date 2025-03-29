from typing import Optional
import typer
from typer import Typer
from click import Choice
from duodecimal_notation.convert import (
    from_duodecimal,
    to_duodecimal,
    apply_mode,
    to_frequency,
    to_midi,
    from_midi,
    to_color,
    Mode,
    value_map,
)

app = Typer(help="Duodecimal notation utility for music theory operations.")

# Use existing constants from convert.py
ACCIDENTALS = ["sharp", "flat"]
MODES = list(Mode.__args__)  # Get modes from the Literal type
VALID_NOTES = list(value_map.keys())  # Get valid notes from the value map


@app.command()
def convert(
    note: str,
    accidental: Optional[str] = typer.Option(
        None,
        "--accidental",
        "-a",
        help="Preferred accidental notation",
        case_sensitive=False,
        click_type=Choice(ACCIDENTALS),
    ),
):
    """Convert between traditional music notation and duodecimal."""
    try:
        if len(note) <= 2 and note[-1] in VALID_NOTES:
            # Converting from duodecimal to traditional
            result = from_duodecimal(note[-1], accidental)
            typer.echo(result)
        else:
            # Converting from traditional to duodecimal
            result = to_duodecimal(note)
            typer.echo(result)
    except KeyError:
        typer.echo(f"Error: Invalid note '{note}'", err=True)
        raise typer.Exit(1)


@app.command()
def mode(
    note: str,
    mode: str = typer.Argument(
        ..., help="Mode to apply (I through VII)", click_type=Choice(MODES)
    ),
):
    """Apply a mode transformation to a duodecimal note."""
    try:
        if note[-1] not in VALID_NOTES:
            raise KeyError("Invalid note")
        result = apply_mode(note[-1], mode)
        typer.echo(result)
    except KeyError:
        typer.echo(f"Error: Invalid note '{note}' or mode '{mode}'", err=True)
        raise typer.Exit(1)


@app.command()
def freq(note: str):
    """Get the frequency in Hz for a given duodecimal note."""
    try:
        result = to_frequency(note)
        typer.echo(f"{result:.2f} Hz")
    except (KeyError, ValueError):
        typer.echo(f"Error: Invalid note '{note}'", err=True)
        raise typer.Exit(1)


@app.command()
def midi(note: str):
    """Convert between MIDI note numbers and duodecimal notation."""
    try:
        if note.isdigit():
            # Converting from MIDI to duodecimal
            result = from_midi(int(note))
        else:
            # Converting from duodecimal to MIDI
            result = to_midi(note)
        typer.echo(result)
    except (KeyError, ValueError):
        typer.echo(f"Error: Invalid input '{note}'", err=True)
        raise typer.Exit(1)


@app.command()
def color(note: str):
    """Get the color representation of a duodecimal note."""
    try:
        result = to_color(note)
        typer.echo(result)
    except KeyError:
        typer.echo(f"Error: Invalid note '{note}'", err=True)
        raise typer.Exit(1)


def main():
    app()


if __name__ == "__main__":
    main()
