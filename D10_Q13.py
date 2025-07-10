data = [(1, 5), (2, 3), (4, 1), (6, 2)]

sorted_data = sorted(data, key=lambda x: x[1])

print("Original list of tuples:", data)
print("Sorted by second element:", sorted_data)
