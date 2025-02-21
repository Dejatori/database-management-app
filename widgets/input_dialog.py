import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime
import re

class InputDialog(tk.Toplevel):
    """
    Clase para crear un cuadro de diálogo de entrada con varios campos.

    Args:
        parent (tk.Tk): Ventana principal de la aplicación.
        title (str): Título del cuadro de diálogo.
        fields (list): Lista de tuplas con el nombre y la etiqueta de cada campo.
        initial_values (list, opcional): Lista de valores iniciales para los campos.
    """

    def __init__(self, parent, title, fields, initial_values=None):
        super().__init__(parent)
        self.result = None
        # Configuración de la ventana
        self.title(title)
        self.transient(parent)
        self.grab_set()
        # Centrar el cuadro de diálogo en la ventana principal
        self.geometry(f"+{parent.winfo_x() + 50}+{parent.winfo_y() + 50}")
        # Crear el formulario
        self.create_form(fields, initial_values)
        # Hacer el cuadro de diálogo modal
        self.wait_window(self)

    def create_form(self, fields, initial_values):
        """
        Crea el formulario con los campos especificados.

        Args:
            fields (list): Lista de tuplas con el nombre y la etiqueta de cada campo.
            initial_values (list, opcional): Lista de valores iniciales para los campos.
        """
        form_frame = ttk.Frame(self, padding="10")
        form_frame.pack(fill='both', expand=True)
        # Diccionario para almacenar los widgets de entrada y sus etiquetas
        self.entries = {}
        self.field_labels = {}
        # Crear campos
        for i, (field, label) in enumerate(fields):
            # Almacenar la etiqueta para cada campo
            self.field_labels[field] = label
            label_widget = ttk.Label(form_frame, text=label)
            label_widget.grid(row=i, column=0, padx=5, pady=5, sticky='e')

            if 'fecha' in field.lower():
                try:
                    initial_date = datetime.now()
                    if initial_values and initial_values[i]:
                        date_str = str(initial_values[i])
                        if '/' in date_str:
                            # Manejar formato DD/MM/YYYY
                            initial_date = datetime.strptime(date_str, '%d/%m/%Y')
                        elif '-' in date_str:
                            # Manejar formato YYYY-MM-DD
                            initial_date = datetime.strptime(date_str, '%Y-%m-%d')
                        elif 'GMT' in date_str:
                            # Manejar formato RFC
                            initial_date = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S GMT')
                        elif 'T' in date_str:
                            # Manejar formato ISO
                            initial_date = datetime.strptime(date_str.split('T')[0], '%Y-%m-%d')

                    date_entry = DateEntry(
                        form_frame,
                        width=12,
                        background='darkblue',
                        foreground='white',
                        borderwidth=2,
                        date_pattern='dd/mm/yyyy',
                        year=initial_date.year,
                        month=initial_date.month,
                        day=initial_date.day
                    )
                    date_entry.grid(row=i, column=1, padx=5, pady=5, sticky='w')
                    self.entries[field] = date_entry

                except (ValueError, TypeError) as e:
                    print(f"Error parsing date for field {field}: {e}")
                    # Volver a la fecha actual si falla el análisis
                    date_entry = DateEntry(
                        form_frame,
                        width=12,
                        background='darkblue',
                        foreground='white',
                        borderwidth=2,
                        date_pattern='dd/mm/yyyy'
                    )
                    date_entry.grid(row=i, column=1, padx=5, pady=5, sticky='w')
                    self.entries[field] = date_entry

            elif 'historial' in field.lower():
                # Crear área de texto para texto más largo
                text_widget = tk.Text(form_frame, height=4, width=40)
                text_widget.grid(row=i, column=1, padx=5, pady=5, sticky='w')
                if initial_values:
                    text_widget.insert('1.0', initial_values[i+1])
                self.entries[field] = text_widget

            elif 'correo' in field.lower():
                # Crear entrada de correo electrónico con validación
                entry = ttk.Entry(form_frame, width=40)
                entry.grid(row=i, column=1, padx=5, pady=5, sticky='w')
                if initial_values:
                    entry.insert(0, initial_values[i+1])
                self.entries[field] = entry

                # Agregar indicador de validación de correo electrónico
                self.email_valid = ttk.Label(form_frame, text="✗", foreground='red')
                self.email_valid.grid(row=i, column=2, padx=5)
                entry.bind('<KeyRelease>', lambda e: self.validate_email(entry.get()))

            else:
                # Crear entrada estándar
                entry = ttk.Entry(form_frame, width=40)
                entry.grid(row=i, column=1, padx=5, pady=5, sticky='w')
                if initial_values:
                    entry.insert(0, initial_values[i+1])
                self.entries[field] = entry

        # Marco de botones
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=len(fields), column=0, columnspan=2, pady=20)

        ttk.Button(button_frame, text="Guardar", command=self.save).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Cancelar", command=self.cancel).pack(side='left', padx=5)

    def validate_email(self, email):
        """
        Valida el formato del correo electrónico.

        Args:
            email (str): Correo electrónico a validar.
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        is_valid = bool(re.match(pattern, email))
        self.email_valid.config(
            text="✓" if is_valid else "✗",
            foreground='green' if is_valid else 'red'
        )

    def save(self):
        """
        Guarda los datos ingresados y cierra el cuadro de diálogo.
        """
        data = {}
        for field, widget in self.entries.items():
            if isinstance(widget, DateEntry):  # Campos de fecha
                # Convertir fecha a formato ISO para la base de datos
                date_obj = widget.get_date()
                data[field] = date_obj.strftime('%Y-%m-%d')
            elif isinstance(widget, tk.Text):  # Áreas de texto
                data[field] = widget.get('1.0', 'end-1c').strip()
            else:  # Entradas regulares
                data[field] = widget.get().strip()

            if not data[field]:
                messagebox.showerror("Error", f"El campo {self.field_labels[field]} es requerido")
                return

            if 'correo' in field.lower() and self.email_valid['text'] == "✗":
                messagebox.showerror("Error", "El correo electrónico no es válido")
                return

        self.result = data
        self.destroy()

    def cancel(self):
        """
        Cancela la operación y cierra el cuadro de diálogo.
        """
        self.destroy()