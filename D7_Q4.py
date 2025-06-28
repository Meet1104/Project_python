dict = {
    "apple" : 20,
    "mango" : 50,
    "orange" : 30,
    "banana" : 10
}

print(dict)

high = max(dict, key = dict.get)
print(high)