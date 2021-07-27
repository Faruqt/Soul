from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
   genres = models.CharField(max_length=100, null=True)

   def __str__(self):
      return self.genres 

class UsersGenre(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE , null=True)
   user_genres= models.ManyToManyField(Genre)

   def __str__(self):
      return f"{self.user.username}'s genres"

