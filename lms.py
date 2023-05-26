# We will make a library management software where we will add functionalities like:
# 1. Showing the database of books available for borrowing
# 2. Allowing users to borrow a book from library and add the person's name, date of borrowing and borrowed book to booklending.txt file
# 3. Removing the borrowed book's name from the database and add it's name to borrowed.txt file
while True:
# MAIN MENU
    print("""
         WELCOME TO BOOKSVILLA - YOUR PERSONAL LIBRARY
    
         Please choose the desired option:
         1. Show Books Available
         2. Borrow a Book
         3. Return a Book
         4. Add a new Book to library
         5. Exit Library
         """)
    # we will take input from user and proceed further
    user_input = input("")
    if user_input == "1":
        # we will open the file and print the database of books available
        with open("books.txt", "r") as books_file:
            books_database = books_file.read()
            print(books_database)
        input("press enter to continue")
        continue
    
    elif user_input == "2":
        #we will take input of book name that user wants to borrow
        bookname = input("Enter Book name you want to borrow: ")
        bookname = bookname.upper()
        #now we will perform a check if that book is available or not in books.txt
        with open("books.txt", 'r') as books_file:
            lines = books_file.readlines()
            lines = [line.strip() for line in lines]
        # if book is available, then we'll remove it from list to lend it, so that database remains updated
        if bookname in lines:
            lines.remove(bookname)
            print("Book available")
        #if book is not available
        else:
            print("Book not available right now, Sorry!")
            input("press enter to continue")
            break
        with open("books.txt", "w") as books_file:
            books_file.writelines(line + '\n' for line in lines)
        # now we will take the input for users name and date on which he borrrows the book
        user_name = input("Enter your name: ")
        borrow_date = input("Enter the date: ")
        # now we will write the details in booklending.txt
        with open("booklending.txt", "a") as lending_details:
            lending_details.write(user_name + '\n' + borrow_date + '\n' + bookname + '\n')
            
            print("Book borrowed successfully, Happy reading!")
        # we will add the book that's borrowed to the borrowed.txt so that we know what books has been issued
        with open("borrowed.txt", 'a') as borrowed_data:
            borrowed_data.write(bookname + '\n')
        input("press enter to continue")
        continue
        
    
    elif user_input == "3":
        #we will take the input of the book person want's to return and delete the book name and details from boorrowed.txt
        returnbook = input("Enter the name of the book you want to return: ")
        returnbook = returnbook.upper()
        # we will open the list where books that are borrowed are listed and read its lines
        with open("borrowed.txt", 'r') as borrowed_list:
            lines = borrowed_list.readlines()
            lines = [line.strip() for line in lines]
        # we will search for the book in list and remove it as it has been returned
        if returnbook in lines:
            lines.remove(returnbook)
            print(returnbook + " has been returned, hope you enjoyed reading!")
        else:
            print("ERROR : No data about " + returnbook + " has been found")
        
        with open("borrowed.txt", 'w') as borrowed_list:
            borrowed_list.writelines(line + '\n' for line in lines)
        with open("books.txt", 'a') as books_file:
            books_file.write(returnbook + '\n')
        input("press enter to continue")
        continue
        
    elif user_input == "4":
        new_book = input("Write the name of the book you want to add: ")
        new_book = new_book.upper()
        with open("books.txt", 'a') as books_list:
            lines1 = books_list.writelines('\n' + new_book)
        print(new_book + " has been added to library.")
        input("press enter to continue")
        continue

    elif user_input == "5":
        print("Thank you for using BOOKSVILLA, Hope you enjoyed reading!")
        input("press enter to continue")
        break


