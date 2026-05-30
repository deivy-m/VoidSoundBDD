from django.urls import path
from . import views

urlpatterns = [
    # Artistas
    path('artistas/', views.ArtistaListView.as_view(), name='artista_list'),
    path('artistas/<int:pk>/', views.ArtistaDetailView.as_view(), name='artista_detail'),
    path('artistas/nuevo/', views.ArtistaCreateView.as_view(), name='artista_create'),
    path('artistas/<int:pk>/editar/', views.ArtistaUpdateView.as_view(), name='artista_update'),
    path('artistas/<int:pk>/eliminar/', views.ArtistaDeleteView.as_view(), name='artista_delete'),

    # Álbumes
    path('albumes/', views.AlbumListView.as_view(), name='album_list'),
    path('albumes/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('albumes/nuevo/', views.AlbumCreateView.as_view(), name='album_create'),
    path('albumes/<int:pk>/editar/', views.AlbumUpdateView.as_view(), name='album_update'),
    path('albumes/<int:pk>/eliminar/', views.AlbumDeleteView.as_view(), name='album_delete'),

    # Canciones
    path('canciones/', views.CancionListView.as_view(), name='cancion_list'),
    path('canciones/<int:pk>/', views.CancionDetailView.as_view(), name='cancion_detail'),
    path('canciones/nuevo/', views.CancionCreateView.as_view(), name='cancion_create'),
    path('canciones/<int:pk>/editar/', views.CancionUpdateView.as_view(), name='cancion_update'),
    path('canciones/<int:pk>/eliminar/', views.CancionDeleteView.as_view(), name='cancion_delete'),

# Géneros
    path('generos/', views.GeneroListView.as_view(), name='genero_list'),
    path('generos/nuevo/', views.GeneroCreateView.as_view(), name='genero_create'),
    path('generos/<int:pk>/editar/', views.GeneroUpdateView.as_view(), name='genero_update'),
    path('generos/<int:pk>/eliminar/', views.GeneroDeleteView.as_view(), name='genero_delete'),
]
