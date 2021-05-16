class library:
    def __init__(self,list,name):
        self.booklist= list
        self.name = name 
        self.lendict= {}

    def show_dict(self):
        for key,value in self.lendict:
            return key,value


    def display_book(self):
        print(f"The following book is avaliablein the {self.name} Library")
        for book in self.booklist:
            print(book) 

    def lend_book(self,book,user):
        if book not in self.lendict.keys():
            self.lendict.update({book:user})
            print("Database has been updated")
        else:
            print(f"The book is already own by{self.lendict[book]}")


    def add_book(self,book):
        self.booklist.append(book)
        print("Book has been updated")  



    def return_book(self,book):
        self.lendict.pop(book)


if __name__ == "__main__":

    while(True):
        Aditya = library(["python", "c++", "c", "DSA", "java",], "Programers's Library")
        Aditya.show_dict()


        print(f"WElcome to the {Aditya.name}")
        print("1. Display Book")
        print("2. Lend Book")
        print("3. Add Book")
        print("4. Return Book")
        print("5. Show the dictniory")

        user_choice = int(input("Enter your choice :"))
        if user_choice == 1:
            Aditya.display_book()

        elif user_choice == 2:
            book = input("Enter the book name:")
            user = input("Enter your name :")
            Aditya.lend_book(book,user)



        elif user_choice == 3:
            book = input("Enter the book name You want to addd:")
            Aditya.add_book(book)


        elif user_choice == 4:
            book = input("Enter the book you want to return :")
            Aditya.return_book(book)


        elif user_choice == 5:
            Aditya.show_dict()
        else:
            print("Enter a valid option")


   
        




