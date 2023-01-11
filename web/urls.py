from django.contrib import admin
from django.urls import include, path

from first_try.views import *

urlpatterns = [
    path("",main,name="main"),
    path("bio/", bio,name="Bio"),
    path("auth/", auth,name="Auth"),
    path('admin/', admin.site.urls),
]
