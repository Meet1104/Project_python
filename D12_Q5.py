class A:
    def display(self):
        print("Class A")

class B(A):
    def display(self):
        super().display()
        print("Class B")

class C(A):
    def display(self):
        super().display()
        print("Class C")

class D(B, C):
    def display(self):
        super().display()
        print("Class D")

d = D()
d.display()
