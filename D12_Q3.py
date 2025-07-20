class Grandparent:
    def role(self):
        print("Grandparent role")

class Parent(Grandparent):
    def role(self):
        super().role()
        print("Parent role")

class Child(Parent):
    def role(self):
        super().role()
        print("Child role")

c = Child()
c.role()

