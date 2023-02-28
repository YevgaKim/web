from django.contrib import auth
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

from first_try.models import Anime
from users.forms import UserLoginForm, UserRegistrationForm
from users.models import User, UserAnime


def login(request):
    error_invalid=False
    if request.method =="POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username,password = password)
            if user:
                auth.login(request,user)
                return HttpResponseRedirect(reverse("main"))
        else:
            if form.error_messages['invalid_login']=='Please enter a correct %(username)s and password. Note that both fields may be case-sensitive.':
                error_invalid = True
    else:
        form = UserLoginForm()
    context = {"form": form,
                "error_invalid": error_invalid,}
    return render(request,"users/login.html", context)



def registration(request):
    error_exists = False
    error_toocommon = False
    error_similiar = False
    erro_similiar_pass_username = False
    if request.method =="POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            UserAnime.objects.create(user=new_user)
            return HttpResponseRedirect(reverse("login"))
        else:
            for k in form.errors:
                if form.errors[k][0]=="A user with that username already exists.":
                    error_exists=True   
                elif form.errors[k][0]=="This password is too common.":
                    error_toocommon=True
                elif form.errors[k][0]=="The two password fields didn’t match.":
                    error_similiar=True 
                elif form.errors[k][0]=="The password is too similar to the username.": 
                    erro_similiar_pass_username=True
                print(form.errors[k][0])
    else:
        form = UserRegistrationForm()
    context = {"form": form,
                "error_exists": error_exists,
                "error_toocommon": error_toocommon,
                "error_similiar": error_similiar,
                "erro_similiar_pass_username":erro_similiar_pass_username,}
    return render(request,"users/registration.html",context)

def exit(request):
    logout(request)
    return render(request,"first_try/main.html")