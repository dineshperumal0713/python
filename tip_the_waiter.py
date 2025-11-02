def total_calc(bill_amount, tip_percentage):
    tip_amount  = tip_percentage / 100 * bill_amount
    total = bill_amount + tip_amount
    print(f"the total bill is:", total)
total_calc(120,20)