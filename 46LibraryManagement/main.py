#Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!

class Library:
    def __init__(self):
        self.noBooks = 0
        self.Books = []

    def addBook(self, Book):
        self.Books.append(Book)
        self.noBooks = len(self.Books)

    def showinfo(self):
        print(f"The library has {self.noBooks} Books and the books are : ")
        for Book in self.Books:
            print(Book)


l1 = Library()
l1.addBook("Endgame"*5)
l1.addBook("Endgame1")
l1.addBook("Endgame2")
l1.addBook("Endgame3")
l1.addBook("Endgame4")
l1.addBook("Endgame5")
l1.addBook("Endgame6")
l1.showinfo()