from tkinter import *


def calculate_kg_to_pounds():
    kg = float(kg_to_convert.get())
    pounds = round(kg * 2.2046, 2)
    converted_kg.config(text=f"{pounds}")


window = Tk()
window.title("Kg to Pounds Converter")
window.minsize(width=300, height=150)
window.config(pady=30, padx=20)

kg_to_convert = Entry(width=10)
kg_to_convert.grid(row=0, column=1)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

kg_label = Label(text="Kg")
kg_label.grid(row=0, column=2)

converted_kg = Label(text="0")
converted_kg.grid(row=1, column=1)

pound_label = Label(text="Pounds")
pound_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=calculate_kg_to_pounds)
calculate_button.grid(row=2, column=1)

window.mainloop()
