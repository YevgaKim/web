g = ['Демоны','Драма, Комедия', 'Демоны, Исторический, Сверхъестественное, Сёнэн, Экшен', 'Драма, Комедия, Повседневность, Сёнэн, Школа', 'Демоны, Исторический, Сверхъестественное, Сёнэн, Экшен', 'Комедия, Повседневность, Школа', 'Комедия, Повседневность, Школа', 'Комедия, Повседневность, Школа', 'Комедия, Повседневность, Школа', 'Комедия, Повседневность, Школа', 'Комедия, Повседневность, Школа', 'Приключения, Сёнэн,Супер сила, Фэнтези, Экшен', 'Драма, Фэнтези, Этти', 'Комедия, Психологическое, Романтика, Сэйнэн, Школа', 'Военное, Детектив, Драма, Сёнэн, Супер сила, Фэнтези, Экшен']

genres = []
for i in g:
    genres.extend(i.split(", "))

print(genres)