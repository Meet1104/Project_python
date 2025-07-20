class Teacher:
    def teach(self):
        print("Teaching subjects.")

class Administrator:
    def manage(self):
        print("Managing the school.")

class Headmaster(Teacher, Administrator):
    def lead(self):
        print("Leading the school.")

hm = Headmaster()
hm.teach()
hm.manage()
hm.lead()
