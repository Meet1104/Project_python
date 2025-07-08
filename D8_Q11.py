def employee_info(**kwargs):
    required = ['name', 'department', 'salary']
    missing = [field for field in required if field not in kwargs]

    if missing:
        print("Missing fields:", ", ".join(missing))
    else:
        print("Employee Info:", kwargs)

employee_info(name="Raj", department="IT", salary=50000)
employee_info(name="Simran", department="HR")
