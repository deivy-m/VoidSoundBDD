from user.models import Usuario
from django.db import models

class Suscripcion(models.Model):
    TIPO_SUS_CHOICES = [('duo', 'Duo'), ('familiar', 'Familiar'), ('free', 'Free'), ('premium', 'Premium')]
    ESTADO_SUS_CHOICES = [('activa', 'Activa'), ('inactiva', 'Inactiva')]

    id_suscripcion = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=10, choices=TIPO_SUS_CHOICES, default='free')
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    estado = models.CharField(max_length=10, choices=ESTADO_SUS_CHOICES, default='activa')
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, db_column='Usuario_id_usuario')

    class Meta:
        db_table = 'Suscripción'  # <-- Mismo nombre (con tilde) que tu CREATE TABLE del SQL

    def __str__(self):
        return f"Suscripción {self.tipo} - {self.usuario.nombre}"


class Pago(models.Model):
    ESTADO_PAGO_CHOICES = [('cancelado', 'Cancelado'), ('pendiente', 'Pendiente')]

    id_pago = models.IntegerField(primary_key=True)
    monto = models.FloatField()
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=15, choices=ESTADO_PAGO_CHOICES, default='pendiente')
    suscripcion = models.ForeignKey(Suscripcion, on_delete=models.PROTECT, db_column='Suscripción_id_suscripcion', null=True, blank=True)

    class Meta:
        db_table = 'Pago'  # <-- Fuerza a buscar el nombre exacto del SQL

    def __str__(self):
        return f"Pago {self.id_pago} - {self.estado}"