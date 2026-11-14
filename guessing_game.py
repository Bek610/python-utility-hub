# guessing_game.py
# Project 3: Number Guessing Game
# The computer picks a secret number. The player tries to guess it.
# After each guess the game says "higher" or "lower".

import random
from helpers import print_title, get_number_between, ask_yes_no

SCORE_FILE = "scores.txt"


class GuessingGame:

    def __init__(self):
        # A dictionary of levels.
        # Each level is a tuple: (name, biggest number, number of tries)
        self.levels = {
            "1": ("Easy", 20, 6),
            "2": ("Medium", 50, 7),
            "3": ("Hard", 100, 7),
        }

        # Best result for each level (fewest tries). Example: {"Easy": 3}
        self.best = {}
        self.load_scores()

        self.games_played = 0
        self.games_won = 0

    # ---------- saving and loading the best scores ----------

    def load_scores(self):
        # Each line in the file looks like:  Easy,3
        try:
            file = open(SCORE_FILE, "r")
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    try:
                        self.best[parts[0]] = int(parts[1])
                    except ValueError:
                        pass  # skip a broken line
            file.close()
        except FileNotFoundError:
            self.best = {}

    def save_scores(self):
        try:
            file = open(SCORE_FILE, "w")
            for level_name in self.best:
                file.write(level_name + "," + str(self.best[level_name]) + "\n")
            file.close()
        except OSError:
            print("Error: could not save the scores.")

    # ---------- hints ----------

    def how_close(self, guess, secret):
        # An extra hint: how far the guess is from the secret number
        distance = abs(guess - secret)
        if distance <= 3:
            return "Very hot!"
        elif distance <= 10:
            return "Warm."
        else:
            return "Cold."

    # ---------- one game ----------

    def play_one_game(self, level):
        name = level[0]
        biggest = level[1]
        tries = level[2]

        secret = random.randint(1, biggest)
        guesses = []  # a list of all the guesses in this game

        print()
        print("I am thinking of a number from 1 to " + str(biggest) + ".")
        print("You have " + str(tries) + " tries. Good luck!")

        for attempt in range(1, tries + 1):
            message = "Try " + str(attempt) + " of " + str(tries) + " - your guess: "
            guess = get_number_between(message, 1, biggest)

            if guess in guesses:
                print("You already guessed that number!")
            guesses.append(guess)

            if guess == secret:
                score = (tries - attempt + 1) * 10
                print("Correct! The number was " + str(secret) + ".")
                print("You needed " + str(attempt) + " tries. Score: " + str(score))
                self.check_best(name, attempt)
                return True
            elif guess < secret:
                print("Go higher. " + self.how_close(guess, secret))
            else:
                print("Go lower. " + self.how_close(guess, secret))

        print("No more tries! The number was " + str(secret) + ".")
        print("Your guesses were:", guesses)
        return False

    def check_best(self, name, attempt):
        # Save a new best result if this one is better
        if name not in self.best or attempt < self.best[name]:
            self.best[name] = attempt
            self.save_scores()
            print("New best result for " + name + "!")

    # ---------- screens ----------

    def show_scores(self):
        print_title("Best Results")
        for key in self.levels:
            name = self.levels[key][0]
            if name in self.best:
                print(name + ": " + str(self.best[name]) + " tries")
            else:
                print(name + ": no wins yet")
        print("This time: won " + str(self.games_won) + " of " + str(self.games_played) + " games")

    def show_rules(self):
        print_title("How to Play")
        print("1. Pick a level.")
        print("2. Guess the secret number.")
        print("3. I tell you to go higher or lower.")
        print("4. Fewer tries = more points!")

    def choose_level(self):
        print("Levels:")
        for key in self.levels:
            level = self.levels[key]
            print(key + ". " + level[0] + " (1 to " + str(level[1]) + ", " + str(level[2]) + " tries)")
        while True:
            choice = input("Choose a level: ").strip()
            if choice in self.levels:
                return self.levels[choice]
            print("Error: please type 1, 2 or 3.")

    # ---------- the menu ----------

    def run(self):
        while True:
            print_title("Number Guessing Game")
            print("1. Play")
            print("2. Best results")
            print("3. How to play")
            print("0. Back to main menu")
            choice = input("Choose an option: ").strip()

            if choice == "0":
                print("Going back to the main menu...")
                break
            elif choice == "1":
                level = self.choose_level()
                play_again = True
                while play_again:
                    self.games_played = self.games_played + 1
                    if self.play_one_game(level):
                        self.games_won = self.games_won + 1
                    play_again = ask_yes_no("Play again?")
            elif choice == "2":
                self.show_scores()
            elif choice == "3":
                self.show_rules()
            else:
                print("Error: '" + choice + "' is not on the menu.")


# Run the game by itself: python3 guessing_game.py
if __name__ == "__main__":
    game = GuessingGame()
    game.run()
