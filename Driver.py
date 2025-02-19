# 12/8/2023
# Final Project

from tkinter import *
from PasswordManagerGUI import PasswordGeneratorGUI

# Algorithm for the password generation:

'''def generate_password(min_length, numbers=True, special_characters=True): 
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True

        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd'''

# Run the GUI:


def run_password_generator_gui():
    root = Tk()
    PasswordGeneratorGUI(root)
    root.mainloop()

# Run main:


def main():

    run_password_generator_gui()

    # We're done! ^o^


if __name__ == '__main__':
    main()
