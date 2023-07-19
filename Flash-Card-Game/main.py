from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
item = {}
new_dic = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    old_data = pandas.read_csv("data/french_words.csv")
    new_dic = old_data.to_dict(orient="records")
else:
    new_dic = data.to_dict(orient="records")


def next_card():
    global item, flip_timer
    window.after_cancel(flip_timer)
    item = random.choice(new_dic)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=item["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=item["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_img)


def is_known():
    new_dic.remove(item)
    data = pandas.DataFrame(new_dic)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


cross_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
wrong_button = Button(image=right_img, highlightthickness=0, command=is_known)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()
