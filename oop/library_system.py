# First, define the classes with inheritance
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a human-readable string representation of the book."""
        return f'"{self.title}" by {self.author}' #

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
        
     # Add the __str__ method here
    def __str__(self):
        # Calls the parent Book's __str__ and appends specific details
        base_str = super().__str__()
        return f"{base_str} | Print Book - {self.pages} pages, {self.weight}g"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    
    # Add the __str__ method here
    def __str__(self):
        # Calls the parent Book's __str__ and appends specific details
        base_str = super().__str__()
        return f"{base_str} | EBook - {self.file_size}MB, format: {self.file_format}"
    

class Library:
    def __init__(self):
        self.books = []  # Composition: Library "has a" list of books

    def add_book(self, book):
        """Adds a Book, EBook, or PrintBook instance to the library."""
        if isinstance(book, Book):  # Ensures only valid book types are added
            self.books.append(book)
        else:
            print("Error: Only Book, EBook, or PrintBook instances can be added.")

    def list_books(self):
        """Prints details of each book in the library."""
        if not self.books:
            print("The library is empty.")
            return

        print("\n--- Library Collection ---")
        for book in self.books:
            print(book.get_details())
        print("--------------------------")