# Este archivo se encarga de importar las rutas de los diferentes modulos de la aplicacion.
from .clinica_routes import bp as clinica_bp
from .restaurante_routes import bp as restaurante_bp
from .automoviles_routes import bp as automoviles_bp

# Se importan las rutas de los modulos de la aplicacion.
__all__ = ['clinica_bp', 'restaurante_bp', 'automoviles_bp']