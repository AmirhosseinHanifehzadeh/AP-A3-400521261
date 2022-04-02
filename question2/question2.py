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

class Library:
    @staticmethod
    def get(member_id, book_id):
        for member in LibraryMember.members:
            if member['id'] == member_id:
                if len(member['borrowedBooks']) > 4:
                    raise ValueError(f"MaxReached : {member['name']} {member['id']}")

                else:
                    for book in Book.books:
                        if book['id'] == book_id:
                            if book['count'] == 0:
                                raise ValueError(f"NotAvailable : {book['name']} {book['id']}")
                            else:
                                book['count'] -= 1
                                member['borrowedBooks'].append(book_id)
                                break
                    break

    @staticmethod
    def Return(member_id, book_id):
        for member in LibraryMember.members:
            if member['id'] == member_id:
                member['borrowedBooks'].remove(book_id)
                break
        for book in Book.books:
            if book['id'] == book_id:
                book['count'] += 1
                break