from turtle import Turtle,Screen

pointer=Turtle()
screen=Screen()

def forward():
    pointer.forward(10)
def backward():
    pointer.backward(10)
def left():
    pointer.left(45)
def right():
    pointer.right(45)
def clear():
    pointer.clear()
    pointer.up()
    pointer.home()
    pointer.down()
 
screen.listen()   
screen.onkeypress(key="Right",fun=right)
screen.onkeypress(key="Left",fun=left)
screen.onkeypress(key="Up",fun=forward)
screen.onkeypress(key="Down",fun=backward)
screen.onkey(key="c",fun=clear)

#we can use onkey or onkeypress both in this case 
#in onkey we have to keep on pressing for func to trigger
#in onkeypress we have to keep the key pressesd for triggering the func continiously
#clear() is used to clear the screen

screen.exitonclick()