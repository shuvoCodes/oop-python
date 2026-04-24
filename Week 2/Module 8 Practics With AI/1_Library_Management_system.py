# 1 Library Management System
#Library DataBase Class

class LibraryDatabase:
    book_list = []

    @classmethod
    def add_book(cls,obj):
        cls.book_list.append(obj)

    @classmethod
    def view_all_book(cls):
        for book in cls.book_list:
            view = Book.view_all_info(book)
            print(view)
    
class Book:
    def __init__(self,book_id,title,author,is_available = True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__available = is_available

        LibraryDatabase.add_book(self)

    @classmethod
    def view_all_info(cls,book):
        return f'Book ID: {book.__book_id}, Title: {book.__title}, Author: {book.__author}, Available: {book.__available}'
    
    @classmethod
    def issue_book(self,id):
        for book in LibraryDatabase.book_list:
            if book.__book_id == id:    
                if book.__available:
                    book.__available = False
                    print(f'Take Your Book.Book Id: {book.__book_id}, Name: {book.__title}, Author: {book.__author}')
                else:
                    raise Exception('This Book is not available.')
            
    @classmethod    
    def return_book(cls,id):
         for book in LibraryDatabase.book_list:
            if book.__book_id == id:        
                if book.__available:
                    raise Exception('This Book is Alrady Returned.')
                else:
                    book.__available = True
                    print('Thank\'s for Return The Book')


# Book List
 
b1 = Book(101,'Python Basics','John Smith')
b2 = Book(102,'Data Structures','Mark Allen')
b3 = Book(103,'Machine Learning Basics','Andrew Ng')
b4 = Book(104,'Clean Code','Robert C. Martin')
b5 = Book(105,'Artificial Intelligence','Stuart Russell')

while True:

    # Manu System

    print('\n----------Library Management System----------\n')
    print('1. View All Books')
    print('2. Issue Book')
    print('3. Return Book')
    print('4. Exit')

    try:
        choose = int(input('Enter Your Selected Option Number: '))
        if choose == 1:
            LibraryDatabase.view_all_book()
        elif choose == 2:
            id = int(input('Enter The Book Id: '))
            Book.issue_book(id)
        elif choose == 3:
            id = int(input('Enter The Book Id: '))
            Book.return_book(id)
        elif choose == 4:
            break
        else:
            raise Exception('Invalid Number You Selected')
        
    except Exception as ve:
        print('Error: ', ve)