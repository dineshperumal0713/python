from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination Converter")
root.configure(bg="lightblue")
root.geometry("650x400")

upload = Image.open("euro pic.jpg")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg= "lightblue" )
label.place(x=180, y=20)

label1 = Label(
    root,
    text="Hey user!Welcome to the denominaton counter application.",
    bg = "lightblue"
)
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    msgbox = messagebox.showinfo(
        "Alert",
        "Do you want to calculate the denomination count?" 
   )
    
    if msgbox == "ok":
        topwin()
    
button1 = Button(
    root,
    text="lets get started!"
)


