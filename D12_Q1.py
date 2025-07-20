class Parent:
    def display(self):
        print("Parent class.")

class Child(Parent):
    def call_parent(self):
        self.display()

c = Child()

c.call_parent()

