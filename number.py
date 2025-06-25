num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
num3 = int(input("Enter the number: "))

if num1 == num2 and num2 == num3 :
    print("all are same")
elif num1 == num2 > num3 :
    print("num1 and num2 is max")
elif num1 == num3 > num2:
    print("num1 and num3 is max")
elif num2 == num3 > num1 :
    print("num2 and num3 is max")
else:
    if num1 > num2:
        if num1 > num3:
            print("num1 is max")
        else:
            print("num3 is max")
    else:
        if num2 > num3:
            print("num2 is max")
        else:
            print("mum3 is max")



