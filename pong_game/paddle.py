from turtle import Turtle

class PADDLE(Turtle):
    
    def __init__(self,x_positions,y_positions):
        super().__init__()
        self.x_positions = x_positions
        self.y_positions = y_positions
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.up()
        self.goto(self.x_positions,self.y_positions)
    
    def move_up(self):
        new_y=self.ycor()+20
        self.goto(x=self.xcor(),y=new_y)

    def move_down(self):
        new_y=self.ycor()-20
        self.goto(x=self.xcor(),y=new_y)
        