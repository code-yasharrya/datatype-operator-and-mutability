# Practical 2 — Data Types, Operators & Mutability

MCA Semester I — Python Programming | Unit I / CO1

## macOS setup
```bash
mkdir -p ~/Documents/Practical2
cd ~/Documents/Practical2
python3 -m venv .venv
source .venv/bin/activate
python practical2.py
```

Copy the provided project files into `~/Documents/Practical2` before running.

## Deliverables
- `practical2.py`: Experiments A–G and inventory challenge.
- `prediction_log.txt`: Predicted outputs, reference observations, explanations.
- `reflection.txt`: Five-line reflection.
- `screenshots/`: Add a screenshot of your actual terminal output here.

To save the terminal output:
```bash
python practical2.py | tee screenshots/challenge_output.txt
```

For an actual screenshot on macOS, press Command + Shift + 4, select the terminal area, then move the resulting screenshot into `screenshots/`.

## Viva quick answers
- `/` gives true division, `//` gives floor division, and `%` gives remainder.
- `==` compares values; `is` checks whether objects are identical.
- Lists, dictionaries and sets are mutable built-in types.
- Aliasing means two variable names refer to the same object.
- `int('twenty')` raises `ValueError` because the text is not a valid integer representation.
