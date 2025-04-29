from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, askokcancel, WARNING
import database as db
import helpers

class CenterWidgetMixin:
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int((ws / 2) - (w / 2))
        y = int((hs / 2) - (h / 2))
        self.geometry(f"{w}x{h}+{x}+{y}")

class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title('Gestor de Clientes')
        self.configure(bg="#f0f0f0")  # Fondo gris claro
        self.build()
        self.center()

    def build(self):
        # Estilo general
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 10), rowheight=25)
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
        style.configure("TButton", font=("Arial", 10), padding=5)

        # Marco superior
        frame = Frame(self, bg="#f0f0f0")
        frame.pack(pady=10)

        # Etiqueta de título
        title_label = Label(frame, text="Gestor de Clientes", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
        title_label.pack(pady=10)

        # Treeview
        treeview_frame = Frame(self, bg="#f0f0f0")
        treeview_frame.pack(pady=10)

        treeview = ttk.Treeview(treeview_frame)
        treeview['columns'] = ('DNI', 'Nombre', 'Apellido')
        treeview.pack()

        # Formato de columnas
        treeview.column("#0", width=0, stretch=NO)
        treeview.column("DNI", anchor=CENTER, width=100)
        treeview.column("Nombre", anchor=CENTER, width=150)
        treeview.column("Apellido", anchor=CENTER, width=150)

        # Encabezados de columnas
        treeview.heading("#0", anchor=CENTER)
        treeview.heading("DNI", text="DNI", anchor=CENTER)
        treeview.heading("Nombre", text="Nombre", anchor=CENTER)
        treeview.heading("Apellido", text="Apellido", anchor=CENTER)

        # Llenar datos en el Treeview
        self.fill_treeview(treeview)

        # Scrollbar
        scrollbar = Scrollbar(treeview_frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        treeview.config(yscrollcommand=scrollbar.set)

        # Marco inferior
        button_frame = Frame(self, bg="#f0f0f0")
        button_frame.pack(pady=20)

        # Botones
        Button(button_frame, text="Listar Clientes", command=self.list_clients, bg="#4CAF50", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10)
        Button(button_frame, text="Buscar Cliente", command=self.search_client, bg="#2196F3", fg="white", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=10)
        Button(button_frame, text="Crear", command=self.create_client_window, bg="#FFC107", fg="black", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=10, pady=5)
        Button(button_frame, text="Modificar", command=self.edit_client_window, bg="#FF9800", fg="black", font=("Arial", 10, "bold")).grid(row=1, column=1, padx=10, pady=5)
        Button(button_frame, text="Borrar", command=self.delete, bg="#F44336", fg="white", font=("Arial", 10, "bold")).grid(row=1, column=2, padx=10, pady=5)

        # Exportar Treeview a la clase
        self.treeview = treeview

    def fill_treeview(self, treeview):
        # Limpiar datos existentes
        for item in treeview.get_children():
            treeview.delete(item)
        # Poblar con datos actuales
        for cliente in db.Clientes.lista:
            treeview.insert(
                parent='', index='end', iid=cliente.dni,
                values=(cliente.dni, cliente.nombre, cliente.apellido)
            )

    def list_clients(self):
        # Mostrar todos los clientes en un cuadro de mensaje
        clientes = "\n".join([str(cliente) for cliente in db.Clientes.lista])
        showinfo("Lista de Clientes", clientes if clientes else "No hay clientes registrados.")

    def search_client(self):
        # Abrir un cuadro para buscar un cliente por DNI
        search_window = Toplevel(self)
        search_window.title("Buscar Cliente")
        search_window.geometry("300x150")
        search_window.transient(self)
        search_window.grab_set()

        Label(search_window, text="Ingrese el DNI del cliente:").pack(pady=10)
        dni_entry = Entry(search_window)
        dni_entry.pack(pady=5)

        def perform_search():
            dni = dni_entry.get().upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                showinfo("Cliente Encontrado", str(cliente))
            else:
                showinfo("Cliente No Encontrado", "No se encontró un cliente con ese DNI.")
            search_window.destroy()

        Button(search_window, text="Buscar", command=perform_search).pack(pady=10)

    def delete(self):
        cliente = self.treeview.focus()
        if cliente:
            campos = self.treeview.item(cliente, 'values')
            confirmar = askokcancel(
                title='Confirmación',
                message=f'¿Borrar a {campos[1]} {campos[2]}?',
                icon=WARNING)
            if confirmar:
                self.treeview.delete(cliente)
                db.Clientes.borrar(campos[0])

    def create_client_window(self):
        CreateClientWindow(self)

    def edit_client_window(self):
        cliente = self.treeview.focus()
        if cliente:
            EditClientWindow(self, self.treeview.item(cliente, 'values'))

class CreateClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Crear cliente')
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()

    def build(self):
        # Top frame
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        # Labels
        Label(frame, text="DNI (2 ints y 1 upper char)").grid(row=0, column=0)
        Label(frame, text="Nombre (2 a 30 chars)").grid(row=0, column=1)
        Label(frame, text="Apellido (2 a 30 chars)").grid(row=0, column=2)

        # Entries
        self.dni = Entry(frame)
        self.dni.grid(row=1, column=0)
        self.dni.bind("<KeyRelease>", lambda ev: self.validate(ev, 0))

        self.nombre = Entry(frame)
        self.nombre.grid(row=1, column=1)
        self.nombre.bind("<KeyRelease>", lambda ev: self.validate(ev, 1))

        self.apellido = Entry(frame)
        self.apellido.grid(row=1, column=2)
        self.apellido.bind("<KeyRelease>", lambda ev: self.validate(ev, 2))

        # Bottom frame
        frame = Frame(self)
        frame.pack(pady=10)

        # Buttons
        self.crear = Button(frame, text="Crear", command=self.create_client)
        self.crear.configure(state=DISABLED)
        self.crear.grid(row=0, column=0)
        Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1)

        # Validation states
        self.validaciones = [0, 0, 0]

    def validate(self, event, index):
        valor = event.widget.get()
        valido = helpers.dni_valido(valor, db.Clientes.lista) if index == 0 else (
            valor.isalpha() and 2 <= len(valor) <= 30
        )
        event.widget.configure({"bg": "Green" if valido else "Red"})
        self.validaciones[index] = valido
        self.crear.config(state=NORMAL if self.validaciones == [1, 1, 1] else DISABLED)

    def create_client(self):
        db.Clientes.crear(self.dni.get(), self.nombre.get(), self.apellido.get())
        self.master.treeview.insert(
            parent='', index='end', iid=self.dni.get(),
            values=(self.dni.get(), self.nombre.get(), self.apellido.get())
        )
        self.close()

    def close(self):
        self.destroy()
        self.update()

class EditClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent, cliente):
        super().__init__(parent)
        self.title('Actualizar cliente')
        self.build(cliente)
        self.center()
        self.transient(parent)
        self.grab_set()

    def build(self, cliente):
        # Top frame
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        # Labels
        Label(frame, text="DNI (no editable)").grid(row=0, column=0)
        Label(frame, text="Nombre (2 a 30 chars)").grid(row=0, column=1)
        Label(frame, text="Apellido (2 a 30 chars)").grid(row=0, column=2)

        # Entries
        self.dni = Entry(frame)
        self.dni.grid(row=1, column=0)
        self.dni.insert(0, cliente[0])
        self.dni.config(state=DISABLED)

        self.nombre = Entry(frame)
        self.nombre.grid(row=1, column=1)
        self.nombre.insert(0, cliente[1])
        self.nombre.bind("<KeyRelease>", lambda ev: self.validate(ev, 0))

        self.apellido = Entry(frame)
        self.apellido.grid(row=1, column=2)
        self.apellido.insert(0, cliente[2])
        self.apellido.bind("<KeyRelease>", lambda ev: self.validate(ev, 1))

        # Bottom frame
        frame = Frame(self)
        frame.pack(pady=10)

        # Buttons
        self.actualizar = Button(frame, text="Actualizar", command=self.update_client)
        self.actualizar.grid(row=0, column=0)
        Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1)

        # Validation states
        self.validaciones = [1, 1]

    def validate(self, event, index):
        valor = event.widget.get()
        valido = valor.isalpha() and 2 <= len(valor) <= 30
        event.widget.configure({"bg": "Green" if valido else "Red"})
        self.validaciones[index] = valido
        self.actualizar.config(state=NORMAL if self.validaciones == [1, 1] else DISABLED)

    def update_client(self):
        db.Clientes.modificar(self.dni.get(), self.nombre.get(), self.apellido.get())
        self.master.treeview.item(
            self.master.treeview.focus(),
            values=(self.dni.get(), self.nombre.get(), self.apellido.get())
        )
        self.close()

    def close(self):
        self.destroy()
        self.update()

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()