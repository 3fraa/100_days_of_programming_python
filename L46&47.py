#Sol of Q1:
print("Sol of Q1:")
class Library:
    def __init__(self, book, shelf):
        self.numOfBook = book
        self.nomOfRow = shelf
myObject = Library(300,45)
print()

#Sol of Q2:
print("Sol of Q2:")
class science_section(Library):
    def __init__(self, book, shelf, name):
        super().__init__(book, shelf)
        self.name = name
x = science_section(300, 45, "Physics_books")
print(" The number of books in the library is:" , x.numOfBook, "\n",
      "The rows number of books in the library is:", x.nomOfRow, "\n",
      "and The book name is:", x.name)
print()

#Sol of Q3:
print("Sol of Q3:")
x.numOfBook = 20
x.nomOfRow = 4
print(" The number of books in the library is:" , x.numOfBook, "\n",
      "The rows number of books in the library is:", x.nomOfRow, "\n",
      "and The book name is:", x.name)
print()
