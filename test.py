import sqlite3

try:
    sqlite_connection = sqlite3.connect('db.sqlite3')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")
    sqlite_insert_query = """INSERT INTO first_try_anime
                            (id, name, rating, episodes, duration, genres, images,urls)
                            VALUES
                            (?, ?, ?, ?, ?, ?, ?,?);"""
    count = cursor.execute(sqlite_insert_query,(1108, "Ван-Пис", float(9.5), int(1052), int(25248), "Драма, Комедия, Приключения, Сёнэн, Супер сила, Фэнтези, Экшен", 
        "https://animego.org/media/cache/thumbs_250x350/upload/anime/images/5ab170d351312102639546.jpg","https://animego.org/anime/van-pis-65"))
    sqlite_connection.commit()
    print("Запись успешно вставлена ​​в таблицу sqlitedb_developers ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")