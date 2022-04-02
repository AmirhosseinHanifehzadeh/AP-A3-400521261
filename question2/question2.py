class Book:
    books = list()
    def __init__(self, name, id, count):
        self.book_name = name 
        self.book_id = id
        self.count = count
        Book.books.append({
            'id':id,
            'name':name,
            'count':int(count)
        })

    
    def addBook(self, id, name, count):
        Book.books.append({
            'id': id, 
            'name': name,
            'count': int(count)
        })


class LibraryMember:
    members = list()

    @classmethod
    def addMember(cls, id, name):
        cls.members.append({ 
            'id':id,
            'name':name,
            'borrowedBooks': list()
        })
    @classmethod
    def memberstat(cls):
        print('----------------------------------------------------------')
        for member in cls.members:
            print(f"{member['name']} {member['id']}")
            for borrowedBook in member['borrowedBooks']:
                print(f"\t- {borrowedBook['name']} {borrowedBook['id']}")
        print('----------------------------------------------------------')

