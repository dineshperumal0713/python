from datetime import datetime
import tkinter as tk


def calculate_age():
    today = datetime.today()

    birth_year = int(year_entry.get())
    birth_month = int(month_entry.get())

    total_months = (
        (today.year - birth_year) * 12 + today.month - birth_month
    )

    years = total_months // 12
    months = total_months % 12

    result_label.config(text=f"Age: {years} years, {months} months")


root = tk.Tk()
root.title("Age Calculator")

tk.Label(root, text="Birth Year (e.g., 1995):").pack()
year_entry = tk.Entry(root)
year_entry.pack()

tk.Label(root, text="Birth Month (1-12):").pack()
month_entry = tk.Entry(root)
month_entry.pack()

btn = tk.Button(root, text="Calculate Age", command=calculate_age)
btn.pack(pady=10)

result_label = tk.Label(root, text="Enter details above", font=("Arial", 12))
result_label.pack()

root.mainloop()