from tkinter import *
from quiz_brain import QuizBrain
from os import path
THEME_COLOR = "#375362"

dir_path = path.dirname(__file__)


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = Label(text=f"Score: {self.quiz.score}/{self.quiz.quiz_length}", bg=THEME_COLOR, fg="#FFFFFF")
        self.score.grid(column=1, row=0, pady=20)    
        self.canvas = Canvas(height=250,width=300,bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            font=("Arial",20,"italic"))
        self.canvas.grid(column=0,row=1,columnspan=2,padx=20,pady=20)
        img_wrong = PhotoImage(file=path.join(dir_path,"images/false.png"))
        img_right = PhotoImage(file=path.join(dir_path,"images/true.png"))
        self.button_right = Button(image=img_right,
                                   bd=0, 
                                   highlightthickness=0, 
                                   activebackground=THEME_COLOR, 
                                   relief="flat", 
                                   padx=20, 
                                   pady=20,
                                   command=self.answer_true
                                   )
        self.button_right.grid(column=0, row=2, pady=20)
        self.button_wrong = Button(image=img_wrong,
                                   bd=0,
                                   highlightthickness=0,
                                   activebackground=THEME_COLOR,
                                   relief="flat",
                                   padx=20,
                                   pady=20,
                                   command=self.answer_false
                                   )
        self.button_wrong.grid(column=1, row=2, pady=20)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.button_wrong.config(state="normal")
            self.button_right.config(state="normal")
            qtext = self.quiz.next_question()
        else:
            qtext = f"You finished the quizz. Your score is {self.quiz.score} out of {self.quiz.question_number}."
        self.score.config(text=f"Score: {self.quiz.score}/{self.quiz.quiz_length}")
        self.canvas.itemconfig(self.question_text,text=qtext)
        self.canvas.config(bg="#FFFFFF")

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    
    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    
     
    def give_feedback (self, is_right):
        self.button_right.config(state="disabled")
        self.button_wrong.config(state="disabled")
        if is_right:
             self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000,self.get_next_question)
    
    
    
    
    
 