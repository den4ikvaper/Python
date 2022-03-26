BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

# <--------------------- NEXT CARD GENERATOR ---------------------->

to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_word, text=current_card["French"], fill='black')
    canvas.itemconfig(card_title, text="French", fill='black')
    window.after(3000, func=flip_card)


# <--------------------- Change side of card ---------------------->


def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')
    canvas.itemconfig(card_title, text="English", fill='white')


# <--------------------- Save word which user don't know ---------------------->


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# <--------------------- UI SETUP ---------------------->

# Windows settings
window = Tk()
window.title("Flash Card Project")
window.minsize(height=726, width=900)
window.maxsize(height=726, width=900)
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

flip_timer = window.after(3000, func=flip_card)

# Flash card settings
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 180, text="Language", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 293, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, bd=0, width=96, height=95, command=next_card)
unknown_button.grid(column=0, row=1, pady=(17, 0))
check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, highlightthickness=0, bd=0, width=96, height=95, command=is_known)
known_button.grid(column=1, row=1, pady=(17, 0))

next_card()
window.mainloop()
