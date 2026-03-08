try:
   num= int(input("enter a number:   "))
   print("you have entered",num)
except ValueError:
    print("exeption has occured",ValueError)