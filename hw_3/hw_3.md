# HW 3

1. Create a Book class with attributes title, author, and pages. Include a method get_summary() that returns a summary of the book details.

    ```py
    book = Book('Dive Into Python', 'Mark Pilgrim', 123)
    assert book.get_summary() == 'Title: Dive Into Python, Author: Mark Pilgrim, Pages: 123'
    ```

2. Extend the Book class by adding __str__, __eq__, and __len__ magic methods.
   - __str__ method should return a formatted string representation of the book
   - __eq__ should compare two books by title and author
   - __len__ should return the number of pages

    ```py
    book1 = Book('Dive Into Python', 'Mark Pilgrim', 123)
    book2 = Book('Python Crash Course', 'Eric Matthes', 321)
    book3 = Book('Dive Into Python', 'Mark Pilgrim', 123)
    assert str(book1) == 'Title: Dive Into Python, Author: Mark Pilgrim, Pages: 123'
    assert book1 != book2
    assert book1 != object()
    assert book1 == book3
    assert len(book1) == 123
    ```

3. Add a from_string class method, that allows creating a Book instance from a string formatted as "Title - Author - Pages".

    ```py
    book = Book.from_string('Dive Into Python - Mark Pilgrim - 123')
    assert book.title == 'Dive Into Python'
    assert book.author == 'Mark Pilgrim'
    assert book.pages == 123
    ```

4. Add add_review method that takes a value between 0 and 5 (otherwise ValueError is raised) and saves to some private variable. Add read-only property rating that returns average rating from the list of reviews.

    ```py
    book = Book('Dive Into Python', 'Mark Pilgrim', 123)
    book.add_review(3)
    assert book.rating == 3
    book.add_review(5)
    assert book.rating == 4
    book.add_review(-1)  # Error
    ```

5. Create a Comic class that inherits from Book but overrides get_summary method. Make sure original get_summary is used

    ```py
    comic = Comic('Batman', 'Jeph Loeb', 50)
    assert comic.get_summary() == 'Genre: Comic, Title: Batman, Author: Jeph Loeb, Pages: 50'
    ```
