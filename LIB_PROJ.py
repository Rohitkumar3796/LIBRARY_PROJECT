# CREATE A LIBRARY CLASS
import sys
class Library:

    def __init__(self,list_of_books): #here we use constructor, its called when an object is created
        self.available_book=list_of_books

    def display_book(self):
            print('these books are available in this library')
            for book in self.available_book:
                print(book)

    def lend_book(self,grant_book): #IF SOMEOME REQUEST TO TAKE BOOK
        if grant_book in self.available_book:
            print("THIS BOOK IS AVALABLE, YOU CAN TAKE IT")
        else:
            print("NOT AVAILABLE")


    def add_book(self, returned_book):  # here i use add book if someone returned bood so i will add in this list
            self.available_book.append(returned_book)
            print(returned_book,"thanks for returned book")


class Student:
    def request_book(self):
        self.book=input("enter the book name you want")
        return self.book

    def return_book(self):
        self.book=input("when do you want to return the book ")
        return self.book

if __name__ == '__main__':
    LIST_OF_BOOKS=["Science","Maths","Politics","Economics"]
    LIB=Library(LIST_OF_BOOKS)
    Rohit=Student()
    option = False
    while option==False:
        print("""
        1.DISPLAY BOOKS
        2.LEND BOOKS
        3.RETURN BOOKS
        4.EXIT
        """)
        choice = int(input("what would you like to do:"))
        if choice==1:
            LIB.display_book()
        elif choice==2:
            LIB.lend_book(Rohit.request_book())
        elif choice==3:
            LIB.add_book(Rohit.return_book())
        elif choice==4:
            sys.exit()



