from abc import ABC, abstractmethod

# Book class (Encapsulation)
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True  # Book is available by default

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

# Library class (Encapsulation & Abstraction)
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("\nAvailable Books in the Library:")
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"{book} - {status}")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.is_available:
                book.is_available = False
                return book
        return None

    def return_book(self, book):
        book.is_available = True

# Abstract Member class (Abstraction)
class Member(ABC):
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    @abstractmethod
    def borrow_book(self, library, isbn):
        pass

    @abstractmethod
    def return_book(self, library, book):
        pass

# Student class (Inheritance & Polymorphism)
class Student(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self.borrowed_books = []

    def borrow_book(self, library, isbn):
        if len(self.borrowed_books) < 2:  # Students can borrow up to 2 books
            book = library.borrow_book(isbn)
            if book:
                self.borrowed_books.append(book)
                print(f"{self.name} borrowed {book}")
            else:
                print("Book not available!")
        else:
            print("Students can only borrow up to 2 books.")

    def return_book(self, library, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            library.return_book(book)
            print(f"{self.name} returned {book}")
        else:
            print("This book was not borrowed by you.")

# Teacher class (Inheritance & Polymorphism)
class Teacher(Member):
    def __init__(self, name, member_id):
        super().__init__(name, member_id)
        self.borrowed_books = []

    def borrow_book(self, library, isbn):
        book = library.borrow_book(isbn)  # Teachers can borrow unlimited books
        if book:
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed {book}")
        else:
            print("Book not available!")

    def return_book(self, library, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            library.return_book(book)
            print(f"{self.name} returned {book}")
        else:
            print("This book was not borrowed by you.")
