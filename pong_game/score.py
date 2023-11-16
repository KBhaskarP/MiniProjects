from turtle import Turtle

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.a=0
        self.b=0
        self.color("white")
        self.up()
        self.hideturtle()
        self.update()
        
        
    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.a,align="center",font=('Courier', 80, 'normal'))
        self.goto(100,200)
        self.write(self.b,align="center",font=('Courier', 80, 'normal'))
     
    def a_point(self):
        self.a+=1
        self.update()
    
    def b_point(self):
        self.b+=1 
        self.update()         