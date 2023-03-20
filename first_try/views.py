import collections
import math

from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from first_try.forms import UserProfileForm
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
        "animes": Anime.objects.all(),
        "answer":answer,
        "time":{
            "minutes": minutes,
            "hours": [hours,minutes_hours],
            "days":[days,hours_days,minutes_hours]
        },
    }
    return render(request,"first_try/main.html",context=context)


@csrf_exempt
def profile(request):
    print(request.FILES)
    ANIME = Anime.objects.all()[:300]
    if request.method == 'POST':

        form = UserProfileForm(data = request.POST, files = request.FILES, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            print(form.errors)

        anime_ids = request.POST.getlist('anime')
        if anime_ids:
            user_anime_objs = []
            for anime_id in anime_ids:
                anime = ANIME.filter(id=anime_id).first()
                if anime:
                    user_anime_objs.append(UserAnime(user=request.user, anime=anime))
            UserAnime.objects.bulk_create(user_anime_objs)
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)

    user_anime_ids = UserAnime.objects.filter(user=request.user).values_list('anime_id', flat=True)
    
    genres = []
    count = 0
    for i in ANIME:
        if i.id in user_anime_ids and i.id!=None:
            genres.append(i.genres)
            count+=1
            if count==len(user_anime_ids)-1:
                break

    genre = [j.strip() for i in genres for j in i.split(", ") ]
    
    counter = collections.Counter(genre)
    most_common = counter.most_common(3)
    g = ",".join([i[0] for i in most_common])
    context = {
        "animes": ANIME,
        "user_anime_ids": user_anime_ids,
        "genres":g,
        'form': form,
    }
    return render(request, "first_try/profile.html", context=context)


