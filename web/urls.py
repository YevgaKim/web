from django.contrib import admin, auth
from django.urls import include, path

from first_try.views import *
from users.views import *

urlpatterns = [
    path("",main,name="main"),
    path("profile/", bio,name="profile"),
    path('admin/', admin.site.urls),
    path("login/",login, name="login"),
    path("registration/", registration,name="registration"),
    path('exit/', exit, name='exit')
]
