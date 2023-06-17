#-------------------------------Rohit Singh--------------------------------------


def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    borrower = input("Enter the borrower's name: ")

    with open("library_database.txt", "a") as file:
        file.write(f"{title},{author},{borrower}\n")
    print("Book added successfully!\n")


def display_books():
    
        try:
            with open("library_database.txt", "r") as file:
            
                for line in (file):
                    title, author, borrower = line.strip().split(",")
                    print(f"\nTitle: {title}\nAuthor: {author}\nBorrower: {borrower}\n")
        except:
            print('Currently no Book in the Database')

def main_menu():
    print("Welcome to the Book Borrowing Database!")
    while True:
        print("\nMain Menu:")
        print("1. Add a book")
        print("2. Display all books")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
