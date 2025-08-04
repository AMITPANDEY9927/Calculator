def sum(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def devide(num1,num2):
    return num1/num2

def multiply(num1,num2):
    return num1*num2

def modulas(num1,num2):
    return num1%num2

def calculate():
    num1=int(input("enter the first number"))
    num2=int(input("enter the second number"))
    session=1
    while(session!=0):
        operation=input("chose the operation to perform \n +  -  /  *  %  ")
        if(operation=="+"):
            print("addition =",sum(num1,num2))
        elif(operation=="-"):
            print("subtraction =",subtract(num1,num2))
        elif(operation=="/"):
            print("devide =",devide(num1,num2))
        elif(operation=="*"):
            print("multiply =",multiply(num1,num2))
        elif(operation=="%"):
            print("modulas =",modulas(num1,num2))
        else:
            print("invalid choice")

        session=int(input("\ndo you want to calculate again? press 1 for re \n press 0 to exit"))
        if(session!=0):
            change_number=int(input("press 1 to change the number"))
            if(change_number==1):
                num1=int(input("enter the first number"))
                num2=int(input("enter the second number\n"))
calculate()

