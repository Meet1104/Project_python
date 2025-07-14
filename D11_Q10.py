class PersonAge:
    def __init__(self):
        self.__age = 0

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

    def get_age(self):
        return self.__age

pa = PersonAge()
pa.set_age(25)
print("Age:", pa.get_age())