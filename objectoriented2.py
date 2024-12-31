class library:
    def __init__(self,list,name):
        self.list=list
        self.name=name
        self.lendDict= {}
    def display_books(self):
        print(f"We have these books in the library:{self.name}")
        for book in self.list:
            print(book)
    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-book database has been updated .You may take the book now.")
        else:
            print("This book is already in use.")
    def addBook(self,book):
        self.list.append(book)
        print("Book has been added to the list.")
    def returnBook(self,book):
        self.lendBook.pop(book)


if __name__ == "__main__":
    books = library(['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "Let's Upskill")
    while(True):
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice=input()
        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            books.display_books()
        elif user_choice == 2:
            input("Enter the name of the book you want to lend: ")
            user=input("Enter your name")
            books.lendBook (user, book)
        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: ")
            books.addBook (book)
        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            books.returnBook(book)

        else:
            print("Not a valid option!")

        print("Press q to quit and c to continue.")
        user_choice2 = ""
        while (user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue