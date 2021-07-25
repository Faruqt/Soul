from django.shortcuts import render
from .models import Explore, Playlist
# Create your views here.

def explore_view(request):
    user= request.user
    explore = Explore.objects.all()

    context = {
        "explore":explore
    }

    return render(request, 'soul/explore.html', context)
