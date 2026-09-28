#!/usr/bin/env python3

from pathlib import Path
import re
import shutil


SAVE_FILE = Path.home() / (
    ".local/share/Steam/steamapps/compatdata/4094660/pfx/"
    "drive_c/users/steamuser/AppData/Local/Rivage/Saved/SaveGames/savefile.sav"
)


# Make sure the save file exists
if not SAVE_FILE.exists():
    print(f"ERROR: Save file not found:")
    print(SAVE_FILE)
    input("\nPress Enter to close...")
    raise SystemExit(1)


# Create a backup before modifying anything
BACKUP_FILE = SAVE_FILE.with_suffix(".sav.backup")

try:
    shutil.copy2(SAVE_FILE, BACKUP_FILE)
    print(f"Backup created:")
    print(BACKUP_FILE)
    print()
except Exception as e:
    print(f"ERROR: Could not create backup: {e}")
    input("\nPress Enter to close...")
    raise SystemExit(1)


# Read the save file
with SAVE_FILE.open("rb") as f:
    data = bytearray(f.read())


# --------------------------------------------------
# Find the date
# --------------------------------------------------

dates = list(re.finditer(rb'\b\d{2}/\d{2}/2435\b', data))

if not dates:
    print("ERROR: Could not find a date ending in 2435.")
    input("\nPress Enter to close...")
    raise SystemExit(1)

date_match = dates[-1]
date = date_match.group().decode("ascii")


# --------------------------------------------------
# Find all numeric sequences
# --------------------------------------------------

numbers = list(re.finditer(rb'\b\d+\b', data))


# Find the last 7-digit number
seven_digit = [
    match for match in numbers
    if len(match.group()) == 7
]

# Find the last 10-digit number
ten_digit = [
    match for match in numbers
    if len(match.group()) == 10
]


if not seven_digit:
    print("ERROR: Could not find a 7-digit number.")
    input("\nPress Enter to close...")
    raise SystemExit(1)


if not ten_digit:
    print("ERROR: Could not find a 10-digit number.")
    input("\nPress Enter to close...")
    raise SystemExit(1)


number1_match = seven_digit[-1]
number2_match = ten_digit[-1]

number1 = number1_match.group().decode("ascii")
number2 = number2_match.group().decode("ascii")


# --------------------------------------------------
# Display what was found
# --------------------------------------------------

print(f"Date:      {date}")
print(f"Number 1:  {number1}")
print(f"Number 2:  {number2}")
print()


# --------------------------------------------------
# Replace the numbers with all fives
# --------------------------------------------------

data[number1_match.start():number1_match.end()] = b"5555555"
data[number2_match.start():number2_match.end()] = b"5555555555"


# --------------------------------------------------
# Write the modified save file
# --------------------------------------------------

with SAVE_FILE.open("wb") as f:
    f.write(data)


print("Save file modified:")
print(f"Number 1 -> 5555555")
print(f"Number 2 -> 5555555555")
print()
print(f"Backup: {BACKUP_FILE}")

input("\nPress Enter to close...")
