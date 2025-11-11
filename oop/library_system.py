class Book:
    """Base class for all books."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def get_details(self) -> str:
        """Returns a string with the basic details of the book."""
        return f"'{self.title}' by {self.author}"

class EBook(Book):
    """Derived class for electronic books."""
    def __init__(self, title: str, author: str, file_size: int):
        # Call the base class constructor
        super().__init__(title, author)
        self.file_size = file_size  # additional attribute

    def get_details(self) -> str:
        """Returns a string with EBook specific details."""
        base_details = super().get_details()
        return f"{base_details} [EBook, Size: {self.file_size}KB]"

class PrintBook(Book):
    """Derived class for print books."""
    def __init__(self, title: str, author: str, page_count: int):
        # Call the base class constructor
        super().__init__(title, author)
        self.page_count = page_count  # additional attribute

    def get_details(self) -> str:
        """Returns a string with PrintBook specific details."""
        base_details = super().get_details()
        return f"{base_details} [Print Book, Pages: {self.page_count}]"

class Library:
    """Class demonstrating composition by managing a collection of books."""
    def __init__(self):
        # The 'books' list is a composition of Book objects
        self.books = []

    def add_book(self, book: Book):
        """Adds a Book, EBook, or PrintBook instance to the library."""
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added book: '{book.title}'")
        else:
            print("Invalid book type.")

    def list_books(self):
        """Prints details of each book in the library."""
        print("\n--- Current Library Collection ---")
        if not self.books:
            print("The library is empty.")
        for book in self.books:
            # Polymorphism in action: calling get_details() on each object
            print(book.get_details())
        print("----------------------------------")

