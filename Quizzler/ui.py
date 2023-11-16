from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.quiz.score=0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        
        
        
        
        self.canvas=Canvas(width=300,height=250,bg="white")
        self.question_text=self.canvas.create_text(150,125,width=280,text="Message",font=('Arial',20,'italic'))
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
        
        self.score_label=Label(text=f"Score : {self.quiz.score}",fg="white",bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)
        
        
        true_image=PhotoImage(file=r"C:\Users\HP\Desktop\AI\Quizzler\images\true.png")
        self.true_button=Button(image=true_image,borderwidth=0,highlightthickness=0,command=self.correct)
        self.true_button.grid(column=0,row=2)
        
        false_image=PhotoImage(file=r"C:\Users\HP\Desktop\AI\Quizzler\images\false.png")
        self.false_button=Button(image=false_image,borderwidth=0,highlightthickness=0,command=self.wrong)
        self.false_button.grid(column=1,row=2)
        
        self.next_ques()
        
        self.window.mainloop()
    
    def next_ques(self):
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text,text="You have reached the end of the Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")            
        
    def correct(self):
        answer="True"
        is_right=self.quiz.check_answer(answer)
        self.give_feedback(is_right)
        
        
        
    def wrong(self):
        answer="False"
        is_right=self.quiz.check_answer(answer)
        self.give_feedback(is_right)
        
        
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.quiz.score+=1
            
            # self.window.after_cancel(clock)
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000,self.reset_feedback)
    def reset_feedback(self):
        self.score_label.config(text=f"Score : {self.quiz.score}")
        self.canvas.config(bg="white")
        self.next_ques()
        
     