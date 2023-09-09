from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=200, height=150)
window.config(padx=50, pady=50)

FONT = ("Arial", 12, "normal")


def mi_to_km():
    miles_val = float(miles_entry.get())
    new_val = miles_val * 1.609
    new_val = round(new_val, ndigits=1)
    conv_val.config(text=f"{new_val}")


# Miles Entry Box
miles_entry = Entry(width=10, font=FONT, justify="center")
miles_entry.insert(END, string="0")
miles_entry.grid(row=0, column=1)

# Miles Label
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)

# Equals Label
equals_label = Label(text="is equal to", font=FONT)
equals_label.grid(row=1, column=0)

# Converted Value Label
conv_val = Label(text="0", font=FONT)
conv_val.grid(row=1, column=1)

# Km Label
km_label = Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)

# Calc Button
calc_btn = Button(text="Calculate", command=mi_to_km, font=FONT)
calc_btn.grid(row=2, column=1)

window.mainloop()
