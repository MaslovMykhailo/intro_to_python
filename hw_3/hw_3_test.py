import unittest

from .hw_3 import Book, Comic


class TestHW3(unittest.TestCase):

    def test_book_get_summary(self):
        book = Book("Dive Into Python", "Mark Pilgrim", 123)

        self.assertEqual(book.get_summary(), "Title: Dive Into Python, Author: Mark Pilgrim, Pages: 123")

    def test_book_magic_methods(self):
        book1 = Book("Dive Into Python", "Mark Pilgrim", 123)
        book2 = Book("Python Crash Course", "Eric Matthes", 321)
        book3 = Book("Dive Into Python", "Mark Pilgrim", 123)

        self.assertEqual(str(book1), "Title: Dive Into Python, Author: Mark Pilgrim, Pages: 123")
        self.assertNotEqual(book1, book2)
        self.assertNotEqual(book1, object())
        self.assertEqual(book1, book3)
        self.assertEqual(len(book1), 123)

    def test_book_from_string(self):
        book = Book.from_string("Dive Into Python - Mark Pilgrim - 123")

        self.assertEqual(book.title, "Dive Into Python")
        self.assertEqual(book.author, "Mark Pilgrim")
        self.assertEqual(book.pages, 123)

    def test_book_add_review(self):
        book = Book("Dive Into Python", "Mark Pilgrim", 123)
        book.add_review(3)

        self.assertEqual(book.rating, 3)

        book.add_review(5)

        self.assertEqual(book.rating, 4)

        self.assertRaises(ValueError, book.add_review, -1)

    def test_comic(self):
        comic = Comic("Batman", "Jeph Loeb", 50)

        self.assertEqual(comic.get_summary(), "Genre: Comic, Title: Batman, Author: Jeph Loeb, Pages: 50")


if __name__ == "__main__":
    unittest.main()
