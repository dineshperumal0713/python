def addition(a,b):
    return(a+b)
def subtraction(a,b):
    return(a-b)
def multiplication(a,b):
    return (a*b)
def division(a,b):
    return(a/b)
print("a=addition")
print("b=subtraction")
print("c=multiplication")
print("d=division")
choice = str(input("enter a choice:  " ))
num1=int(input("enter first number"))
num2=int(input("enter second number"))
if choice == "a" or choice ==  "addition":
    print (num1,"+",num2,"=",addition(num1,num2))
elif choice == "b" or choice == "subtraction":
    print (num1,"-",num2,"=",subtraction(num1,num2))
elif choice == "c" or choice == "multiplication":
    print (num1,"*",num2,"=",multiplication(num1,num2))
elif choice == "d" or choice == "division":
    print (num1,"/",num2,"=",division(num1,num2))
else:
    print("invalid input")

