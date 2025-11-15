bill = int(input("Enter the total bill amount: "))
paid = int(input("Enter the amount paid: "))
if paid < bill:
    bill - paid
    print("Insufficient amount paid. You still owe:", bill - paid)
elif paid > bill:
    change = paid - bill
    print("Change to be returned:", change)
