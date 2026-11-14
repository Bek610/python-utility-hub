# Python Utility Hub

A console program that combines three Python mini-projects in one menu:

1. **Simple Calculator** – add, subtract, multiply, divide, power, remainder, square root, with history
2. **To-Do List** – add, show, finish, edit, delete and search tasks, show them by priority, statistics; tasks are saved to `tasks.txt`
3. **Number Guessing Game** – three levels, higher/lower and hot/cold hints, score, best results saved to `scores.txt`

## How to run

You need Python 3. No extra libraries are needed.

```
python3 main.py
```

(On Windows type `python main.py`.)

Each program can also be run by itself:

```
python3 calculator.py
python3 todo_list.py
python3 guessing_game.py
```

## Files

| File | What it does |
|------|--------------|
| `main.py` | Main menu, starts the three programs |
| `helpers.py` | Input functions that keep asking until the input is correct |
| `calculator.py` | `Calculator` class |
| `todo_list.py` | `TodoList` class, saves tasks to a text file |
| `guessing_game.py` | `GuessingGame` class, saves best results to a text file |

## Python topics used

- Loops: `while True` menus, `for` loops, `break`, `continue`
- Data types: `int`, `float`, `str`, `bool`
- Lists, tuples and dictionaries
- Functions with parameters and return values
- Exceptions: `try` / `except`, `raise`, `ValueError`, `ZeroDivisionError`, `IndexError`, `FileNotFoundError`
- Classes and objects: `__init__`, `self`, methods
- Reading and writing text files

Built-in modules used: `math`, `random`.
