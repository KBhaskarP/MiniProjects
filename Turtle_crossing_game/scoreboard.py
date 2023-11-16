from turtle import Turtle
FONT = ("Courier", 18, "normal")
over_font=("Courier", 24, "normal")
score_position=(225,270)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.hideturtle()
        self.color("black")
        self.up()
        self.update()
        
    def update(self):
        self.clear()
        self.goto(score_position)
        self.write(f"Score: {self.score}",align="center",font=FONT)
        
    def score_increase(self):
        self.score+=5
        self.update()
        
    def game_over(self):
        self.color("black")
        self.hideturtle
        self.goto(0,0)
        self.write("Game Over",align="center",font=over_font)
        
