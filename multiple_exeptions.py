try:
   num1,num2 = input(int("please enter two numbers separated by a comma"))
   sum = num1/num2
   print("sum =", sum)
except ZeroDivisionError:
    print ("numbers cannot be divided by zero")
except SyntaxError:
    print("please place a comma between the numbers")
except ValueError:
    print("please enter a integer number")
except:
    print("wrong input")
else:
    print("there are no exceptions")
finally:
    print("code has ran succsessfully")
