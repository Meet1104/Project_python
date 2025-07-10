# array_2d = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

# total_sum = 0

# for row in array_2d:
#     total_sum = total_sum + sum(row)

# print( total_sum)


# arr = []
# sum = 0

# row_size = int(input("Enter your row size"))
# col_size = int(input("Enter your col size"))

# for i in range(row_size):
#     a = []
#     for j in range(col_size):
#         a.append(int(input("Enter array elem:")))
#     arr.append(a)

# print("Array is")
# for i,row in enumerate(arr):
#     for j,elem in enumerate(row):
#         sum = sum + elem
#     print()

# print("sum is %d" %sum)


arr = [[2, 6, 2], [5, 2, 7], [8, 4, 3]]

sum = 0

for i, row in enumerate(arr):
    for j, col in enumerate(row):
        sum += col

print(sum)
