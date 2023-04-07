class Library:
    def __init__(self, *books):
        self.__books = list(books)
        self.__issuedBooks = []
        self.updateIssuedBooks()

    def updateBooks(self):
        with open("issuedBooks.txt", "w") as f:
            for book in self.__issuedBooks:
                f.write(f"{book},")

    def updateIssuedBooks(self, book="", i=0):
        if i == -1:
            self.__issuedBooks.append(book)
            self.updateBooks()
        elif i == 1:
            self.__issuedBooks.remove(book)
            self.updateBooks()

        else:
            with open("issuedBooks.txt", "r") as f:
                line = f.readline().rstrip()
                books = line.split(",")[:-1]
                self.__issuedBooks = books

        for book in self.__issuedBooks:
            if book in self.__books:
                self.__books.remove(book)

    def displayIssuedBooks(self):
        print(f"Value of __issuedBooks attribute: {self.__issuedBooks}")
        if self.__issuedBooks:
            print("Issued Books: ")
            for i, book in enumerate(self.__issuedBooks):
                print(f"{i}. {book}")
        else:
            print("No books have been issued yet.")

            # for i, book in enumerate(self.__issuedBooks):
            #     print(f"{i}. {book}")

    def displayAvailableBooks(self):
        print("Available Books:")
        for i, book in enumerate(self.__books):
            print(f"{i}. {book}")

    def lendBook(self, requestedBook):
        if requestedBook in self.__books:
            print("You have now borrowed the book")
            self.__books.remove(requestedBook)
            self.updateIssuedBooks(requestedBook, -1)

        else:
            print("Sorry, the book is not available in our list")

    def addBook(self, returnedBook):
        self.__books.append(returnedBook)
        self.updateIssuedBooks(returnedBook, 1)
        print("You have returned the book. Thank you!")


class Customer:
    def requestBook(self):
        self.__book = input("Enter the name of a book you would like to borrow: ")
        return self.__book

    def returnBook(self):
        self.__book = input("Enter the name of the book which you are returning: ")
        return self.__book


def main():
    library = Library(
        "Think and Grow Rich", "Who Will Cry When You Die", "For One More Day"
    )
    customer = Customer()
    done = False
    while done == False:
        print(
            """
        ======LIBRARY MENU=======
        1. Display all available books
        2. Request a book
        3. Return a book
        4. See Issued Books
        5. Exit
        """
        )
        choice = int(input("Enter Choice: "))
        if choice == 1:
            library.displayAvailableBooks()
        elif choice == 2:
            library.lendBook(customer.requestBook())
        elif choice == 3:
            library.addBook(customer.returnBook())
        elif choice == 4:
            library.displayIssuedBooks()
        elif choice == 5:
            done = True


if __name__ == "__main__":
    main()
