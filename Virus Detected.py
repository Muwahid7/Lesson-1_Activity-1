from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x500")
def msg():
    messagebox.showwarning("alert","stop, virus found")
button = Button(root,text = "Scan for virus",command = msg)
button.place(x=40,y=80)
root.mainloop()