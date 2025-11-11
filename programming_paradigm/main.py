from library_management import Book, Library

def main():
    library = Library()

    # Add books
    book1 = Book("Brave New World", "Aldous Huxley")
    book2 = Book("1984", "George Orwell")

    library.add_book(book1)
    library.add_book(book2)

    library.list_available_books()

    # Check out a book
    library.check_out_book("1984") # Check out another book
    library.list_available_books()

    # Try to check out an already checked out book
    library.check_out_book("1984")

    # Return a book
    library.return_book("1984")
    library.list_available_books()



if __name__ == "__main__":
    main()
