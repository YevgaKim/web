from django.contrib import admin, auth
from django.urls import include, path

from first_try.views import *
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("first_try.urls")),
    path("",include("users.urls")),
]
