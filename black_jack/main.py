import random
import itertools

def drawn_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    deck = list(itertools.product(cards, suits))
    random.shuffle(deck)
    return random.choice(deck)[0]

def c_score(hand):
    global computer_score
    has_ace = False
    while True:
        for card in hand:
            if card == 'ace':
                has_ace = True
            elif card == 'jack' or card == 'queen' or card == 'king':
                computer_score += 10
            else:
                computer_score += int(card)
        
        if has_ace:
            if computer_score in [11, 12, 13, 14, 15] or computer_score <= 5:
                hand.append(drawn_card())
                computer_score = 0
                continue
            elif computer_score in [6, 7, 8, 9, 10]:
                computer_score += 11
                break
            else:
                computer_score += 1
                break

        if computer_score <= 15 and 'ace' not in hand:
            hand.append(drawn_card())
            computer_score = 0
            continue
        else:
            break
    return computer_score

def u_score(hand):
    global user_score
    has_ace = False
    while True:
        for card in hand:
            if card == 'ace':
                has_ace = True
            elif card == 'jack' or card == 'queen' or card == 'king':
                user_score += 10
            else:
                user_score += int(card)
        print(f"Your cards: {hand}, current score: {user_score}")

        if has_ace:
            want_card = input("Do you want to get a card? Type (yes/no): ").lower()
            if want_card != 'no':
                hand.append(drawn_card())
                user_score = 0
                continue
            else:
                ace = 0
                for card in hand:
                    if card == 'ace':
                        ace += 1
                
                if ace == 1:
                    ace_point = int(input("What point do you want for ace?: "))
                    if ace_point == 11:
                        user_score += 11
                    else:
                        user_score += 1
                else:
                    while True:
                        ace_point = int(input("What point do you want for ace?: "))
                        if ace_point == 11:
                            user_score += 11
                        else:
                            user_score += 1
                        ace -= 1
                        if ace == 0:
                            break
                break
        else:
            want_card = input("Do you want to get a card? Type (yes/no): ").lower()
            if want_card != 'no':
                hand.append(drawn_card())
                user_score = 0
                continue
            else:
                break

def compare(machine, user):
    if user == machine:
        return "Draw 🙃"
    elif user > 21:
        return "You went over. You lose 😭"
    elif machine > 21:
        return "Opponent went over. You win 😁"
    elif user > machine:
        return "You win 😃"
    else:
        return "You lose 😤"

while input("Do you want to play a game of Blackjack? Type (yes/no): ").lower() == 'yes':
    computer_hand = []
    user_hand = []
    for _ in range(2):
        computer_hand.append(drawn_card())
        user_hand.append(drawn_card())

    computer_score = 0
    user_score = 0

    c_score(computer_hand)
    print(f"Computer's first card: {computer_hand[0]}")
    u_score(user_hand)
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(f"Your final hand: {user_hand}, final score: {user_score}")
    print(compare(computer_score, user_score))
