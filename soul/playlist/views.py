from django.shortcuts import render,redirect
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

    if request.method == "POST": 
        if "music_selected" in request.POST:

            selected_music = request.POST.getlist('music_select')
            your_playlist = Playlist(user=user)
            your_playlist.save()
            your_playlist.playlist.add(*selected_music)

            if user is not None:
                return redirect('playlist')

    context = {
        "explore":explore,
    }

    return render(request, 'soul/explore.html', context)

def playlist_view(request):
    user= request.user
    play_list = Playlist.objects.filter(user=user) 
    for play in play_list:
        your_playlist = play.playlist.all()

    context={
        "your_playlist":your_playlist
    }

    return render(request, 'soul/playlist.html', context)
