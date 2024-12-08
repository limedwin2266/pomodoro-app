from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = "#000080"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="BREAK", fg=RED)
    elif reps % 2 == 1:
        count_down(work_sec)
        timer_label.config(text="WORK", fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="BREAK", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    #math floor will return the largest whole number that is less than or equal to x eg: 4.8 will return 4
    count_min = math.floor(count/60)
    count_sec = count%60
    if len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
        # 1000 is milli second
        # count_down is a function
        # count-1 is the argument in the function
        # the whole sentence mean run the loop every 1 second with the function and pass the argument in to the function
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range (work_session):
            marks += "✔"

        tick_label.config(text=marks)
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = "00:00")
    timer_label.config(text = "Timer",fg=BLUE)
    tick_label.config(text = "")
    global reps
    reps = 0
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)


canvas = Canvas(width = 200, height=224,bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102,112, image = tomato_img)
timer_text = canvas.create_text(103,130, text="00:00", fill = "white", font = (FONT_NAME,35,"bold"))
canvas.grid(column = 1, row = 1)


timer_label = Label(text = "Timer",bg=YELLOW,fg=BLUE,font = (FONT_NAME, 50, "bold"))
timer_label.grid(column = 1, row = 0)

tick_label = Label(fg=GREEN,bg=YELLOW)
tick_label.grid(column = 1, row = 3)

start_btn = Button(text = "Start",command=start_timer)
start_btn.grid(column = 0, row = 2)

reset_btn = Button(text = "Reset", command=reset_timer)
reset_btn.grid(column = 2, row = 2)

window.mainloop()