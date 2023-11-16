from turtle import Turtle,Screen
from paddle import PADDLE
from ball import BALL
import time
from score import Score_board

screen=Screen()
screen.setup(width=800,height=600)
screen.title("PONG")
screen.bgcolor("black")
screen.tracer(0)#This is used to basically switch the animation off

l_pad=PADDLE(-380,20)
r_pad=PADDLE(380,2)
game_ball=BALL()
score_a=Score_board()
score_b=Score_board()
speed_num=0


screen.listen()

screen.onkeypress(key="Up",fun=r_pad.move_up)
screen.onkeypress(key="Down",fun=r_pad.move_down)

screen.onkeypress(key="w",fun=l_pad.move_up)
screen.onkeypress(key="s",fun=l_pad.move_down)






game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    game_ball.move_ball()
    
    if game_ball.ycor()>280 or game_ball.ycor()<-280:
        game_ball.bounce_back_y()
        
    if game_ball.distance(r_pad)<50 and game_ball.xcor()>340 or game_ball.distance(l_pad)<50 and game_ball.xcor()<-340:
        game_ball.bounce_back_x()
        speed_num +=1
        game_ball.speed(speed_num)
        
        
        
    if game_ball.xcor()>370:
        game_ball.home()
        game_ball.bounce_back_x()
        score_a.a_point()
        
        
    if game_ball.xcor()<-370:
        game_ball.home()
        game_ball.bounce_back_x()
        score_b.b_point()
        







screen.exitonclick()