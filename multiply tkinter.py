import tkinter as tk


def multiply():
    # Get values, multiply them, and update the result
    res = float(num1.get()) * float(num2.get())
    result_label.config(text=res)


root = tk.Tk()

# Input boxes
num1 = tk.Entry(root)
num1.pack()
num2 = tk.Entry(root)
num2.pack()

# Button to trigger multiplication
btn = tk.Button(root, text="Multiply", command=multiply)
btn.pack()

# Label to show the final answer
result_label = tk.Label(root)
result_label.pack()

root.mainloop()