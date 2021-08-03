from .models import Playlist
from django.contrib.auth.models import User
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

@receiver(post_save, sender=User)
def post_save_create_playlist (sender, instance, created, **kwargs):
    if created:
        Playlist.objects.create(user=instance)

