from django.shortcuts import render, get_object_or_404
from .models import Album

def index(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})

def detail(request, alPk):
    album = get_object_or_404(Album, pk=alPk)
    return render(request, 'music/detail.html', {'album': album})
# Create your views here.
