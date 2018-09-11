from django.db import models


# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    atitle = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    alogo = models.FileField()

    def __str__(self):
        return self.album_title + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    stitle = models.CharField(max_length=250)
    type = models.CharField(max_length=5)

    def __str__(self):
        return self.song_title
