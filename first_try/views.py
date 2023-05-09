import collections
import math

import Levenshtein
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from first_try.forms import UserProfileForm
from first_try.models import Anime
from users.models import User, UserAnime


def define_anime_status(request):
    genres = []
    value = 0
    ANIME = Anime.objects.all()
    user_anime_ids = UserAnime.objects.filter(user=request.user).values_list('anime_id', flat=True)
    viewed_animes = ANIME.filter(pk__in=user_anime_ids)
    unviewed_animes = ANIME.exclude(pk__in=list(user_anime_ids))

    for i in viewed_animes:
        genres.append(i.genres)
        value +=i.duration

    return genres, viewed_animes, unviewed_animes, value

def define_genres(genres,viewed_animes,request):
    genre_lst = [j.strip() for i in genres for j in i.split(", ")]
    genre_set = set(genre_lst)
    genres_1={}
    for i in genre_set: 
        for j in viewed_animes:
            if i in j.genres:
                if i in genres_1:
                    genres_1[i]+=j.duration
                else:
                    genres_1[i]=j.duration
    counter = collections.Counter(genre_lst)

    for k,v in counter.items():
        genres_1[k]*=v
    
    try:
        sorted_genres = sorted(genres_1.items(), key=lambda x: x[1], reverse=True)[:3]
    except:
        sorted_genres = sorted(genres_1.items(), key=lambda x: x[1], reverse=True)


    g = ", ".join([i[0] for i in sorted_genres])
    return g

def pagination(request,animes):
    paginator= Paginator(animes,100)
    return paginator.get_page(request.GET.get("page_unviewed"))

# @cache_page(60)
@login_required
@csrf_exempt
def profile(request):
    ANIME = Anime.objects.all()
    c=""

    genres, viewed_animes, unviewed_animes, value = define_anime_status(request)

    g = define_genres(genres,viewed_animes,request)

    page_unviewed_animes = pagination(request,unviewed_animes)

    page_viewed_animes = pagination(request,viewed_animes)

    if request.GET.get("page_viewed"):
        c = "checked"

    User.objects.filter(pk=request.user.id).update(favorite_genres=g)

    if request.method == 'POST':
        anime_ids_unviewed = request.POST.getlist('anime_unviewed')
        anime_ids_viewed =  request.POST.getlist('anime_viewed')
        if anime_ids_unviewed:
            user_anime_objs = []
            for anime_id in anime_ids_unviewed:
                anime = ANIME.filter(id=anime_id).first()
                if anime:
                    user_anime_objs.append(UserAnime(user=request.user, anime=anime))
            UserAnime.objects.bulk_create(user_anime_objs)
            return redirect('profile')
        elif anime_ids_viewed:
            ANIMEDB = UserAnime.objects.all()
            for anime_id in anime_ids_viewed:
                anime = ANIMEDB.filter(user_id = request.user.id, anime_id=anime_id)
                anime.delete()
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
        "genres":g,
        'form': form,
        "value":value,
        "percents": math.ceil(value*100/342692),
        "page_unviewed_animes":page_unviewed_animes,
        "page_viewed_animes":page_viewed_animes,
        "c":c,
    }
    return render(request,"first_try/profile.html", context=context)



####################MAIN###############################

def algorithm_for_selecting_anime(request, ANIME):
    if request.user.is_authenticated:
        animes=[]
        user_anime_ids = list(UserAnime.objects.filter(user=request.user).values_list('anime_id', flat=True))
        gen = request.user.favorite_genres
        if gen:
            ge = gen.split(",")
            g = [i.strip() for i in ge]
        else:
            g=[]
        if len(g)==3:
            for i in ANIME:
                if i.id not in user_anime_ids and i.id!=None:
                    if g[0] in i.genres and g[1] in i.genres and g[2] in i.genres:
                        animes.append(i)
                        user_anime_ids.append(i.id)

            for i in ANIME:
                if i.id not in user_anime_ids and i.id!=None:
                    if  g[0] in i.genres and g[1] in i.genres  or  g[1] in i.genres and g[2] in i.genres  or  g[0] in i.genres and g[2] in i.genres :
                        animes.append(i)
                        user_anime_ids.append(i.id)

            for i in ANIME:
                if i.id not in user_anime_ids and i.id!=None:
                    if g[0] in i.genres or g[1] in i.genres or g[2] in i.genres:
                        animes.append(i)
                        user_anime_ids.append(i.id)
        elif len(g)==2:
            for i in ANIME:
                if i.id not in user_anime_ids and i.id!=None:
                    if g[0] in i.genres and g[1] in i.genres:
                        animes.append(i)
                        user_anime_ids.append(i.id)
            
            for i in ANIME:
                if i.id not in user_anime_ids and i.id!=None:
                    if g[0] in i.genres or g[1] in i.genres:
                        animes.append(i)
                        user_anime_ids.append(i.id)

        elif len(g)==1:
            for i in ANIME:
                if i.id not in user_anime_ids and i.id!=None:
                    if g[0] in i.genres:
                        animes.append(i)
                        user_anime_ids.append(i.id)
        
        else:
            animes=ANIME
        
    else:
        g=[]
        animes = ANIME

    return g, animes

def find_most_similar_element(example, lst):
    min_distance = float('inf')
    most_similar_element = None
    for elem in lst:
        distance = Levenshtein.distance(example, elem.name.lower())
        if distance < min_distance:
            min_distance = distance
            most_similar_element = elem
    return most_similar_element

# @cache_page(60)
def main(request):
    answer = ""
    time=0
    anime_name = request.GET.get('search')
    if isinstance(anime_name,str):
        answer = find_most_similar_element(anime_name.lower(),Anime.objects.all())
        time = answer.duration
    minutes = time
    hours = math.floor(time/60)
    minutes_hours = math.floor(time%60)
    days = math.floor(time/(24*60))
    hours_days = math.floor(time/60%24)

    g,animes = algorithm_for_selecting_anime(request, Anime.objects.all())

    context ={
        "animes": animes[:100 if len(animes)>=100 else len(animes)],
        "answer":answer,
        "time":{
            "minutes": minutes,
            "hours": [hours,minutes_hours],
            "days":[days,hours_days,minutes_hours]
        },
        "g":g,
    }
    return render(request,"first_try/main.html",context=context)

def about(request):
    return render(request,"first_try/about.html")