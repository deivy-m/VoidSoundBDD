from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Artista, Album, Cancion, Genero
from .forms import ArtistaForm, AlbumForm, CancionForm, GeneroForm


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


class ArtistaDeleteView(DeleteView):
    model = Artista
    success_url = reverse_lazy('artista_list')


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


class CancionDeleteView(DeleteView):
    model = Cancion
    success_url = reverse_lazy('cancion_list')


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

class GeneroDeleteView(DeleteView):
    model = Genero
    success_url = reverse_lazy('genero_list')


# -- Index --

class IndexView(ListView):
    model = Cancion
    template_name = 'voidsound/index.html'
    context_object_name = 'canciones'

    def get_queryset(self):

        return Cancion.objects.filter(estado='activa').select_related('album__artista')