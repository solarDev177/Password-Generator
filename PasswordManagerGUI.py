# 12/8/2023
# Final Project

from tkinter import *
from tkinter import messagebox
import random
import string
from SmileyFunctions import SmileyFunctions


class PasswordGeneratorGUI:

    # Initialize the GUI:

    def __init__(self, master):
        self.master = master
        master.title("Password Generator")
        master.geometry("300x450")

        self.lights_lbl1 = Label(master, text="*************************", pady=10, padx=10)
        self.lights_lbl1.pack()

        self.label_length = Label(master, text="Enter Minimum Length:")
        self.label_length.pack()

        self.min_length_entry = Entry(master)
        self.min_length_entry.pack()

        self.label_site = Label(master, text="Site/Account:")
        self.label_site.pack()

        self.site_entry = Entry(master)
        self.site_entry.pack()

        self.label_password = Label(master, text="Password:")
        self.label_password.pack()

        self.password_entry = Entry(master)
        self.password_entry.pack()

        self.label_filename = Label(master, text="Enter Filename:")
        self.label_filename.pack()

        self.filename_entry = Entry(master)
        self.filename_entry.pack()

        self.generate_button = Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.save_button = Button(master, text="Save to File", command=self.save_to_file)
        self.save_button.pack()

        self.label_encrypted_password = Label(master, text="Encrypted Password:")
        self.label_encrypted_password.pack()

        self.encrypted_password_entry = Entry(master)
        self.encrypted_password_entry.pack()

        self.retrieve_button = Button(master, text="Retrieve Password", command=self.retrieve_password)
        self.retrieve_button.pack()

        self.label_retrieved_password = Label(master, text="Retrieved Password:")
        self.label_retrieved_password.pack()

        self.retrieved_password_entry = Entry(master)
        self.retrieved_password_entry.pack()

        self.smiley_functions = SmileyFunctions(master)
        self.smiley_label = Label(master, text="😊", font=("Arial", 20))  # Smiling emoticon label
        self.smiley_label.pack()

        # Pass the smiley_label reference to the SmileyFunctions instance
        self.smiley_functions.set_smiley_label(self.smiley_label)

        self.smiley_label.bind("<Button-1>", self.smiley_functions.toggle_smile)  # Binding smile event
        self.save_button.bind("<Button-1>", self.smiley_functions.smile_on_save)  # Binding smile on save button

        self.lights_lbl2 = Label(master, text="*************************", pady=10, padx=10)
        self.lights_lbl2.pack()

        self.label_colors = [self.label_length, self.label_site, self.label_password, self.label_filename,
                             self.lights_lbl1, self.lights_lbl2, self.label_retrieved_password,
                             self.label_encrypted_password]

        self.current_color_index = 0
        self.cycle_label_colors()

    # GUI Helper functions

    def generate_password(self):

        min_length = int(self.min_length_entry.get())  # Get the user input for minimum length

        # Algorithm for generation:

        # ------------------------------------------------------------------
        has_number = True  # Default settings
        has_special = True  # Default settings

        letters = string.ascii_letters
        digits = string.digits
        special = string.punctuation

        characters = letters
        if has_number:
            characters += digits
        if has_special:
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

            if has_number:
                meets_criteria = has_number
            if has_special:
                meets_criteria = meets_criteria and has_special
    # ------------------------------------------------------------------

        self.password_entry.delete(0, END)  # <<<---Clear previous entry
        self.password_entry.insert(0, pwd)

    # Simple Caesar Cipher:

    def caesar_cipher(self, text, shift):
        # Caesar cipher implementation:
        # ---------------------------------------------
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shifted = ord(char) + shift
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    elif shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    elif shifted < ord('A'):
                        shifted += 26
                encrypted_text += chr(shifted)
            else:
                encrypted_text += char
        return encrypted_text
        # ---------------------------------------------

        # Save:

    def save_to_file(self):
        site = self.site_entry.get()
        password = self.password_entry.get()
        filename = self.filename_entry.get()

        if site and password and filename:
            shift = 3  # <<<---Shift value for Caesar cipher, you can adjust this

            # Encrypt the password using Caesar cipher
            encrypted_password = self.caesar_cipher(password, shift)

            with open(filename, "a") as file:
                file.write(f"Site/Account: {site}\t Encrypted Password: {encrypted_password} \n")

            self.site_entry.delete(0, END)
            self.password_entry.delete(0, END)
            self.encrypted_password_entry.delete(0, END)  # <<<---Clear previous encrypted password
            self.encrypted_password_entry.insert(0, encrypted_password)  # <<<---Display encrypted password

            self.retrieve_password()  # <<<---Retrieve and display decrypted password

            self.smiley_functions.smile_on_save(None)
        else:
            messagebox.showerror("Error", "All fields including the filename are required!")

    # Retrieve:

    def retrieve_password(self):
        encrypted_password = self.encrypted_password_entry.get()
        shift = 3  # Shift value for Caesar cipher, same as encryption.

        # Decrypt the password using Caesar cipher (reverse shift):
        decrypted_password = self.caesar_cipher(encrypted_password, -shift)

        # Display the decrypted password in the entry:
        self.retrieved_password_entry.delete(0, END)
        self.retrieved_password_entry.insert(0, decrypted_password)

    # Decor/Label coloring:

    def cycle_label_colors(self):
        self.change_label_color()
        self.master.after(3000, self.cycle_label_colors)

    def change_label_color(self):
        colors = ["red", "green", "blue"]
        self.current_color_index = (self.current_color_index + 1) % len(colors)
        color = colors[self.current_color_index]
        for label in self.label_colors:
            label.config(fg=color)
