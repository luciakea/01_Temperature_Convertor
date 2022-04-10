from tkinter import *
import random


class Converter:
    def __init__(self, parent):

        # GUI Setup
        self.converter_frame = Frame(padx=10, pady=10)
        self.converter_frame.grid()

        # Heading (row 1)
        self_heading_label = Label(self.converter_frame, text="Temperature Converter",
                                   font=("Arial", "16", "bold"))
        self_heading_label.grid(row=0)

        # Buttons
        self_help_button = Button(self.converter_frame, text="Help",
                                  font=("Arial", "14"), command=self.help)
        self_help_button.grid(row=1)

    def help(self):
        get_help = Help()
        get_help.help_text.configure(text="Help goes here")

class Help:
    def __init__(self):

        self.help_box = Toplevel()

        self.help_frame = Frame(self.help_box)
        self.help_frame.grid()

        # Help Heading....
        self.help_heading_label = Label(self.help_frame, text="Help",
                                        font=("Arial", "16", "bold"))
        self.help_heading_label.grid(row=0)

        # Help Text
        self.help_text = Label(self.help_frame, text="")
        self.help_text.grid(row=1)

        # Dismiss Button
        self.dismiss_button = Button(self.help_frame, text="Dismiss",
                                     font=("Arial", "14"), command=self.close_help)
        self.dismiss_button.grid(row=2, padx=10)

    def close_help(self):
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Converter(root)
    root.mainloop()