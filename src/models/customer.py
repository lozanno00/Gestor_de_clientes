class Cliente:
    def __init__(self, id_cliente, nombre, correo, telefono):
        self.id = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    def actualizar(self, nombre=None, correo=None, telefono=None):
        if nombre is not None:
            self.nombre = nombre
        if correo is not None:
            self.correo = correo
        if telefono is not None:
            self.telefono = telefono

    def eliminar(self):
        # Lógica para eliminar el registro del cliente
        pass

    def __str__(self):
        return f"Cliente(id={self.id}, nombre={self.nombre}, correo={self.correo}, telefono={self.telefono})"