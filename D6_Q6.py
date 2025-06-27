list = []


for i in range(1,5) :
    words = int(input("Enter the number :- "))
    list.append(words)
    
print(list)

print("largest number is :" , max(list))

print("smallest number is :" ,min(list))