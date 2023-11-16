import tkinter


window=tkinter.Tk() #This is just like turtle.Screen()

window.title("GUI test 1") #This is used to add title just like screen.title()

window.minsize(width=200,height=300) #This is used to create a window of min specified size just screen.setup(width,height)

my_label=tkinter.Label(text="label",font=("Arial",24,"bold ")) #This is used to create a component which is to be displayed inside the gui

# my_label.pack(side="top") #This is used to basically make the label show in center automatically
#in label we have side="center" by default this is used to position our label in left right bottom sides

my_label.grid(column=0,row=0)



def button_pressed():
    # my_label.config(text="The Button got pressed") #The config method is used to update the label or component
    
    # my_label["text"]="The Button got pressed" #This is also a method to update the label, by usig the fact that it is of a dictionary type
    new_input=entry.get()
    my_label.config(text=new_input) #With this the input we got is shown as the text of the label
    print(entry.get())#when ever the nuuton is pressed the input get printed
    # print("The Button got pressed") #This will be printed in the output console
    
    # print(big_box.get("1.0",tkinter.END)) #Get's current value in textbox at line 1, character 0 till the END


def submit_it():
    print(submit.get())

submit=tkinter.Button(text="Submit",command=submit_it)
submit.grid(column=2,row=0)





button=tkinter.Button(text="Click me",command=button_pressed) #The Button class is used to create a button component on the screen with text "manual"
#just like the event listeners in turtle like onkey or onkeypress(key, fun) here this is inside the Button class using the parameter "command=fun"

# button.pack() #This is used to show the components on the screen
button.grid(column=1,row=5)

entry=tkinter.Entry(width=20) #Entry is used to create a input box and here we have specified the width so as to increase the box size
entry.insert(tkinter.END,"Start here") #This is used to enter some text to begin with at position 0
# entry.pack() #This is used to show the component on the screen

# entry.focus() #This is used to basically set the cursor in the input box

entry.grid(column=3,row=8)




# big_box=tkinter.Text(width=20,height=8) #This is used to create a textbox
# big_box.insert(tkinter.END,"Paragraph here") #here the tkinter.END to access the value at 0
# big_box.pack()
# big_box.focus()



# print(entry.get())#This method is used to get the input from the Entry method in  form of string
#This will print nothing because it does not have a source to perform the action thus I am writting this inside the button_pressed function 
#So that when ever the nuuton is pressed the input get printed



#Layout Managers

#just like pack() there are other layout managers like place(x,y) and grid().

#pack()

#It basically shows all the component next to each other which means no styling at all the sides are top.bottom left and right

#place(x,y)

#This allows us to move the layout to our desired position but we have to prvide the x and y position


#grid(column,row)

#this considers the whole gui as a grid and we can place the layouts by specifying the column and row.
#But it needs to go sequentially like when col 1 is filled only then col 2 will be filled we can not go directly to col 2 when col1 is empty.









window.mainloop() #This is just like screen.exitonclick() but here we are using the window.mainloop
    
def add(a=5,b=4):
    return a+b

add()