from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)
        self.score_text = Label(self.window, text= "Score: 0", font=("Arial", 16), fg="white", bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1, pady=(0, 20))
        self.canvas = Canvas(master=self.window, height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125, text="Here goes the looong question text. Yes, right here.", font=("Arial", 20, "italic"), width=280, justify="center")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(0, 50))
        self.false_img = PhotoImage(file="images/false.png")
        self.true_img = PhotoImage(file="images/true.png")
        self.false_btn = Button(image=self.false_img, highlightthickness=0, command=self.next_question())
        self.true_btn = Button(image=self.true_img, highlightthickness=0, command=self.next_question())
        self.true_btn.grid(row=2, column=0, pady=(0, 20))
        self.false_btn.grid(row=2, column=1, pady=(0, 20))

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)