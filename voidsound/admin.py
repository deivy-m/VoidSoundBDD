from django.contrib import admin

from voidsound.models import Artista, Cancion, Genero, Album

admin.site.register(Artista)
admin.site.register(Genero)
admin.site.register(Cancion)
admin.site.register(Album)

# Register your models here.
