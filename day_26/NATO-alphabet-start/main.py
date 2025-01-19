import pandas as pd

data = pd.read_csv('./NATO-alphabet-start/nato_phonetic_alphabet.csv')
words_dict = {row.letter:row.code for (index, row) in data.iterrows()}

user_word = input("Enter a word: ").upper()
user_letters = [letter for letter in user_word]

phonetic_words = [word for (letter, word) in words_dict.items() if letter in user_letters]
print(phonetic_words)