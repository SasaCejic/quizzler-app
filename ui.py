from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)
        self.score_text = Label(self.window, text= f"Score: {self.quiz.score}", font=("Arial", 16), fg="white", bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1, pady=(0, 20))
        self.canvas = Canvas(master=self.window, height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, text="Question text", font=("Arial", 20, "italic"), width=280, justify="center")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(0, 50))
        self.false_img = PhotoImage(file="images/false.png")
        self.true_img = PhotoImage(file="images/true.png")
        self.false_btn = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)
        self.true_btn = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.true_btn.grid(row=2, column=0, pady=(0, 20))
        self.false_btn.grid(row=2, column=1, pady=(0, 20))

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.false_btn.config(state="disabled")
            self.true_btn.config(state="disabled")

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right:
            self.score_text.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
            self.window.after(1000, self.next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.next_question)
