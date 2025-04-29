import sys
import os

# Agregar la carpeta 'gestor' al sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'gestor'))

from gestor.ui import MainWindow
from gestor.menu import iniciar

if __name__ == "__main__":
    # Verificar si el programa debe ejecutarse en modo terminal
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        iniciar()  # Iniciar el menú en la terminal
    else:
        # Iniciar la interfaz gráfica con Tkinter
        app = MainWindow()
        app.mainloop()
