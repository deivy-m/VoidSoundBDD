from django.contrib import admin
from .models import Usuario, Playlist, CancionPlaylist, Likes, Reproduccion

admin.site.register(Usuario)
admin.site.register(Playlist)
admin.site.register(CancionPlaylist)
admin.site.register(Likes)
admin.site.register(Reproduccion)