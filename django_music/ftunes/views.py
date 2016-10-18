from django.shortcuts import render

from models import Album, Track, Artist, Genre

def albums(request):
    albums = Album.objects.all()

    context = {
        albums: 'albums',
    }

    return render(request, "ftunes/index.html", context)