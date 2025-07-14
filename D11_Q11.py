class Student:
    def __init__(self, name, m1, m2, m3):
        self.__name = name
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3

    def calculate_average(self):
        return (self.__m1 + self.__m2 + self.__m3) / 3

    def display_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        else:
            grade = "D"
        print(f"{self.__name}'s Grade: {grade}")

s = Student("Rahul", 85, 90, 80)
print("Average:", s.calculate_average())
s.display_grade()