class Library:
    def __init__(self, books):
        self.__books = books

    def displayAvailableBooks(self):
        print("Available Books:")
        for book in self.__books:
            print(book)
