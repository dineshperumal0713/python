number = float(input("enter a number to find its sqaure root: "))
if number < 0:
    print("Sorry,square root of negative numbers is not defined in real numbers.")
else:
    square_root = number**0.5
    print (f"The square root of {number} is {square_root}")  


