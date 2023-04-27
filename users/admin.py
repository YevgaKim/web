from django.contrib import admin

from users.models import User


class UsersAdmin(admin.ModelAdmin):
    list_display = ("id","username","image")
    list_display_links = ("id","username")
    search_fields = ("username",)


admin.site.register(User, UsersAdmin)
