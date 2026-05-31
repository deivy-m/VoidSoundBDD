from django.contrib import messages
from django.db import connection
from django.db.models import Max
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormMixin

from voidsound.models import Cancion
from .models import Playlist, Usuario, Likes, CancionPlaylist
from .forms import RegistroUsuarioForm, PlaylistForm, LoginForm, EditUserForm, AddSongForm
from django.views.generic import CreateView, FormView, TemplateView, UpdateView, DeleteView, DetailView
from django.views import View

from voidsound.models import Cancion

#region Usuario y Perfil

class RegistroUserView(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'user/registro.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        max_id = Usuario.objects.aggregate(Max('id_usuario'))['id_usuario__max']
        user.id_usuario = (max_id + 1) if max_id is not None else 1
        user.save()

        self.request.session['usuario_id'] = user.id_usuario
        return redirect('lista_playlists')


class LoginView(FormView):
    template_name = 'user/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('lista_playlists')

    def form_valid(self, form):
        usuario = form.user
        self.request.session['usuario_id'] = usuario.id_usuario
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        # Captura la petición de salida mandada desde el menú
        if request.POST.get('logout') == 'true':
            request.session.flush()
            return redirect('login_usuario')
        return super().post(request, *args, **kwargs)


class UserProfileView(TemplateView):
    template_name = 'user/profile.html'

    def dispatch(self, request, *args, **kwargs):
        if 'usuario_id' not in request.session:
            return redirect('login_usuario')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuario = Usuario.objects.get(id_usuario=self.request.session['usuario_id'])
        context['usuario'] = usuario
        context['playlists'] = Playlist.objects.filter(usuario=usuario)
        return context


class EditUserView(UpdateView):
    model = Usuario
    template_name = 'user/edit.html'
    form_class = EditUserForm
    success_url = reverse_lazy('profile')

    def dispatch(self, request, *args, **kwargs):
        if 'usuario_id' not in request.session:
            return redirect('login_usuario')
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return Usuario.objects.get(id_usuario=self.request.session['usuario_id'])


class DeleteUserView(DeleteView):
    model = Usuario
    template_name = 'user/delete.html'
    success_url = reverse_lazy('registrar_usuario')

    def dispatch(self, request, *args, **kwargs):
        if 'usuario_id' not in request.session:
            return redirect('login_usuario')
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return Usuario.objects.get(id_usuario=self.request.session['usuario_id'])

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.delete()
        self.request.session.flush()
        return redirect(success_url)

#endregion

#region Playlists
class ListaPlaylistsView(View):
    template_name = 'user/playlists.html'

    def dispatch(self, request, *args, **kwargs):
        if 'usuario_id' not in request.session:
            return redirect('login_usuario')
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
            playlist.usuario = usuario_actual
            max_id = Playlist.objects.aggregate(Max('id_playlist'))['id_playlist__max']
            playlist.id_playlist = (max_id + 1) if max_id is not None else 1
            playlist.save()
            return redirect('lista_playlists')

        playlists = Playlist.objects.filter(usuario=usuario_actual)
        return render(request, self.template_name, {'playlists': playlists, 'form': form, 'usuario': usuario_actual})


class ShowPlaylistdetailView(FormMixin, DetailView):
    model = Playlist
    template_name = 'user/playlist_detail.html'
    form_class = AddSongForm
    context_object_name = 'playlist'
    
    def dispatch(self, request, *args, **kwargs):
        if 'usuario_id' not in request.session:
            return redirect('login_usuario')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['canciones'] = CancionPlaylist.objects.filter(playlist = self.object).select_related('cancion')
        context['form'] = self.get_form()
        return context

    def post(self, *args, **kwargs):

        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



    def form_valid(self, form):
        cancion_id = form.cleaned_data['cancion'].id_cancion

        playlist_id = self.object.id_playlist
        #sentencia directa por culpa de problemas del orm
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT COUNT(*) FROM [Usuarios].[CancionPlaylist] WHERE Playlist_id_playlist = %s AND Cancion_id_cancion = %s",
                [playlist_id, cancion_id]
            )
            ya_existe = cursor.fetchone()[0] > 0

        if ya_existe:
            messages.error(self.request, "Esta canción ya se encuentra en la playlist.")
            return HttpResponseRedirect(self.get_success_url())

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO [Usuarios].[CancionPlaylist] (Playlist_id_playlist, Cancion_id_cancion) VALUES (%s, %s)",
                [playlist_id, cancion_id]
            )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('detalle_playlist', kwargs={'pk': self.object.pk})




#endregion

class IndexView(View):
    template_name = 'user/index.html'
    
    def dispatch(self, request, *args, **kwargs):
        if 'usuario_id' not in request.session:
            return redirect('login_usuario')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        usuario_actual = Usuario.objects.get(id_usuario=request.session['usuario_id'])
        canciones = Cancion.objects.all()

        context = {
            'canciones': canciones,
            'usuario': usuario_actual
        }
        return render(request, self.template_name, context)
