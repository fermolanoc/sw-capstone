"""
Author: Fernando Molano

Program to define an Author class and some basic methods to manage their published books
Each Author instance will have an empty list of books by default.
"""


class Author:
    def __init__(self, name):
        self.name = name
        self.books = []  # empty list of published books by default

    def published(self, title):
        self.books.append(title)  # add a book title to the books list

    def __str__(self):
        # separate each book title by comma or print default message if no books on list
        titles = ', '.join(self.books) or 'No published books'
        return f'{self.name}. Books: {titles}'


def main():
    # Create instances of Author
    marquez = Author("Gabriel Garcia Marquez")
    brown = Author("Dan Brown")
    rowling = Author("J.K. Rowling")

    # Add books to some authors
    marquez.published("Cien años de soledad")
    marquez.published("El coronel no tiene quien le escriba")
    rowling.published("The Cuckoo's Calling")

    # Show authors names and their books if any
    print(marquez)
    print(brown)
    print(rowling)


main()
