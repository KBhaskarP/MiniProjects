import tkinter as tk

window=tk.Tk() #To create a window
window.minsize(width=200,height=200) # To setup the minimum size for the window



#Creating the label for the text "is equal to" and setting the position

my_label=tk.Label(text="is equal to",font=("Arial",9)) 
my_label.grid(column=0,row=1)


#Creating the input text field to take miles from the user

entry=tk.Entry()
entry.grid(column=1,row=0)

#creating the miles label

miles_label=tk.Label(text="Miles")
miles_label.grid(column=2,row=0)

#Function which is going to be called on click and creating the button for click

def calculate_miles_to_km():
    miles=int(entry.get())
    km=round(miles*1.609,2)
    distance_in_km=tk.Label(text=f"{km}")
    distance_in_km.grid(column=1,row=1)
    

calculate_button=tk.Button(text="calculate",command=calculate_miles_to_km)
calculate_button.grid(column=1,row=2)

#creating the label for km and setting its position

km_label=tk.Label(text="km")
km_label.grid(column=2,row=1)















#This is for allowing the gui to keep runnning untill instruction to finish


window.mainloop()