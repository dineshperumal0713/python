from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("virus scanner")
root.geometry("200x200")

def msg():
    messagebox.askquestion("Virus Detected", "Virus Found! Do You Want To Remove It?")
btn = Button(root, text = "Check To Find Viruses", command = msg)
btn.place(x=50, y=50)
root.mainloop()