import sys
from ui import MainWindow
from menu import iniciar

if __name__ == "__main__":
    # Check if the program should run in terminal mode
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        iniciar()  # Launch terminal menu
    else:
        # Launch the Tkinter GUI
        app = MainWindow()
        app.mainloop()
