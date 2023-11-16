from turtle import Turtle
LEVEL_POSITION= (-240,270)

class LEVEL(Turtle):
    def __init__(self):
        super().__init__()
        self.floor=1
        self.color("black")
        self.up()
        self.hideturtle()
        self.update()
        
        
    def update(self):
        self.clear()
        self.goto(LEVEL_POSITION)
        self.write(f"Level:{self.floor}",align="center" ,font=("Courier", 18, "normal"))
        
        
    def level_increase(self):
        self.floor+=1
        # print(self.floor)
        self.update()
        