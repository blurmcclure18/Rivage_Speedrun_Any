from pathlib import Path
import os
import re


# Windows save file location
SAVE_FILE = (
    Path(os.environ["LOCALAPPDATA"])
    / "Rivage"
    / "Saved"
    / "SaveGames"
    / "savefile.sav"
)


# Make sure the save file exists
if not SAVE_FILE.exists():
    print(f"ERROR: Save file not found:")
    print(SAVE_FILE)
    input("\nPress Enter to close...")
    raise SystemExit(1)


with SAVE_FILE.open("rb") as f:
    data = f.read()


# Find the date with the fixed year 2435
dates = re.findall(rb'\b\d{2}/\d{2}/2435\b', data)

if not dates:
    print("ERROR: Could not find a date ending in 2435.")
    input("\nPress Enter to close...")
    raise SystemExit(1)

date = dates[-1].decode("ascii")


# Find all digit sequences
numbers = re.findall(rb'\b\d+\b', data)


# Find the last 7-digit number
seven_digit = [
    n for n in numbers
    if len(n) == 7
]

# Find the last 10-digit number
ten_digit = [
    n for n in numbers
    if len(n) == 10
]


if not seven_digit:
    print("ERROR: Could not find a 7-digit number.")
    input("\nPress Enter to close...")
    raise SystemExit(1)


if not ten_digit:
    print("ERROR: Could not find a 10-digit number.")
    input("\nPress Enter to close...")
    raise SystemExit(1)


number1 = seven_digit[-1].decode("ascii")
number2 = ten_digit[-1].decode("ascii")


# Display results
print(f"Date:      {date}")
print(f"Number 1:  {number1}")
print(f"Number 2:  {number2}")


# Keep the window open
input("\nPress Enter to close...")
