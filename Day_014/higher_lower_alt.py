from art import logo, vs
from game_data import data
import random


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_cntry = account["country"]
    return f"{account_name}, a {account_desc}, from {account_cntry}."


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if the guess is correct."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display art
print(logo)
score = 0
game_over = False
account_b = random.choice(data)

while not game_over:

    # Generate random accounts from game data
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input(f"Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower counts
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {score}")
