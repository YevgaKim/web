import math

from django.http import HttpResponse
from django.shortcuts import render

from first_try.models import Anime


def main(request):
    answer = ""
    time=0
    anime_name = request.GET.get('search')
    if isinstance(anime_name,str):
        for i in Anime.objects.all():
            if anime_name.lower() in i.name.lower():
                answer= i
                time=int(i.duration)
                break
    minutes = time
    hours = math.floor(time/60)
    minutes_hours = math.floor(time%60)
    days = math.floor(time/(24*60))
    hours_days = math.floor(time/60%24)
    context ={
        "animes": Anime.objects.all()[:100],
        "answer":answer,
        "time":{
            "minutes": minutes,
            "hours": [hours,minutes_hours],
            "days":[days,hours_days,minutes_hours]
        },
    }
    return render(request,"first_try/main.html",context=context)

def bio(request):
    print(request.GET)
    img = False
    context = {
        "img":img,
        "animes": Anime.objects.all()[:100],
    }
    return render(request,"first_try/profile.html",context=context)


