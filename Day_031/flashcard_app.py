from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")


current_card = {}


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    fr_word = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=fr_word, fill="black")
    canvas.itemconfig(canvas_img, image=card_front)
    timer = window.after(3000, flip_card)


def flip_card():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(canvas_img, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def known():
    to_learn.remove(current_card)
    words_to_learn = pandas.DataFrame(to_learn)
    words_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# Window Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, flip_card)

# Canvas Setup
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front)

card_title = canvas.create_text(400, 150, text="Title", fill="black", font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, text="Word", fill="black", font=('Arial', 60, 'bold'))

canvas.grid(column=0, row=0, columnspan=2)

# Buttons Setup
x_img = PhotoImage(file="./images/wrong.png")
unknown_btn = Button(image=x_img, highlightthickness=0, command=next_card)
unknown_btn.grid(column=0, row=1)

check_img = PhotoImage(file="./images/right.png")
known_btn = Button(image=check_img, highlightthickness=0, command=known)
known_btn.grid(column=1, row=1)

next_card()

window.mainloop()
