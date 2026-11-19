def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def divide(num1,num2):
    return num1/num2

def multiply(num1,num2):
    return num1+num2

def CircleArea(r):
    if r>=0:
       return 3.14 * r * r
    else:
       return "Error"

def main():
    choice=int(input("please enter a number for your operation\n 1=add, 2=sub, 3=/, 4=*, 5=area"))
    num1=float(input("please enter your first number"))
    num2=float(input("please enter your second number(useless for area"))
    match choice:
        case 1:
            result=add(num1,num2)
            print(result)
        case 2:
            result=subtract(num1,num2)
            print(result)
        case 3:
            result=divide(num1,num2)
            print(result)
        case 4:
            result=multiply(num1,num2)
            print(result)
        case 5:
           result=CircleArea(num1)
           print(result)
           
if __name__=="__main__":
    main()
