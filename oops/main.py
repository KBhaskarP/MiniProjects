from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain

Question_bank=[]

for items in range(0,len(question_data)):
    ques=question_data[items]["text"]
    ans=question_data[items]["answer"]
    new_question=Question(ques,ans)
    Question_bank.append(new_question)
    
quiz=Quiz_Brain(Question_bank)
while quiz.still_has_question():
    quiz.next_ques()

    
# print(Question_bank)
