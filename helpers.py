# helpers.py
# Small functions that all three programs use.
# They ask the user for input and keep asking until the input is correct.


def print_title(title):
    # Print a title between two lines of "=" signs
    print()
    print("=" * 40)
    print("   " + title)
    print("=" * 40)


def get_number(message):
    # Ask for any number (it can have a decimal point, like 2.5)
    while True:
        text = input(message)
        try:
            number = float(text)
            return number
        except ValueError:
            print("Error: that is not a number. Try again.")


def get_whole_number(message):
    # Ask for a whole number (like 1, 2, 3)
    while True:
        text = input(message)
        try:
            number = int(text)
            return number
        except ValueError:
            print("Error: please type a whole number. Try again.")


def get_number_between(message, smallest, biggest):
    # Ask for a whole number that is between smallest and biggest
    while True:
        number = get_whole_number(message)
        if number < smallest:
            print("Error: the number must be", smallest, "or more.")
        elif number > biggest:
            print("Error: the number must be", biggest, "or less.")
        else:
            return number


def get_text(message):
    # Ask for text. Empty text is not allowed.
    while True:
        text = input(message).strip()
        if text == "":
            print("Error: you did not type anything. Try again.")
        else:
            return text


def ask_yes_no(message):
    # Ask a yes/no question. Returns True for yes, False for no.
    while True:
        answer = input(message + " (y/n): ").strip().lower()
        if answer == "y" or answer == "yes":
            return True
        elif answer == "n" or answer == "no":
            return False
        else:
            print("Error: please type y or n.")
