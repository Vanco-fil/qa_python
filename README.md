# qa_python

## Методы

### `test_add_new_book_add_two_books`
Проверяет что добавилось именно 2 книги

### `test_add_new_book_name_too_long`
Проверяет что название книги может содержать максимум 40 символов

### `test_set_book_genre_success`
Проверяет возможность установить жанр для книги

### `test_get_book_genre_existing_book`
Проверяет, что возвращается ожидаемый жанр для существующей книги

### `test_get_books_with_specific_genre_included`
Проверяет, что все книги в списке имеют указанный жанр

### `test_book_without_genre`
Проверяет, что у добавленной книги нет жанра

### `test_get_books_for_children_suitable`
Проверяет, что метод возвращает правильные книги для детей

### `test_get_books_for_children_not_suitable`
Проверяет, что книги с возрастным рейтингом отсутствуют в списке книг для детей

### `test_added_book_in_favorites`
Проверяет, что книга успешно добавлена в избранное

### `test_delete_book_from_favorites`
Проверяет, что книга успешно удалена из избранного

### `test_get_list_of_favorites_books_added`
Проверяет, что список избранных книг создается