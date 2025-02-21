from flask import Blueprint, request, jsonify
from routes.base_routes import BaseRoutes
from services.base_service import BaseService
from repositories.base_repository import BaseRepository
from models import db, Paciente, Medico, Cita, Tratamiento

# Este archivo contiene las rutas para los endpoints relacionados con la tabla de la clínica
bp = Blueprint('clinica', __name__)

# Se crean los servicios para cada tabla
paciente_service = BaseService(BaseRepository(db, Paciente))
medico_service = BaseService(BaseRepository(db, Medico))
cita_service = BaseService(BaseRepository(db, Cita))
tratamiento_service = BaseService(BaseRepository(db, Tratamiento))

# Los servicios se utilizan para crear las rutas de cada tabla
pacientes_routes = BaseRoutes(
    paciente_service,
    Paciente,
    ['nombre', 'direccion', 'telefono', 'fecha_nacimiento', 'historial_medico'],
    'Paciente'
)

# Se definen las rutas del método GET, POST, PUT y DELETE para la tabla de pacientes
@bp.route('/pacientes', methods=['GET'])
def get_pacientes():
    """
    Obtiene todos los pacientes.

    Returns:
        Response: Respuesta con la lista de todos los pacientes.
    """
    return pacientes_routes.get_all()

@bp.route('/pacientes', methods=['POST'])
def add_paciente():
    """
    Agrega un nuevo paciente.

    Returns:
        Response: Respuesta con el paciente agregado.
    """
    return pacientes_routes.create()

@bp.route('/pacientes/<int:id>', methods=['PUT'])
def update_paciente(id):
    """
    Actualiza un paciente existente.

    Args:
        id (int): Identificador del paciente a actualizar.

    Returns:
        Response: Respuesta con el paciente actualizado.
    """
    return pacientes_routes.update(id)

@bp.route('/pacientes/<int:id>', methods=['DELETE'])
def delete_paciente(id):
    """
    Elimina un paciente existente.

    Args:
        id (int): Identificador del paciente a eliminar.

    Returns:
        Response: Respuesta indicando si el paciente fue eliminado.
    """
    return pacientes_routes.delete(id)

# Médicos routes
medicos_routes = BaseRoutes(
    medico_service,
    Medico,
    ['nombre', 'especialidad', 'licencia_medica', 'informacion_contacto'],
    'Médico'
)

@bp.route('/medicos', methods=['GET'])
def get_medicos():
    """
    Obtiene todos los médicos.

    Returns:
        Response: Respuesta con la lista de todos los médicos.
    """
    return medicos_routes.get_all()

@bp.route('/medicos', methods=['POST'])
def add_medico():
    """
    Agrega un nuevo médico.

    Returns:
        Response: Respuesta con el médico agregado.
    """
    return medicos_routes.create()

@bp.route('/medicos/<int:id>', methods=['PUT'])
def update_medico(id):
    """
    Actualiza un médico existente.

    Args:
        id (int): Identificador del médico a actualizar.

    Returns:
        Response: Respuesta con el médico actualizado.
    """
    return medicos_routes.update(id)

@bp.route('/medicos/<int:id>', methods=['DELETE'])
def delete_medico(id):
    """
    Elimina un médico existente.

    Args:
        id (int): Identificador del médico a eliminar.

    Returns:
        Response: Respuesta indicando si el médico fue eliminado.
    """
    return medicos_routes.delete(id)

# Citas routes
citas_routes = BaseRoutes(
    cita_service,
    Cita,
    ['id_paciente', 'id_medico', 'fecha_hora', 'motivo_visita'],
    'Cita'
)

@bp.route('/citas', methods=['GET'])
def get_citas():
    """
    Obtiene todas las citas.

    Returns:
        Response: Respuesta con la lista de todas las citas.
    """
    return citas_routes.get_all()

@bp.route('/citas', methods=['POST'])
def add_cita():
    """
    Agrega una nueva cita.

    Returns:
        Response: Respuesta con la cita agregada.
    """
    return citas_routes.create()

@bp.route('/citas/<int:id>', methods=['PUT'])
def update_cita(id):
    """
    Actualiza una cita existente.

    Args:
        id (int): Identificador de la cita a actualizar.

    Returns:
        Response: Respuesta con la cita actualizada.
    """
    return citas_routes.update(id)

@bp.route('/citas/<int:id>', methods=['DELETE'])
def delete_cita(id):
    """
    Elimina una cita existente.

    Args:
        id (int): Identificador de la cita a eliminar.

    Returns:
        Response: Respuesta indicando si la cita fue eliminada.
    """
    return citas_routes.delete(id)

# Tratamientos routes
tratamientos_routes = BaseRoutes(
    tratamiento_service,
    Tratamiento,
    ['nombre', 'descripcion', 'costo'],
    'Tratamiento'
)

@bp.route('/tratamientos', methods=['GET'])
def get_tratamientos():
    """
    Obtiene todos los tratamientos.

    Returns:
        Response: Respuesta con la lista de todos los tratamientos.
    """
    return tratamientos_routes.get_all()

@bp.route('/tratamientos', methods=['POST'])
def add_tratamiento():
    """
    Agrega un nuevo tratamiento.

    Returns:
        Response: Respuesta con el tratamiento agregado.
    """
    return tratamientos_routes.create()

@bp.route('/tratamientos/<int:id>', methods=['PUT'])
def update_tratamiento(id):
    """
    Actualiza un tratamiento existente.

    Args:
        id (int): Identificador del tratamiento a actualizar.

    Returns:
        Response: Respuesta con el tratamiento actualizado.
    """
    return tratamientos_routes.update(id)

@bp.route('/tratamientos/<int:id>', methods=['DELETE'])
def delete_tratamiento(id):
    """
    Elimina un tratamiento existente.

    Args:
        id (int): Identificador del tratamiento a eliminar.

    Returns:
        Response: Respuesta indicando si el tratamiento fue eliminado.
    """
    return tratamientos_routes.delete(id)