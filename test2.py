g = [' Комедия, Повседневность, Школа', 'Демоны, Исторический, Сверхъестественное, Сёнэн, Экшен', 'Военное, Детектив, Драма, Сёнэн, Супер сила, Фэнтези, Экшен', 'Драма, Комедия, Повседневность, Романтика, Сверхъестественное, Сёдзё', 'Демоны, Исторический, Сверхъестественное, Сёнэн, Экшен', 'Комедия, Повседневность, Сэйнэн', 'Драма, Приключения, Сверхъестественное, Сёнэн, Экшен', 'Комедия, Сёнэн, Экшен', 'Военное, Детектив, Драма, Сёнэн, Супер сила, Фэнтези, Экшен', 'Драма, Комедия, Космос, Приключения, Фантастика, Экшен', 'Драма, Исторический, Приключения, Сэйнэн, Экшен', 'Драма, Супер сила, Сэйнэн, Фантастика, Экшен', 'Драма, Комедия, Романтика, Сёнэн, Спорт, Школа', 'Демоны, Комедия, Магия, Приключения, Фэнтези, Экшен', 'Демоны, Комедия, Романтика, Сверхъестественное, Сёдзё, Фэнтези']

genre = [j.strip() for i in g for j in i.split(", ") ]

print(genre)