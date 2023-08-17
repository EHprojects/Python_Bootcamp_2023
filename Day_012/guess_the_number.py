# Welcome to the Number Guessing Game!
# I'm thinking of a number between 1 and 100.
# Pssst, the correct answer is 57
# Choose a difficulty. Type 'easy' or 'hard':
# You have 10 attempts remaining to guess the number.
# Make a guess:
# Make a guess: 50
# Too high.
# Guess again.
# You have 9 attempts remaining to guess the number.
# You got it! The answer was 27.
# You've run out of guesses, you lose.

from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_guess(user_guess, secret_num, turns):
    if user_guess == secret_num:
        print(f"You got it! The answer was {secret_num}.")
    elif user_guess < secret_num:
        print(f"Too low.")
        return turns - 1
    else:
        print("Too high.")
        return turns - 1


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")

    secret_num = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct answer is {secret_num}")

    turns = set_difficulty()

    user_guess = 0
    while user_guess != secret_num:
        print(f"You have {turns} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        turns = check_guess(user_guess, secret_num, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif user_guess != secret_num:
            print("Guess again.")


game()
