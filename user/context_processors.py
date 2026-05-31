from .models import Usuario

def usuario_sesion(request):
    # Si el ID del usuario existe en la sesión, lo buscamos y lo dejamos disponible globalmente
    if 'usuario_id' in request.session:
        try:
            usuario = Usuario.objects.get(id_usuario=request.session['usuario_id'])
            return {'usuario_logueado': usuario}
        except Usuario.DoesNotExist:
            pass
    return {'usuario_logueado': None}