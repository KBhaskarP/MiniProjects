from turtle import Turtle,Screen
from random import randint


tim=Turtle()
# tim.color("red") #color specifies the color of the turtle
tim.shape(name="turtle") # shape is used to choose the shape of the turtle as arrow or turtle etc

#Movement of the turtle
#we tried making a fish

# tim.forward(100)
# tim.left(120)
# tim.forward(100)
# tim.left(120)
# tim.forward(100)
# tim.right(120)   
# tim.backward(100)
# tim.left(120)
# tim.forward(100)
# tim.left(120)
# tim.forward(100)
# tim.left(120)
# tim.forward(100)
# tim.left(120)
# tim.backward(100)

#challenge 1 : DRAW A SQUARE

# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

#using for loop

# for move in range(0,4):
#     tim.forward(100)
#     tim.right(90)
    

# Challenge 2 : Draw a Dashed line

# for steps in range(12):
#     tim.forward(10)
#     tim.up() #this will keep the pen up and we can do movements
#     tim.forward(10)
#     tim.down() #this will the pen down and we can do movements and use pen
    

# Challenge 3 : Draw a triange,square,pentagon,hexagon,heptagon,octagon,
#nonagon and decagon
# sides=3
# col=["red","blue","green","yellow","black","pink","orange","violet"]
# col_index=0
# tim.width(10)
# def draw_shapes(sides):
#     angle=360/sides
#     tim.color(col[col_index])
#     for i in range(sides):
#         tim.forward(40)
#         tim.right(angle)
#         tim.forward(40)
#     for i in range(sides):
#         tim.forward(40)
#         tim.left(angle)
#         tim.forward(40)
# while sides<11:
#     draw_shapes(sides)
#     sides+=1
#     col_index+=1

# challenge 4: Draw random walk

# tim.width(15)
# steps=200
# color=["yellow", "gold", "orange", "red", 
# "maroon", "violet", "purple",
# "navy", "blue", "skyblue", "cyan", "turquoise"]

# mov_list=[0,90,180,270]


# while steps!=0:
#     for move in range(steps):
#         color_choice=randint(0,len(color)-1)
#         move_choice=randint(0,len(mov_list)-1)
        
#         path_color=color[color_choice]
#         path_dirn=mov_list[move_choice]
        
#         tim.color(f"{path_color}")
#         tim.setheading(mov_list[move_choice])
#         tim.forward(30)
#         steps-=1

#Challenge 5 : Draw a spirograph
color=["yellow", "gold", "orange", "red", 
"maroon", "violet", "purple",
"navy", "blue", "skyblue", "cyan", "turquoise"]

steps=100
tim.speed(0)#This makes the drawing faster 0 for fastest 3 for slowest
def complete_circle(size_of_gap):
    for i in range(int(360/size_of_gap)):
        color_choice=randint(0,len(color)-1)
        circle_color=color[color_choice]
        tim.color(circle_color)
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap) #tim.heading() gives the current position of the turtle we are adding size_of_gap everytime and thus for that using tim.setheading()
complete_circle(5)




    
    
    
    
    
    


#to keep the video exit on click

screen=Screen()
screen.exitonclick()

