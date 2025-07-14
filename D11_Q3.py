class person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created.")

obj1 = person("Meet")
del obj1

obj2 = person("Jay")
del obj2

obj3 = person("Hello")
del obj3
