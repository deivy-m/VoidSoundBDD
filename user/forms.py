from django import forms
from .models import Usuario, Playlist


#el id de usuario no debería ingresarse, ni su tipo de usuario, por defecto es free
#solo nombre, email y password
#personalizar los campos más para pasar a los templates
class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")

    class Meta:
        model = Usuario
        fields = ['id_usuario', 'nombre', 'email', 'contraseña', 'tipo_usuario']


class LoginForm(forms.Form):
    email = forms.EmailField(help_text=False, label=False, widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Email'}))
    contraseña = forms.CharField(help_text=False, label=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        contraseña = cleaned_data.get('contraseña')

        if email and contraseña:
            try:
                usuario = Usuario.objects.get(email=email, contraseña = contraseña)
                self.user = usuario
            except Usuario.DoesNotExist:
                raise forms.ValidationError("Correo o contraseña incorrectos")
        return cleaned_data




#no id, solo nombre al crear playlist
class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['id_playlist', 'nombrePlaylist']