############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# Do you want to play a game of Blackjack? Type 'y' or 'n': Traceback (most recent call last):


# Your cards: [9, 7], current score: 16
# Computer's first card: 11
# Type 'y' to get another card, type 'n' to pass:
#
# Your final hand: [9, 7], final score: 16
# Computer's final hand: [11, 6], final score: 17
# You lose 😤
# You went over. You lose 😭
# Draw 🙃
# Opponent went over. You win 😁
# You win 😃
# Win with a Blackjack 😎
# Lose, opponent has Blackjack 😱

from art import logo
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calc_hand(cards):
    total = 0
    for i in range(len(cards)):
        total = total + cards[i]
        if total > 21 and cards[i] == 11:
            cards[i] = 1
            total -= 10
    return total


print(logo)
game_on = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while game_on == "y":
    player_cards = []
    dealer_cards = []

    player_cards.append(deal_card())
    dealer_cards.append(deal_card())
    player_cards.append(deal_card())
    dealer_cards.append(deal_card())

    player_total = calc_hand(player_cards)
    dealer_total = calc_hand(dealer_cards)

    print(f"Your cards: {player_cards}, current score: {player_total}")
    print(f"Computer's first card: {dealer_cards[0]}")

    another_card = False
    player_move = input(f"Type 'y' to get another card, type 'n' to pass: ")

    if player_move == "y":
        another_card = True

    while another_card:
        player_cards.append(deal_card())
        player_total = calc_hand(player_cards)
        print(f"Your cards: {player_cards}, current score: {player_total}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if player_total <= 21:
            player_move = input(f"Type 'y' to get another card, type 'n' to pass: ")
            if player_move == "y":
                another_card = True
            else:
                another_card = False
        else:
            another_card = False

    while dealer_total < 17:
        dealer_cards.append(deal_card())
        dealer_total = calc_hand(dealer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_total}")
    print(f"Computer's final hand: {dealer_cards}, final score: {dealer_total}")

    if (player_total == 21 and len(player_cards) == 2) and (dealer_total == 21 and len(dealer_cards) == 2):
        print("Draw 🙃")
    elif player_total == 21 and len(player_cards) == 2:
        print("Win with a Blackjack 😎")
    elif dealer_total == 21 and len(dealer_cards) == 2:
        print("Lose, opponent has Blackjack 😱")
    elif player_total > 21:
        print("You went over. You lose 😭")
    elif dealer_total > 21:
        print("Opponent went over. You win 😁")
    elif player_total == dealer_total:
        print("Draw 🙃")
    elif player_total > dealer_total:
        print("You win 😃")
    elif dealer_total > player_total:
        print("You lose 😤")

    game_on = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
