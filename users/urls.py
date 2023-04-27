from django.urls import path

from users.views import *

urlpatterns = [
    path("login/",LoginUser.as_view(), name="login"),
    path("registration/", RegistrationView.as_view(),name="registration"),
    path('exit/', exit, name='exit'),
]