class Book:
    def __init__(self, type, title, author):
        self.type = type
        self.title = title
        self.author = author
    
    def display_info(self):
        print(f"Type: {self.type}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


my_book = Book("Fiction", "1984", "George Orwell")
my_book.display_info()
my_book = Book("self help", "Let them theory", "Mel Robbins")
my_book.display_info()
my_book = Book("inspiration", "psycology of money", "Coleman")
my_book.display_info()
