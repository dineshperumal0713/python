import tkinter as tk


def multiply():
  
    res = float(num1.get()) * float(num2.get())
    result_label.config(text=res)


root = tk.Tk()


num1 = tk.Entry(root)
num1.pack()
num2 = tk.Entry(root)
num2.pack()


btn = tk.Button(root, text="Multiply", command=multiply)
btn.pack()


result_label = tk.Label(root)
result_label.pack()

root.mainloop()