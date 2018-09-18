from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Album


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'albums'  # override the default return var 'object_list'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'atitle', 'genre', 'alogo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'atitle', 'genre', 'alogo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')
