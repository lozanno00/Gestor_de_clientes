# File: /Gestor_de_clientes/Gestor_de_clientes/src/main.py

import gestor.database as db 
from utils import helpers

def main():
    print("Bienvenido al Sistema de Gestión de Clientes")
    while True:
        print("\nMenú:")
        print("1. Añadir Cliente")
        print("2. Ver Cliente")
        print("3. Actualizar Cliente")
        print("4. Eliminar Cliente")
        print("5. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            print("Añadiendo un cliente...\n")
            while True:
                dni = helpers.leer_texto(3, 3, "DNI (2 números y 1 letra)").upper()
                if helpers.dni_valido(dni, db.Clientes.lista):
                    break
            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 caracteres)").capitalize()
            apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 caracteres)").capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente añadido correctamente.")
        
        elif choice == '2':
            print("Buscando un cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 números y 1 letra)").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("Cliente no encontrado.")
        
        elif choice == '3':
            print("Actualizando un cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 números y 1 letra)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(2, 30, f"Nombre (de 2 a 30 caracteres) [{cliente.nombre}]").capitalize()
                apellido = helpers.leer_texto(2, 30, f"Apellido (de 2 a 30 caracteres) [{cliente.apellido}]").capitalize()
                db.Clientes.modificar(dni, nombre, apellido)
                print("Cliente actualizado correctamente.")
            else:
                print("Cliente no encontrado.")
        
        elif choice == '4':
            print("Eliminando un cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 números y 1 letra)").upper()
            if db.Clientes.borrar(dni):
                print("Cliente eliminado correctamente.")
            else:
                print("Cliente no encontrado.")
        
        elif choice == '5':
            print("Saliendo de la aplicación.")
            break
        
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()