from tkinter import *
import pyttsx3
from tkinter import font
import json
import difflib
from tkinter import messagebox



#--------------------------------------Text to speech-----------------------------
engine=pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)

def speak_word():
    engine.say(word_entry.get())
    engine.runAndWait()

def speak_meaning():
    engine.say(meaning_entry.get('1.0','end'))
    engine.runAndWait()


#--------------------------------------Clear Function-------------------------------
def clear():
    word_entry.delete(0,'end')
    meaning_entry.delete('1.0','end')


#--------------------------------------Search Function-------------------------------

def search():
    meaning_entry.delete("1.0",'end')
    word=word_entry.get().lower()
    with open("data.json",mode="r") as file:
        content=json.load(file)
        if word in content:
            # print(content[word])
            meaning=content[word]
            for item in meaning:
                meaning_entry.insert(END,item+"\n\n")
        elif len(difflib.get_close_matches(word,content.keys()))>0:
            close_match=difflib.get_close_matches(word,content)
            if messagebox.askyesno(title="Confirm",message=f"Do you mean {close_match[0]}"):
                word_entry.delete(0,'end')
                word_entry.insert(END,close_match[0])
            else:
                for item in range(1,len(close_match)):
                    if messagebox.askyesno(title="Confirm",message=f"Do you mean {close_match[item]}"):
                        word_entry.delete(0,'end')
                        word_entry.insert(END,close_match[item])
                        break
                    else:
                        messagebox.showinfo(title="Not found",message="This is not a correct word")
                        word_entry.delete(0,'end')
                        break
        else:
            word_entry.delete(0,'end')
            messagebox.showerror(title="Not found",message="This is not a correct word")
                    
                
            
            
        

#--------------------------------------User Interface--------------------------------
window=Tk()
window.title("Oxford Dictionary")
window.geometry('1000x600')
window.resizable(False,False)


canvas=Canvas(width=1000,height=600)
background_img=PhotoImage(file="bg.png")
canvas.create_image(500,290,image=background_img)

canvas.create_text(680,100,text="Enter Word",font=("Arial",40,'bold'),fill="red")
canvas.grid(column=0,row=0)

custom_font=font.Font(size=25)
word_entry=Entry(font=custom_font)
word_entry.place(x=530,y=160,width=300,height=50)


button_img=PhotoImage(file="Picol-Picol-Speaker-Louder.48.png")
speak_word_button=Button(image=button_img,bg="whitesmoke",borderwidth=0,command=speak_word)
speak_word_button.place(x=550,y=240,width=50,height=50)

search_img=PhotoImage(file="Custom-Icon-Design-Mono-General-2-Search.48.png")
search_word_button=Button(image=search_img,borderwidth=0,bg="whitesmoke",command=search)
search_word_button.place(x=730,y=240,width=50,height=50)

meaning_text=Label(text="Meaning",font=("Arial",40,'bold'),fg="red",bg="whitesmoke")
meaning_text.place(x=580,y=300)

meaning_entry_custom_font=font.Font(size=15)
meaning_entry=Text(font=meaning_entry_custom_font,borderwidth=2)
meaning_entry.place(x=500,y=380,width=400,height=130)

meaning_speaker_image=PhotoImage(file="Picol-Picol-Speaker-Louder.48.png")
meaning_speaker=Button(image=meaning_speaker_image,borderwidth=0,bg="#F9F9F9",command=speak_meaning)
meaning_speaker.place(x=550,y=520)

clear_image=PhotoImage(file="Oxygen-Icons.org-Oxygen-Actions-edit-clear-locationbar-rtl.48.png")
clear_image_button=Button(image=clear_image,bg="#F9F9F9",borderwidth=0,command=clear)
clear_image_button.place(x=730,y=520)












window.mainloop()