from tkinter import *

window = Tk()
window.title("Traffic Lights")
window.geometry("200x220")

button1 = Button(window,text="Stop", bg="red", width=20)
button1.grid(row= 0, column=0, padx=10, pady =10)

button2 = Button(window, text="Wait", bg="orange",width=20)
button2.grid(row= 1, column=0, padx =10, pady=10)

button3 = Button(window, text="Go",bg="green", width=20)
button3.grid(row=2, column= 0, padx=10, pady= 10)


window.mainloop()