#asking the question
#checking if the answer is correct
#checking if we are at the end of the quiz
class Quiz_Brain:
    def __init__(self,q_list):
        self.ques_number=0
        self.list=q_list
        self.score=0
    
    def still_has_question(self):
        if self.ques_number<len(self.list):
            return True
        else:
            return False
    
    def next_ques(self):
        current_ques=self.list[self.ques_number]
        self.ques_number+=1
        user_ans=input(f"Q{self.ques_number}: {current_ques.text} (True/False)?: ")
        self.check_answer(user_ans,current_ques.ans)
        
    def check_answer(self,user_ans,correct_answer):
        if user_ans.lower()==correct_answer.lower():
            print("You got it right")
            self.score+=1
        else:
            print("The answer was wrong")
        print(f"The Correct answer was {correct_answer}")   
        print(f"Your current score is {self.score}/{self.ques_number}")    
        
    
        