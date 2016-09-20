from django.contrib import admin

from .models import Album, Track, Genre, Artist
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
	search_fields = ('name',)

admin.site.register(Album, Track, Genre, Artist, AlbumAdmin)