from game_data import data
import random

def display(account_a, account_b):
    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
    print(f"Compare B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")

score = 0
while True:
    a = random.choice(data)
    b = random.choice(data)
    higher_followers = a['follower_count'] > b['follower_count']
    if higher_followers:
        higher_followers = 'a'
    else:
        higher_followers = 'b'

    display(a, b)
    user_guess = input("Who was more followers? type (a/b) ").lower()
    if user_guess == higher_followers:
        score += 1
        print(f"You're right! Current score: {score}")
        continue
    else:
        print(f"SOrry, that's wrong. Final score: {score}")
        break
