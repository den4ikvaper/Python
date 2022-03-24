from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Circle"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="WORK TIMER")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="BREAK")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="BREAK")
    else:
        count_down(work_sec)
        title_label.config(text="WORK")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        works_sessions = math.floor(reps/2)
        for _ in range(works_sessions):
            marks += "🍅"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW)


title_label = Label(text="WORK TIMER", font=(FONT_NAME, 36), fg="#e17153", bg=YELLOW)
title_label.config(pady=20)
title_label.grid(column=0, row=0)

canvas = Canvas(width=300, height=220, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="background.gif")
canvas.create_image(150, 100, image=tomato_img)
timer_text = canvas.create_text(150, 100, text="00:00", fill="#f7f5dd", font=(FONT_NAME, 72))
canvas.grid(column=0, row=1)


start_button = Button()
start_button = Button(text="Start", highlightthickness=0, command=start_timer, height=50, width=120)
start_button_img = PhotoImage(file='start.gif')
start_button.config(image=start_button_img)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset_time, height=50, width=120)
reset_button_img = PhotoImage(file='reset.gif')
reset_button.config(image=reset_button_img)
reset_button.grid(column=0, row=3)

check_marks = Label(text="", font=(FONT_NAME, 36), fg=GREEN)
check_marks.config(pady=20)
check_marks.config(bg=YELLOW)
check_marks.grid(column=0, row=4)

window.mainloop()
