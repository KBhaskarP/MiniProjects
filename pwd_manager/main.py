from tkinter import * 
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pwd_entry.delete(0,'end')
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pwd_letters=random.randint(8,10)
    pwd_numbers=random.randint(4,5)
    pwd_symbols=random.randint(1,3)

    password_list=[]

    for char in range(pwd_letters):
        password_list.append(random.choice(letters))
    for num in range (pwd_numbers):
        password_list.append(random.choice(numbers))
    for items in range(pwd_symbols):
        password_list.append(random.choice(symbols))
    random.shuffle(password_list)

    final_password=""
    for items in password_list:
        final_password+=items
    # print(final_password)
    pwd_entry.insert(0,final_password)
    
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_input():
    
    web_name=website_entry.get()
    email_id=email_entry.get()
    pwd_selected=pwd_entry.get()
    data_dictionary={
        web_name:{
            "email":email_id,
            "password":pwd_selected
    }
        }
    if web_name == "" or email_id=="" or pwd_selected=="":
        messagebox.showwarning(title="Oops",message="You left some fields empty")
    else:
    
        if messagebox.askokcancel(title="Please Confirm",message=f" Website: {web_name}\n Email: {email_id}\n Password: {pwd_selected}"):
            # with open("data.json",mode='r') as dump_file:
            #     # file.write(f"{web_name} | {email_id} | {pwd_selected}\n")
            #     #Reading the data
            #     data=json.load(dump_file)
            #     #updating the data
            #     data.update(data_dictionary)
            # with open("data.json",mode='w') as dump_file:
            #     json.dump(data,dump_file,indent=4)
            #     messagebox.showinfo(title="Completed",message="Saved Successfully ")
            
            # website_entry.delete(0,'end')
            # pwd_entry.delete(0,'end')
            try:
                with open("new_data.json",mode="r") as data_file:
                    data=json.load(data_file)
                    data.update(data_dictionary)
            except FileNotFoundError:
                with open("new_data.json",mode="w") as data_file:
                    json.dump(data_dictionary,data_file,indent=4)
            else:
                with open("new_data.json",mode="w") as data_file:
                    json.dump(data,data_file,indent=4)
                    messagebox.showinfo(title="Completed",message="Saved Successfully ")
            finally:
                website_entry.delete(0,'end')
                pwd_entry.delete(0,'end')
                
# ----------------------------Search Results --------------------------#
def search_results():
    web_name=website_entry.get()
    try:
        with open("new_data.json",mode="r") as file_search:
            data=json.load(file_search)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR",message="No such file or directory found")
    else:
        for key in data.keys():
            if key==web_name:
                result_pwd=data[key]["password"]
                result_email=data[key]["email"]
                messagebox.showinfo(title=f"Results for {web_name}",message=f"E-mail: {result_email}\n Password: {result_pwd}")
                website_entry.delete(0,"end")
            else:
                messagebox.showinfo(title="Not Found",message=f"No information for {web_name}")
                break
            
                
        
# ---------------------------- UI SETUP ------------------------------- # 
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50,bg="#FBF0B2")


canvas=Canvas(width=200,height=150,bg="#FBF0B2",highlightthickness=0)
lock_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:",font=("Arial",13,'bold'),bg="#FBF0B2")
website_label.grid(column=0,row=1)

website_entry=Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

email_label=Label(text="Email/Username:",font=("Ariel",13,'bold'),bg="#FBF0B2")
email_label.grid(column=0,row=2)


email_entry=Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"kumarbhaskar.forworks@gmail.com")

pwd_label=Label(text="Password:",font=("Ariel",13,'bold'),bg="#FBF0B2")
pwd_label.grid(column=0,row=3)

pwd_entry=Entry(width=21)
pwd_entry.grid(column=1,row=3)

gen_pwd_button=Button(text="Generate Password",borderwidth=0,command=generate_password,bg="#FBF0B2")
gen_pwd_button.grid(column=2,row=3)

add_button=Button(text="Add",width=36,borderwidth=0,command=save_input,bg="#FBF0B2")
add_button.grid(column=1,row=4,columnspan=2)

search_button=Button(text="    Search",borderwidth=0,command=search_results,bg="#FBF0B2")
search_button.grid(column=2,row=1)
window.mainloop()