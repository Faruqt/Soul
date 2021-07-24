from django.shortcuts import render
from .models import Genre,UsersGenre
# Create your views here.

def genres_view(request):
    user= request.user
    genre = Genre.objects.all()

    if request.method == "POST": 
        if "genreSelected" in request.POST: 

            picked_genre = request.POST.getlist('genre_select')
            user_genre = UsersGenre(user=user)
            user_genre.save()  
            user_genre.user_genres.add(*picked_genre)

    print(user)     
    
    context = {
        "genres":genre,
        "users":user,
    }

    return render(request, 'soul/genre.html', context)
