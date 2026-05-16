import tkinter as tk


def convert():
    
    cm = float(inches_entry.get()) * 2.54
    result_label.config(text=f"{cm} cm")


root = tk.Tk()
root.title("Inches to CM")


inches_entry = tk.Entry(root)
inches_entry.pack(pady=5)


btn = tk.Button(root, text="Convert to CM", command=convert)
btn.pack(pady=5)


result_label = tk.Label(root, text="0 cm")
result_label.pack(pady=5)

root.mainloop()
