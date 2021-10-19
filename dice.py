from tkinter import *
import random
from tkinter import font

root = Tk()
root.title("Roll the dice")
root.geometry("500x500")

def get_number(x):
    if x == "\u2680":
        return(1)
    elif x == "\u2681":
        return(2)
    elif x == "\u2682":
        return(3)
    elif x == "\u2683":
        return(4)
    elif x == "\u2684":
        return(5)
    elif x == "\u2685":
        return(6)


def roll_dice():
    d1 = random.choice(my_dice)
    d2 = random.choice(my_dice)

    sd1 = get_number(d1)
    sd2 = get_number(d2)

    dice_label1.config(text=d1)
    dice_label2.config(text=d2)

    sub_dice_label1.config(text=sd1)
    sub_dice_label2.config(text=sd2)

    sum = sd1 + sd2
    sum_label.config(text=f"You rolled: {sum}")


my_dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

my_frame = Frame(root)
my_frame.pack(pady=20)

dice_label1 = Label(my_frame, text="", font=("Helvetica", 100), fg="dark green")
dice_label1.grid(row=0, column=0, padx=5)
sub_dice_label1 = Label(my_frame, text="")
sub_dice_label1.grid(row=1, column=0)


dice_label2 = Label(my_frame, text="", font=("Helvetica", 100), fg="dark green")
dice_label2.grid(row=0, column=1, padx=5)
sub_dice_label2 = Label(my_frame, text="")
sub_dice_label2.grid(row=1, column=1)

my_button = Button(root, text="Roll Dice", command=roll_dice, font=("Helvetica", 24))
my_button.pack(padx=20)

sum_label = Label(root, text="", font=("Helventica", 24), fg='gray')
sum_label.pack(pady=40)

roll_dice()
root.mainloop()
