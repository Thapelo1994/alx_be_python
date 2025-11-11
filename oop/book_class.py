# book_class.py

class Book:
    """
    Represents a book with a title, author, and publication year.
    Implements magic methods for initialization, deletion, and string representation.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Initializes the Book instance with title, author, and year.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor that prints a message upon object deletion.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns a human-readable string representation of the book.
        Format: "(title) by (author), published in (year)"
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official string representation that can recreate the object.
        Format: f"Book('{self.title}', '{self.author}', {self.year})"
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

