from models import db
from sqlalchemy.orm import validates

class Paciente(db.Model):
    """
    Modelo que representa a un paciente.

    Atributos:
        __bind_key__ (str): Enlace a la base de datos 'clinica'.
        __tablename__ (str): Nombre de la tabla en la base de datos.
        id (int): Identificador único del paciente.
        nombre (str): Nombre del paciente.
        direccion (str): Dirección del paciente.
        telefono (str): Teléfono del paciente.
        fecha_nacimiento (date): Fecha de nacimiento del paciente.
        historial_medico (str): Historial médico del paciente.
        citas (list): Lista de citas asociadas al paciente.
    """
    __bind_key__ = 'clinica'
    __tablename__ = 'paciente'
    id = db.Column('ID_Paciente', db.Integer, primary_key=True)
    nombre = db.Column('Nombre', db.String(100), nullable=False)
    direccion = db.Column('Direccion', db.String(255), nullable=False)
    telefono = db.Column('Telefono', db.String(15), nullable=False)
    fecha_nacimiento = db.Column('Fecha_Nacimiento', db.Date, nullable=False)
    historial_medico = db.Column('Historial_Medico', db.Text, nullable=False)
    citas = db.relationship('Cita', backref='paciente', lazy=True)

    @validates('telefono')
    def validate_telefono(self, key, telefono):
        """
        Valida que el teléfono tenga un máximo de 15 caracteres.

        Args:
            key (str): Nombre del campo.
            telefono (str): Valor del teléfono a validar.

        Returns:
            str: Teléfono validado.

        Raises:
            AssertionError: Si el teléfono tiene más de 15 caracteres.
        """
        assert len(telefono) <= 15, "El teléfono debe tener máximo 15 caracteres"
        return telefono

class Medico(db.Model):
    """
    Modelo que representa a un médico.

    Atributos:
        __bind_key__ (str): Enlace a la base de datos 'clinica'.
        __tablename__ (str): Nombre de la tabla en la base de datos.
        id (int): Identificador único del médico.
        nombre (str): Nombre del médico.
        especialidad (str): Especialidad del médico.
        licencia_medica (str): Licencia médica del médico.
        informacion_contacto (str): Información de contacto del médico.
        citas (list): Lista de citas asociadas al médico.
    """
    __bind_key__ = 'clinica'
    __tablename__ = 'medico'
    id = db.Column('ID_Medico', db.Integer, primary_key=True)
    nombre = db.Column('Nombre', db.String(100), nullable=False)
    especialidad = db.Column('Especialidad', db.String(100), nullable=False)
    licencia_medica = db.Column('Licencia_Medica', db.String(50), nullable=False)
    informacion_contacto = db.Column('Informacion_Contacto', db.Text, nullable=False)
    citas = db.relationship('Cita', backref='medico', lazy=True)

class Cita(db.Model):
    """
    Modelo que representa una cita médica.

    Atributos:
        __bind_key__ (str): Enlace a la base de datos 'clinica'.
        __tablename__ (str): Nombre de la tabla en la base de datos.
        id (int): Identificador único de la cita.
        id_paciente (int): Identificador del paciente asociado a la cita.
        id_medico (int): Identificador del médico asociado a la cita.
        fecha_hora (datetime): Fecha y hora de la cita.
        motivo_visita (str): Motivo de la visita.
    """
    __bind_key__ = 'clinica'
    __tablename__ = 'cita'
    id = db.Column('ID_Cita', db.Integer, primary_key=True)
    id_paciente = db.Column('ID_Paciente', db.Integer, db.ForeignKey('paciente.ID_Paciente'), nullable=False)
    id_medico = db.Column('ID_Medico', db.Integer, db.ForeignKey('medico.ID_Medico'), nullable=False)
    fecha_hora = db.Column('Fecha_Hora', db.DateTime, nullable=False, default=db.func.current_timestamp())
    motivo_visita = db.Column('Motivo_Visita', db.Text, nullable=False)

class Tratamiento(db.Model):
    """
    Modelo que representa un tratamiento médico.

    Atributos:
        __bind_key__ (str): Enlace a la base de datos 'clinica'.
        __tablename__ (str): Nombre de la tabla en la base de datos.
        id (int): Identificador único del tratamiento.
        nombre (str): Nombre del tratamiento.
        descripcion (str): Descripción del tratamiento.
        costo (decimal): Costo del tratamiento.
    """
    __bind_key__ = 'clinica'
    __tablename__ = 'tratamiento'
    id = db.Column('ID_Tratamiento', db.Integer, primary_key=True)
    nombre = db.Column('Nombre', db.String(100), nullable=False)
    descripcion = db.Column('Descripcion', db.Text, nullable=False)
    costo = db.Column('Costo', db.Numeric(10, 2), nullable=False)