from django.urls import path
from . import views

#cuando las vistas sean basadas en clases, poner los as_view()
urlpatterns = [
    path('registro/', views.registrar_usuario, name='registrar_usuario'),
    path('playlists/', views.lista_playlists, name='lista_playlists'),
]