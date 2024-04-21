class Book():
    __genre_dict = {0: 'Romance', 1: 'Mystery', 2: 'Science Fiction', 3: 'Thriller', 4: 'Young Adult',
                           5: 'Children’s Fiction', 6: 'Self-help', 7: 'Fantasy', 8: 'Historical Fiction', 9: 'Poetry'}

    def __init__(self, isbn, title, author, genre, available):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__available = available


    def get_genre_dict():
        return Book.__genre_dict

    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_available(self):
        return self.__available

    def get_genre_name(self):
        return Book.get_genre_dict()[self.__genre]

    def get_availability(self):
        if self.__available:
            return 'Available'
        else:
            return 'Borrowed'

    def set_isbn(self, isbn):
        self.__isbn = isbn

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_genre(self, genre):
        self.__genre = genre

    def borrow_it(self):
        self.__available = False

    def return_it(self):
        self.__available = True

    def __str__(self):
        return "{:14s} {:25s} {:25s} {:20s} {:s}".format(self.get_isbn(), self.get_title(), self.get_author(), self.get_genre_name(), self.get_availability())