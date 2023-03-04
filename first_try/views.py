import collections
import math

from django.http import HttpResponse
from django.shortcuts import redirect, render

from first_try.models import Anime
from users.models import UserAnime


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

def profile(request):
    if request.method == 'POST':
        anime_ids = request.POST.getlist("anime")
        if anime_ids:
            for i in anime_ids:
                anime = Anime.objects.get(id=i)
                useranime = UserAnime(user=request.user, anime=anime)
                useranime.save()
            return redirect('profile')
    img = False
    anime_ids = UserAnime.objects.filter(user=request.user).values_list('anime_id', flat=True)

    genres = []
    print(1)
    for i in anime_ids:
        if i!=None:
            anime = Anime.objects.get(id=i)
            genres.append(anime.genres)
    print(2)

    # genre = [genres.extend(i.split(", ")) for i in genres]
    
    print(genres)
    # counter = collections.Counter(genre)
    # most_common = counter.most_common(3)
    # print(3)
    # print(most_common)
    context = {
        "img":img,
        "animes": Anime.objects.all()[:100],
        "anime_ids":anime_ids,
    }
    return render(request,"first_try/profile.html",context=context)


