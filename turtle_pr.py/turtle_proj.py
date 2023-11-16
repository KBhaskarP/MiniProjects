# from turtle import Turtle,Screen
# timmy=Turtle()
# print(timmy)
# timmy.shape("turtle") 
# timmy.color("green")
# timmy.forward(100)
# timmy.left(100)
# timmy.forward(100)

# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable
table=prettytable.PrettyTable()
# print(table)
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Types",["Electric","Water","Fire"])
table.align="l"  #allignment l for left c for center r for right
print(table)

