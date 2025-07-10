arr = []

row = int(input("Enter the row number : "))
col = int(input("Enter the col number : "))

for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input("enter the elem : ")))
    arr.append(a)

print(arr)

transpose = []


for i in range(col):
    temp = []
    for j in range(row):
        temp.append(arr[j][i])
    transpose.append(temp)

print(transpose)