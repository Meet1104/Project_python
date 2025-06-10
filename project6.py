print("Welcome to Personal Journal Manager! ")

class Filehandling:
    def __init__(self,filename,filemode):
        self.filename = filename
        self.filemode = filemode
        self.file = open(self.filename, self.filemode)
    
def Entry():
    with open("journal.txt", "a") as file:
        date = input("Write your journal entry date:\n")
        time = input("Write your journal entry time:\n")    
        entry = input("Write your journal entry:\n")
        file.write(f"{date} :{time} :{entry}\n")
    print("Entry added successfully.\n")



def Read():
    try:
        with open("journal.txt", "r") as file:
            print("\nYour Journal Entries:\n")
            print(file.read())
    except FileNotFoundError:
        print("No journal entries found.")


def search():
    word = input("Enter a word: ")
    with open("journal.txt", "r") as file:
        for i in file:
            if word == i:
                print(i)


def delete():
    confirm = input("Are you sure you want to delete all entries? (yes/no): ")
    if confirm == "yes":
        with open("journal.txt", "w") as file:
            pass
        print("All entries have been deleted.\n")
    

while True :
    print("\nPlease Select an option: \n")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit\n")

    choose = int(input("User Input: "))

    match choose :
        case 1:
            Entry()
        case 2:
            Read()
        case 3:
            search()
        case 4:
            delete()
        case 5:
            print("Thank you for using Personal Journal Manager. Goodbye! ")
            break
        case _:
            print("Invaild option.Please Select a valid option from the menu.")
