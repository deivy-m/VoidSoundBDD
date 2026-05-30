from django import forms
from .models import Usuario, Playlist

class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    class Meta:
        model = Usuario
        fields = ['id_usuario', 'nombre', 'email', 'password', 'tipo_usuario']

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['id_playlist', 'nombrePlaylist']