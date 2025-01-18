from alphabet import lower_alphabet, upper_alphabet

def caesar(char, key, encode_or_decode):
    output_text = ''
    if encode_or_decode == 'decode':
        key *= -1

    for letter in char:
        if letter.isalpha():
            if letter.islower():
                key_position = lower_alphabet.index(letter) + key
                key_position %= len(lower_alphabet)
                output_text += lower_alphabet[key_position]
            else:
                key_position = upper_alphabet.index(letter) + key
                key_position %= len(upper_alphabet)
                output_text += upper_alphabet[key_position]
        else:
            output_text += letter

    print(f"{encode_or_decode.title()}: {output_text}")

while True:
    direction = input("Encode or Decode : ").lower()
    if direction not in ['encode', 'decode']:
        print("Type Carefully!")
        continue
    text = input("text: ")
    shift = int(input("key: "))

    caesar(text, shift, direction)
    try_again = input("Want to go again? Type (yes/no) ")
    if try_again != 'yes':
        break