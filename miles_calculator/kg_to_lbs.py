from tkinter import *

window=Tk()
window.title("Kg to LBS ")
window.minsize(width=400,height=250)
window.config(bg="#FFCC70")


kg_label=Label(text="Kg",font=("Times New Roman",18))
kg_label.grid(column=0,row=0)

kg_entry=Entry()
kg_entry.grid(column=3,row=0)

lbs_label=Label(text="lbs",font=("Times New Roman",18))
lbs_label.grid(column=0,row=2)

lbs_answer=Label(text="0",font=("Times New Roman",18))
lbs_answer.grid(column=3,row=2)

def convert():
    kg=float(kg_entry.get())
    lbs=kg*2.2
    return lbs_answer.config(text=round(lbs,2))
    
    
button=Button(text="Convert",command=convert)
button.grid(column=2,row=1)












window.mainloop()