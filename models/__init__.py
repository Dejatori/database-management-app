# Importa la clase SQLAlchemy de flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# Crea una instancia de SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    """
    Inicializa la base de datos con la aplicación Flask proporcionada.

    Args:
        app (Flask): La instancia de la aplicación Flask.
    """
    db.init_app(app)

# Importa las clases de los modelos
from .clinica import Paciente, Medico, Cita, Tratamiento
from .restaurante import ClienteRestaurante, Empleado, Plato, Ingrediente, Pedido
from .automoviles import ClienteAutomoviles, Vendedor, Vehiculo, Venta

# Define qué elementos se exportan cuando se importa el módulo
__all__ = ['db', 'init_db',
           'Paciente', 'Medico', 'Cita', 'Tratamiento',
           'ClienteRestaurante', 'Empleado', 'Plato', 'Ingrediente', 'Pedido',
           'ClienteAutomoviles', 'Vendedor', 'Vehiculo', 'Venta'
           ]