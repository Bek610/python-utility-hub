# main.py
# Python Utility Hub - START THE PROGRAM HERE
# How to run:  python3 main.py
#
# This file shows the main menu and opens one of the three projects:
#   1. Simple Calculator
#   2. To-Do List
#   3. Number Guessing Game

from calculator import Calculator
from todo_list import TodoList
from guessing_game import GuessingGame
from helpers import print_title, ask_yes_no


def main():
    print_title("Welcome to the Python Utility Hub")

    # Make one object for each program.
    # (So the calculator history is kept while the program is open.)
    calculator = Calculator()
    todo = TodoList()
    game = GuessingGame()

    while True:
        print_title("Main Menu")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Guessing Game")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            calculator.run()
        elif choice == "2":
            todo.run()
        elif choice == "3":
            game.run()
        elif choice == "0":
            if ask_yes_no("Do you really want to exit?"):
                print("Goodbye! Thank you for using the Utility Hub.")
                break
        else:
            print("Error: '" + choice + "' is not on the menu.")


# The program starts here
try:
    main()
except KeyboardInterrupt:
    # The user pressed Ctrl+C
    print()
    print("Program closed. Goodbye!")
