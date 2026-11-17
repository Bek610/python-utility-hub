import random
import string

while True:
    print("=" * 40)
    print("    Password Generator")
    print("=" * 40)
    print("1. Generate a Password")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if not choice.isdigit():
        print("Please enter a number")
        continue

    choice = int(choice)

    if choice == 1:
        length = input("Enter your password length: ")

        if not length.isdigit():
            print("Please enter a number.")
            continue

        length = int(length)

        if length < 8:
            print("Safe password's length must be at least 8")
            continue

        password = ""

        for i in range(length):
            password += random.choice(string.ascii_letters + string.digits + string.punctuation)
        print("Generated Password:", password)

    elif choice == 2:
        print(" Exiting the program")
        break
    else:
        print("Invalid choice")
