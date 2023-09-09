# import tkinter
from tkinter import *

# window = tkinter.Tk()
window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
# my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    # print("I got clicked!")
    # my_label.config(text="Button got clicked!")
    my_label.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()

window.mainloop()
