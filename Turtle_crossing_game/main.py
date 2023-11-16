import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from level_manager import LEVEL



screen = Screen()
screen.title("The Turtle Cross")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

level=LEVEL()
player=Player()
points=Scoreboard()
car=CarManager()

screen.onkeypress(key="Up",fun=player.move)



game_is_on = True
while game_is_on:
    
    time.sleep(0.1)
    screen.update()
    
    car.create_car()
    car.move_car()
    
    for el in car.cars_list:
        if player.distance(el)<20:
            points.game_over()
            game_is_on=False
    
    if player.line_cross() :
        player.turtle_reset()
        level.level_increase()
        points.score_increase()
        car.car_speed()
    
screen.exitonclick()