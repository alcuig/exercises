class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []

library_1 = Library("Alyssa Library", "Aldgate East")


class Person: 
    def __init__(self, name, nationality, gender):
        self.name = name
        self.nationality = nationality
        self.gender = gender
    
class Book:
    def __init__(self, name, genre, pages, authors):
        self.name = name
        self.genre = genre
        self.pages = pages
        self.authors = authors
        self.is_borrowed = False
        self.borrowed_by = None

    
    def list_authors(self):
        string_authors = ""
        for author in self.authors:
            string_authors = string_authors + author.name + ", "
        return string_authors[:-2]

    def rent_book (self, borrower: Person):
        self.is_borrowed = True
        self.borrowed_by = borrower

    def list_borrower_details(self):
        return f"This book has been borrowed by {self.borrowed_by.name}. He is {self.borrowed_by.nationality}, and is {self.borrowed_by.gender}."


class Author(Person):
    def __init__(self, name, nationality, gender):
        super().__init__(name, nationality, gender)
        self.bibliography = []

    def add_book_to_bibliography(self, book: Book) -> None:
        assert type(book) == Book, f"book needs to be of type 'Book', but is of type {type(book)}."
        self.bibliography.append(book)
    
    def list_bibliography(self):
        list_of_book_names = []
        for book in self.bibliography: 
            list_of_book_names.append(book.name)
        return list_of_book_names 


author_1 = Author("J.R.R. Tolkien", "british", "male")
author_2 = Author("Alyssa Cuignet", "british", "female")

book_1 = Book("Return of the King", "Fantasy", 1000, [author_1, author_2] )
book_2 = Book("The Hobbit", "Fantasy", 450, [author_1, author_2])

author_1.add_book_to_bibliography(book_2)
author_1.add_book_to_bibliography(book_1)



person_1=Person("Louis Alecu", "soon to be british", "non-binary")
print(person_1)
print(vars(person_1))
person_2 = Person ("Victoire de Brosses", "french", "female")

print(book_1.borrowed_by)
book_1.rent_book(person_1)
print(book_1.borrowed_by)
print(book_1.borrowed_by.name)


         