class Book:
    __reviews = []

    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return self.get_summary()

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Book):
            return False

        return self.title == value.title and self.author == value.author and self.pages

    def __len__(self) -> int:
        return self.pages

    def get_summary(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    @classmethod
    def from_string(cls, string: str):
        title, author, pages = map(lambda x: x.strip(), string.split(" - "))

        if int(pages) < 1:
            raise ValueError("Pages must be a positive number")

        return cls(title, author, int(pages))

    def add_review(self, rating: int):
        if type(rating) is not int:
            raise TypeError("Rating must be an integer")

        if rating < 0 or rating > 5:
            raise ValueError("Rating must be between 0 and 5")

        self.__reviews.append(rating)

    @property
    def rating(self) -> int:
        return int(sum(self.__reviews) / len(self.__reviews)) if len(self.__reviews) > 0 else 0


class Comic(Book):
    __genre = "Comic"

    def __init__(self, title: str, author: str, pages: int):
        super().__init__(title, author, pages)

    def get_summary(self) -> str:
        return f"Genre: {self.__genre}, {super().get_summary()}"
