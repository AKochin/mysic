
from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # /music/<album_PK>/
    url(r'^(?P<alPk>\d+)/$', views.detail, name='detail'),
]
