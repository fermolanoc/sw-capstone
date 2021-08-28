"""
Author: Fernando Molano
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def published(self, title):
        self.books.append(title)

    def __str__(self):
        titles = ', '.join(self.books) or 'No published books'
        return f'{self.name}. Books: {titles}'


def main():
    marquez = Author("Gabriel Garcia Marquez")
    brown = Author("Dan Brown")
    rowling = Author("J.K. Rowling")

    marquez.published("Cien años de soledad")
    marquez.published("El coronel no tiene quien le escriba")
    rowling.published("The Cuckoo's Calling")

    print(marquez)
    print(brown)
    print(rowling)


main()
