
while True:
    print("=" * 40)
    print("     Escape the Haunted House!!!")
    print("=" * 40)
    print("1. Start Game")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if not choice.isdigit():
        print("Invalid choice! Please enter a number")
        continue
    choice = int(choice)

    if choice == 1:
        name = input("Enter your name: ")
        if not name.strip() or not name.replace(" ", "").isalpha():
            print("Invalid! Please enter a valid name")
            continue
        name = name.title()
        print("Welcome,", name)

        while True:
            print("\nYou woke up in a dark hallway.")
            print("There are two doors in front of you.")
            print("1. Enter the left door which leads to the library.")
            print("2. Enter the right door which leads to the basement.")
            door = input("Which door will you choose? ")

            if not door.isdigit():
                print("Invalid choice! Please enter a number")
                continue
            door = int(door)

            if door == 1:
                print("\nYou entered the mysterious library.")
                print("You found a hidden key under an old book!")
                print("There is a locked door in front of you.")

                while True:
                    print("\n1. Use the key to open the door")
                    print("2. Search the bookshelves")

                    library_choice = input("Enter your choice: ")
                    if not library_choice.isdigit():
                        print("Invalid choice! Please enter a number")
                        continue
                    library_choice = int(library_choice)

                    if library_choice == 1:
                        print("\nYou opened the door!")
                        print("You discovered a secret passage.")
                        print("There are two paths ahead.")

                        while True:
                            print("\n1. Follow the strange footsteps")
                            print("2. Enter the dark tunnel")
                            passage_choice = input("Enter your choice: ")

                            if passage_choice == "1":
                                print("\nYou followed the footsteps.")
                                print("A ghost suddenly appeared!")
                                print("1. Run away")
                                print("2. Hide behind a statue")

                                while True:
                                    ghost_choice = input("Enter your choice: ")

                                    if ghost_choice == "1":
                                        print("You tried to run away!")
                                        print("But the ghost caught you!")
                                        print("YOU DIED! GAME OVER!")
                                        break

                                    elif ghost_choice == "2":
                                        print("You hid behind the statue.")
                                        print("The ghost passed without noticing you.")
                                        print("You discovered a hidden staircase!")
                                        print("You followed it and escaped!")
                                        print("CONGRATULATIONS! YOU WON!")
                                        break

                                    else:
                                        print("Invalid choice!")

                                break

                            elif passage_choice == "2":
                                print("\nYou entered the dark tunnel.")
                                print("You discovered another locked door!")
                                print("There is a strange message on the door.")
                                print("It says: Solve the riddle to escape!")

                                print("\nWhat has keys but cannot open locks?")
                                print("1. A piano")
                                print("2. A clock")
                                print("3. A mirror")

                                while True:
                                    answer = input("Enter your answer: ")

                                    if answer == "1":
                                        print("Correct answer!")
                                        print("The door opened!")
                                        print("You found the exit!")
                                        print("CONGRATULATIONS! YOU WON!")
                                        break

                                    elif answer == "2" or answer == "3":
                                        print("Wrong answer!")
                                        print("The door disappeared!")
                                        print("You are trapped forever!")
                                        print("GAME OVER!")
                                        break

                                    else:
                                        print("Invalid choice!")

                                break

                            else:
                                print("Invalid choice!")

                        break

                    elif library_choice == 2:
                        print("\nYou searched the bookshelves.")
                        print("You discovered a mysterious note!")
                        print("The note says: 'The darkness hides the truth.'")
                        print("You hear footsteps approaching!")
                        print("1. Hide under the table")
                        print("2. Run toward the library door")

                        while True:
                            library_second = input("Enter your choice: ")

                            if library_second == "1":
                                print("You hid under the table.")
                                print("The footsteps disappeared.")
                                print("You found a secret trapdoor!")
                                print("You climbed through it and escaped!")
                                print("CONGRATULATIONS! YOU WON!")
                                break

                            elif library_second == "2":
                                print("You ran toward the door.")
                                print("But a ghost was waiting for you!")
                                print("YOU DIED! GAME OVER!")
                                break

                            else:
                                print("Invalid choice!")

                        break

                    else:
                        print("Invalid choice!")

                break

            elif door == 2:
                print("\nYou entered the dark basement.")
                print("You encountered a ghost!!!!!")
                print("The ghost started chasing you!")

                print("\n1. Hide behind some boxes")
                print("2. Run toward the staircase")

                while True:
                    basement_choice = input("Enter your choice: ")

                    if basement_choice == "1":
                        print("\nYou hid behind some boxes.")
                        print("The ghost passed without seeing you.")
                        print("You noticed a flashlight and an old chest.")

                        print("\n1. Pick up the flashlight")
                        print("2. Open the old chest")

                        while True:
                            item_choice = input("Enter your choice: ")

                            if item_choice == "1":
                                print("\nYou picked up the flashlight.")
                                print("You discovered a hidden tunnel!")
                                print("You entered the tunnel.")
                                print("There is a window and another door.")

                                print("\n1. Open the window")
                                print("2. Open the mysterious door")

                                while True:
                                    final_choice = input("Enter your choice: ")

                                    if final_choice == "1":
                                        print("You opened the window.")
                                        print("You climbed outside!")
                                        print("CONGRATULATIONS! YOU ESCAPED!")
                                        break

                                    elif final_choice == "2":
                                        print("You opened the mysterious door.")
                                        print("A friendly ghost appeared!")
                                        print("The ghost showed you a secret exit.")
                                        print("SECRET ENDING! YOU WON!")
                                        break

                                    else:
                                        print("Invalid choice!")

                                break

                            elif item_choice == "2":
                                print("\nYou opened the old chest.")
                                print("A loud alarm started ringing!")
                                print("The ghost heard the noise.")
                                print("The ghost caught you!")
                                print("YOU DIED! GAME OVER!")
                                break

                            else:
                                print("Invalid choice!")

                        break

                    elif basement_choice == "2":
                        print("\nYou ran toward the staircase.")
                        print("Suddenly, the stairs collapsed!")
                        print("You fell into a dark hole!")
                        print("YOU DIED! GAME OVER!")
                        break

                    else:
                        print("Invalid choice!")

                break

            else:
                print("Invalid choice! Please choose 1 or 2")

        print("\nWould you like to play again?")
        print("1. Yes")
        print("2. No")

        while True:
            again = input("Enter your choice: ")

            if again == "1":
                break

            elif again == "2":
                print("Thanks for playing!")
                exit()

            else:
                print("Invalid choice!")

    elif choice == 2:
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice!")
