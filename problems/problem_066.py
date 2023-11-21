# Write a class that meets these requirements.
#
# Name:       Book
#
# Required state:
#    * author name, a string
#    * title, a string
#
# Behavior:
#    * get_author: should return "Author: «author name»"
#    * get_title:  should return "Title: «title»"
#
# Example:
#    book = Book("Natalie Zina Walschots", "Hench")
#
#    print(book.get_author())  # prints "Author: Natalie Zina Walschots"
#    print(book.get_title())   # prints "Title: Hench"
#
# There is pseudocode availabe for you to guide you

class Book:
    def __init__(self, author_name, book_title):
        self.get_author = print(f"Author: {author_name}")
        self.get_title = print(f"Title: {book_title}")


book = Book("Natalie Zina Walschots", "Hench")
book.get_author
book.get_title
