from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1  # 25
SHORT_BREAK_MIN = 0.15  # 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_lbl.config(text="Timer")
    checks_lbl.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 1:
        title_lbl.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps % 2 == 0 and reps % 8 != 0:
        title_lbl.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_lbl.config(text="Break", fg=RED)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_mins = count // 60
    count_secs = count % 60
    if count_secs < 10:
        count_secs = f"0{count_secs}"
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 == 1:
            # Easy Way
            # num_marks = reps // 2
            # checks_lbl.config(text="✔" * num_marks)

            # Harder Way?
            checks_lbl.config(text=checks_lbl.cget("text") + "✔")
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_lbl = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 48, "normal"))
title_lbl.grid(column=1, row=0)

start_btn = Button(text="Start", command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(column=2, row=2)

checks_lbl = Label(fg=GREEN, bg=YELLOW)
checks_lbl.grid(column=1, row=3)

window.mainloop()
