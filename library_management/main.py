class Book:
    library_name = "City Library"

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def display_info(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author}, ISBN: {self.isbn} - {status}"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}'.")

    def display_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has not borrowed any books.")
        else:
            print(f"{self.name} has borrowed:")
            for book in self.borrowed_books:
                print(f"-- {book.display_info()}")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, isbn):
        book_to_remove = None
        for book in self.books:
            if book.isbn == isbn:
                book_to_remove = book
                break
        if book_to_remove:
            if book_to_remove.is_borrowed:
                print(f"Cannot remove '{book_to_remove.title}' because it is currently borrowed.")
            else:
                self.books.remove(book_to_remove)
                print(f"Book '{book_to_remove.title}' removed from the library.")
        else:
            print(f"No book with ISBN '{isbn}' found.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered in the library.")

    def remove_member(self, member_id):
        member_to_remove = None
        for member in self.members:
            if member.member_id == member_id:
                member_to_remove = member
                break
        if member_to_remove:
            if member_to_remove.borrowed_books:
                print(f"Cannot remove member '{member_to_remove.name}' because they have borrowed books.")
            else:
                self.members.remove(member_to_remove)
                print(f"Member '{member_to_remove.name}' removed from the library.")
        else:
            print(f"No member with ID '{member_id}' found.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in library:")
            for book in self.books:
                print(f"-- {book.display_info()}")

    def display_members(self):
        if not self.members:
            print("No members in the library.")
        else:
            print("Members:")
            for member in self.members:
                print(f"-- {member.name} (ID: {member.member_id})")

    def search_books_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            print(f"Books matching title '{title}':")
            for book in found_books:
                print(f"-- {book.display_info()}")
        else:
            print(f"No books found matching title '{title}'.")

    def search_books_by_author(self, author):
        found_books = [book for book in self.books if author.lower() in book.author.lower()]
        if found_books:
            print(f"Books by author '{author}':")
            for book in found_books:
                print(f"-- {book.display_info()}")
        else:
            print(f"No books found by author '{author}'.")

    def display_borrowed_books(self):
        borrowed = [book for book in self.books if book.is_borrowed]
        if not borrowed:
            print("No books are currently borrowed.")
        else:
            print("Borrowed books:")
            for book in borrowed:
                print(f"-- {book.display_info()}")

    def is_book_available(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    print(f"Book '{book.title}' is currently borrowed.")
                else:
                    print(f"Book '{book.title}' is available.")
                return
        print(f"No book with ISBN '{isbn}' found.")

    def display_member_borrowed_books(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                member.display_borrowed_books()
                return
        print(f"No member with ID '{member_id}' found.")


def main():
    library = Library()
    member_id_counter = 1

    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Add Member")
        print("4. Remove Member")
        print("5. Search Books by Title")
        print("6. Search Books by Author")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. Display All Books")
        print("10. Display All Members")
        print("11. Display Borrowed Books")
        print("12. Display Member's Borrowed Books")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            isbn = input("Enter ISBN: ").strip()
            library.add_book(Book(title, author, isbn))

        elif choice == "2":
            isbn = input("Enter ISBN of book to remove: ").strip()
            library.remove_book(isbn)

        elif choice == "3":
            name = input("Enter member name: ").strip()
            library.add_member(Member(name, member_id_counter))
            member_id_counter += 1

        elif choice == "4":
            try:
                member_id = int(input("Enter member ID to remove: ").strip())
                library.remove_member(member_id)
            except ValueError:
                print("Invalid member ID.")

        elif choice == "5":
            title = input("Enter title keyword to search: ").strip()
            library.search_books_by_title(title)

        elif choice == "6":
            author = input("Enter author keyword to search: ").strip()
            library.search_books_by_author(author)

        elif choice == "7":
            try:
                member_id = int(input("Enter member ID: ").strip())
                isbn = input("Enter ISBN of book to borrow: ").strip()

                member = next((m for m in library.members if m.member_id == member_id), None)
                book = next((b for b in library.books if b.isbn == isbn), None)

                if member and book:
                    member.borrow_book(book)
                else:
                    if not member:
                        print("Member not found.")
                    if not book:
                        print("Book not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "8":
            try:
                member_id = int(input("Enter member ID: ").strip())
                isbn = input("Enter ISBN of book to return: ").strip()

                member = next((m for m in library.members if m.member_id == member_id), None)
                book = next((b for b in library.books if b.isbn == isbn), None)

                if member and book:
                    member.return_book(book)
                else:
                    if not member:
                        print("Member not found.")
                    if not book:
                        print("Book not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "9":
            library.display_books()

        elif choice == "10":
            library.display_members()

        elif choice == "11":
            library.display_borrowed_books()

        elif choice == "12":
            try:
                member_id = int(input("Enter member ID: ").strip())
                library.display_member_borrowed_books(member_id)
            except ValueError:
                print("Invalid member ID.")

        elif choice == "0":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number from 0 to 12.")


if __name__ == "__main__":
    main()
