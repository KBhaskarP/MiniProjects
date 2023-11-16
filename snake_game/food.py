from turtle import Turtle
import random


class FOOD(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
        
    def refresh(self):
        X=random.randint(-280,280)
        Y=random.randint(-280,260)
        self.goto(X,Y)