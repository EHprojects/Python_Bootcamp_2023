import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
choices = [rock, paper, scissors]
player_choice = int(input("What do you choose? 0 - Rock, 1 - Paper, 2 - Scissors\n"))
computer_choice = random.randint(0, 2)

print(choices[player_choice])
print(f"Computer chose:\n{choices[computer_choice]}")

if player_choice == computer_choice:
    print("It's a draw.")
elif player_choice == 0 and computer_choice == 2:
    print("You win.")
elif player_choice == 1 and computer_choice == 0:
    print("You win.")
elif player_choice == 2 and computer_choice == 1:
    print("You win.")
else:
    print("You lose.")
