from book import Book
import os

MAIN_HEADING = 'Main'
LIBRARIAN_HEADING = 'Librarian'
MAIN_MENU = {1: 'Search for books', 2: 'Borrow a book', 3: 'Return a book', 0: 'Exit the system'}
LIBRARIAN_MENU = {1: 'Search for books', 2: 'Borrow a book', 3: 'Return a book', 4: 'Add a book', 5: 'Remove a book',
                  6: 'Print catalog', 0: 'Exit the system'}


def load_books(books_list, file):
    f = open(file, 'r')
    line = f.readline()
    while line != '':
        book_details = line.split(',')
        isbn = book_details[0]
        title = book_details[1]
        author = book_details[2]
        genre = int(book_details[3])
        available = book_details[4]
        books_list.append(Book(isbn, title, author, genre, available))
        line = f.readline()
    f.close()

    total_books = len(books_list)
    return total_books


def print_menu(heading, menu_dict):
    menu_heading = f"Reader's Guild Library - {heading} Menu"
    print(menu_heading)
    print('='*len(menu_heading))
    for i in menu_dict:
        print(f"{i}. {menu_dict[i]}")

    if heading == 'Main':
        selection = int(input('Enter your selection: '))

        if selection == 2130:
            return selection

        while selection < 0 or selection > 3:
            print('Invalid option')
            selection = int(input('Enter your selection: '))
        return selection

    elif heading == 'Librarian':
        selection = int(input('Enter your selection: '))
        while selection < 0 or selection > 6:
            print('Invalid option')
            selection = int(input('Enter your selection: '))
        return selection


def search_book(book_list, search_string):
    search_result = []
    for i in book_list:
        if search_string in i.__str__():
            search_result.append(i)

    return search_result


def find_book_by_isbn(book_list, isbn):
    for i in book_list:
        if isbn == i.get_isbn():
            return book_list.index(i)
            break
        else:
            return -1


def borrow_book(book_list):
    isbn = input('Enter the 13-digit ISBN (format 999-9999999999):')
    match = find_book_by_isbn(book_list, isbn)

    if match == -1:
        print('No book found with that ISBN.')
    else:
        if book_list[match].get_availability() == 'Available':
            book_list[match].borrow_it()
            print(f"'{book_list[match].get_title}' with ISBN {isbn} successfully borrowed.")

        else:
            print(f"'{book_list[match].get_title}' with ISBN {isbn} is not currently available.")


def return_book(book_list):
    isbn = input('Enter the 13-digit ISBN (format 999-9999999999):')
    match = find_book_by_isbn(book_list, isbn)

    if match == -1:
        print('No book found with that ISBN.')
    else:
        if book_list[match].get_availability() == 'Borrowed':
            book_list[match].return_it()
            print(f"'{book_list[match].get_title}' with ISBN {isbn} successfully returned.")

        else:
            print(f"'{book_list[match].get_title}' with ISBN {isbn} is not currently borrowed.")


def add_book(book_list):
    isbn = input('Enter the 13-digit ISBN (format 999-9999999999):')
    title = input('Enter title: ')
    author = input('Enter author name: ')
    genre = input('Enter genre: ')
    while genre not in Book.get_genre_dict().values():
        print("Invalid genre. Choices are: Romance, Mystery, Science Fiction, Thriller, Young Adult, Children's Fiction"
              ", Self-help, Fantasy, Historical Fiction, Poetry")
        genre = input('Enter genre: ')

    for i in Book.get_genre_dict():
        if genre == Book.get_genre_dict()[i]:
            genre_int = i

    book_list.append(Book(isbn, title, author, genre_int, True))
    print(f"'{title}' with ISBN {isbn} successfully added.")


def remove_book(book_list):
    isbn = input('Enter the 13-digit ISBN (format 999-9999999999):')
    match = find_book_by_isbn(book_list, isbn)

    if match == -1:
        print('No book found with that ISBN.')
    else:
        print(f"'{book_list[match].get_title}' with ISBN {isbn} successfully removed.")
        book_list.pop(match)


def print_books(book_list):
    print("{:14s} {:25s} {:25s} {:20s} {:s}".format("ISBN", "Title", "Author", "Genre", "Availability"))
    print(f"{'-'*14} {'-'*25} {'-'*25} {'-'*20} {'-'*12}")
    for i in book_list:
        print(i.__str__())


def save_books(book_list, file):
    books_str = ""
    for i in book_list:
        books_str += f"{i.get_isbn()},{i.get_title()},{i.get_author()},{i.get_genre()},{i.get_available()}\n"

    f = open(file, 'w')
    f.write(books_str)
    f.close()

    return len(book_list)


def main():
    default_menu = MAIN_MENU
    default_menu_heading = MAIN_HEADING
    book_list = []

    print('Starting the system ...')
    file_path = input('Enter book catalog filename: ')
    while not os.path.exists(file_path):
        file_path = input('File not found. Re-enter book catalog filename: ')

    else:
        load_books(book_list, file_path)
        print('Book catalog has been loaded.\n')

        selection = print_menu(default_menu_heading, default_menu)
        while selection != 0:
            if selection == 2130:
                default_menu = LIBRARIAN_MENU
                default_menu_heading = 'Librarian'
                selection = print_menu(default_menu_heading, default_menu)

            if selection == 1:
                print('\n-- Search for books --')
                search_str = input('Enter search value: ')

                search_result = search_book(book_list, search_str.capitalize())
                if len(search_str) == 0:
                    print('No matching books found\n')
                else:
                    print_books(search_result)
                    print('')

            elif selection == 2:
                print('\n-- Borrow a book --')
                borrow_book(book_list)
                print('\n')

            elif selection == 3:
                print('\n-- Return a book --')
                return_book(book_list)
                print('')

            elif selection == 4:
                print('\n-- Add a book --')
                add_book(book_list)
                print('')

            elif selection == 5:
                print('\n-- Remove a book --')
                return_book(book_list)
                print('')

            elif selection == 6:
                print('\n-- Print book catalog --')
                print_books(book_list)
                print('')

            selection = print_menu(default_menu_heading, default_menu)

        else:
            print('\n-- Exit the system --')
            save_books(book_list, file_path)
            print('Book catalog has been saved.\nGood Bye!')



if __name__ == '__main__':
    main()