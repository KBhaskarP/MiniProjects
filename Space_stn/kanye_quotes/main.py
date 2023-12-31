from tkinter import *
import requests


def get_quote():
    response=requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data=response.json()
    quotes=data['quote']
    canvas.itemconfig(quote_text,text=quotes)



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50,bg="#FFF5E0")

canvas = Canvas(width=300, height=414,bg="#FFF5E0",highlightthickness=0)
background_img = PhotoImage(file=r"kanye_quotes\background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 15, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye_quotes\kanye.png")
kanye_button = Button(image=kanye_img, borderwidth=0, command=get_quote,bg="#FFF5E0")
kanye_button.grid(row=1, column=0)



window.mainloop()