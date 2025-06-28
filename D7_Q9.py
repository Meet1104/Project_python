my_list = [1, 2, 3, 4, 5, 2, 3]

my_set = set(my_list)
my_tuple = tuple(my_list)

print("Original list:", my_list)
print("Converted to set:", my_set)
print("Converted to tuple:", my_tuple)

print("Set to list:", list(my_set))
print("Set to tuple:", tuple(my_set))

print("List keeps order and duplicates.")
print("Set removes duplicates and is unordered.")
print("Tuple is immutable version of list.")