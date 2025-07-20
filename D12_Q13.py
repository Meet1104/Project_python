def outer(length, breadth):
    def area_rectangle():
        return length * breadth

    def area_square():
        return length * length

    print("Rectangle area:", area_rectangle())
    print("Square area:", area_square())

outer(5, 3)
