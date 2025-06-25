num1 = int(input("Enter your number :"))
num2 = int(input("Enter your number :"))
operation = input("Enter operation (+, -, *, /): ")

add = num1 + num2
sub = num1 - num2
multi = num1 * num2
div = num1 / num2


match operation :
    case '+' : print(add)
    case '-' : print(sub)
    case 'multi' : print(multi)
    case 'div' : print(div)
    case _: print("Invaild")
