from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from voidsound.models import Cancion


class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('free', 'Free'),
        ('premium', 'Premium'),
    ]

    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    contraseña = models.CharField(max_length=50)
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES, default='free')

    class Meta:
        db_table = '[Usuarios].[Usuario]'

    def __str__(self):
        return self.nombre



class Playlist(models.Model):
    id_playlist = models.IntegerField(primary_key=True)
    nombrePlaylist = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, db_column='Usuario_id_usuario')
    canciones = models.ManyToManyField(Cancion, through='CancionPlaylist')

    class Meta:
        db_table = '[Usuarios].[Playlist]'

    def __str__(self):
        return self.nombrePlaylist



class CancionPlaylist(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, db_column='Playlist_id_playlist')
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE, db_column='Cancion_id_cancion')

    class Meta:
        db_table = '[Usuarios].[CancionPlaylist]'
        unique_together = (('playlist', 'cancion'),)


class Likes(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='Usuario_id_usuario')
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE, db_column='Cancion_id_cancion')

    class Meta:
        db_table = '[Usuarios].[Likes]'
        unique_together = (('usuario', 'cancion'),)



class Reproduccion(models.Model):
    id_reproduccion = models.IntegerField(primary_key=True)
    fecha = models.DateTimeField()
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, db_column='Usuario_id_usuario')
    cancion = models.ForeignKey(Cancion, on_delete=models.SET_NULL, null=True, db_column='Cancion_id_cancion')

    class Meta:
        db_table = '[Usuarios].[Reproduccion]'