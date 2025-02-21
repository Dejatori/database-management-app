from models import db
from sqlalchemy.orm import validates

class ClienteAutomoviles(db.Model):
    """
    Modelo que representa a un cliente de automóviles.

    Atributos:
        __bind_key__ (str): Enlace a la base de datos 'automoviles'.
        __tablename__ (str): Nombre de la tabla en la base de datos.
        id (int): Identificador único del cliente.
        nombre (str): Nombre del cliente.
        direccion (str): Dirección del cliente.
        correo_electronico (str): Correo electrónico del cliente.
        telefono (str): Teléfono del cliente.
        ventas (list): Lista de ventas asociadas al cliente.
    """
    __bind_key__ = 'automoviles'
    __tablename__ = 'cliente'

    id = db.Column('ID_Cliente', db.Integer, primary_key=True)
    nombre = db.Column('Nombre', db.String(100), nullable=False)
    direccion = db.Column('Direccion', db.String(255), nullable=False)
    correo_electronico = db.Column('Correo_Electronico', db.String(100), nullable=False, unique=True)
    telefono = db.Column('Telefono', db.String(15), nullable=False)
    ventas = db.relationship('Venta', backref='cliente', lazy=True)

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

class Vendedor(db.Model):
    """
    Modelo que representa a un vendedor.

    Atributos:
        __bind_key__ (str): Enlace a la base de datos 'automoviles'.
        __tablename__ (str): Nombre de la tabla en la base de datos.
        id (int): Identificador único del vendedor.
        nombre (str): Nombre del vendedor.
        direccion (str): Dirección del vendedor.
        telefono (str): Teléfono del vendedor.
        fecha_contratacion (datetime): Fecha de contratación del vendedor.
        ventas (list): Lista de ventas asociadas al vendedor.
    """
    __bind_key__ = 'automoviles'
    __tablename__ = 'vendedor'
    id = db.Column('ID_Vendedor', db.Integer, primary_key=True)
    nombre = db.Column('Nombre', db.String(100), nullable=False)
    direccion = db.Column('Direccion', db.String(255), nullable=False)
    telefono = db.Column('Telefono', db.String(15), nullable=False)
    fecha_contratacion = db.Column('Fecha_Contratacion', db.DateTime, nullable=False, default=db.func.current_timestamp())
    ventas = db.relationship('Venta', backref='vendedor', lazy=True)

class Vehiculo(db.Model):
    """
    Modelo que representa a un vehículo.

    Atributos:
        __bind_key__ (str): Enlace a la base de datos 'automoviles'.
        __tablename__ (str): Nombre de la tabla en la base de datos.
        vin (str): Número de identificación del vehículo (VIN).
        marca (str): Marca del vehículo.
        modelo (str): Modelo del vehículo.
        anio (int): Año del vehículo.
        color (str): Color del vehículo.
        tipo (str): Tipo del vehículo.
        precio (decimal): Precio del vehículo.
        fecha_recepcion (datetime): Fecha de recepción del vehículo.
        ventas (list): Lista de ventas asociadas al vehículo.
    """
    __bind_key__ = 'automoviles'
    __tablename__ = 'vehiculo'
    vin = db.Column('VIN', db.String(17), primary_key=True)
    marca = db.Column('Marca', db.String(50), nullable=False)
    modelo = db.Column('Modelo', db.String(50), nullable=False)
    anio = db.Column('Anio', db.Integer, nullable=False)
    color = db.Column('Color', db.String(20), nullable=False)
    tipo = db.Column('Tipo', db.String(50), nullable=False)
    precio = db.Column('Precio', db.Numeric(10, 2), nullable=False)
    fecha_recepcion = db.Column('Fecha_Recepcion', db.DateTime, nullable=False, default=db.func.current_timestamp())
    ventas = db.relationship('Venta', backref='vehiculo', lazy=True)

class Venta(db.Model):
    """
    Modelo que representa una venta.

    Atributos:
        __bind_key__ (str): Enlace a la base de datos 'automoviles'.
        __tablename__ (str): Nombre de la tabla en la base de datos.
        id (int): Identificador único de la venta.
        id_cliente (int): Identificador del cliente asociado a la venta.
        id_vendedor (int): Identificador del vendedor asociado a la venta.
        vin (str): Número de identificación del vehículo (VIN) asociado a la venta.
        fecha (datetime): Fecha de la venta.
        precio (decimal): Precio de la venta.
    """
    __bind_key__ = 'automoviles'
    __tablename__ = 'venta'
    id = db.Column('ID_Venta', db.Integer, primary_key=True)
    id_cliente = db.Column('ID_Cliente', db.Integer, db.ForeignKey('cliente.ID_Cliente'), nullable=False)
    id_vendedor = db.Column('ID_Vendedor', db.Integer, db.ForeignKey('vendedor.ID_Vendedor'), nullable=False)
    vin = db.Column('VIN', db.String(17), db.ForeignKey('vehiculo.VIN'), nullable=False)
    fecha = db.Column('Fecha', db.DateTime, nullable=False, default=db.func.current_timestamp())
    precio = db.Column('Precio', db.Numeric(10, 2), nullable=False)