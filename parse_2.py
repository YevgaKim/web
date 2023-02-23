import json
import random
import time

import requests
from bs4 import BeautifulSoup

start = time.time()
err1=0
err2=0
err3=0
with open("text.txt","r", encoding="utf-8") as f:
    urls=f.readlines()
anime=[]
count=1
try:
    for i in urls:
        src = requests.get(i.strip())
        soup = BeautifulSoup(src.text,"html.parser")
        try:
            if soup.find("dd",class_="col-6 col-sm-8 mb-1").text!="ТВ Сериал":
                err1+=1
                continue
            rating = soup.find("span",class_="rating-value").text
            name = soup.find("div",class_='anime-title').find("h1").text
            genre = soup.find("dd",class_="col-6 col-sm-8 mb-1 overflow-h").find_all("a")
            genres=",".join([i.text for i in genre])
            episodes = soup.find_all("dd",class_="col-6 col-sm-8 mb-1")[1].text
            duration = soup.find_all("dd",class_="col-6 col-sm-8 mb-1")[7].text.strip().split(" ")[0]
            image = soup.find("div", class_="anime-poster position-relative cursor-pointer").find("img").get("src")
        except:
            err2+=1
            continue

        
        if not duration.isdigit() or not episodes.isdigit():
            err3+=1
            continue

        anime.append(
            {
                "rating":rating,
                "name":name,
                "episodes":episodes,
                "genres":genres.replace(",",", "),
                "duration":duration,
                "image":image,
                "url":i.strip(),
            }
        )
        count+=1
        time.sleep(random.randint(3,5))
        print(count)
except:
    pass
finally:
    with open("result.json","w",encoding="utf-8") as f:
        json.dump(anime,f,indent=4,ensure_ascii=False)
    print(f"{err1} - ERROR 1\n{err2} - ERROR 2\n{err3} - ERROR 3")
    finish_time=time.time()-start
    print(f"Script running time - {finish_time}")

