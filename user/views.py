from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Max
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .models import Playlist, Usuario, Likes
from .forms import RegistroUsuarioForm, PlaylistForm, LoginForm, EditUserForm
from django.views.generic import CreateView, FormView, TemplateView, UpdateView, DeleteView
from django.views import View


#Cambiar por vistas basadas en clases, pasando formularios y templates para hacer más fácil

class RegistroUserView(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'user/registro.html'

    def form_valid(self, form):

        user = form.save(commit=False) #aun no guardar hasta conseguir nuevo id
        max_id = Usuario.objects.aggregate(Max('id_usuario'))['id_usuario__max']
        user.id_usuario = (max_id + 1) if max_id is not 0 else 1
        user.save()

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

class UserProfileView(TemplateView):
    template_name = 'user/profile.html'

    def dispatch(self, request, *args, **kwargs):
        if 'usuario_id' not in request.session:
            return redirect('login_usuario')
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #User actual
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
            max_id = Playlist.objects.aggregate(Max('id_playlist'))['id_playlist__max']
            playlist.id_playlist = (max_id + 1) if max_id is not 0 else 1
            playlist.save()
            return redirect('lista_playlists')

        # Si el formulario no es válido, volvemos a renderizar con los errores
        playlists = Playlist.objects.filter(usuario=usuario_actual)
        return render(request, self.template_name, {'playlists': playlists, 'form': form, 'usuario': usuario_actual})