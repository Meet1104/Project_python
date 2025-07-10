arr = [
    [12, 45, 74],
    [33, 84, 29],
    [11, 67, 22]
]

max_value = arr[0][0]
min_value = arr[0][0]
for row in arr:
    for element in row:
        if element > max_value:
            max_value = element

print(max_value)

for row in arr:
    for element in row:
        if element < min_value:
            min_value = element

print(min_value)


