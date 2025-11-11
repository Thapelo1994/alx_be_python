# First, define the classes with inheritance
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """Returns a human-readable string representation of the book."""
        return f'"{self.title}" by {self.author}' #

class PrintBook(Book):
    def __init__(self, title, author, weight):
        super().__init__(title, author)
        self.weight = weight
        
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

# Create some objects (instances)
book_instance = Book("Generic Title", "Generic Author")
print_book_instance = PrintBook("Print Title", "Print Author", 1.5)
ebook_instance = EBook("Ebook Title", "Ebook Author", 2.1)
not_a_book = "I am a string"

# The check using isinstance()
# It returns True if the object is an instance of Book or any class derived from Book
print(f"Is book_instance a Book or derived? {isinstance(book_instance, Book)}")
print(f"Is print_book_instance a Book or derived? {isinstance(print_book_instance, Book)}")
print(f"Is ebook_instance a Book or derived? {isinstance(ebook_instance, Book)}")
print(f"Is not_a_book a Book or derived? {isinstance(not_a_book, Book)}")

# You can also check against a specific list of derived classes if needed
print(f"Is print_book_instance PrintBook or EBook? {isinstance(print_book_instance, (PrintBook, EBook))}")
