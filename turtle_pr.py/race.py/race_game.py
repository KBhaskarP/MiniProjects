from turtle import Turtle,Screen
from random import randint

game=False
x_cor=-230
y_cor=-120
color=["red","yellow","blue","green","black","orange"]
screen=Screen()

screen.setup(width=500,height=400) #setup() is used to create a screen with specified width and height
user_bet=screen.textinput("Make the choice","Who will win the Race?")#This will create a dialog box to pop up which will ask for an input
if user_bet:
    game = True
    
print(f"You choose : {user_bet.upper()}")
turtle_list=[]
for items in range(0,len(color)):
    new_turtle=Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color[items])
    new_turtle.up()
    new_turtle.goto(x_cor,y_cor)
    y_cor+=50
    turtle_list.append(new_turtle)
    
while game is True:
    for items in turtle_list:
        if items.xcor()>230:
            winner=items.pencolor()#color() gives both (pencolor,fillcolor) while .pencolor() gives only pencolor
            game=False
            if user_bet==winner.upper():
                print(f"You guessed it right {user_bet} turtle is the winner")
            else:
                print(f"You lost! {winner} turtle is the winner not {user_bet}")
        dist=randint(0,10)
        items.forward(dist)

    

screen.exitonclick()