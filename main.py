from tkinter import *

Window = Tk()
Window.title("Mile to Km Converter")
Window.geometry("500x400")
Window.config(padx=20, pady=20)


def calculate():
    input = my_input.get()
    input_int = float(input)
    km = round(input_int * 1.60934, 2)
    answer_label.config(text= km)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

answer_label = Label(text="0")
answer_label.grid(column=1, row=1)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

my_input = Entry(width=6)
my_input.grid(column=1, row=0)

button = Button(text="Calculate", command= calculate)
button.grid(column=1, row=2)





Window.mainloop()