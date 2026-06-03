from tkinter import * 
from tkinter.ttk import *

window=Tk()

progress = Progressbar(window, orient = HORIZONTAL, length = 100,
                       mode = "determinate")

def bar():
    import time

    progress['value'] = 20
    window.update_idletasks()
    time.sleep(1)

    progress['value'] = 40
    window.update_idletasks()
    time.sleep(1)

    progress['value'] = 50
    window.update_idletasks()
    time.sleep(1)

    progress['value'] = 60
    window.update_idletasks()
    time.sleep(1)

    progress['value'] = 80
    window.update_idletasks()
    time.sleep(1)

    progress['value'] = 100

progress.pack(pady = 10)

Button(window, text = "Start", command = bar).pack(pady = 10)

window.mainloop()


