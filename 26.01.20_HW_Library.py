

from typing import override


class Book:
    def __init__(self, book_name, book_author, isbn_number, issue_year):
        self.name = book_name
        self.author = book_author
        self.isbn = isbn_number
        self.year = issue_year
        self.available = "Available"


    def __str__(self):
        return (f"{self.name} from {self.author}, ISBN: {self.isbn}, Year: {self.year}, {self.available}\n")


    def borrow_book(self, isbn_num):
        pass


    def return_book(self, isbn_num):
        pass




class Library(Book):
    def __init__(self, library_name):
        library_name = library_name
        self.books = []


    @override
    def borrow_book(self, isbn_num):
        for book in self.books:
            if book.isbn == isbn_num and book.available == "Available":
                book.available = "Unavailable"


    @override
    def return_book(self, isbn_num):
        for book in self.books:
            if book.isbn == isbn_num and book.available == "Unavailable":
                book.available = "Available"


    def add_book(self, book):
        self.books.append(book)


    def search_book(self, book_name):
        for book in self.books:
            if book.name == book_name:
                return book


    def display_books(self):
        for book in self.books:
            if book.available == "Available":
                print(f"{book.name} from {book.author}\nISBN: {book.isbn}\nYear: {book.year}\n{book.available}\n")


    def print_book(self, book):
        print(f"{book.name} from {book.author}\nISBN: {book.isbn}\nYear: {book.year}\n{book.available}\n")


####################################################

book1 = Book("Harry Potter", "Rowling", 123, 2010)
book2 = Book("Lord of Rings", "Tolkien", 321, 2003)
book3 = Book("Anne of Green Gables", "Lucy Maud Montgomery", 222, 1908)

library = Library("Library Bratislava")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.borrow_book(123)
print(book1)
print(book2)
print("----------")
library.display_books()

