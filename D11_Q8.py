class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

b = Book("Python", "Guido")
print(b.get_title(), b.get_author())