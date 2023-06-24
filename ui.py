from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title('Quizler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.lbl_score = Label(text=f'Score: {self.quiz.score}', bg=THEME_COLOR, fg='white')
        self.lbl_score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=250,
                                                     text='test text',
                                                     font=('Arial', 20, 'italic'),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        img_true = PhotoImage(file='images/true.png')
        self.btn_true = Button(image=img_true, highlightthickness=0, command=self.guess_true)
        self.btn_true.grid(row=2, column=0)

        img_false = PhotoImage(file='images/false.png')
        self.btn_false = Button(image=img_false, highlightthickness=0, command=self.guess_false)
        self.btn_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
            self.lbl_score.config(text=f'score: {self.quiz.score}')
        else:
            self.canvas.itemconfig(self.question_text, text='you have reached the end of questions')
            self.btn_true.config(state='disabled')
            self.btn_false.config(state='disabled')

    def guess_true(self):
        print('user guessed true')

        is_correct = self.quiz.check_answer('true')
        self.give_feedback(is_correct)

    def guess_false(self):
        print('user guessed false')

        is_correct = self.quiz.check_answer('false')
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)
