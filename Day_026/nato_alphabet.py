import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_alpha = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# nato_alpha_dict = {}
#
# for (index, row) in nato_alpha.iterrows():
#     # print(row.letter)
#     # print(row.code)
#     nato_alpha_dict[row.letter] = row.code


nato_alpha_dict = {row.letter: row.code for (index, row) in nato_alpha.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.

word_input = input("Enter a word: ")

# output = []
#
# for char in word_input:
#     output.append(nato_alpha_dict[char.upper()])

output = [nato_alpha_dict[char.upper()] for char in word_input]

print(output)
