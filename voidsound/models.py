from django.db import models


class Artista(models.Model):
    id_artista = models.IntegerField(primary_key=True, help_text="Id único de cada artista")
    nombreArtista = models.CharField(max_length=50, help_text="Nombre registrado del artista")
    paisArtista = models.CharField(max_length=50, help_text="País de origen del artista")

    def __str__(self):
        return self.nombreArtista


class Genero(models.Model):
    id_genero = models.IntegerField(primary_key=True)
    nombreGenero = models.CharField(max_length=100)

    def __str__(self):
        return self.nombreGenero


class Album(models.Model):
    id_album = models.IntegerField(primary_key=True)
    nombreAlbum = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    artista = models.ForeignKey(Artista, on_delete=models.PROTECT, db_column='Artista_id_artista', null=True,
                                blank=True)

    def __str__(self):
        return self.nombreAlbum


class Cancion(models.Model):
    ESTADO_CHOICES = [
        ('activa', 'Activa'),
        ('inactiva', 'Inactiva'),
    ]
    id_cancion = models.IntegerField(primary_key=True)
    nombreCancion = models.CharField(max_length=100)
    duracion = models.IntegerField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='activa')
    album = models.ForeignKey(Album, on_delete=models.PROTECT, db_column='Album_id_album')
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, db_column='Genero_id_genero')

    def __str__(self):
        return self.nombreCancion


from django.db import models

# Create your models here.
