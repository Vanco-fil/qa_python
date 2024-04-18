import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_name_too_long(self):
        collector = BooksCollector()
        # Попытка добавить книгу с именем длиннее 40 символов
        name = "О" * 41
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book("Космодесант")
        # Устанавливаем и проверяем жанр для добавленной книги
        collector.set_book_genre("Космодесант", "Фантастика")
        assert collector.get_book_genre("Космодесант") == "Фантастика"

    @pytest.mark.parametrize("book_name, genre", [("Человек-молекула", "Фантастика"), ("Лавандовое море", "Комедии")])
    def test_get_book_genre_existing_book(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        # Проверяем, что возвращается ожидаемый жанр для существующей книги
        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize("book_names, genre", [(["Книга1", "Книга2", "Книга3"], "Фантастика"), (["Книга1", "Книга2", "Книга3"], "Ужасы")])
    def test_get_books_with_specific_genre_included(self, book_names, genre):
        collector = BooksCollector()
        for book_name in book_names:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, genre)
        books_with_genre = collector.get_books_with_specific_genre(genre)
        # Проверяем, что все книги в списке имеют указанный жанр
        for book_name in book_names:
            assert book_name in books_with_genre

    def test_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Танцор")
        # Проверяем, что у добавленной книги нет жанра
        assert collector.get_book_genre("Танцор") == ''

    def test_get_books_for_children_suitable(self):
        collector = BooksCollector()
        collector.add_new_book("Милый дом")
        collector.add_new_book("Ну погоди")
        collector.set_book_genre("Милый дом", "Фантастика")
        collector.set_book_genre("Ну погоди", "Мультфильмы")
        # Проверяем, что метод возвращает правильные книги для детей
        assert "Милый дом" in collector.get_books_for_children()
        assert "Ну погоди" in collector.get_books_for_children()

    @pytest.mark.parametrize("book_name, genre", [("Резня", "Ужасы"), ("Коломбо", "Детективы")])
    def test_get_books_for_children_not_suitable(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        # Проверяем, что книги с возрастным рейтингом отсутствуют в списке книг для детей
        assert "Резня" not in collector.get_books_for_children()
        assert "Коломбо" not in collector.get_books_for_children()
    def test_added_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Генерал")
        # Проверяем, что книга успешно добавлена в избранное
        collector.add_book_in_favorites("Генерал")
        assert "Генерал" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Генерал")
        collector.add_book_in_favorites("Генерал")
        # Проверяем, что книга успешно удалена из избранного
        collector.delete_book_from_favorites("Генерал")
        assert "Генерал" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_added(self):
        collector = BooksCollector()
        collector.add_new_book("Танцор")
        collector.add_new_book("Как я съел собаку")
        collector.add_book_in_favorites("Танцор")
        collector.add_book_in_favorites("Как я съел собаку")
        # Проверяем, что метод возвращает правильный список избранных книг
        assert collector.get_list_of_favorites_books() == ["Танцор", "Как я съел собаку"]
