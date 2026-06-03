from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Menubar demonstration")

menubar = Menu(window)

#FILE MENU
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "File", menu = file)

file.add_command(label = "New file", command = None)
file.add_command(label = "Open...", command = None)
file.add_command(label = "Save",command = None)
file.add_separator()

file.add_command(label = "Exit", command = window.destroy)

#EDIT MENU
edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Edit", menu = edit)

edit.add_command(label = "Undo", command = None)
edit.add_command(label = "Redo...", command = None)
edit.add_separator()
edit.add_command(label = "Cut",command = None)
edit.add_command(label = "Copy",command = None)
edit.add_command(label = "Paste",command = None)
edit.add_command(label = "Select all",command = None)
edit.add_separator()
edit.add_command(label = "Find...",command = None)
edit.add_command(label = "Find again",command = None)

#HELP MENU
help = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Help", menu = help)

help.add_command(label = "TK Help", command = None)
help.add_command(label = "Documentation", command = None)
help.add_separator()
help.add_command(label = "Restart to Update", command = None)
help.add_command(label = "About", command = None)

window.configure(menu=menubar)
window.mainloop()






