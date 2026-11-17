# Python Group Project

This is our group project for COP 1500 (Introduction to Computer Science) at FGCU.
We made 6 small Python programs, 3 each.

**Bilguun Shagdarsuren**
- Simple Calculator
- To-Do List
- Number Guessing Game

**Tsogzolmaa Mandalbayar**
- Unit Converter
- Password Generator
- Text-based Adventure Game (Escape the Haunted House)

## How to run

You just need Python 3, nothing else to install.

Open a terminal in this folder and type the name of the program you want:

```
python3 main.py
python3 unit_converter.py
python3 password_generator.py
python3 text_based_adventure_game.py
```

(on Windows use `python` instead of `python3`)

`main.py` opens a menu with the calculator, the to-do list and the guessing game.

## What each program does

**Calculator** - add, subtract, multiply, divide, power, remainder and square root. It remembers your answers in a history list. If you divide by zero or type letters it shows an error instead of crashing.

**To-Do List** - add tasks with a priority (high, medium, low), mark them done, edit, delete and search them. Tasks are saved in `tasks.txt` so they are still there next time.

**Guessing Game** - the computer picks a random number and you try to guess it. You get "higher" or "lower" hints. There are 3 levels and your best results are saved in `scores.txt`.

**Unit Converter** - converts temperature, distance, weight and time.

**Password Generator** - makes a random password with the length you choose.

**Adventure Game** - you are stuck in a haunted house and you pick doors and paths. Some choices win and some lose.

## Files

- `main.py` - main menu (start here)
- `helpers.py` - small functions for checking user input
- `calculator.py`, `todo_list.py`, `guessing_game.py` - Bilguun's programs
- `unit_converter.py`, `password_generator.py`, `text_based_adventure_game.py` - Tsogzolmaa's programs
