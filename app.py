# app.py

# Sistema de Gestión Multibase
# Copyright (C) 2025 David Javier Toscano Rico
#
# Este programa es software libre: puede redistribuirlo y/o modificarlo
# bajo los términos de la Licencia Pública General de GNU según lo publicado por
# la Free Software Foundation, ya sea la versión 3 de la Licencia, o
# (a su elección) cualquier versión posterior.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA; sin siquiera la garantía implícita de
# COMERCIABILIDAD o IDONEIDAD PARA UN PROPÓSITO PARTICULAR. Vea la
# Licencia Pública General de GNU para más detalles.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import pymysql
from models import init_db
from routes import clinica_routes, restaurante_routes, automoviles_routes

# Instala el controlador MySQLdb para pymysql
pymysql.install_as_MySQLdb()
# Carga las variables de entorno desde un archivo .env
def create_app():
    """
    Crea y configura una instancia de la aplicación Flask.

    Returns:
        Flask: La aplicación Flask configurada.
    """
    flask_app = Flask(__name__)

    # Obtiene las credenciales de la base de datos desde las variables de entorno
    db_username = os.getenv('DB_USERNAME')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')

    # Configura la conexión a la base de datos
    connection_params = f'mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}'
    connection_args = {'ssl': {'ssl-mode': 'disabled'}, 'auth_plugin': 'mysql_native_password'}

    # Configura las URIs de las bases de datos
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = f'{connection_params}/clinica?charset=utf8mb4'
    flask_app.config['SQLALCHEMY_BINDS'] = {
        'clinica': f'{connection_params}/clinica?charset=utf8mb4',
        'restaurante': f'{connection_params}/restaurante?charset=utf8mb4',
        'automoviles': f'{connection_params}/venta_automoviles?charset=utf8mb4'
    }
    flask_app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'connect_args': connection_args
    }
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa la base de datos
    init_db(flask_app)

    # Registra los blueprints con prefijos de URL
    flask_app.register_blueprint(clinica_routes.bp, url_prefix='/api/clinica')
    flask_app.register_blueprint(restaurante_routes.bp, url_prefix='/api/restaurante')
    flask_app.register_blueprint(automoviles_routes.bp, url_prefix='/api/automoviles')

    return flask_app

# Crea una instancia de la aplicación
app = create_app()

if __name__ == '__main__':
    # Ejecuta la aplicación en modo de depuración
    app.run(debug=True)