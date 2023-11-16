from turtle import Turtle
starting_pos=[(0, 0),(-20, 0),(-40, 0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0
move_dist=20

class Snake: 
    
    def __init__(self):
        self.snakes=[]
        self.create_snake()
        self.head=self.snakes[0]
        
    def create_snake(self):
        for pos in range(0,len(starting_pos)):
            # self.add_snake(starting_pos[pos])
            block=Turtle()
            block.shape("square")
            block.color("red")
            block.up()
            block.goto(starting_pos[pos])
            self.snakes.append(block)
            
    def reset(self):
        for items in self.snakes:
            items.goto(1000,1000)
        self.snakes.clear()
        
            
    # def add_snake(self,position):
    #         block=Turtle()
    #         block.shape("square")
    #         block.color("white")
    #         block.up()
    #         block.goto(position)
    #         self.snakes.append(block)
    def snake_length_increase(self):
            block=Turtle()
            block.shape("square")
            block.color("white")
            block.up()
            block.goto(self.snakes[-1].position())# self.add_snake(self.snakes[-1].position())#here position() is method from turtle class
            self.snakes.append(block)
        
    
        
            
    def move_snake(self):
            for item in range(len(self.snakes)-1,0,-1):
                new_x=self.snakes[item-1].xcor()
                new_y=self.snakes[item-1].ycor()
                self.snakes[item].goto(new_x,new_y)
            self.snakes[0].forward(move_dist)
            
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        