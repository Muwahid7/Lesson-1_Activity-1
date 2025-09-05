from tkinter import *
from datetime import date
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')
lbl = Label(text="Hey There!", fg="white", bg="blue", height=1, width=300)
name_lbl = Label(text="Full Name", bg="light blue")
name_entry = Entry()
def display():
    name = name_entry.get()
    text_box.delete("1.0", END)
    message = "Welcome to the Application! \nToday's date is: "
    greet = "Hello " + name + "\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, str(date.today()))
text_box = Text(height=3)
btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg='white')
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()