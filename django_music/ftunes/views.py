from django.shortcuts import render

from models import Album, Track, Artist, Genre

def albums(request):
    albums = Album.objects.all()
#    tracks = albums.track_set.all()

    context = {
        'albums': albums,
#        'tracks': tracks,
    }

    return render(request, "ftunes/index.html", context)