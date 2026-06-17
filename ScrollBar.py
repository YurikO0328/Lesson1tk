"""from tkinter import *

win = Tk()
win.geometry("150x200")
w = Label(win, text="HelloHello", font = "50")
w.pack()
sb = Scrollbar(win)
sb.pack(side = RIGHT, fill = Y)
myList = Listbox(win, yscrollcommand=sb.set)

for line in range(1,26):
    myList.insert(END, "Hi" + str(line))

myList.pack(side = LEFT, fill = BOTH)

sb.config(command=myList.yview)
win.mainloop()"""

from tkinter import *

win = Tk()
win.geometry("300x150")

win.title("My Playlist")
listbox = Listbox(win, height = 10, width = 15, bg = "grey",
                  fg = "yellow", activestyle = "dotbox", font = "Helvetica")

win.geometry("300x250")
label = Label(win, text = "Fodd Items")
listbox.insert(1, "Song")
listbox.insert(2, "Song")
listbox.insert(3,"Song")
listbox.insert(4, "Song")
listbox.insert(5, "Song")
listbox.insert(6,"Song")


#Forgot how to make the split in the frames

l = Label(win, text="Playlist", font = "50")
l.pack()
listbox.pack()

frame = Frame(win,bg = "grey")
frame.pack()

bottomFrame = Frame(win)
bottomFrame.pack(side = BOTTOM)

b1 = Button(frame, text = "Pause", fg = "red", bg = "beige")
b1.pack(side = LEFT, padx=10)

b2 = Button(frame, text = "Play", fg = "brown", bg = "beige")
b2.pack(side= LEFT, padx=10)

win.mainloop()