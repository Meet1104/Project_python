class Counter :

    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count += 1

    def display(self):
        print(f"{self.count}")


c = Counter()

c.display()

c.increment()

c.display()

c.increment()

c.display()