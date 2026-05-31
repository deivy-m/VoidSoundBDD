from django.urls import path
from . import views

# cuando las vistas sean basadas en clases, poner los as_view()
urlpatterns = [
    # Página de Inicio (Catálogo de canciones)
    path('inicio/', views.IndexView.as_view(), name='index'),

    # Perfil, Registro y Autenticación
    path('registro/', views.RegistroUserView.as_view(), name='registrar_usuario'),
    path('login/', views.LoginView.as_view(), name='login_usuario'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('editprofile/', views.EditUserView.as_view(), name='edit_profile'),
    path('deleteprofile/', views.DeleteUserView.as_view(), name='delete_profile'),

    # Gestión de Playlists
    path('playlists/', views.ListaPlaylistsView.as_view(), name='lista_playlists'),
]