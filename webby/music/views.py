from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def index(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})

def detail(request, alPk):
    album = get_object_or_404(Album, pk=alPk)
    return render(request, 'music/detail.html', {'album': album})

def favor(request, alPk):
    album = get_object_or_404(Album, pk=alPk)
    for pkey in request.POST.getlist('sname'):
        try:
            selected = album.song_set.get(pk=pkey)
        except (KeyError, Song.DoesNotExist):
            return render(request, 'music/detail.html', {'album': album, 'err_msg': "You didn't select right song", })
        else:
            selected.is_fav = True
            selected.save()
    return render(request, 'music/detail.html', {'album': album})
# Create your views here.
