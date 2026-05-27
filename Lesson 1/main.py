from tkinter import *
 
window = Tk()
window.title("System login")
window.geometry("300x180")

Label(window, text = "Username").grid(row =0, column=0, padx=10, pady=10)
Label(window, text = "password").grid(row=1, column=0, padx=10, pady=10)

us_entry = Entry(window, width=20)
us_entry.grid(row=0, column=1, padx=10, pady=10)

pass_entry = Entry(window, width=20, show="*")
pass_entry.grid(row=1, column=1, padx=10, pady=10)

def login():
    username = us_entry.get()
    password = pass_entry.get()

    print("Username: ", username)
    print("Password: ", password)

def cancel():
    window.destroy()

logbtn = Button(window, text="Login", bg="lightgreen", width=10, command = login)
logbtn.grid(row=2, column=0, padx=10, pady=20)

canbtn = Button(window, text="Cancel", bg="Orange", width=10, command=cancel)
canbtn.grid(row=2, column=1, padx=10, pady=20)

window.mainloop()