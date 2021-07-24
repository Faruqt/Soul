from django.shortcuts import render
from .models import Explore, Playlist
# Create your views here.

def explore_view(request):
    user= request.user

    context = {
    }
    
    return render(request, 'soul/explore.html', context)
