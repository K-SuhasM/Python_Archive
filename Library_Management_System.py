
class Library:
        no_of_books= 0
        i=0
        books = []
while True:
    print("What do you want to do?\n1. Total books.\n2. All books.\n3. Add a book.")
    choice=int(input("Choice: "))
    if choice not in (1,2,3): 
        raise ValueError("Enter a value.")

    if choice == 1:
        print(f"The total amount of books in the library is {Library.no_of_books}.")

    if choice == 2:
        print("Books in library: ")
        for i in Library.books:
            print(i)

    if choice== 3:
        addbook=input("Enter the name of book to add: ")
        Library.books.append(addbook)
        Library.no_of_books= Library.no_of_books+1
        print(f"Book \"{addbook}\" added successfully.")
