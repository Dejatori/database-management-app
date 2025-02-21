from flask import Blueprint, request, jsonify
from routes.base_routes import BaseRoutes
from services.base_service import BaseService
from repositories.base_repository import BaseRepository
from models import db, ClienteRestaurante, Empleado, Plato, Ingrediente, Pedido

# Este archivo contiene las rutas para los endpoints relacionados con la tabla del restaurante
bp = Blueprint('restaurante', __name__)

# Se crean los servicios para cada tabla
cliente_service = BaseService(BaseRepository(db, ClienteRestaurante))
empleado_service = BaseService(BaseRepository(db, Empleado))
plato_service = BaseService(BaseRepository(db, Plato))
ingrediente_service = BaseService(BaseRepository(db, Ingrediente))
pedido_service = BaseService(BaseRepository(db, Pedido))

# Los servicios se utilizan para crear las rutas de cada tabla
clientes_routes = BaseRoutes(
    cliente_service,
    ClienteRestaurante,
    ['nombre', 'correo_electronico', 'telefono'],
    'Cliente'
)

# Se definen las rutas del método GET, POST, PUT y DELETE para la tabla de clientes del restaurante
@bp.route('/clientes_restaurante', methods=['GET'])
def get_clientes():
    """
    Obtiene todos los clientes del restaurante.

    Returns:
        Response: Respuesta con la lista de todos los clientes.
    """
    return clientes_routes.get_all()

@bp.route('/clientes_restaurante', methods=['POST'])
def add_cliente():
    """
    Agrega un nuevo cliente del restaurante.

    Returns:
        Response: Respuesta con el cliente agregado.
    """
    return clientes_routes.create()

@bp.route('/clientes_restaurante/<int:id>', methods=['PUT'])
def update_cliente(id):
    """
    Actualiza un cliente del restaurante existente.

    Args:
        id (int): Identificador del cliente a actualizar.

    Returns:
        Response: Respuesta con el cliente actualizado.
    """
    return clientes_routes.update(id)

@bp.route('/clientes_restaurante/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    """
    Elimina un cliente del restaurante existente.

    Args:
        id (int): Identificador del cliente a eliminar.

    Returns:
        Response: Respuesta indicando si el cliente fue eliminado.
    """
    return clientes_routes.delete(id)

# Empleados routes
empleados_routes = BaseRoutes(
    empleado_service,
    Empleado,
    ['nombre', 'posicion', 'fecha_contratacion'],
    'Empleado'
)

@bp.route('/empleados', methods=['GET'])
def get_empleados():
    """
    Obtiene todos los empleados.

    Returns:
        Response: Respuesta con la lista de todos los empleados.
    """
    return empleados_routes.get_all()

@bp.route('/empleados', methods=['POST'])
def add_empleado():
    """
    Agrega un nuevo empleado.

    Returns:
        Response: Respuesta con el empleado agregado.
    """
    return empleados_routes.create()

@bp.route('/empleados/<int:id>', methods=['PUT'])
def update_empleado(id):
    """
    Actualiza un empleado existente.

    Args:
        id (int): Identificador del empleado a actualizar.

    Returns:
        Response: Respuesta con el empleado actualizado.
    """
    return empleados_routes.update(id)

@bp.route('/empleados/<int:id>', methods=['DELETE'])
def delete_empleado(id):
    """
    Elimina un empleado existente.

    Args:
        id (int): Identificador del empleado a eliminar.

    Returns:
        Response: Respuesta indicando si el empleado fue eliminado.
    """
    return empleados_routes.delete(id)

# Platos routes
platos_routes = BaseRoutes(
    plato_service,
    Plato,
    ['nombre', 'cantidad_disponible', 'unidad_medida'],
    'Plato'
)

@bp.route('/platos', methods=['GET'])
def get_platos():
    """
    Obtiene todos los platos.

    Returns:
        Response: Respuesta con la lista de todos los platos.
    """
    return platos_routes.get_all()

@bp.route('/platos', methods=['POST'])
def add_plato():
    """
    Agrega un nuevo plato.

    Returns:
        Response: Respuesta con el plato agregado.
    """
    return platos_routes.create()

@bp.route('/platos/<int:id>', methods=['PUT'])
def update_plato(id):
    """
    Actualiza un plato existente.

    Args:
        id (int): Identificador del plato a actualizar.

    Returns:
        Response: Respuesta con el plato actualizado.
    """
    return platos_routes.update(id)

@bp.route('/platos/<int:id>', methods=['DELETE'])
def delete_plato(id):
    """
    Elimina un plato existente.

    Args:
        id (int): Identificador del plato a eliminar.

    Returns:
        Response: Respuesta indicando si el plato fue eliminado.
    """
    return platos_routes.delete(id)

# Ingredientes routes
ingredientes_routes = BaseRoutes(
    ingrediente_service,
    Ingrediente,
    ['nombre', 'cantidad_disponible', 'unidad_medida'],
    'Ingrediente'
)

@bp.route('/ingredientes', methods=['GET'])
def get_ingredientes():
    """
    Obtiene todos los ingredientes.

    Returns:
        Response: Respuesta con la lista de todos los ingredientes.
    """
    return ingredientes_routes.get_all()

@bp.route('/ingredientes', methods=['POST'])
def add_ingrediente():
    """
    Agrega un nuevo ingrediente.

    Returns:
        Response: Respuesta con el ingrediente agregado.
    """
    return ingredientes_routes.create()

@bp.route('/ingredientes/<int:id>', methods=['PUT'])
def update_ingrediente(id):
    """
    Actualiza un ingrediente existente.

    Args:
        id (int): Identificador del ingrediente a actualizar.

    Returns:
        Response: Respuesta con el ingrediente actualizado.
    """
    return ingredientes_routes.update(id)

@bp.route('/ingredientes/<int:id>', methods=['DELETE'])
def delete_ingrediente(id):
    """
    Elimina un ingrediente existente.

    Args:
        id (int): Identificador del ingrediente a eliminar.

    Returns:
        Response: Respuesta indicando si el ingrediente fue eliminado.
    """
    return ingredientes_routes.delete(id)

# Pedidos routes
pedidos_routes = BaseRoutes(
    pedido_service,
    Pedido,
    ['id_cliente', 'id_empleado', 'fecha_hora'],
    'Pedido'
)

@bp.route('/pedidos', methods=['GET'])
def get_pedidos():
    """
    Obtiene todos los pedidos.

    Returns:
        Response: Respuesta con la lista de todos los pedidos.
    """
    return pedidos_routes.get_all()

@bp.route('/pedidos', methods=['POST'])
def add_pedido():
    """
    Agrega un nuevo pedido.

    Returns:
        Response: Respuesta con el pedido agregado.
    """
    return pedidos_routes.create()

@bp.route('/pedidos/<int:id>', methods=['PUT'])
def update_pedido(id):
    """
    Actualiza un pedido existente.

    Args:
        id (int): Identificador del pedido a actualizar.

    Returns:
        Response: Respuesta con el pedido actualizado.
    """
    return pedidos_routes.update(id)

@bp.route('/pedidos/<int:id>', methods=['DELETE'])
def delete_pedido(id):
    """
    Elimina un pedido existente.

    Args:
        id (int): Identificador del pedido a eliminar.

    Returns:
        Response: Respuesta indicando si el pedido fue eliminado.
    """
    return pedidos_routes.delete(id)