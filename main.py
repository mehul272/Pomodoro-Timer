 from tkinter import *
import math
import tkinter.messagebox

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    start_button.config(state="normal")
    reset_button.config(state="disabled")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    heading_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    start_button.config(state="disabled")
    reset_button.config(state="normal")
    work_sec = WORK_MIN * 1
    short_break_sec = SHORT_BREAK_MIN * 1
    long_break_sec = LONG_BREAK_MIN * 1
    reps += 1

    if reps % 8 == 0:
        tkinter.messagebox.showinfo(title="Break", message="Long Break")
        heading_label.config(text="Break",fg =PINK)
        count_down(long_break_sec)
    elif reps % 2 ==0:
        tkinter.messagebox.showinfo(title="Break", message="Short Break")
        heading_label.config(text="Break",fg=GREEN)
        count_down(short_break_sec)
    else:
        tkinter.messagebox.showinfo(title="Work", message="Start Working")
        window.attributes('-topmost', 0)
        heading_label.config(text="Work" ,fg=RED)
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec <10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,count_down, count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✓"

        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Pomodoro Game")
window.config(padx = 100 , pady = 50,bg=YELLOW)



canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness= 0)
my_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=my_image)
timer_text = canvas.create_text(100,130, text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

#label
heading_label = Label(text="Timer", font = (FONT_NAME,50,"bold"), bg=YELLOW, fg=GREEN)
heading_label.grid(column=1,row=0)

#start_button
start_button = Button(text="Start",highlightthickness= 0,command = start_timer)
start_button.grid(column=0,row=2)

#reset_button
reset_button = Button(text="Reset",highlightthickness= 0,command = reset_timer)
reset_button.grid(column=2,row=2)

#Checkbutton
check_marks = Label(fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)



window.mainloop()
