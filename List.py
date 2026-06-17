from tkinter import *

win = Tk()
win.title("My Favorite Dishes")
listbox = Listbox(win, height = 10, width = 15, bg = "grey",
                  fg = "yellow", activestyle = "dotbox", font = "Helvetica")

win.geometry("300x250")
label = Label(win, text = "Fodd Items")
listbox.insert(1, "Nachos")
listbox.insert(2, "Sandwhich")
listbox.insert(3,"Burger")
listbox.insert(4, "Pizza")
listbox.insert(5, "Burrito")
listbox.insert(6,"Pasta")
label.pack()
listbox.pack()
win.mainloop()