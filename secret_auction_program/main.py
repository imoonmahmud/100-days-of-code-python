import os, platform
from art import logo

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder, amount in bidding_record.items():
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print(f"The winner is {winner.title()} with a bid of ${highest_bid}")

bids = {}
while True:
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    bids[name] = bid

    should_continue = input("Are there any other bidders? Type (yes/no) ").lower()
    while should_continue not in ['yes', 'no']:
        should_continue = input("Are there any other bidders? Type (yes/no) ").lower()

    if should_continue != 'no':
        clear()
        continue
    else:
        clear()
        print(logo)
        find_highest_bidder(bids)
        break