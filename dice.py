from tkinter import *
import random
from tkinter import font

root = Tk()
root.title("Roll the dice")
root.geometry("500x500")

def roll_dice():
    d1 = random.choice(my_dice)
    d2 = random.choice(my_dice)

    dice_label1.config(text=d1)
    dice_label2.config(text=d2)


my_dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

my_frame = Frame(root)
my_frame.pack(pady=20)

dice_label1 = Label(my_frame, text="", font=("Helvetica", 100))
dice_label1.grid(row=0, column=0, padx=5)

dice_label2 = Label(my_frame, text="", font=("Helvetica", 100))
dice_label2.grid(row=0, column=1, padx=5)

my_button = Button(root, text="Roll Dice", command=roll_dice)
my_button.pack(padx=20)

root.mainloop()
