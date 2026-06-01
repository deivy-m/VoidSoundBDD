from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Artista, Album, Cancion, Genero
from .forms import ArtistaForm, AlbumForm, CancionForm, GeneroForm
from django.contrib import messages
from django.db.models import ProtectedError
from django.db import transaction
from .models import Artista, Album, Cancion
from django.apps import apps
from user.models import Reproduccion, Likes, CancionPlaylist


# === CRUD ARTISTAS ===
class ArtistaListView(ListView):
    model = Artista
    context_object_name = 'artistas'


class ArtistaDetailView(DetailView):
    model = Artista


class ArtistaCreateView(CreateView):
    model = Artista
    form_class = ArtistaForm
    success_url = reverse_lazy('artista_list')


class ArtistaUpdateView(UpdateView):
    model = Artista
    form_class = ArtistaForm
    success_url = reverse_lazy('artista_list')

    def form_valid(self, form):
        id_antigua = self.get_object().pk
        id_nueva = form.cleaned_data.get('id_artista')

        if id_nueva and id_antigua != id_nueva:
            # 1. Guardar el nuevo artista con la ID nueva
            nuevo_objeto = form.save(commit=False)
            nuevo_objeto.pk = id_nueva
            nuevo_objeto.save()

            # 2. Mover todos los álbumes del artista viejo al nuevo ID para evitar el ProtectedError
            Album.objects.filter(artista_id=id_antigua).update(artista_id=id_nueva)

            # 3. Ahora que el ID viejo está libre y sin hijos, lo podemos borrar de forma segura
            Artista.objects.filter(pk=id_antigua).delete()
            return redirect(self.success_url)

        return super().form_valid(form)


class ArtistaDeleteView(DeleteView):
    model = Artista
    success_url = reverse_lazy('artista_list')

    def form_valid(self, form):
        artista = self.get_object()

        # Cargamos los modelos dinámicamente apuntando a la app 'user'
        # (Si tu app se llama 'usuarios' en Django, cambia 'user' por 'usuarios')
        Reproduccion = apps.get_model('user', 'Reproduccion')
        Likes = apps.get_model('user', 'Likes')
        CancionPlaylist = apps.get_model('user', 'CancionPlaylist')

        with transaction.atomic():
            albumes_ids = Album.objects.filter(artista=artista).values_list('pk', flat=True)
            canciones = Cancion.objects.filter(album_id__in=albumes_ids)
            canciones_ids = canciones.values_list('pk', flat=True)

            # Ahora Python ya reconocerá las variables perfectamente:
            Reproduccion.objects.filter(cancion_id__in=canciones_ids).delete()
            Likes.objects.filter(cancion_id__in=canciones_ids).delete()
            CancionPlaylist.objects.filter(cancion_id__in=canciones_ids).delete()

            canciones.delete()
            Album.objects.filter(artista=artista).delete()

            return super().form_valid(form)

# === CRUD ÁLBUMES ===
class AlbumListView(ListView):
    model = Album
    context_object_name = 'albumes'


class AlbumDetailView(DetailView):
    model = Album


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy('album_list')


class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    success_url = reverse_lazy('album_list')

    def form_valid(self, form):
        id_antigua = self.get_object().pk
        id_nueva = form.cleaned_data.get('id_album')

        if id_nueva and id_antigua != id_nueva:
            nuevo_objeto = form.save(commit=False)
            nuevo_objeto.pk = id_nueva
            nuevo_objeto.save()

            # Mover todas las canciones del álbum viejo al nuevo ID del álbum
            Cancion.objects.filter(album_id=id_antigua).update(album_id=id_nueva)

            Album.objects.filter(pk=id_antigua).delete()
            return redirect(self.success_url)

        return super().form_valid(form)


class AlbumDeleteView(DeleteView):
    model = Album
    success_url = reverse_lazy('album_list')


# === CRUD CANCIONES ===
class CancionListView(ListView):
    model = Cancion
    context_object_name = 'canciones'


class CancionDetailView(DetailView):
    model = Cancion


class CancionCreateView(CreateView):
    model = Cancion
    form_class = CancionForm
    success_url = reverse_lazy('cancion_list')


class CancionUpdateView(UpdateView):
    model = Cancion
    form_class = CancionForm
    success_url = reverse_lazy('cancion_list')

    def form_valid(self, form):
        id_antigua = self.get_object().pk
        id_nueva = form.cleaned_data.get('id_cancion')

        if id_nueva and id_antigua != id_nueva:
            nuevo_objeto = form.save(commit=False)
            nuevo_objeto.pk = id_nueva
            nuevo_objeto.save()

            # Las canciones comúnmente no tienen tablas hijas directas (a menos que dependan de listas de reproducción),
            # si tu tabla 'Likes' o 'Playlist_Cancion' usa 'id_cancion', deberías actualizarla aquí de forma similar:
            # Likes.objects.filter(cancion_id=id_antigua).update(cancion_id=id_nueva)

            Cancion.objects.filter(pk=id_antigua).delete()
            return redirect(self.success_url)

        return super().form_valid(form)


class CancionDeleteView(DeleteView):
    model = Cancion
    success_url = reverse_lazy('cancion_list')


# === CRUD GÉNEROS ===
class GeneroListView(ListView):
    model = Genero
    context_object_name = 'generos'


class GeneroCreateView(CreateView):
    model = Genero
    form_class = GeneroForm
    success_url = reverse_lazy('genero_list')


class GeneroUpdateView(UpdateView):
    model = Genero
    form_class = GeneroForm
    success_url = reverse_lazy('genero_list')

    def form_valid(self, form):
        id_antigua = self.get_object().pk
        id_nueva = form.cleaned_data.get('id_genero')

        if id_nueva and id_antigua != id_nueva:
            nuevo_objeto = form.save(commit=False)
            nuevo_objeto.pk = id_nueva
            nuevo_objeto.save()

            # Mover todas las canciones vinculadas a este género hacia el nuevo ID
            Cancion.objects.filter(genero_id=id_antigua).update(genero_id=id_nueva)

            Genero.objects.filter(pk=id_antigua).delete()
            return redirect(self.success_url)

        return super().form_valid(form)


class GeneroDeleteView(DeleteView):
    model = Genero
    success_url = reverse_lazy('genero_list')