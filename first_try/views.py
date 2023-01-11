from django.http import HttpResponse
from django.shortcuts import render

from first_try.models import Anime


def main(request):
    context ={
        "animes": Anime.objects.all(),
    }
    return render(request,"first_try/main.html",context=context)

def bio(request):
    return render(request,"first_try/profile.html")

def auth(request):
    return render(request,"first_try/auth.html")
