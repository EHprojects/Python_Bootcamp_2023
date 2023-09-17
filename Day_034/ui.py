from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=50)
        self.question_txt = self.canvas.create_text(150, 125, text="This is a test.", fill=THEME_COLOR,
                                                    font=("Arial", 20, "italic"), width=280)
        self.score = 0
        self.score_lbl = Label(text=f"Score {self.score}", bg=THEME_COLOR, fg="white")
        self.score_lbl.grid(column=1, row=0)

        true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.true_answer)
        self.true_btn.grid(column=0, row=2)
        false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.false_answer)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_lbl.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_txt, text=q_text)
        else:
            self.canvas.itemconfig(self.question_txt, text="You've reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_answer(self):
        # is_right = self.quiz.check_answer("true")
        self.give_feedback(self.quiz.check_answer("true"))

    def false_answer(self):
        # is_wrong = self.quiz.check_answer("false")
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(ms=1000, func=self.get_next_question)
