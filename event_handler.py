from tkinter import *

root = Tk()
root.title("keyboard events")
root.geometry("400x500")
def handle_keypress(event):
    print(event.char)
root.bind("<Key>", handle_keypress)
def handle_click(event):
    print("\nthe button was clicked")
btn = Button(text = "click")
btn.pack()
btn.bind("<Button-1>", handle_click)
root.mainloop()
