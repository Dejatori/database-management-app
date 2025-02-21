# Este archivo contiene las rutas para los endpoints relacionados con la tabla de automóviles
from flask import Blueprint, request, jsonify
from routes.base_routes import BaseRoutes
from services.base_service import BaseService
from repositories.base_repository import BaseRepository
from models import db, ClienteAutomoviles, Vendedor, Vehiculo, Venta

# Esta variable contiene la definición de la ruta de este archivo
bp = Blueprint('automoviles', __name__)

# Se crean los servicios para cada tabla
cliente_service = BaseService(BaseRepository(db, ClienteAutomoviles))
vendedor_service = BaseService(BaseRepository(db, Vendedor))
vehiculo_service = BaseService(BaseRepository(db, Vehiculo))
venta_service = BaseService(BaseRepository(db, Venta))

# Los servicios se utilizan para crear las rutas de cada tabla
clientes_routes = BaseRoutes(
    cliente_service,
    ClienteAutomoviles,
    ['nombre', 'direccion', 'correo_electronico', 'telefono'],
    'Cliente'
)

# Se definen las rutas del método GET, POST, PUT y DELETE para la tabla de automóviles
@bp.route('/clientes_automoviles', methods=['GET'])
def get_clientes_automoviles():
    """
    Obtiene todos los clientes de automóviles.

    Returns:
        Response: Respuesta con la lista de todos los clientes.
    """
    return clientes_routes.get_all()

@bp.route('/clientes_automoviles', methods=['POST'])
def add_cliente_automoviles():
    """
    Agrega un nuevo cliente de automóviles.

    Returns:
        Response: Respuesta con el cliente agregado.
    """
    return clientes_routes.create()

@bp.route('/clientes_automoviles/<int:id>', methods=['PUT'])
def update_cliente_automoviles(id):
    """
    Actualiza un cliente de automóviles existente.

    Args:
        id (int): Identificador del cliente a actualizar.

    Returns:
        Response: Respuesta con el cliente actualizado.
    """
    return clientes_routes.update(id)

@bp.route('/clientes_automoviles/<int:id>', methods=['DELETE'])
def delete_cliente_automoviles(id):
    """
    Elimina un cliente de automóviles existente.

    Args:
        id (int): Identificador del cliente a eliminar.

    Returns:
        Response: Respuesta indicando si el cliente fue eliminado.
    """
    return clientes_routes.delete(id)

# Las demás rutas se crean de la misma forma que las de los clientes
vendedores_routes = BaseRoutes(
    vendedor_service,
    Vendedor,
    ['nombre', 'direccion', 'telefono', 'fecha_contratacion'],
    'Vendedor'
)

@bp.route('/vendedores', methods=['GET'])
def get_vendedores():
    """
    Obtiene todos los vendedores.

    Returns:
        Response: Respuesta con la lista de todos los vendedores.
    """
    return vendedores_routes.get_all()

@bp.route('/vendedores', methods=['POST'])
def add_vendedor():
    """
    Agrega un nuevo vendedor.

    Returns:
        Response: Respuesta con el vendedor agregado.
    """
    return vendedores_routes.create()

@bp.route('/vendedores/<int:id>', methods=['PUT'])
def update_vendedor(id):
    """
    Actualiza un vendedor existente.

    Args:
        id (int): Identificador del vendedor a actualizar.

    Returns:
        Response: Respuesta con el vendedor actualizado.
    """
    return vendedores_routes.update(id)

@bp.route('/vendedores/<int:id>', methods=['DELETE'])
def delete_vendedor(id):
    """
    Elimina un vendedor existente.

    Args:
        id (int): Identificador del vendedor a eliminar.

    Returns:
        Response: Respuesta indicando si el vendedor fue eliminado.
    """
    return vendedores_routes.delete(id)

# Vehículos routes
vehiculos_routes = BaseRoutes(
    vehiculo_service,
    Vehiculo,
    ['vin', 'marca', 'modelo', 'anio', 'color', 'tipo', 'precio', 'fecha_recepcion'],
    'Vehículo'
)

@bp.route('/vehiculos', methods=['GET'])
def get_vehiculos():
    """
    Obtiene todos los vehículos.

    Returns:
        Response: Respuesta con la lista de todos los vehículos.
    """
    return vehiculos_routes.get_all()

@bp.route('/vehiculos', methods=['POST'])
def add_vehiculo():
    """
    Agrega un nuevo vehículo.

    Returns:
        Response: Respuesta con el vehículo agregado.
    """
    return vehiculos_routes.create()

@bp.route('/vehiculos/<string:vin>', methods=['PUT'])
def update_vehiculo(vin):
    """
    Actualiza un vehículo existente.

    Args:
        vin (str): Identificador del vehículo a actualizar.

    Returns:
        Response: Respuesta con el vehículo actualizado.
    """
    return vehiculos_routes.update(vin)

@bp.route('/vehiculos/<string:vin>', methods['DELETE'])
def delete_vehiculo(vin):
    """
    Elimina un vehículo existente.

    Args:
        vin (str): Identificador del vehículo a eliminar.

    Returns:
        Response: Respuesta indicando si el vehículo fue eliminado.
    """
    return vehiculos_routes.delete(vin)

# Ventas routes
ventas_routes = BaseRoutes(
    venta_service,
    Venta,
    ['id_cliente', 'id_vendedor', 'vin', 'fecha', 'precio'],
    'Venta'
)

@bp.route('/ventas', methods=['GET'])
def get_ventas():
    """
    Obtiene todas las ventas.

    Returns:
        Response: Respuesta con la lista de todas las ventas.
    """
    return ventas_routes.get_all()

@bp.route('/ventas', methods=['POST'])
def add_venta():
    """
    Agrega una nueva venta.

    Returns:
        Response: Respuesta con la venta agregada.
    """
    return ventas_routes.create()

@bp.route('/ventas/<int:id>', methods=['PUT'])
def update_venta(id):
    """
    Actualiza una venta existente.

    Args:
        id (int): Identificador de la venta a actualizar.

    Returns:
        Response: Respuesta con la venta actualizada.
    """
    return ventas_routes.update(id)

@bp.route('/ventas/<int:id>', methods=['DELETE'])
def delete_venta(id):
    """
    Elimina una venta existente.

    Args:
        id (int): Identificador de la venta a eliminar.

    Returns:
        Response: Respuesta indicando si la venta fue eliminada.
    """
    return ventas_routes.delete(id)