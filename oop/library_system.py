# First, define the classes with inheritance
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class PrintBook(Book):
    def __init__(self, title, author, weight):
        super().__init__(title, author)
        self.weight = weight

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

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
