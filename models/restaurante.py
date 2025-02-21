from models import db
from sqlalchemy.orm import validates

class ClienteRestaurante(db.Model):
    """
    Modelo que representa a un cliente de restaurante.

    Atributos:
        __bind_key__ (str): Enlace a la base de datos 'restaurante'.
        __tablename__ (str): Nombre de la tabla en la base de datos.
        id (int): Identificador único del cliente.
        nombre (str): Nombre del cliente.
        correo_electronico (str): Correo electrónico del cliente.
        telefono (str): Teléfono del cliente.
        pedidos (list): Lista de pedidos asociados al cliente.
    """
    __bind_key__ = 'restaurante'
    __tablename__ = 'cliente'
    id = db.Column('ID_Cliente', db.Integer, primary_key=True)
    nombre = db.Column('Nombre', db.String(100), nullable=False)
    correo_electronico = db.Column('Correo_Electronico', db.String(100), nullable=False, unique=True)
    telefono = db.Column('Telefono', db.String(15), nullable=False)
    pedidos = db.relationship('Pedido', backref='cliente', lazy=True)

    @validates('correo_electronico')
    def validate_correo_electronico(self, key, correo_electronico):
        """
        Valida que el correo electrónico contenga un '@'.

        Args:
            key (str): Nombre del campo.
            correo_electronico (str): Valor del correo electrónico a validar.

        Returns:
            str: Correo electrónico validado.

        Raises:
            AssertionError: Si el correo electrónico no contiene un '@'.
        """
        assert '@' in correo_electronico, "Correo Electronico debe contener @"
        return correo_electronico

class Empleado(db.Model):
    """
    Modelo que representa a un empleado.

    Atributos:
        __bind_key__ (str): Enlace a la base de datos 'restaurante'.
        __tablename__ (str): Nombre de la tabla en la base de datos.
        id (int): Identificador único del empleado.
        nombre (str): Nombre del empleado.
        posicion (str): Posición del empleado.
        fecha_contratacion (datetime): Fecha de contratación del empleado.
        pedidos (list): Lista de pedidos asociados al empleado.
    """
    __bind_key__ = 'restaurante'
    __tablename__ = 'empleado'
    id = db.Column('ID_Empleado', db.Integer, primary_key=True)
    nombre = db.Column('Nombre', db.String(100), nullable=False)
    posicion = db.Column('Posicion', db.String(50), nullable=False)
    fecha_contratacion = db.Column('Fecha_Contratacion', db.DateTime, nullable=False, default=db.func.current_timestamp())
    pedidos = db.relationship('Pedido', backref='empleado', lazy=True)

class Plato(db.Model):
    """
    Modelo que representa un plato.

    Atributos:
        __bind_key__ (str): Enlace a la base de datos 'restaurante'.
        __tablename__ (str): Nombre de la tabla en la base de datos.
        id (int): Identificador único del plato.
        nombre (str): Nombre del plato.
        cantidad_disponible (int): Cantidad disponible del plato.
        unidad_medida (str): Unidad de medida del plato.
    """
    __bind_key__ = 'restaurante'
    __tablename__ = 'plato'
    id = db.Column('ID_Platillo', db.Integer, primary_key=True)
    nombre = db.Column('Nombre', db.String(100), nullable=False)
    cantidad_disponible = db.Column('Cantidad_Disponible', db.Integer, nullable=False)
    unidad_medida = db.Column('Unidad_Medida', db.String(20), nullable=False)

class Ingrediente(db.Model):
    """
    Modelo que representa un ingrediente.

    Atributos:
        __bind_key__ (str): Enlace a la base de datos 'restaurante'.
        __tablename__ (str): Nombre de la tabla en la base de datos.
        id (int): Identificador único del ingrediente.
        nombre (str): Nombre del ingrediente.
        cantidad_disponible (int): Cantidad disponible del ingrediente.
        unidad_medida (str): Unidad de medida del ingrediente.
    """
    __bind_key__ = 'restaurante'
    __tablename__ = 'ingrediente'
    id = db.Column('ID_Ingrediente', db.Integer, primary_key=True)
    nombre = db.Column('Nombre', db.String(100), nullable=False)
    cantidad_disponible = db.Column('Cantidad_Disponible', db.Integer, nullable=False)
    unidad_medida = db.Column('Unidad_Medida', db.String(20), nullable=False)

class Pedido(db.Model):
    """
    Modelo que representa un pedido.

    Atributos:
        __bind_key__ (str): Enlace a la base de datos 'restaurante'.
        __tablename__ (str): Nombre de la tabla en la base de datos.
        id (int): Identificador único del pedido.
        id_cliente (int): Identificador del cliente asociado al pedido.
        id_empleado (int): Identificador del empleado asociado al pedido.
        fecha_hora (datetime): Fecha y hora del pedido.
    """
    __bind_key__ = 'restaurante'
    __tablename__ = 'pedido'
    id = db.Column('ID_Pedido', db.Integer, primary_key=True)
    id_cliente = db.Column('ID_Cliente', db.Integer, db.ForeignKey('cliente.ID_Cliente'), nullable=False)
    id_empleado = db.Column('ID_Empleado', db.Integer, db.ForeignKey('empleado.ID_Empleado'), nullable=False)
    fecha_hora = db.Column('Fecha_Hora', db.DateTime, nullable=False, default=db.func.current_timestamp())