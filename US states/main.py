import turtle
import pandas as pd

screen=turtle.Screen()
screen.title("US States Game")
img=r"C:\Users\HP\Desktop\AI\US states\blank_states_img.gif"
screen.bgpic(img) #This is used to basically setup the background image
# with open(r"US states\50_states.csv") as csv_file:
#     data=csv_file.read()
#     # print(data)


# print(answer_state)
df=pd.read_csv(r"US states\50_states.csv")
state_list=df.state.to_list()
guess_list=[]
while len(guess_list)<50:
    answer_state=screen.textinput(title=f"Guess {len(guess_list)}/50",prompt="What's the state name?").title()
    if answer_state=="Exit":
        missing_states=[]
        for items in state_list:
            if items not in guess_list:
                missing_states.append(items)
        miss_data=pd.DataFrame(missing_states)
        miss_data.to_csv()
        break
    if answer_state not in guess_list:
        if answer_state in state_list:
            state_data=df[df.state==answer_state]
            x_cor=state_data.x
            y_cor=state_data.y
            point=turtle.Turtle()
            point.hideturtle()
            point.up()
            point.goto(int(x_cor),int(y_cor))
            point.write(f"{answer_state}",align="center",font=("Arial",12))
            guess_list.append(answer_state)
            
    



    
    
screen.mainloop()