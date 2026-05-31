from django.urls import path
from . import views

urlpatterns = [
    # Suscripciones
    path('suscripciones/', views.SuscripcionListView.as_view(), name='suscripcion_list'),
    path('suscripciones/<int:pk>/', views.SuscripcionDetailView.as_view(), name='suscripcion_detail'),
    path('suscripciones/nuevo/', views.SuscripcionCreateView.as_view(), name='suscripcion_create'),
    path('suscripciones/<int:pk>/editar/', views.SuscripcionUpdateView.as_view(), name='suscripcion_update'),
    path('suscripciones/<int:pk>/eliminar/', views.SuscripcionDeleteView.as_view(), name='suscripcion_delete'),

    # Pagos
    path('pagos/', views.PagoListView.as_view(), name='pago_list'),
    path('pagos/<int:pk>/', views.PagoDetailView.as_view(), name='pago_detail'),
    path('pagos/nuevo/', views.PagoCreateView.as_view(), name='pago_create'),
    path('pagos/<int:pk>/editar/', views.PagoUpdateView.as_view(), name='pago_update'),
    path('pagos/<int:pk>/eliminar/', views.PagoDeleteView.as_view(), name='pago_delete'),
]