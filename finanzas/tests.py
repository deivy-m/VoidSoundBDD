from django.test import TestCase
from django.utils import timezone
from .models import Usuario, Suscripcion, Pago


class FinanzasModelsTestCase(TestCase):

    def setUp(self):
        # Crear un usuario de prueba
        self.usuario = Usuario.objects.create(
            id_usuario=1,
            nombre="Juan Perez",
            email="juan@voidsound.com",
            contraseña="securepassword123",
            tipo_usuario="premium"
        )

        # Crear una suscripción de prueba
        self.suscripcion = Suscripcion.objects.create(
            id_suscripcion=10,
            tipo="premium",
            fecha_inicio=timezone.now(),
            fecha_fin=timezone.now() + timezone.timedelta(days=30),
            estado="activa",
            usuario=self.usuario
        )

    def test_creacion_usuario(self):
        usuario = Usuario.objects.get(id_usuario=1)
        self.assertEqual(usuario.nombre, "Juan Perez")
        self.assertEqual(usuario.tipo_usuario, "premium")

    def test_creacion_suscripcion(self):
        suscripcion = Suscripcion.objects.get(id_suscripcion=10)
        self.assertEqual(suscripcion.tipo, "premium")
        self.assertEqual(suscripcion.usuario, self.usuario)

    def test_creacion_pago(self):
        pago = Pago.objects.create(
            id_pago=100,
            monto=9.99,
            fecha=timezone.now(),
            estado="pendiente",
            suscripcion=self.suscripcion
        )
        self.assertEqual(pago.monto, 9.99)
        self.assertEqual(pago.estado, "pendiente")