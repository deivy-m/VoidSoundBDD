from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registrar_usuario, name='registrar_usuario'),
    path('playlists/', views.lista_playlists, name='lista_playlists'),
]