class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Already checked out

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Not checked out

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        status = "Available" if self.is_available() else "Checked Out"
        return f"'{self.title}' by {self.author} ({status})"

class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        if not isinstance(book, Book):
            print("Error: Only Book objects can be added to the library.")
            return
        self._books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Book '{title}' checked out successfully.")
                    return True
                else:
                    print(f"Book '{title}' is already checked out.")
                    return False
        print(f"Book '{title}' not found in the library.")
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Book '{title}' returned successfully.")
                    return True
                else:
                    print(f"Book '{title}' was not checked out.")
                    return False
        print(f"Book '{title}' not found in the library.")
        return False

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            print("\nAvailable Books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("\nNo books currently available in the library.")
