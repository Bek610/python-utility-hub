# calculator.py
# Project 1: Simple Calculator
# The user picks an operation, types two numbers, and sees the answer.
# Every answer is saved in a history list.

import math
from helpers import print_title, get_number, ask_yes_no


class Calculator:

    def __init__(self):
        # A list that keeps every calculation the user made
        self.history = []

        # A dictionary: menu number -> name of the operation
        self.menu = {
            "1": "Add (+)",
            "2": "Subtract (-)",
            "3": "Multiply (*)",
            "4": "Divide (/)",
            "5": "Power (^)",
            "6": "Remainder (%)",
            "7": "Square root",
            "8": "Show history",
            "9": "Clear history",
            "0": "Back to main menu",
        }

    # ---------- the math ----------

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("You cannot divide by zero.")
        return a / b

    def power(self, a, b):
        try:
            return a ** b
        except OverflowError:
            raise ValueError("The answer is too big.")

    def remainder(self, a, b):
        if b == 0:
            raise ZeroDivisionError("You cannot divide by zero.")
        return a % b

    def square_root(self, a):
        if a < 0:
            raise ValueError("You cannot take the square root of a negative number.")
        return math.sqrt(a)

    # ---------- history ----------

    def save_to_history(self, text):
        self.history.append(text)

    def show_history(self):
        print_title("History")
        if len(self.history) == 0:
            print("No calculations yet.")
        else:
            number = 1
            for item in self.history:
                print(str(number) + ". " + item)
                number = number + 1

    def clear_history(self):
        if ask_yes_no("Do you want to delete the history?"):
            self.history = []
            print("History deleted.")

    # ---------- show a number nicely ----------

    def nice(self, number):
        # Show 5.0 as 5, and 3.14159265 as 3.1416
        if number == int(number):
            return str(int(number))
        return str(round(number, 4))

    # ---------- the menu ----------

    def show_menu(self):
        print_title("Simple Calculator")
        for key in self.menu:
            print(key + ". " + self.menu[key])

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose an option: ").strip()

            if choice == "0":
                print("Going back to the main menu...")
                break
            elif choice == "8":
                self.show_history()
            elif choice == "9":
                self.clear_history()
            elif choice == "7":
                self.do_square_root()
            elif choice in ["1", "2", "3", "4", "5", "6"]:
                self.do_two_numbers(choice)
            else:
                print("Error: '" + choice + "' is not on the menu.")

    def do_square_root(self):
        a = get_number("Enter a number: ")
        try:
            answer = self.square_root(a)
            text = "sqrt(" + self.nice(a) + ") = " + self.nice(answer)
            print("Answer:", text)
            self.save_to_history(text)
        except ValueError as error:
            print("Math error:", error)

    def do_two_numbers(self, choice):
        a = get_number("Enter the first number: ")
        b = get_number("Enter the second number: ")

        # A tuple with the symbols, in the same order as the menu (1 to 6)
        symbols = ("+", "-", "*", "/", "^", "%")
        symbol = symbols[int(choice) - 1]

        try:
            if choice == "1":
                answer = self.add(a, b)
            elif choice == "2":
                answer = self.subtract(a, b)
            elif choice == "3":
                answer = self.multiply(a, b)
            elif choice == "4":
                answer = self.divide(a, b)
            elif choice == "5":
                answer = self.power(a, b)
            else:
                answer = self.remainder(a, b)

            text = self.nice(a) + " " + symbol + " " + self.nice(b) + " = " + self.nice(answer)
            print("Answer:", text)
            self.save_to_history(text)

        except ZeroDivisionError as error:
            print("Math error:", error)
        except ValueError as error:
            print("Math error:", error)


# This lets you run the calculator by itself: python3 calculator.py
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
