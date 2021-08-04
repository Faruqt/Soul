"""soul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home, discover
from genre.views import genres_view
from playlist.views import explore_view,playlist_view
from login_register.views import login_view,logout_view, registerUserView
from profiles.views import my_profile_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('discover/', discover, name="discover"),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', registerUserView, name='register'),
    path('pick_genres/', genres_view, name='genre'),
    path('explore/', explore_view, name='explore'),
    path('playlist/', playlist_view, name='playlist'),
    path('profile/', my_profile_view, name='profile'),
]

urlpatterns += static (settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
