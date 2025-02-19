# 12/8/2023
# Final Project

class SmileyFunctions:

    # Create smiley variables:

    __is_smiling = False
    __smiley_label = None

    # Init

    def __init__(self, master, smiling=False, smiley=None):
        self.master = master
        self.set_is_smiling(smiling)
        self.set_smiley_label(smiley)

    # Helpers

    def toggle_smile(self, event):
        if self.__is_smiling:
            self.__smiley_label.config(text="😊")  # Reset to normal emoticon
        else:
            self.__smiley_label.config(text="😄")  # Wider smile
            self.master.after(2000, self.reset_smile)  # After 2 seconds, reset the smile
        self.__is_smiling = not self.__is_smiling

    def smile_on_save(self, event):
        if not self.__is_smiling:
            self.toggle_smile(None)

    def reset_smile(self):
        if self.__is_smiling:
            self.__smiley_label.config(text="😊")  # Reset to normal emoticon
            self.__is_smiling = False

    # No getters needed for this one, as we won't return a string. We will use a label. :)

    # Setters

    def set_smiley_label(self, smiley):
        self.__smiley_label = smiley

    def set_is_smiling(self, smiling):
        self.__is_smiling = smiling

    # Boom, done. ^o^
