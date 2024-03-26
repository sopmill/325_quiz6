from abc import ABC, abstractmethod

# Define the Book class
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

# Interface for searching books
class SearchInterface(ABC):
    @abstractmethod
    def search_by_title(self, title):
        pass
    
    @abstractmethod
    def search_by_author(self, author):
        pass
    
    @abstractmethod
    def search_by_genre(self, genre):
        pass

# Interface for managing borrowing and returning of books
class BorrowingInterface(ABC):
    @abstractmethod
    def borrow_book(self, book):
        pass
    
    @abstractmethod
    def return_book(self, book):
        pass

# Interface for managing catalog operations (for librarian)
class CatalogManagementInterface(ABC):
    @abstractmethod
    def add_book(self, book):
        pass
    
    @abstractmethod
    def remove_book(self, book):
        pass

# Interface for generating reports (for librarian)
class ReportingInterface(ABC):
    @abstractmethod
    def generate_borrowings_report(self):
        pass
    
    @abstractmethod
    def generate_overdue_report(self):
        pass
    
    @abstractmethod
    def generate_popularity_report(self):
        pass

# Library class implementing the interfaces
class Library(SearchInterface, BorrowingInterface, CatalogManagementInterface, ReportingInterface):
    def __init__(self):
        # Initialize library attributes
        self.catalog = []
        self.borrowed_books = []

    def add_book(self, book):
        self.catalog.append(book)
        print(f"Book '{book.title}' added to catalog.")

    def remove_book(self, book):
        if book in self.catalog:
            self.catalog.remove(book)
            print(f"Book '{book.title}' removed from catalog.")
        else:
            print("Book not found in catalog.")

    def search_by_title(self, title):
        return [book for book in self.catalog if book.title == title]

    def search_by_author(self, author):
        return [book for book in self.catalog if book.author == author]

    def search_by_genre(self, genre):
        return [book for book in self.catalog if book.genre == genre]

    def borrow_book(self, book):
        if book in self.catalog:
            self.borrowed_books.append(book)
            self.catalog.remove(book)
            print(f"Book '{book.title}' borrowed.")
        else:
            print("Book not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.catalog.append(book)
            self.borrowed_books.remove(book)
            print(f"Book '{book.title}' returned.")
        else:
            print("Book not borrowed by any user.")

    def generate_borrowings_report(self):
        print("Generating borrowings report...")

    def generate_overdue_report(self):
        print("Generating overdue report...")

    def generate_popularity_report(self):
        print("Generating popularity report...")

# Example usage
if __name__ == "__main__":
    # Creating library object
    library = Library()

    # Adding books to the catalog
    python_book = Book("Matilda", "Ronald Dhal", "Story")
    algorithms_book = Book("The Missing Piece", "Shel Silverstien", "Poetry")
    library.add_book(python_book)
    library.add_book(algorithms_book)

    # Searching for books
    print(library.search_by_author("John Smith"))

    # Borrowing and returning books
    library.borrow_book(python_book)
    library.return_book(python_book)

    # Generating reports
    library.generate_borrowings_report()
    library.generate_overdue_report()
    library.generate_popularity_report()
