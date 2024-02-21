class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        raise NameError("Имя книги не может быть изменено")

    @property
    def autor(self) -> str:
        return self._author

    @autor.setter
    def autor(self, autor: str):
        raise NameError("Автор книги не может быть изменён")

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """Бумажная книга"""

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if not (type(pages) == int and pages > 0):
            raise ValueError("Количество страниц должно быть целым положительным числом")
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages})"


class AudioBook(Book):
    """Аудио-книга"""

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, duration: float) -> None:
        if not (isinstance(duration, float) and duration > 0):
            raise ValueError("Продолжительность должна иметь тип float и быть положительным числом")
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration})"


if __name__ == "__main__":
    audio_book = AudioBook("name 1", "autor 1", 30.2)
    print(audio_book)
    print(repr(audio_book))

    paper_book = PaperBook("name 2", "autor 2", 50)
    print(paper_book)
    print(repr(paper_book))
