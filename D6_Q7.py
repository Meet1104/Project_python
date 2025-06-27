# tuple = (1,2,2,3,4,4,5)

# new_tuple = (set(tuple))

# print(tuple)
# print(new_tuple)


original_tuple = (1, 2, 2, 3, 4, 4, 5)


unique_list = []

for i in original_tuple:
    if i not in unique_list:
        unique_list.append(i)

unique_tuple = tuple(unique_list)


print("Original tuple:", original_tuple)
print("Unique values :", unique_tuple)

