import copy
import unittest
import database as db
import helpers
import csv
import config

class TestDatabase(unittest.TestCase):
    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('15J', 'Marta', 'Pérez'),
            db.Cliente('48H', 'Manolo', 'López'),
            db.Cliente('28Z', 'Ana', 'García')
        ]
        db.Clientes.guardar()

    def test_buscar_cliente(self):
        copia_lista = copy.deepcopy(db.Clientes.lista)
        cliente = db.Clientes.buscar_cliente('15J')
        self.assertEqual(cliente.dni, '15J')
        self.assertEqual(cliente.nombre, 'Marta')
        self.assertEqual(cliente.apellido, 'Pérez')
        self.assertEqual(copia_lista, db.Clientes.lista)

    def test_crear_cliente(self):
        copia_lista = copy.deepcopy(db.Clientes.lista)
        db.Clientes.crear_cliente('67K', 'Luis', 'Martínez')
        self.assertEqual(len(db.Clientes.lista), len(copia_lista) + 1)
        cliente = db.Clientes.lista[-1]
        self.assertEqual(cliente.dni, '67K')
        self.assertEqual(cliente.nombre, 'Luis')
        self.assertEqual(cliente.apellido, 'Martínez')

    def test_modificar_cliente(self):
        copia_lista = copy.deepcopy(db.Clientes.lista)
        db.Clientes.modificar_cliente('15J', 'María', 'Pérez')
        cliente = db.Clientes.buscar_cliente('15J')
        self.assertEqual(cliente.nombre, 'María')
        self.assertEqual(cliente.apellido, 'Pérez')
        self.assertEqual(copia_lista, db.Clientes.lista)

    def test_borrar_cliente(self):
        copia_lista = copy.deepcopy(db.Clientes.lista)
        db.Clientes.borrar_cliente('15J')
        self.assertEqual(len(db.Clientes.lista), len(copia_lista) - 1)
        cliente = db.Clientes.buscar_cliente('15J')
        self.assertIsNone(cliente)

    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('00A', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('23223S', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('F35', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('48H', db.Clientes.lista))

    def test_escritura_csv(self):
        db.Clientes.borrar('48H')
        db.Clientes.borrar('15J')
        db.Clientes.modificar('28Z', 'Mariana', 'Pérez')
        with open(config.DATABASE_PATH, newline="\n") as fichero:
            reader = csv.reader(fichero, delimiter=";")
            dni, nombre, apellido = next(reader)
            self.assertEqual(dni, '28Z')
            self.assertEqual(nombre, 'Mariana')
            self.assertEqual(apellido, 'Pérez')

if __name__ == '__main__':
    unittest.main()