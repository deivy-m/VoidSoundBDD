from django import forms
from .models import Usuario, Playlist


#el id de usuario no debería ingresarse, ni su tipo de usuario, por defecto es free
#solo nombre, email y password
#personalizar los campos más para pasar a los templates
class RegistroUsuarioForm(forms.ModelForm):
    contraseña = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Contraseña")

    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'contraseña']


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



class PlaylistForm(forms.ModelForm):

    nombrePlaylist = forms.CharField(help_text=False, label=False, widget=forms.TextInput(
        attrs={'placeholder': 'Nombre de la playlist'}))

    class Meta:
        model = Playlist
        fields = ['nombrePlaylist', ]

class EditUserForm(forms.ModelForm):

    nombre = forms.CharField(help_text=False, label=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Nombre'}))

    email = forms.EmailField(help_text=False, label=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}
    ))

    class Meta:
        model = Usuario
        fields = ['nombre', 'email']