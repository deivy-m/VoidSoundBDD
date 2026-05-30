from django.urls import path
from . import views

#cuando las vistas sean basadas en clases, poner los as_view()
urlpatterns = [
    path('registro/', views.RegistroUserView.as_view(), name='registrar_usuario'),
    path('playlists/', views.ListaPlaylistsView.as_view(), name='lista_playlists'),
    path('login/', views.LoginView.as_view(), name='login_usuario'),
]