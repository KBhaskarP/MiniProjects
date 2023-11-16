from turtle import Turtle

class SCORE(Turtle):
    def __init__(self):
        super().__init__()
        self.points=0
        with open("snake_game\hscore.txt") as data:
            contents=data.read()
            self.high_score=int(contents)
        self.color("white")
        self.up()
        self.hideturtle()#this hides the turtle
        self.goto(0,260)
        self.update()
        
    def update(self):
        self.clear()#This clears the writting 
        self.write(f"Score: {self.points}  High Score: {self.high_score}",align="center",font=('Arial', 16, 'normal'))#with this we can write o the 
        
    
    def points_increase(self):
        self.points += 1
        self.update()
        
        
    def hs(self):
        if self.points>self.high_score:
            self.high_score = self.points
            with open("snake_game\hscore.txt",mode="w") as data:
                data.write(f"{self.points}")     
        self.points=0   
        self.update()
        