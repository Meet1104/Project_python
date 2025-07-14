class animal:
    def __init__(self):
        self.name = input("Enter animal name : ")
    
    def getdata(self):
        print(f"Animal : {self.name}")

a1 = animal()
a2 = animal()

a1.getdata()
a2.getdata()

