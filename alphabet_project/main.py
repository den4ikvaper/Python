import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}

while True:
    user_word = input("Enter a word: ").upper()
    try:
        output_list = [alphabet_dict[item] for item in user_word]
    except KeyError:
        print("Sorry, only letter in the alphabet, please!")
    else:
        print(output_list)
        break


