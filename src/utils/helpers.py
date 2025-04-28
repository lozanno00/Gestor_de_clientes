def validar_correo(correo):
    import re
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, correo) is not None

def formatear_datos_cliente(cliente):
    return {
        'ID': cliente.id,
        'Nombre': cliente.nombre,
        'Correo': cliente.correo,
        'Teléfono': cliente.telefono
    }