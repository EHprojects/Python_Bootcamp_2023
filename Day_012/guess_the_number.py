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

print(logo)
print("Welcome to the Number Guessing Game!")

secret_num = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {secret_num}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

num_guesses = 0
if difficulty == "easy":
    num_guesses = 10
else:
    num_guesses = 5


def check_guess(user_guess, secret_num):
    pass


game_over = False
# repeat from here

while not game_over:
    print(f"You have {num_guesses} attempts remaining to guess the number.")

    user_guess = int(input("Make a guess: "))

    if user_guess == secret_num:
        print(f"You got it! The answer was {secret_num}.")
    elif user_guess < secret_num:
        print(f"Too low.")
        num_guesses -= 1
    else:
        print("Too high.")
        num_guesses -= 1

    if num_guesses > 0:
        print("Guess again.")
    else:
        print("You've run out of guesses, you lose.")
        game_over = True



