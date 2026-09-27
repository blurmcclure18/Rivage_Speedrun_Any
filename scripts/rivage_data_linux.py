#!/usr/bin/env python3

from pathlib import Path
import re

SAVE_FILE = Path.home() / (
    ".local/share/Steam/steamapps/compatdata/4094660/pfx/"
    "drive_c/users/steamuser/AppData/Local/Rivage/Saved/SaveGames/savefile.sav"
)

with SAVE_FILE.open("rb") as f:
    data = f.read()


# Find the date with the fixed year 2435
dates = re.findall(rb'\b\d{2}/\d{2}/2435\b', data)

if not dates:
    raise RuntimeError("Could not find a date ending in 2435")

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
    raise RuntimeError("Could not find a 7-digit number")

if not ten_digit:
    raise RuntimeError("Could not find a 10-digit number")


number1 = seven_digit[-1].decode("ascii")
number2 = ten_digit[-1].decode("ascii")


print(f"Date:      {date}")
print(f"ID:  {number1}")
print(f"Code:  {number2}")
input("\nPress Enter to Close...")
