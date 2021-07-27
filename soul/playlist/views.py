from django.shortcuts import render
from genre.models import UsersGenre
from .models import Explore, Playlist
# Create your views here.

def explore_view(request):
    user= request.user
    user_genre = UsersGenre.objects.filter(user=user) 
    for genre in user_genre:
            genre1=genre.user_genres.all()[0]
            genre2=genre.user_genres.all()[1]
            genre3=genre.user_genres.all()[2]

    explore = Explore.objects.filter(genre__genres=genre1) | Explore.objects.filter(genre__genres =genre2) | Explore.objects.filter(genre__genres =genre3)  

    context = {
        "explore":explore
    }

    return render(request, 'soul/explore.html', context)
