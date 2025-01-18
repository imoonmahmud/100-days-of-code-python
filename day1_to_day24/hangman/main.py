import random 
from hangman_words import word_list
from hangman_art import logo
print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ''
for _ in range(len(chosen_word)):
    placeholder += '_'
print(f"Word to guess: {placeholder}")

correct_letters = []
live = 6
while True:
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You already guessed {guess}")
        continue

    display = ''
    for letter in chosen_word:
        if letter == guess:
            correct_letters.append(letter)
            display += letter
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'

    print(display)

    if guess not in chosen_word:
        live -= 1
        print(f"'{guess}' is not in the word, you lost 1 life.")
        if live == 0:
            print("Game Over!")
            print(f"\nThe word was '{chosen_word}'")
            break

    if '_' not in display:
        print("\nGenius! You won!")
        break
