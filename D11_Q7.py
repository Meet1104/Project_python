class Employee:
    def __init__(self):
        self.name = "Default"
        self.position = "Intern"
        print("Employee created")

    def __del__(self):
        print("Employee deleted")

e = Employee()