from turtle import Turtle

class BALL(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_pace=10
        self.y_pace=10
        
    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.goto(x=0,y=0)
        
    def move_ball(self):
        self.up()
        new_x=self.xcor()+self.x_pace
        new_y=self.ycor()+self.y_pace
        self.goto(new_x,new_y)
       
        
    def bounce_back_y(self):
       self.y_pace*=-1
    def bounce_back_x(self):
        self.x_pace*=-1
        
        
    