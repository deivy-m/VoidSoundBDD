from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .models import Playlist, Usuario, Likes
from .forms import RegistroUsuarioForm, PlaylistForm, LoginForm
from django.views.generic import CreateView, FormView
from django.views import View


#Cambiar por vistas basadas en clases, pasando formularios y templates para hacer más fácil

class RegistroUserView(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'user/registro.html'

    def form_valid(self, form):

        user = form.save()

        self.request.session['usuario_id'] = user.id_usuario
        return redirect('lista_playlists')

class LoginView(FormView):
    template_name = 'user/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('lista_playlists') #Redirección

    def form_valid(self, form):
        usuario = form.user
        self.request.session['usuario_id'] = usuario.id_usuario

        return super().form_valid(form)




class ListaPlaylistsView(View):
    template_name = 'user/playlists.html'

    def dispatch(self, request, *args, **kwargs):

        if 'usuario_id' not in request.session:
            return redirect('registrar_usuario')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        usuario_actual = Usuario.objects.get(id_usuario=request.session['usuario_id'])
        playlists = Playlist.objects.filter(usuario=usuario_actual)
        form = PlaylistForm()

        context = {
            'playlists': playlists,
            'form': form,
            'usuario': usuario_actual
        }
        return render(request, self.template_name, context)

    def post(self, request):
        usuario_actual = Usuario.objects.get(id_usuario=request.session['usuario_id'])
        form = PlaylistForm(request.POST)

        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.usuario = usuario_actual  # Asignamos el usuario de la sesión
            playlist.save()
            return redirect('lista_playlists')

        # Si el formulario no es válido, volvemos a renderizar con los errores
        playlists = Playlist.objects.filter(usuario=usuario_actual)
        return render(request, self.template_name, {'playlists': playlists, 'form': form, 'usuario': usuario_actual})