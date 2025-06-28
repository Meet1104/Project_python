my_list = [1, 2, 2, 3, 4, 3, 5]

new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)

print("Original list:", my_list)
print("List without duplicates:", new_list)
