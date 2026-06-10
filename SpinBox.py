from tkinter import *

window=Tk()
window.title("Food ordering Form")
window.geometry("700x400")
window.configure(bg = "white")

Label(window, text = "Email", bg = "white").grid (row=0, column = 0, padx = 10, pady = 10)

emailentry = Entry(window, width = 40)
emailentry.grid(row = 0, column = 1, padx = 10, pady = 10)

Label(window, text = "Password", bg = "white").grid (row=1, column = 0, padx = 10, pady = 10)

passentry = Entry(window, width = 40, show = "*")
passentry.grid(row =1, column = 1, padx = 10, pady = 10)

Label(window, text = "What food you like?", bg = "white").grid(row = 2, column = 0, padx = 10, pady = 10)

foodSpin = Spinbox(window, values = ("Chicken Sandwich", "Veg Sandwich", "Pasta"))
foodSpin.grid(row = 2, column = 1, padx = 10)

Label(window, text = "What Beverage would you like?", bg = "white").grid(row = 3, column = 0, padx = 10, pady = 10)

bevSpin = Spinbox(window, values = ("Cola", "Orange Juice", "Water", "None"))
bevSpin.grid(row = 3, column = 1, padx = 10, pady = 10)

Label(window, text = "What Dessert would you like?", bg = "white").grid(row = 4, column = 0, padx = 10, pady = 10)

desSpin = Spinbox(window, values = ("Chocolate Cake", "Ice Cream", "Donut", "None"))
desSpin.grid(row = 4, column = 1, padx = 10, pady = 10)

def submit():
    email = emailentry.get()
    password = passentry.get()
    food = foodSpin.get()
    beverage = bevSpin.get()
    dessert = desSpin.get()
    
    result.config(text = f"Order Placed!\n{food}, {beverage} and {dessert}\n {email}\n{password}")


Button(window, text = "Submit Order", command=submit).grid(row = 6, column = 0, columnspan = 2, padx = 20)
result = Label(window, text = "", bg = "white")
result.grid(row = 7, column = 0, columnspan = 2)

window.mainloop()