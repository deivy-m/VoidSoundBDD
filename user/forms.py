from django import forms
from .models import Usuario, Playlist


#el id de usuario no debería ingresarse, ni su tipo de usuario, por defecto es free
#solo nombre, email y password
#personalizar los campos más para pasar a los templates
class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    class Meta:
        model = Usuario
        fields = ['id_usuario', 'nombre', 'email', 'password', 'tipo_usuario']


#no id, solo nombre al crear playlist
class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['id_playlist', 'nombrePlaylist']