data = input("Enter comma-separated numbers: ")

data = data.replace(" ", "").split(",")

num_list = [int(i) for i in data]

print("List:", num_list)
print("Set:", set(num_list))
print("Tuple:", tuple(num_list))
