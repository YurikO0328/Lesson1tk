from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("System Updater")

Label(window, text = "Downloading Updates...").pack(pady = 10)

progress = Progressbar(window, orient = HORIZONTAL, length = 300, mode = "determinate")

def bar():
    import time

    progress['value'] = 10
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] =20
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 30
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 40
    window.update_idletasks()
    time.sleep( 0.5)

    progress['value'] = 50
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 60
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 70
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] =80
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 90
    window.update_idletasks()
    time.sleep(0.5)

    progress['value'] = 100

progress.pack(pady = 10)

Button(window, text = "Start Download", command = bar).pack(pady = 10)

window.mainloop()