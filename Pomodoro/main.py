from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK="✔️"
reps=0
clock=None
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    window.after_cancel(clock)
    canvas.itemconfig(timer_text,text="00:00")
    timer_variable.config(text="Timer")
    tick_variable.config(text="")
    global reps
    reps=0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    
    WORK_MIN_SEC=WORK_MIN*60
    SHORT_BREAK_MIN_SEC=SHORT_BREAK_MIN*60
    LONG_BREAK_MIN_SEC=LONG_BREAK_MIN*60
    
    if reps%2!=0:
        count_down(WORK_MIN_SEC) #green
        timer_variable.config(text="WORK",fg=GREEN)
    elif reps==2 or reps==4 or reps==6:
        count_down(SHORT_BREAK_MIN_SEC) #pink
        timer_variable.config(text="Short Break",fg=PINK)
    else:
        count_down(LONG_BREAK_MIN_SEC) #red
        timer_variable(text="Long Break",fg=RED)
        
    # count_down(*60)


def count_down(timer):
    global clock
    timer_min=math.floor(timer/60)
    timer_sec=timer%60
    if timer_sec==0 or timer_sec<10:
        canvas.itemconfig(timer_text,text=f"{timer_min}:0{timer_sec}")
    else:
        canvas.itemconfig(timer_text,text=f"{timer_min}:{timer_sec}")
    
    if timer > 0:
        clock=window.after(1000,count_down,timer-1) #This takes ms,fn,*args as parameter
    else:
        start_timer()
        mark=""
        work_sessions=math.floor(reps/2)
        for items in range(work_sessions):
            mark+=CHECK_MARK
        tick_variable.config(text=mark,bg=YELLOW)
            
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.minsize(width=400,height=300)
window.config(padx=100,pady=50,bg=YELLOW)


timer_variable=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,'bold'))
timer_variable.grid(column=1,row=0)

tick_variable=Label(fg="green")
tick_variable.grid(column=1,row=3)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0) #This creates a canvas
img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


start_button=Button(text="Start",borderwidth=0,font=(FONT_NAME,10,'bold'),bg=YELLOW,command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",borderwidth=0,font=(FONT_NAME,10,'bold'),bg=YELLOW,command=timer_reset)
reset_button.grid(column=2,row=2)

 









window.mainloop()