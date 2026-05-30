from django.shortcuts import render, redirect, get_object_or_404
from .models import Playlist, Usuario, Likes
from .forms import RegistroUsuarioForm, PlaylistForm


#Cambiar por vistas basadas en clases, pasando formularios y templates para hacer más fácil
def registrar_usuario(min_request):
    if min_request.method == 'POST':
        form = RegistroUsuarioForm(min_request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('lista_playlists')
    else:
        form = RegistroUsuarioForm()
    return render(min_request, 'user/registro.html', {'form': form})



def lista_playlists(min_request):
    playlists = Playlist.objects.all()
    if min_request.method == 'POST':
        form = PlaylistForm(min_request.POST)
        if form.is_valid():
            # Por ahora asignamos un usuario estático para pruebas hasta que implementes el login formal
            playlist = form.save(commit=False)
            playlist.usuario = Usuario.objects.first()
            playlist.save()
            return redirect('lista_playlists')
    else:
        form = PlaylistForm()

    return render(min_request, 'user/playlists.html', {'playlists': playlists, 'form': form})