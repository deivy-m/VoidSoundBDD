from django import forms
from .models import Usuario, Suscripcion, Pago

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'nombre', 'email', 'contraseña', 'tipo_usuario']
        widgets = {
            'id_usuario': forms.NumberInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contraseña': forms.PasswordInput(attrs={'class': 'form-control', 'render_value': True}),
            'tipo_usuario': forms.Select(attrs={'class': 'form-control'}),
        }


class SuscripcionForm(forms.ModelForm):
    class Meta:
        model = Suscripcion
        fields = ['id_suscripcion', 'tipo', 'fecha_inicio', 'fecha_fin', 'estado', 'usuario']
        widgets = {
            'id_suscripcion': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'fecha_fin': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }


class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['id_pago', 'monto', 'fecha', 'estado', 'suscripcion']
        widgets = {
            'id_pago': forms.NumberInput(attrs={'class': 'form-control'}),
            'monto': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'suscripcion': forms.Select(attrs={'class': 'form-control'}),
        }