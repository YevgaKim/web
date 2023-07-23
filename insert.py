import json

import psycopg2

with open('result.json', 'r', encoding='utf-8') as f: 
    text = json.load(f) 
text.pop(0)
id=[]  
name = []
rating = []
episodes = []
genres = []
duration = []
images = []
urls=[]
count=1
for txt in text[:750]:
    id.append(count)
    name.append(txt['name'])
    rat = txt["rating"].replace(",",".")
    rating.append(rat)
    episodes.append(txt["episodes"])
    genres.append(txt["genres"])
    duration.append(int(txt["duration"])*int(txt["episodes"]))
    urls.append(txt["url"])
    images.append(f'static/vendor/anime_images/image_{count-1}.jpg')
    count+=1


try:
    conn = psycopg2.connect(database="postgres", user="YevgaKim", password="mydbforanitiming",host="postgres",port="5432")
    print("Успешно подключено к PostgreSQL")
    cur = conn.cursor()
    count=0
    for id2, name2, rating2, episodes2, duration2, genres2, image2, url2 in zip(id, name, rating, episodes, duration, genres, images, urls):
        postgres_insert_query = """INSERT INTO first_try_anime 
                                (id, name, rating, episodes, duration, genres, images, urls) 
                                VALUES 
                                (%s, %s, %s, %s, %s, %s, %s, %s)"""

        record_to_insert = (id2, name2, float(rating2), int(episodes2), int(duration2), genres2, image2, url2)
        cur.execute(postgres_insert_query, record_to_insert)
        conn.commit()

        print(count, "строк добавлено в таблицу")

    cur.close()
    conn.close()
    print("Соединение с PostgreSQL закрыто")

except (Exception, psycopg2.Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if conn:
        conn.close()
        print("Соединение с PostgreSQL закрыто")
