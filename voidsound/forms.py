from django import forms
from .models import Artista, Album, Cancion

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ['id_artista', 'nombreArtista', 'paisArtista']
        widgets = {
            'id_artista': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombreArtista': forms.TextInput(attrs={'class': 'form-control'}),
            'paisArtista': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['id_album', 'nombreAlbum', 'fecha_lanzamiento', 'artista']
        widgets = {
            'id_album': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombreAlbum': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_lanzamiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'artista': forms.Select(attrs={'class': 'form-control'}),
        }

class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ['id_cancion', 'nombreCancion', 'duracion', 'estado', 'album', 'genero']
        widgets = {
            'id_cancion': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombreCancion': forms.TextInput(attrs={'class': 'form-control'}),
            'duracion': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'album': forms.Select(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
        }