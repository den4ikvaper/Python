from tkinter import *


def button_clicked():
    my_lable["text"] = round(int(input.get())*1.609, 2)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=100)
window.config(padx=50, pady=10)

# Label
my_lable = Label(text="is equal to", font=("Arial", 18, "normal"))
my_lable.grid(column=0, row=2)

# Miles
my_lable = Label(text="Miles", font=("Arial", 18, "normal"))
my_lable.grid(column=3, row=1)

# Km
my_lable = Label(text=0, font=("Arial", 18, "normal"))
my_lable.grid(column=2, row=2)

# KM info
km_info = Label(text="Km", font=("Arial", 18, "normal"))
km_info.grid(column=3, row=2)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=4)

# Input
input = Entry(width=7)
input.grid(column=2, row=1)

window.mainloop()
