from django.urls import path

from users.views import *

urlpatterns = [
    path("login/",login, name="login"),
    path("registration/", registration,name="registration"),
    path('exit/', exit, name='exit'),
]