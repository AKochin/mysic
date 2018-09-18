
from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/<album_PK>/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/2
    url(r'^album/(?P<pk>\d+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/2/delete
    url(r'^album/(?P<pk>\d+)/delete/$', views.AlbumDelete.as_view(), name='album-del'),

    # /music/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
]
