from tkinter import *

window=Tk()
window.title("Morning Bakery")
window.geometry("300x500")
window.configure(bg="white")

Label(window, text = "Breakfast Menu", bg = "white").grid(row=0, column=0, columnspan=2, padx=10, pady=10)

Label(window, text = "Donuts ($2)", bg ="white").grid(row=1, column=0, padx=10, pady=10)

donutSpin = Spinbox(window, from_ = 0, to = 12)
donutSpin.grid(row=1, column=1, padx=10, pady=10)

Label(window, text = "Muffins ($3)", bg = "white").grid(row=2, column=0, padx=10, pady=10)

muffinSpin = Spinbox(window, from_=0, to=12)
muffinSpin.grid(row=2, column=1, padx=10, pady=10)

Label(window, text = "Coffee ($4)", bg = "white").grid(row=3, column=0, padx=10, pady=10)

coffeeSpin = Spinbox(window, from_=0, to=5)
coffeeSpin.grid(row=3, column=1, padx=10, pady=10)

def submit():
    donuts = donutSpin.get()
    muffins = muffinSpin.get()
    coffee = coffeeSpin.get()

    result.config(text = "Order Placed!\nDonuts: " + donuts + "\nMuffins: " + muffins + "\nCoffee: " + coffee)

Button(window, text = "Place Order", command = submit).grid(row=4, column=0, columnspan=2, padx=20)

result = Label(window, text = "", bg = "white")
result.grid(row = 5, column = 0, columnspan = 2)

window.mainloop()