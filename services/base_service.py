from typing import TypeVar, Generic, List, Optional
from repositories.base_repository import BaseRepository

T = TypeVar('T')

class BaseService(Generic[T]):
    """
    Clase base para servicios que maneja operaciones CRUD para un modelo específico.

    Atributos:
        repository (BaseRepository): Repositorio base para manejar las operaciones CRUD.
    """

    def __init__(self, repository: BaseRepository[T]):
        """
        Inicializa la clase BaseService con el repositorio.

        Args:
            repository (BaseRepository): Repositorio base para manejar las operaciones CRUD.
        """
        self.repository = repository

    def get_all(self) -> List[T]:
        """
        Obtiene todos los registros del modelo.

        Returns:
            List[T]: Lista de todos los registros.
        """
        return self.repository.get_all()

    def get_by_id(self, id: int) -> Optional[T]:
        """
        Obtiene un registro por su identificador.

        Args:
            id (int): Identificador del registro.

        Returns:
            Optional[T]: Registro encontrado o None si no existe.
        """
        return self.repository.get_by_id(id)

    def create(self, data: dict) -> T:
        """
        Crea un nuevo registro en el modelo.

        Args:
            data (dict): Datos del nuevo registro.

        Returns:
            T: Registro creado.
        """
        return self.repository.create(**data)

    def update(self, id: int, data: dict) -> Optional[T]:
        """
        Actualiza un registro existente en el modelo.

        Args:
            id (int): Identificador del registro a actualizar.
            data (dict): Datos actualizados del registro.

        Returns:
            Optional[T]: Registro actualizado o None si no existe.
        """
        return self.repository.update(id, **data)

    def delete(self, id: int) -> bool:
        """
        Elimina un registro existente en el modelo.

        Args:
            id (int): Identificador del registro a eliminar.

        Returns:
            bool: True si el registro fue eliminado, False si no existe.
        """
        return self.repository.delete(id)