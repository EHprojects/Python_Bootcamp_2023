from art import logo

print(logo)
print("Welcome to the secret auction program.")


def find_highest(bid_record):
    high_bidder = ""
    high_bid = 0

    for bidder in bid_record:
        if bids[bidder] > high_bid:
            high_bidder = bidder
            high_bid = bids[bidder]

    print(f"The winner is {high_bidder} with a bid of ${high_bid}.")


bids = {}

continue_bidding = True
while continue_bidding:
    bidder = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[bidder] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ")
    if more_bidders == "no":
        continue_bidding = False

find_highest(bids)
