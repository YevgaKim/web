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
def profile(request, view=None,page=None):
    ANIME = Anime.objects.all()
    START_U = 0
    FINISH_U = 0
    START = 0
    FINISH = 0
    value = 0
    genres = []
    count = 0
    user_anime_ids = UserAnime.objects.filter(user=request.user).values_list('anime_id', flat=True)

    viewed_animes = []
    unviewed_animes = []
    for i in ANIME:
        if i.id in user_anime_ids and i.id!=None:
            viewed_animes.append(i)
        else:
            unviewed_animes.append(i)
    for i in viewed_animes:
            genres.append(i.genres)
            count+=1
            value +=i.duration
            if count==len(user_anime_ids)-1:
                break
    genre = [j.strip() for i in genres for j in i.split(", ") ]
    genre_1 = {j.strip() for i in genres for j in i.split(", ")}
    genres_1={}
    for i in genre_1:
        for j in viewed_animes:
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

    if len(unviewed_animes)!=0:
        unviewed_pages = list(range(1,math.ceil(len(unviewed_animes)/100)+1 if len(unviewed_animes)%100!=0 else len(unviewed_animes)/100))
    else:
        unviewed_pages=[]


    if view=="unviewed":
        if page!=None:
            unviewed_pages[int(page)-1]=f"{page} "
        else:
            unviewed_pages[0]="1 "

        if page!=None:
            page = int(page)
        if page==None and page==1 and page==unviewed_pages[-1]:
            START_U = 0
            FINISH_U = len(unviewed_animes)
        elif page==unviewed_pages[-1] and page!=1:
            START_U = page*100-100
            FINISH_U = page*100+page%100
        else:
            if page!=None:
                START_U= (page-1)*100
                FINISH_U = page*100
            else:
                START_U= 0
                FINISH_U = 100
    else:
        START_U = 0
        FINISH_U = 100 if len(unviewed_animes)>=100 else len(unviewed_animes)
        unviewed_pages[0]="1 "

    

    if len(viewed_animes)!=0:
        viewed_pages = list(range(1,math.ceil(len(viewed_animes)/100)+1 if len(viewed_animes)%100!=0 else len(viewed_animes)/100))
    else:
        viewed_pages=[]
    
    

    if view=="viewed":
        if page!=None:
            viewed_pages[int(page)-1]=f"{page} "
        else:
            viewed_pages[0]="1 "

        if page!=None:
            page = int(page)
        if page==None and page==1 and page==viewed_pages[-1]:
            START = 0
            FINISH = len(viewed_animes)
        elif page==viewed_pages[-1] and page!=1:
            START = page*100-100
            FINISH = page*100+page%100
        else:
            if page!=None:
                START= (page-1)*100
                FINISH = page*100
            else:
                START= 0
                FINISH = 100
    else:
        START = 0
        FINISH = 100 if len(viewed_animes)>=100 else len(viewed_animes)
        viewed_pages[0]="1 "

    request.user.favorite_genres = g
    request.user.save()


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
        "unviewed_animes": unviewed_animes[START_U:FINISH_U],
        "viewed_animes": viewed_animes[START:FINISH],
        "viewed_pages":viewed_pages,
        "unviewed_pages":unviewed_pages,
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
        "animes": ANIME[:500],
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