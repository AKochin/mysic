from django.db import models


# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    atitle = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    alogo = models.CharField(max_length=250)

    def __str__(self):
        return self.atitle + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    stitle = models.CharField(max_length=250)
    type = models.CharField(max_length=5)
    is_fav = models.BooleanField(default=False)

    def __str__(self):
        return self.stitle
