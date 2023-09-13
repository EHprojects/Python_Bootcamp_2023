from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# Window Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas Setup
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front)

canvas.create_text(400, 150, text="Title", fill="black", font=('Arial', 40, 'italic'))
canvas.create_text(400, 263, text="Word", fill="black", font=('Arial', 60, 'bold'))

canvas.grid(column=0, row=0, columnspan=2)

# Buttons Setup
x_img = PhotoImage(file="./images/wrong.png")
x_btn = Button(image=x_img, highlightthickness=0)
x_btn.grid(column=0, row=1)

check_img = PhotoImage(file="./images/right.png")
check_btn = Button(image=check_img, highlightthickness=0)
check_btn.grid(column=1, row=1)

window.mainloop()
