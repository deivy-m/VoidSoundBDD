from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Artista, Album, Cancion
from .forms import ArtistaForm, AlbumForm, CancionForm


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


from django.shortcuts import render

# Create your views here.
