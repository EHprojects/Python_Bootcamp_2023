# import tkinter
from tkinter import *

# window = tkinter.Tk()
window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_clicked():
    # print("I got clicked!")
    # my_label.config(text="Button got clicked!")
    my_label.config(text=input.get())


# Label
# my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.pack(side="left")
# my_label.place(x=100, y=200)
my_label.config(padx=50, pady=50)
my_label.grid(column=0, row=0)


# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button_02 = Button(text="New Button")
button_02.grid(column=2, row=0)

# Entry
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)

window.mainloop()
