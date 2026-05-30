from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Usuario, Suscripcion, Pago
from .forms import UsuarioForm, SuscripcionForm, PagoForm

# === CRUD USUARIOS ===
class UsuarioListView(ListView):
    model = Usuario
    context_object_name = 'usuarios'


class UsuarioDetailView(DetailView):
    model = Usuario


class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('usuario_list')


class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('usuario_list')


class UsuarioDeleteView(DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuario_list')


# === CRUD SUSCRIPCIONES ===
class SuscripcionListView(ListView):
    model = Suscripcion
    context_object_name = 'suscripciones'


class SuscripcionDetailView(DetailView):
    model = Suscripcion


class SuscripcionCreateView(CreateView):
    model = Suscripcion
    form_class = SuscripcionForm
    success_url = reverse_lazy('suscripcion_list')


class SuscripcionUpdateView(UpdateView):
    model = Suscripcion
    form_class = SuscripcionForm
    success_url = reverse_lazy('suscripcion_list')


class SuscripcionDeleteView(DeleteView):
    model = Suscripcion
    success_url = reverse_lazy('suscripcion_list')


# === CRUD PAGOS ===
class PagoListView(ListView):
    model = Pago
    context_object_name = 'pagos'


class PagoDetailView(DetailView):
    model = Pago


class PagoCreateView(CreateView):
    model = Pago
    form_class = PagoForm
    success_url = reverse_lazy('pago_list')


class PagoUpdateView(UpdateView):
    model = Pago
    form_class = PagoForm
    success_url = reverse_lazy('pago_list')


class PagoDeleteView(DeleteView):
    model = Pago
    success_url = reverse_lazy('pago_list')