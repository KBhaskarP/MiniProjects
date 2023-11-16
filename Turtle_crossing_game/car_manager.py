from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars_list=[]
        self.speed=STARTING_MOVE_DISTANCE
        
    def create_car(self):
        chance=random.randint(1,6)
        if chance==1:
            new_car=Turtle()
            new_car.shape("square")
            new_car.up()
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_y=random.randint(-260,260)
            new_car.setheading(180)
            new_car.goto(300,new_y)
            self.cars_list.append(new_car)
        
    def move_car(self):
        for items in self.cars_list:
            items.forward(self.speed)
    def car_speed(self):
        self.speed+=MOVE_INCREMENT
        self.move_car()
        
        
        