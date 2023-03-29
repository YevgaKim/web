import collections
import math

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from first_try.forms import UserProfileForm
from first_try.models import Anime
from users.models import User, UserAnime


@login_required
@csrf_exempt
def profile(request):
    ANIME = Anime.objects.all()
    value = 0
    genres = []
    count = 0
    user_anime_ids = UserAnime.objects.filter(user=request.user).values_list('anime_id', flat=True)

    for i in ANIME:
        if i.id in user_anime_ids and i.id!=None:
            genres.append(i.genres)
            count+=1
            value +=i.duration
            if count==len(user_anime_ids)-1:
                break
    genre = [j.strip() for i in genres for j in i.split(", ") ]
    genre_1 = {j.strip() for i in genres for j in i.split(", ")}
    genres_1={}
    for i in genre_1:
        for j in ANIME:
            if j.id in user_anime_ids and j.id!=None:
                if i in j.genres:
                    if i in genres_1:
                        genres_1[i]+=j.duration
                    else:
                        genres_1[i]=j.duration
    counter = collections.Counter(genre)

    for k,v in counter.items():
        genres_1[k]*=v
    
    try:
        sorted_genres = sorted(genres_1.items(), key=lambda x: x[1], reverse=True)[:3]
    except:
        sorted_genres = sorted(genres_1.items(), key=lambda x: x[1], reverse=True)


    g = ", ".join([i[0] for i in sorted_genres])

    request.user.favorite_genres = g
    request.user.save()
    if request.method == 'POST':
        anime_ids = request.POST.getlist('anime')
        if anime_ids:
            user_anime_objs = []
            for anime_id in anime_ids:
                anime = ANIME.filter(id=anime_id).first()
                if anime:
                    user_anime_objs.append(UserAnime(user=request.user, anime=anime))
            UserAnime.objects.bulk_create(user_anime_objs)
            return redirect('profile')
        form = UserProfileForm(data = request.POST, files = request.FILES, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    
    context = {
        "animes": ANIME[:100],
        "user_anime_ids": user_anime_ids,
        "genres":g,
        'form': form,
        "value":value,
        "percents": math.ceil(value*100/342692),
    }
    return render(request,"first_try/profile.html", context=context)


def main(request):
    animes = Anime.objects.all()
    answer = ""
    ANIME=[]
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

    if request.user.is_authenticated:
        user_anime_ids = list(UserAnime.objects.filter(user=request.user).values_list('anime_id', flat=True))
        gen = request.user.favorite_genres
        if gen:
            ge = gen.split(",")
            g = [i.strip() for i in ge]
        else:
            g=[]
        if len(g)==3:
            for i in animes:
                if i.id not in user_anime_ids and i.id!=None:
                    if g[0] in i.genres and g[1] in i.genres and g[2] in i.genres:
                        ANIME.append(i)
                        user_anime_ids.append(i.id)

            for i in animes:
                if i.id not in user_anime_ids and i.id!=None:
                    if  g[0] in i.genres and g[1] in i.genres  or  g[1] in i.genres and g[2] in i.genres  or  g[0] in i.genres and g[2] in i.genres :
                        ANIME.append(i)
                        user_anime_ids.append(i.id)

            for i in animes:
                if i.id not in user_anime_ids and i.id!=None:
                    if g[0] in i.genres or g[1] in i.genres or g[2] in i.genres:
                        ANIME.append(i)
                        user_anime_ids.append(i.id)
        elif len(g)==2:
            for i in animes:
                if i.id not in user_anime_ids and i.id!=None:
                    if g[0] in i.genres and g[1] in i.genres:
                        ANIME.append(i)
                        user_anime_ids.append(i.id)
            
            for i in animes:
                if i.id not in user_anime_ids and i.id!=None:
                    if g[0] in i.genres or g[1] in i.genres:
                        ANIME.append(i)
                        user_anime_ids.append(i.id)

        elif len(g)==1:
            for i in animes:
                if i.id not in user_anime_ids and i.id!=None:
                    if g[0] in i.genres:
                        ANIME.append(i)
                        user_anime_ids.append(i.id)
        
        else:
            ANIME=animes
        

    else:
        g=[]
    context ={
        "animes": ANIME[:1],
        "answer":answer,
        "time":{
            "   minutes": minutes,
            "hours": [hours,minutes_hours],
            "days":[days,hours_days,minutes_hours]
        },
        "g":g,
    }
    return render(request,"first_try/main.html",context=context)