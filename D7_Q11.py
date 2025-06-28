my_dict = {'x': 100, 'y': 200, 'z': 300}

key_list = list(my_dict.keys())
key_set = set(my_dict.keys())

val_list = list(my_dict.values())
val_tuple = tuple(my_dict.values())

print("Keys as list:", key_list)
print("Keys as set:", key_set)
print("Values as list:", val_list)
print("Values as tuple:", val_tuple)