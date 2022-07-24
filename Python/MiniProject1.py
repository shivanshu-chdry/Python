#Library Management System

print('Welcome to Library Management System')
class Library:
    books = {}
    def __init__(self,lsb,lname):
        self.lname = lname
        self.lsb = lsb

    def display_book(self):
        print(f"Available books are: {self.lsb}")

    def add_book(self):
       a = input("Enter the name of the book you want to donate")
       self.lsb.append(a)
       print('Thanks! The book is successfully added to our library')


    def lend(self):
        book_name = input("Enter the name of the book you want to lend")
        user_name = input("Please enter your name")
        if book_name in self.lsb:
            print(f'{user_name} you have lended {book_name} successfully!')
            self.lsb.remove(book_name)
            self.books.update({book_name:user_name})

        elif book_name in self.books.keys() :
            a = self.books[book_name]
            print(f"book is already lended to {a} ")
        else :
            print("This book is not available in our library")



    def return_book(self):
        a = input("Please enter the name of the book you want to return")
        if a in self.books:
            self.lsb.append(a)
            del self.books[a]
            print('Thanks for returning the book!')
        else:
            print('The book is not lent yet!')
            
Shivanshu_Library = Library(["Wings of Fire","Data Structures And Algorithms","Brief Answers To Big Questions","The Invisible Man"],"harry library")

def main():
    while True :
        user_in = input('1. Display Book \n2. Add Book \n3. Lend Book \n4. Return Book\n')
        if user_in == "1":
            Shivanshu_Library.display_book()

        elif user_in == "2" :
            Shivanshu_Library.add_book()

        elif user_in == "3":
            Shivanshu_Library.lend()

        elif user_in == "4":
            Shivanshu_Library.return_book()

        else:
            print("Invalid Input!")

main()
