# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as names:
    invited_names = names.readlines()

for i in range(len(invited_names) - 1):
    invited_names[i] = invited_names[i].strip()

# with open("./Input/Letters/starting_letter.txt") as letter:
#     starting_letter = letter.readlines()
#
# for name in invited_names:
#     output = starting_letter.copy()
#     output[0] = output[0].replace("[name]", name)
#     with open(f"./Output/ReadyToSend/{name}_letter.txt", "w") as file:
#         file.writelines(output)

with open("./Input/Letters/starting_letter.txt") as letter:
    starting_letter = letter.read()
    for name in invited_names:
        new_letter = starting_letter.replace("[name]", name)
        with open(f"./Output/ReadyToSend/{name}_letter.txt", "w") as file:
            file.write(new_letter)
