class ServicioCliente:
    def __init__(self):
        self.clientes = {}

    def agregar_cliente(self, cliente):
        if cliente.id in self.clientes:
            raise ValueError("Ya existe un cliente con este ID.")
        self.clientes[cliente.id] = cliente

    def obtener_cliente(self, id_cliente):
        return self.clientes.get(id_cliente, None)

    def actualizar_cliente(self, cliente):
        if cliente.id not in self.clientes:
            raise ValueError("Cliente no encontrado.")
        self.clientes[cliente.id] = cliente

    def eliminar_cliente(self, id_cliente):
        if id_cliente not in self.clientes:
            raise ValueError("Cliente no encontrado.")
        del self.clientes[id_cliente]