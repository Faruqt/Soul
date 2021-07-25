from django.db import models
from genre.models import Genre,UsersGenre
from django.contrib.auth.models import User

# Create your models here.
class Explore(models.Model): 
    song = models.CharField(max_length=50)  
    artist= models.CharField(max_length=20) 
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
      verbose_name = ("Explore")
      verbose_name_plural = ("Explore")

    def __str__(self):
        return f"{self.song} by {self.artist} [{self.genre}]"

class Playlist(models.Model): 
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    song = models.CharField(max_length=50)  
    artist= models.CharField(max_length=20) 
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
      verbose_name = ("Playlist")
      verbose_name_plural = ("Playlist")

    def __str__(self):
        return f"Playlist of {self.user.username}"
