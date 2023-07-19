import tkinter
from tkinter import *

window = Tk()
window.title("Mile to Km Convertor")
window.minsize(width=300, height=150)
window.config(padx=30, pady=30)


def button_clicked():
    # converting miles to km
    n = (inp.get())
    res = round(1.60934 * int(n))
    my_label_km.config(text=f"{res}")


# Label1
my_label1 = Label(text="is equal to", font=("Arial", 20))
my_label1.grid(column=0, row=1)

# label2
my_label1 = Label(text="Miles", font=("Arial", 20))
my_label1.grid(column=2, row=0)

# label3
my_label1 = Label(text="Km", font=("Arial", 20))
my_label1.grid(column=2, row=1)


# label km

my_label_km = Label(text="0", font=("Arial", 20))
my_label_km.grid(column=1, row=1)



# Button
button = Button(text="Calculate", command= button_clicked)
button.grid(column=1, row=2)

# Entry
inp = Entry(width=10)
print(inp.get())
inp.grid(column=1, row=0)



window.mainloop()

