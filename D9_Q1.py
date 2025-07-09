def fact(num):

    if num <= 1:
        return 1
    else :
        return num*fact(num - 1)

num = int(input("Enter the number : "))

ans = fact(num)

print(ans)