from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("the main window")

def toplevel():
    top = Toplevel()
    top.title("the top level window")
    top.geometry("300x300")

    l2 = Label(top, text="this is a toplevel window")
    l2.pack()
    top.mainloop()

l = Label(root, text="this is the main window")
btn = Button(root, text="click here to open another window", command=toplevel)

l.pack()
btn.pack()

root.mainloop()



