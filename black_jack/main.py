import random
import itertools

def drawn_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    deck = list(itertools.product(cards, suits))
    random.shuffle(deck)
    return random.choice(deck)[0]

def computer_score(hand):
    global c_score
    has_ace = False
    while True:
        for card in hand:
            if card == 'ace':
                has_ace = True
            elif card == 'jack' or card == 'queen' or card == 'king':
                c_score += 10
            else:
                c_score += int(card)
        
        if has_ace:
            if c_score <= 5 or 11 <= c_score <= 15:
                computer_hand.append(drawn_card())
                c_score = 0
                continue
            elif 6 <= c_score <= 10:
                c_score += 11
                break
            else:
                c_score += 1
                break
        
        if c_score <= 15:
            computer_hand.append(drawn_card())
            c_score = 0
            continue
        else:
            break

def user_score(hand):
    global u_score
    has_ace = False
    while True:
        for card in hand:
            if card == 'ace':
                has_ace = True
            elif card == 'jack' or card == 'queen' or card == 'king':
                u_score += 10
            else:
                u_score += int(card)
        print(f"Your cards: {hand}, current score: {u_score}")

        if has_ace:
            want_card = input("Do you want another card? type (y/n) ").lower()
            if want_card != 'n':
                user_hand.append(drawn_card())
                u_score = 0
                continue
            else:
                ace = 0
                for card in hand:
                    if card == 'ace':
                        ace += 1
                if ace == 1:
                    ace_point = int(input("What point do you want for ace? "))
                    if ace_point == 1:
                        u_score += 1
                        break
                    else:
                        u_score += 11
                        break
                else:
                    while True:
                        ace_point = int(input("What point do you want for ace?: "))
                        if ace_point == 11:
                            u_score += 11
                            break
                        else:
                            u_score += 1
                        ace -= 1
                        if ace == 0:
                            break
                break
        else:
            want_card = input("Do you want another card? type (y/n) ").lower()
            if want_card != 'n':
                user_hand.append(drawn_card())
                u_score = 0
                continue
            else:
                break

def compare(computer, user):
    if user == computer:
        return "Draw 🙃"
    elif user == computer and user > 21:
        return "You went over. You lose 😭"
    elif user > 21:
        return "You went over. You lose 😭"
    elif computer > 21:
        return "Opponent went over. You win 😁"
    elif user > computer:
        return "You win 😃"
    else:
        return "You lose 😤"
    

while True:
    computer_hand = []
    user_hand = []
    c_score = 0
    u_score = 0
    for _ in range(2):
        computer_hand.append(drawn_card())
        user_hand.append(drawn_card())

    computer_score(computer_hand)
    print(f"Computer's first card: {computer_hand[0]}")
    user_score(user_hand)

    print(f"Computer's final hand: {computer_hand}, final score: {c_score}")
    print(f"Your final hand: {user_hand}, final score: {u_score}")
    print(compare(c_score, u_score))

    if input("Play again? type (y/n) ").lower() != 'y':
        break
    else:
        computer_hand.clear()
        user_hand.clear()