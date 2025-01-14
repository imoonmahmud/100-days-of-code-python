names = []
with open('./Input/Names/invited_names.txt', 'r') as name_file:
    for name in name_file.readlines():
        names.append(name.replace('\n', ''))

for name in names:
        with open(f'./Output/letter_for_{name.lower()}.txt', 'w') as write_letter:
            with open('./Input/Letters/starting_letter.txt', 'r') as read_letter:
                letter_contents = read_letter.read()
                write_letter.write(letter_contents.replace('[name]', name))
                