from django.urls import path

from first_try.views import *

urlpatterns = [
    path("",main,name="main"),
    path("profile/", profile,name="profile"),
    path("profile/<str:view>/<str:page>/", profile,name="profile"),
    path("about/",about, name="about"),
]