from django.contrib import admin

from first_try.models import Anime


class FirstTryAdmin(admin.ModelAdmin):
    list_display = ("id","name","rating")
    list_display_links = ("id","name")
    search_fields = ("name",)
    list_filter = ("rating",)


admin.site.register(Anime, FirstTryAdmin)