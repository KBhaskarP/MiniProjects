import tkinter as tk

#Window Creation and features
window=tk.Tk() #window create


window.title("GUI Window") #Giving the window a title
window.minsize(width=500, height=500) #Specify the size of the window
window.config(padx=50,pady=50)


#Label

my_label=tk.Label(text="My exaple Label",font=("Arial",18,"bold")) #Added text on the window
#my_label.pack() #Which part of screen text should be displayed default is top but now we will be using grid layout

my_label.grid(column=0,row=0)
my_label.config(text="level 1")



#Entry

input=tk.Entry() #Creates an entry field
# input.pack() #displays the netry field on the screen but we will be using grid layout
input.grid(column=4,row=4)
input.get() #return whatever is in the entry field as string

#Button


def btn_clk(): #Fn is created so as to trigger event
    print("Button clicked")
    my_label.config(text=input.get())
    

    
button=tk.Button(text="press",command=btn_clk) #Added button to the window which when clicked triggers btn_clk fn
#button.pack() #Used to display the button on the window default is top but we will be using grid layout
button.grid(column=1,row=2)

new_button=tk.Button(text="New_button")
new_button.grid(column=2,row=1)


window.mainloop() #window keep runin


# def add(*args):
#     sum=0
#     for item in args:
#         sum+=item
#     return sum

# print(add(1,2,3,4,5,6,7,8,9,10,11,12))