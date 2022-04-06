with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

for name in names_list:
    name_to_str = str(name)
    edited_name = name_to_str.strip()
    with open("Input/Letters/starting_letter.txt") as example:
        example_letter = example.read()
        new_letter = example_letter.replace(f"[name]", edited_name)
        with open(f"Output/ReadyToSend/letter_for_{edited_name}.txt", mode='w') as letter_for:
            letter_for.write(new_letter)
