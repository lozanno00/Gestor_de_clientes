import sys
from ui import MainWindow
from menu import iniciar

if __name__ == "__main__":
    # Verificar si el programa debe ejecutarse en modo terminal
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        iniciar()  # Iniciar el menú en la terminal
    else:
        # Iniciar la interfaz gráfica con Tkinter
        app = MainWindow()
        app.mainloop()
