class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author 

    def get_title(self):
        return 'Title: ' + self.title

    def get_author(self):
        return "Author: " + self.author

PP = Book('Pride and Prejudice', 'Jane Austen')
H = Book('Hamlet', 'William Shakespeare')
WP = Book('War and Peace', 'Leo Tolstoy')
HP = Book('Harry Potter', 'J.K. Rowling')

print(HP.title) 
print(HP.author)
print(HP.get_title())
print(HP.get_author())