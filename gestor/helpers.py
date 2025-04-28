import os
import platform
import re

def limpiar_pantalla():
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    texto = input(mensaje) if mensaje else input("Introduce un texto: ")
    while len(texto) < longitud_min or len(texto) > longitud_max:
        print(f"El texto debe tener entre {longitud_min} y {longitud_max} caracteres.")
        texto = input(mensaje) if mensaje else input("Introduce un texto: ")
    return texto

def dni_valido(dni, lista):
    if not re.match('[0-9]{2}[A-Z]$', dni):
        print("DNI incorrecto, debe cumplir el formato.")
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print("DNI utilizado por otro cliente.")
            return False
    return True