import json
import sqlite3

with open('result.json', 'r', encoding='utf-8') as f: 
    text = json.load(f) 

id=[]  
name = []
rating = []
episodes = []
genres = []
duration = []
images = []
urls=[]
count=1
for txt in text[:300]:
    id.append(count)
    name.append(txt['name'])
    rat = txt["rating"].replace(",",".")
    rating.append(rat)
    episodes.append(txt["episodes"])
    genres.append(txt["genres"])
    duration.append(int(txt["duration"])*int(txt["episodes"]))
    images.append(txt["image"])
    urls.append(txt["url"])
    count+=1



try:
    sqlite_connection = sqlite3.connect('db.sqlite3')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")
    for id2, name2, rating2, episodes2, duration2, genres2, image2,url2 in zip(id, name, rating, episodes, duration, genres, images,urls):
        sqlite_insert_query = """INSERT INTO first_try_anime
                            (id, name, rating, episodes, duration, genres, images,urls)
                            VALUES
                            (?, ?, ?, ?, ?, ?, ?,?);"""
        count = cursor.execute(sqlite_insert_query,(id2, name2, float(rating2), int(episodes2), int(duration2), genres2, image2,url2))
        sqlite_connection.commit()
        print("Запись успешно вставлена ​​в таблицу sqlitedb_developers ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
