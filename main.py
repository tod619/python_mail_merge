# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"
PLACEHOLDER_Name = "Angela"
MY_NAME = "Trevor"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        letter_with_name = new_letter.replace(PLACEHOLDER_Name, MY_NAME)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completted_letter:
            completted_letter.write(letter_with_name)
