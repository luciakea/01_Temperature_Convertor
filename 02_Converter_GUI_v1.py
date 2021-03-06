from tkinter import *
from functools import partial  # to prevent unwanted windows


class Converter:
    def __init__(self):
        # Formatting Variables
        background_colour = "light blue"

        self.all_calculations = []

        # Converter Frame
        self.converter_frame = Frame(width=600, height=600, bg=background_colour, pady=10)
        self.converter_frame.grid()

        # Temperature Converter Heading (row 0)
        self.temp_heading_label = Label(self.converter_frame, text="Temperature Convertor",
                                        font="Arial 16 bold",
                                        bg=background_colour,
                                        padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # User Instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame, text="Type in the amount to be "
                                                                        "converted and then push "
                                                                        "one of the buttons below...",
                                             font="Arial 10 italic", justify=LEFT, bg=background_colour, padx=10,
                                             pady=10)
        self.temp_instructions_label.grid(row=1)
        # Temperature Entry Box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # Conversion Buttons Frame (row 3)
        self.conversion_buttons_frame = Frame(self.converter_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font="Arial 10 bold",
                                  bg="khaki1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg="Orchid1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        # Answer Label (row 4)
        self.converted_label = Label(self.converter_frame, font="Arial 14 bold",
                                     fg="purple", bg=background_colour,
                                     pady=10, text="")
        self.converted_label.grid(row=4)

        # History / Help Button Frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                       text="Calculation History", width=15)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5, command=self.help)
        self.help_button.grid(row=0, column=1)

    def help(self):
        Help(self)
        # get_help.help_text.configure(text ="Help text goes here")

    def temp_convert(self, low):
        print(low)

        error = "#ffafaf"  # Pale pink background for when entry box has errors

        # Retrieve amount entered into Entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # Check amount is a valid number

            # convert from C to F
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9 / 5) + 32
                to_convert = self.round_item(to_convert)
                fahrenheit = self.round_item(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)

            # check and convert to centigrade
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5 / 9
                to_convert = self.round_item(to_convert)
                celsius = self.round_item(celsius)
                answer = "{} degrees F is {} degrees C".format(to_convert, celsius)

            else:
                # input is invalid (too cold)!!
                answer = "Too cold!"
                has_errors = "yes"

            # Display answer
            print(answer)
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

            # Add Answer to list for History
            if answer != "too cold":
                self.all_calculations.append(answer)
                print(self.all_calculations)

        except ValueError:
            self.converted_label.configure(text="Enter a number!!", fg="red")
            self.to_convert_entry.configure(bg=error)

    @staticmethod
    def round_item(to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded


class Help:
    def __init__(self, partner):
        background = "Orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # set up child window (ie: help box)
        self.help_box = Toplevel()

        # if cross at top right of help box is pressed, close help box and enable help button in convertor GUI
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # set up GUI frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        # set up 'help' heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background)
        self.help_text.grid(column=0, row=1)

        # Dismiss button (row2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="orange", font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
