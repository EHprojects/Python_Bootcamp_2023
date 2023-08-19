from art import logo, vs
from game_data import data
import random

score = 0
correct_choice = "a"
game_over = False

# logo
print(logo)

# compare A - Compare A: FC Barcelona, a Football club, from Spain.
compare_a = data[random.randint(0, len(data) - 1)]

# compare B
compare_b = data[random.randint(0, len(data) - 1)]
while compare_b == compare_a:  # ensures the two random comparisons are not the same
    compare_b = data[random.randint(0, len(data) - 1)]

while not game_over:
    if correct_choice == "b":
        compare_a = compare_b

    compare_b = data[random.randint(0, len(data) - 1)]

    while compare_b == compare_a:  # ensures the two random comparisons are not the same
        compare_b = data[random.randint(0, len(data) - 1)]

    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")
    print(vs)
    print(f"Compare B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")

    # input - Who has more followers? Type 'A' or 'B':
    user_choice = input(f"Who has more followers? Type 'A' or 'B': ").lower()

    # You're right! Current score: 2.
    # Sorry, that's wrong. Final score: 3
    if user_choice == "a" and compare_a["follower_count"] > compare_b["follower_count"]:
        correct_choice = "a"
        score += 1
        print(f"You're right! Current score: {score}.")
    elif user_choice == "b" and compare_b["follower_count"] > compare_a["follower_count"]:
        correct_choice = "b"
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
