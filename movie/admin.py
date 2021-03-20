from django.contrib import admin
from .models import Movie ,Category,Country
# Register your models here.


class MovieInline(admin.StackedInline):
    model = Movie
    extra = 2
    max_num = 10


class MovieAdmin(admin.ModelAdmin):
    list_display = ["title","year"]
    list_filter = ["year"]






admin.site.register(Movie,MovieAdmin)
admin.site.register(Category)
admin.site.register(Country)