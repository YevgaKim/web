from django.contrib import admin, auth
from django.urls import include, path

from first_try.views import *
from users.views import *
from web import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("first_try.urls")),
    path("",include("users.urls")),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns