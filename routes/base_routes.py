from flask import Blueprint, request, jsonify
from services.base_service import BaseService
from models import db

class BaseRoutes:
    """
    Clase base para definir rutas que manejan operaciones CRUD para un modelo específico.

    Atributos:
        service (BaseService): Servicio base para manejar las operaciones CRUD.
        model (db.Model): Modelo de la base de datos para el cual se crean las rutas.
        required_fields (list): Lista de campos requeridos para las operaciones CRUD.
        endpoint (str): Nombre del endpoint para los mensajes de respuesta.
    """

    def __init__(self, service, model, required_fields, endpoint):
        """
        Inicializa la clase BaseRoutes con el servicio, modelo, campos requeridos y endpoint.

        Args:
            service (BaseService): Servicio base para manejar las operaciones CRUD.
            model (db.Model): Modelo de la base de datos.
            required_fields (list): Lista de campos requeridos.
            endpoint (str): Nombre del endpoint.
        """
        self.service = service
        self.model = model
        self.required_fields = required_fields
        self.endpoint = endpoint

    def _get_pagination_params(self):
        """
        Obtiene los parámetros de paginación de la solicitud.

        Returns:
            tuple: Página, tamaño de página y texto de filtro.
        """
        page = request.args.get('page', 1, type=int)
        page_size = request.args.get('page_size', 10, type=int)
        filter_text = request.args.get('filter', '').lower()
        return page, page_size, filter_text

    def _paginate_query(self, query, page, page_size):
        """
        Pagina la consulta dada.

        Args:
            query (db.Query): Consulta a paginar.
            page (int): Número de página.
            page_size (int): Tamaño de la página.

        Returns:
            tuple: Datos paginados, total de registros y total de páginas.
        """
        offset = (page - 1) * page_size
        total_records = query.count()
        total_pages = (total_records + page_size - 1) // page_size
        paginated_data = query.offset(offset).limit(page_size).all()
        return paginated_data, total_records, total_pages

    def _validate_required_fields(self, data):
        """
        Valida que los campos requeridos estén presentes en los datos.

        Args:
            data (dict): Datos a validar.

        Returns:
            Response: Respuesta con mensaje de error si faltan campos, None si todos los campos están presentes.
        """
        missing_fields = [field for field in self.required_fields if field not in data]
        if missing_fields:
            return jsonify({'message': f'Campos requeridos faltantes: {", ".join(missing_fields)}'}), 400
        return None

    def _handle_exception(self, e, message):
        """
        Maneja excepciones y devuelve una respuesta con el mensaje de error.

        Args:
            e (Exception): Excepción capturada.
            message (str): Mensaje de error.

        Returns:
            Response: Respuesta con el mensaje de error.
        """
        return jsonify({'message': str(e) if str(e) else message}), 500

    def get_all(self):
        """
        Obtiene todos los registros del modelo con paginación y filtro opcional.

        Returns:
            Response: Respuesta con los datos paginados y la información de paginación.
        """
        page, page_size, filter_text = self._get_pagination_params()
        query = self.model.query

        if filter_text:
            query = query.filter(
                db.or_(
                    *[getattr(self.model, field).ilike(f'%{filter_text}%') for field in self.required_fields]
                )
            )

        paginated_data, total_records, total_pages = self._paginate_query(query, page, page_size)

        return jsonify({
            'data': [{
                'id': getattr(item, 'id'),
                **{field: getattr(item, field) for field in self.required_fields}
            } for item in paginated_data],
            'pagination': {
                'page': page,
                'page_size': page_size,
                'total_records': total_records,
                'total_pages': total_pages,
                'has_next': page < total_pages,
                'has_prev': page > 1
            }
        })

    def create(self):
        """
        Crea un nuevo registro en el modelo.

        Returns:
            Response: Respuesta con el mensaje de éxito o error.
        """
        data = request.get_json()
        validation_result = self._validate_required_fields(data)
        if validation_result:
            return validation_result

        try:
            self.service.create(data)
            return jsonify({'message': f'{self.endpoint} creado'}), 201
        except Exception as e:
            return self._handle_exception(e, 'Error al crear el recurso')

    def update(self, id):
        """
        Actualiza un registro existente en el modelo.

        Args:
            id (int): Identificador del registro a actualizar.

        Returns:
            Response: Respuesta con el mensaje de éxito o error.
        """
        data = request.get_json()
        resource = self.service.get_by_id(id)
        if not resource:
            return jsonify({'message': 'Recurso no encontrado'}), 404

        validation_result = self._validate_required_fields(data)
        if validation_result:
            return validation_result

        try:
            self.service.update(id, data)
            return jsonify({'message': f'{self.endpoint} actualizado'}), 200
        except Exception as e:
            return self._handle_exception(e, 'Error al actualizar el recurso')

    def delete(self, id):
        """
        Elimina un registro existente en el modelo.

        Args:
            id (int): Identificador del registro a eliminar.

        Returns:
            Response: Respuesta con el mensaje de éxito o error.
        """
        try:
            success = self.service.delete(id)
            if not success:
                return jsonify({'message': 'Recurso no encontrado'}), 404
            return jsonify({'message': f'{self.endpoint} eliminado'}), 200
        except Exception as e:
            return self._handle_exception(e, 'Error al eliminar el recurso')