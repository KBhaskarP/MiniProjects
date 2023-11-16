from tkinter import *
from tkinter import messagebox
import pandas as pd
import random



BACKGROUND_COLOR = "#B1DDC6"
dict_word={}
#--------------------------------------Reading Data From Csv----------------------
df=pd.read_csv(r"C:\Users\HP\Desktop\AI\Flash Card\data\french_words.csv")
dict=df.to_dict(orient="records")

#-------------------------------------Generating Random words----------------------
def random_french_words():
    global dict_word,timer
    window.after_cancel(timer)
    dict_word=random.choice(dict) #This will return the dictionary
    canvas.itemconfig(french_word,text=dict_word["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    canvas.itemconfig(front_title,text="French",fill="black")  
    timer=window.after(3000,flip)
    
    
    
#--------------------------------------Flipping-----------------------------------
def flip():
    canvas.itemconfig(card_background,image=card_back_image)
    canvas.itemconfig(front_title,text="English",fill="white")
    canvas.itemconfig(french_word,text=dict_word["English"],fill="white")
    
#--------------------------------------UI Interface-- ------------------------------
window=Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

timer=window.after(3000,flip)



canvas=Canvas(width=800,height=526)

card_front_img=PhotoImage(file="images/card_front.png")
card_back_image=PhotoImage(file="images/card_back.png")

card_background=canvas.create_image(400,263,image=card_front_img)

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

front_title=canvas.create_text(400,150,text="French",font=("Arial",40,'italic'))
french_word=canvas.create_text(400,263,text="Word",font=("Arial",60,'bold'))

canvas.grid(column=0,row=0,columnspan=2)


wrong_image=PhotoImage(file="images\wrong.png")
cancel_button=Button(image=wrong_image,borderwidth=0,highlightthickness=0,command=random_french_words)
cancel_button.grid(column=0,row=1)

right_image=PhotoImage(file=r"C:\Users\HP\Desktop\AI\Flash Card\images\right.png")
right_button=Button(image=right_image,borderwidth=0,highlightthickness=0,command=random_french_words)
right_button.grid(column=1,row=1)


random_french_words()



















window.mainloop()

