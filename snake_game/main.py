from turtle import Turtle,Screen
from snake import Snake
from food import FOOD
from score import SCORE
import time
screen=Screen()
screen.title("The Great Snake Game")#This will give the title for the screen
screen.setup(width=600,height=600)#This will create a screen of 600x600
screen.bgcolor("black")#This will make the bg of screen to be black
screen.tracer(0)

score_board=SCORE()
snake=Snake()
food=FOOD()

screen.listen() # This is to allow our screen to start listening the keys
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

    
game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food)<15: #snake.head=snakes[0] snake is the object we created while snakes is the list of objects
        # print("chop chop")
        food.refresh()
        snake.snake_length_increase()
        score_board.points_increase()
        
        
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 : 
        over=Turtle()
        over.hideturtle()
        over.color("white")
        over.write("GAME OVER",align="center",font=('Arial', 16, 'normal'))
        score_board.hs()
        game_on=False
    for items in snake.snakes:
        if items==snake.head:#This is because we just want to not bite the body other than head
            pass
        elif snake.head.distance(items)<10:
            over=Turtle()
            over.hideturtle()
            over.color("white")
            over.write("GAME OVER",align="center",font=('Arial', 16, 'normal'))
            score_board.hs()
            game_on=False
            
    
        
screen.exitonclick()