students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 75},
    {"name": "Charlie", "marks": 95}
]

sorted_students = sorted(students, key=lambda x: x["marks"])

print("Original list of dictionaries:", students)
print("Sorted by marks:", sorted_students)
